# render/ — 一页纸 Research Statement 渲染管线

把 `proposals/` 下的"多节合一"工作稿(含撰写说明等不外发内容)切出**正文区**,渲染成自包含 A4 HTML(CSS 内联、无外链依赖),供打印/另存为 PDF 外发。环境无 PDF 引擎(xelatex/tectonic/typst/weasyprint/wkhtmltopdf 均不可用,2026-08-13 探测),故默认走"HTML + Windows 浏览器打印"路线;若日后装了任一引擎,脚本会自动探测并同时直出 `.pdf`。

## 用法(三行)

```bash
cd render/
./render_onepager.sh ../onepager_draft_v1.md          # 默认切中文正文,出 out/onepager_draft_v1_zh.html
./render_onepager.sh ../onepager_draft_v1.md --en     # 切英文正文,出 out/onepager_draft_v1_en.html
```

> **外发红线**:`out/` 内 HTML 属草稿渲染(占位符未填时带浅黄高亮),**未经用户确认、未填完占位符、未删说明区前禁止外发**;定稿流程见 `final_review_20260813.md` §⑤ 放行检查单。

## Windows 侧打印成 PDF

1. 资源管理器打开 `D:\MyResearch\MAS_Safety_Project\research\map\proposals\render\out\`,双击 `onepager_draft_v1_zh.html` 用 Edge/Chrome 打开;
2. `Ctrl+P` → 打印机选"另存为 PDF / Microsoft Print to PDF";
3. **边距选"无"(None)**——CSS `@page` 已内置上下 2cm、左右 1.8cm 边距,浏览器再加就双重了;
4. 更多设置里取消勾选"页眉和页脚"(否则会印出 URL/日期),勾选"背景图形"(保留占位符浅黄高亮;定稿填完占位符后无此项也无影响)→ 保存。

## 切片标记约定

脚本按以下三条约定从工作稿中定位正文区(当前 `onepager_draft_v1.md` 天然满足,后续 v2/v3 沿用即可):

1. **语言区头**:二级标题行 `## 中文版...`(`--zh` 匹配)或 `## English Version...`(`--en` 匹配,忽略大小写),标题后可跟任意备注文字;
2. **正文起点**:语言区头之后的**第一个一级标题行**(`# Research Statement · ...`),此行起进入外发正文;
3. **正文终点**:下一个二级标题行(`## `)之前;结尾的空行与 `---` 分隔线自动剔除。

即:撰写说明、素材来源等节只要不放在"语言区头 → 下一个 `## `"之间的一级标题之后,就绝不会被渲染进外发稿。占位符 `[姓名]`/`[学校]` 等在产出 HTML 中自动加浅黄高亮(`.placeholder`),方便发前逐个检查填空;**全部填完后高亮自然消失**。

其他行为:输入文件不存在/找不到语言区标记时报错退出(非静默);产出统一落在 `render/out/`,命名 `<输入文件名>_<zh|en>.html`。

## 一页溢出估算(v1 中文正文,2026-08-13)

按验收口径估算——A4 可用高度 29.7 − 2×2 = **25.7cm**,11pt/1.45 行距每行 ≈ 0.55cm,中文每行按 38–42 字:

- v1 中文正文实测 **863 个 CJK 字符**(另含少量拉丁术语,已按 0.55 倍字宽折算),标题 1 行 + 正文约 **32–34 行**;
- 总高约 **19.4–20.5cm < 25.7cm** → **一页放得下,不超页**,且实际渲染用 10.5pt 比估算口径更省;
- 余量约 5.2–6.3cm ≈ 9–11 行 ≈ **还能再加约 350–440 字**;反过来,正文超过约 **1250 汉字当量**才需要开始减字(减字优先级建议:三、研究兴趣段的"备选方向"句 → 二、三件套各条的技术栈细节)。

## 文件清单

| 文件 | 说明 |
| --- | --- |
| `render_onepager.sh` | 渲染脚本(切片 → pandoc → 内联 CSS 组装 → PDF 引擎探测) |
| `onepager.css` | A4 学术 statement 样式(打印排版 + 屏幕预览 + 占位符高亮) |
| `out/` | 渲染产物(HTML/PDF),可整目录删除重生成 |
