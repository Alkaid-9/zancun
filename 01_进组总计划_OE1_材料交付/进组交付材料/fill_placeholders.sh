#!/usr/bin/env bash
# fill_placeholders.sh — 把 placeholder_config.env 中的值填入对外材料副本
#
# 用法:  ./fill_placeholders.sh <md文件> [更多md文件...]
# 示例:  ./fill_placeholders.sh onepager_draft_v1.md OE1_lu_email_v4.md
#
# 行为:
#   * 读取脚本同目录的 placeholder_config.env(模板见 placeholder_sheet.md 第三节);
#     可用环境变量 PLACEHOLDER_CONFIG=/path/to/xx.env 覆盖(自测/高级用法)。
#   * 对每个传入 md 生成 <原名>_filled.md 副本,绝不覆盖原稿。
#   * config 中空值的键跳过替换并警告;替换后扫描副本中残留的 [占位符] 并打印警告。

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG="${PLACEHOLDER_CONFIG:-$SCRIPT_DIR/placeholder_config.env}"

if [[ ! -f "$CONFIG" ]]; then
  echo "错误:未找到配置文件 $CONFIG" >&2
  echo "请先打开同目录 placeholder_sheet.md,把第三节的 placeholder_config.env 模板段抄成该文件并填值。" >&2
  exit 1
fi

if [[ $# -lt 1 ]]; then
  echo "用法:$0 <md文件> [更多md文件...]" >&2
  echo "示例:$0 onepager_draft_v1.md OE1_lu_email_v4.md" >&2
  exit 1
fi

# 替换逻辑用内嵌 python3:纯字符串替换,无 sed 方括号转义问题,对中文/全角标点稳。
python3 - "$CONFIG" "$@" <<'PYEOF'
import os
import re
import sys

config_path = sys.argv[1]
md_files = sys.argv[2:]

# env 键 -> 文中占位符 token(同一键的多个写法变体都列出;按长度降序替换防子串误伤)
MAPPING = {
    "NAME_ZH":         ["[姓名]"],
    "NAME_EN":         ["[Name]"],
    "SCHOOL_ZH":       ["[学校]"],
    "SCHOOL_EN":       ["[university]"],
    "MAJOR_ZH":        ["[专业]"],
    "MAJOR_EN":        ["[major]"],
    "IDENTITY_ZH":     ["[身份表述]"],
    "IDENTITY_EN":     ["[status]"],
    "LAB_ZH":          ["[课题组/实验室名]", "[课题组]"],
    "LAB_EN":          ["[lab]"],
    "CONTACT_ZH":      ["[联系方式]"],
    "CONTACT_EN":      ["[contact]"],
    "PHONE_WECHAT":    ["[电话 / 微信]", "[电话/微信]"],
    "GPA_HOURS":       ["[GPA / 每周可投入时长，选填]", "[GPA/投入时长（选填）]", "[GPA(选填)]", "[GPA]"],
    "REISIG_PROGRESS": ["[填实际进度]", "[Reisig 进度]"],
    "DATE_DAY":        ["[日]"],
    "DATE_FULL":       ["[日期]"],
    "NSFC_PROJECT":    ["[项目名称/方向]"],
}

# --- 解析 config(KEY=VALUE;支持引号与行尾 # 注释)---
LINE_RE = re.compile(
    r"""^([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(?:"([^"]*)"|'([^']*)'|([^#]*?))\s*(?:\#.*)?$"""
)
cfg = {}
with open(config_path, encoding="utf-8") as f:
    for ln, raw in enumerate(f, 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        m = LINE_RE.match(line)
        if not m:
            print(f"警告:配置第 {ln} 行无法解析,已忽略:{line}")
            continue
        key = m.group(1)
        val = [g for g in (m.group(2), m.group(3), m.group(4)) if g is not None][0].strip()
        if key not in MAPPING:
            print(f"警告:配置第 {ln} 行的键 {key} 不在已知占位符映射中,已忽略。")
            continue
        cfg[key] = val

empty_keys = sorted(k for k, v in cfg.items() if v == "")
if empty_keys:
    print("警告:以下键值为空,对应占位符将保留不替换:")
    for k in empty_keys:
        print(f"  - {k}  (→ {' / '.join(MAPPING[k])})")

LEFTOVER_RE = re.compile(r"\[[^\]]{1,20}\]")
exit_code = 0

for path in md_files:
    print(f"\n==> 处理 {path}")
    if not os.path.isfile(path):
        print(f"错误:文件不存在,跳过:{path}")
        exit_code = 1
        continue
    with open(path, encoding="utf-8") as f:
        text = f.read()

    total = 0
    for key, tokens in MAPPING.items():
        val = cfg.get(key, "")
        if val == "":
            continue
        for tok in sorted(tokens, key=len, reverse=True):
            n = text.count(tok)
            if n:
                text = text.replace(tok, val)
                print(f"    {tok} -> {val}  ({n} 处)")
                total += n

    stem, ext = os.path.splitext(path)
    out_path = f"{stem}_filled{ext or '.md'}"
    if os.path.abspath(out_path) == os.path.abspath(path):
        print(f"错误:输出路径与原稿相同,拒绝写入:{path}")
        exit_code = 1
        continue
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"    共替换 {total} 处 -> 副本已写入 {out_path}(原稿未动)")

    leftovers = {}
    for mobj in LEFTOVER_RE.finditer(text):
        leftovers[mobj.group(0)] = leftovers.get(mobj.group(0), 0) + 1
    if leftovers:
        print(f"    警告:副本中仍残留 {sum(leftovers.values())} 处未替换的方括号占位符,请人工核对:")
        for tok, n in sorted(leftovers.items(), key=lambda kv: -kv[1]):
            print(f"      {tok}  x{n}")
    else:
        print("    残留扫描:无未替换占位符。")

sys.exit(exit_code)
PYEOF
