#!/usr/bin/env bash
# render_onepager.sh — 一页纸 Research Statement 渲染管线
# 从"多节合一"工作稿中切出指定语言区正文,渲染为自包含 A4 HTML(探测到 PDF 引擎则同时出 PDF)。
# 用法: ./render_onepager.sh <draft.md> [--zh|--en]   (默认 --zh;切片标记约定见 README.md)
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CSS_FILE="$SCRIPT_DIR/onepager.css"
OUT_DIR="$SCRIPT_DIR/out"

usage() { echo "用法: $0 <draft.md> [--zh|--en]  (默认 --zh)" >&2; exit 1; }

INPUT=""
REGION="zh"
for arg in "$@"; do
  case "$arg" in
    --zh) REGION="zh" ;;
    --en) REGION="en" ;;
    -h|--help) usage ;;
    -*) echo "错误: 未知选项: $arg" >&2; usage ;;
    *) INPUT="$arg" ;;
  esac
done

[[ -n "$INPUT" ]] || usage
[[ -f "$INPUT" ]] || { echo "错误: 输入文件不存在: $INPUT" >&2; exit 1; }
[[ -f "$CSS_FILE" ]] || { echo "错误: 缺少样式文件: $CSS_FILE" >&2; exit 1; }
command -v pandoc  >/dev/null 2>&1 || { echo "错误: 未找到 pandoc" >&2; exit 1; }
command -v python3 >/dev/null 2>&1 || { echo "错误: 未找到 python3" >&2; exit 1; }

mkdir -p "$OUT_DIR"
BASE="$(basename "$INPUT")"; BASE="${BASE%.md}"
OUT_HTML="$OUT_DIR/${BASE}_${REGION}.html"

TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT
BODY_MD="$TMP_DIR/body.md"
BODY_HTML="$TMP_DIR/body.html"

# ---- 1. 切片:按标记约定抽取语言区正文 ----
#   语言区头: "## 中文版..."(--zh)/ "## English Version..."(--en)
#   正文起点: 语言区头之后的第一个一级标题行 "# ..."
#   正文终点: 下一个 "## " 标题行之前(去掉尾部空行与 "---" 分隔线)
python3 - "$INPUT" "$REGION" > "$BODY_MD" <<'PY'
import re, sys
path, region = sys.argv[1], sys.argv[2]
lines = open(path, encoding="utf-8").read().splitlines()
if region == "zh":
    head_pat, head_name = re.compile(r"^##\s*中文版"), "## 中文版"
else:
    head_pat, head_name = re.compile(r"^##\s*English Version", re.I), "## English Version"
try:
    ri = next(i for i, l in enumerate(lines) if head_pat.match(l))
except StopIteration:
    sys.exit(f"错误: 未找到语言区标记「{head_name}」")
try:
    start = next(i for i in range(ri + 1, len(lines)) if re.match(r"^#\s", lines[i]))
except StopIteration:
    sys.exit(f"错误: 「{head_name}」之后未找到一级标题(# ...)作为正文起点")
end = next((i for i in range(start + 1, len(lines)) if re.match(r"^##\s", lines[i])), len(lines))
body = lines[start:end]
while body and (not body[-1].strip() or body[-1].strip() == "---"):
    body.pop()
if not body:
    sys.exit(f"错误: 「{head_name}」正文区为空")
print("\n".join(body))
PY

# ---- 2. pandoc: markdown -> HTML 正文片段 ----
#   +lists_without_preceding_blankline: 工作稿里"段落行后直接接 - 列表"也能正确成列表
#   -smart: 不做引号/破折号智能替换(中文语境下 smart 会把 "..." 猜成两个右弯引号)
#   --wrap=none: 不在中文字符间插入换行,避免浏览器把换行渲染成多余空格
pandoc -f markdown+lists_without_preceding_blankline-smart --wrap=none -t html "$BODY_MD" -o "$BODY_HTML"

# ---- 3. 组装自包含 HTML: 内联 CSS + 占位符 [xxx] 浅黄高亮 ----
python3 - "$BODY_HTML" "$CSS_FILE" "$REGION" "$OUT_HTML" <<'PY'
import html as H, re, sys
body_path, css_path, region, out_path = sys.argv[1:5]
body = open(body_path, encoding="utf-8").read().strip()
css = open(css_path, encoding="utf-8").read().rstrip()
body = re.sub(r"\[([^\[\]<>]{1,40}?)\]", r'<span class="placeholder">[\1]</span>', body)
m = re.search(r"<h1[^>]*>(.*?)</h1>", body, re.S)
title = re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else "Research Statement"
lang = "zh-CN" if region == "zh" else "en"
doc = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{H.escape(title)}</title>
<style>
{css}
</style>
</head>
<body>
{body}
</body>
</html>
"""
open(out_path, "w", encoding="utf-8").write(doc)
PY

echo "HTML 已生成: $OUT_HTML"

# ---- 4. PDF 引擎探测: 有则直出 PDF,无则走浏览器打印路线 ----
OUT_PDF="$OUT_DIR/${BASE}_${REGION}.pdf"
if command -v weasyprint >/dev/null 2>&1; then
  weasyprint "$OUT_HTML" "$OUT_PDF" && echo "PDF 已生成(weasyprint): $OUT_PDF"
elif command -v wkhtmltopdf >/dev/null 2>&1; then
  wkhtmltopdf --enable-local-file-access "$OUT_HTML" "$OUT_PDF" && echo "PDF 已生成(wkhtmltopdf): $OUT_PDF"
elif command -v typst >/dev/null 2>&1; then
  pandoc "$BODY_MD" -o "$OUT_PDF" --pdf-engine=typst \
    && echo "PDF 已生成(typst): $OUT_PDF"
elif command -v tectonic >/dev/null 2>&1 || command -v xelatex >/dev/null 2>&1; then
  ENGINE=xelatex; command -v tectonic >/dev/null 2>&1 && ENGINE=tectonic
  pandoc "$BODY_MD" -o "$OUT_PDF" --pdf-engine="$ENGINE" \
    -V documentclass=article -V fontsize=10.5pt \
    -V geometry:"top=2cm,bottom=2cm,left=1.8cm,right=1.8cm" \
    -V CJKmainfont="Noto Serif CJK SC" \
    && echo "PDF 已生成($ENGINE): $OUT_PDF"
else
  echo "未探测到 PDF 引擎(weasyprint/wkhtmltopdf/typst/tectonic/xelatex),仅输出 HTML。"
  echo "→ 用 Windows 浏览器打开上面的 HTML,Ctrl+P 另存为 PDF(步骤见 render/README.md)。"
fi
