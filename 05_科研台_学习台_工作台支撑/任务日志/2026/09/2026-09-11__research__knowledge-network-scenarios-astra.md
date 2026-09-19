---
id: TASK-20260911-006
title: 多层知识网络三场景设计（Astra路线）
date: 2026-09-11
runtime:
  model: Codex（实际SKU未独立核验）
  effort: UNKNOWN
  effort_source: 当前工具未提供可核字段
  launch: API coding agent
type: research
status: done
area: research-desk
project: none
todo_ids: []
owners:
  - user
  - codex
related:
  - progress/decisions/2026-09-11__research__knowledge-network-scenarios-astra-v0.1.md
---

# 目标

按用户“两边各自独立画，你来对比”的安排，完成本窗口三场景设计供Fable比较。不修改代码／施工合同，不自动接C04。

# 最终结果

已写三场景：论文深挖遇工业线索、工业动向倒查谱系并开学习分支、学习失败调用指导回原问题。包含对象／事件图、三台流程图、读写回流、负例验收、合同差异和比较问题表。

独立性明确降格：已读用户粘贴的Fable摘要，未打开其v0.3场景稿正文，因此是另一份自行设计，不是严格盲审。未核Fable提交bf9f45c或其全部交付测试，不为其结果背书。

# 修改内容

- 新建本路线场景稿，引用现有第一波合同、指导规格及实际_source_refs。
- 指出关系发现／来源断言／科学判断需分开；使用记录继承已有guidance/uses设计。
- 外部网页尚缺来源登记到操作／导出全链合同；实际校验已含非工作簿anchor，不能说只认工作簿或必然报错。
- 记录三台写入权威与四种跨层桥；事件模式先定语义，真实案例再定必要字段。

# 验收与证据

| 项 | 结果 | 证据 |
|---|---|---|
| 三场景及返回路径 | 设计已完成 | 场景稿§2–4 |
| 对象／层／事件语义 | 设计已完成 | 场景稿§1、§5 |
| 比较范围及独立性 | 已明示 | 场景稿开头、§7 |
| 代码／浏览器验证 | 未运行，不属于本任务 | 仅静态读取_source_refs |

# 当前状态

READY-FOR-COMPARISON / DESIGN-ONLY。中央服务发号TASK-20260911-006。未改应用、来源、Fable稿、合同；未commit/push、未启动或停止服务。

# 尚未完成

Fable对照、用户选择、正式合同amendment、真实来源实例及运行验证。

# 下一步

用户将本稿交给Fable，按§7比较共同结论、实质差异、未决实例，不把模型赞同次数当独立事实证据。

# 可拓展方向

网页证据版本、组织角色有效期、事件参与、指导USE与个人／研究评价接口。

# 风险与回滚

示例全为DEMO，不证实真实工业采用或个人能力。删除本路线新增文档可回退稿件；任务号不回收；共享登记仅保形追加，不清理他窗内容。

# 文件和产物

- progress/decisions/2026-09-11__research__knowledge-network-scenarios-astra-v0.1.md
- 本日志与task_logs/INDEX登记；RD-2 TODO追记及生成视图。

## Amendment：同轮用户补充小满学习台需求

三场景稿完成后，用户补充及时反馈／记录／调整目的及四个参考入口。进行了有界只读访问，获得MLDLRL/AI/blog说明及kaoyan目录、学习状态／规划／经验贴片段和auto_run脚本；没有克隆、执行、安装或网页交互实测。另存`progress/decisions/2026-09-11__research__learning-feedback-xiaoman-reference-note.md`，与原场景稿分开供对比。未核CoE实验数字，不据转述宣称学习效果。
