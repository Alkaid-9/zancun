# 本轮参考与需求核验回执

2026-09-10；主窗口+唯一只读执行位`ua_3d_feasibility`，串行完成三包；无代理文件变更/派生/安装/登录/上传/服务或付费模型调用。工具未返回可验证模型版本/调用费用，不据窗口名称报价格。

## E01 仓库核验：partial

执行位查看`/mnt/d/MyResearch`顶层、`external`一级、`/home/alkaid/tools`两级，未发现名称匹配Understand-Anything的checkout；仅是已查范围，不代表全机不存在。

实际请求：`https://raw.githubusercontent.com/Egonex-AI/Understand-Anything/main/README.md`，timeout12秒，curl(7)，约9.314秒，HTTP000。未取得README。该路径中的main只是假定访问路径，不是已核默认分支；不能声称测过其他GitHub入口或确定仓库不可用。

## E04 原需求对账：本包范围complete

读取首批v0.1、讨论详档、原Map README、Graph/Canvas v0.4、盘点04相关段落，未重读10289行讨论。返回24行初表与八层、七图名称；主控形成26行追踪表，补自身工作流、日志边界、三维兴趣等去向。

主控直接抽查：原Map README:11–41；Graph规格:5–48；盘点04:124–193。确认八层/七图名称、L0-L2与W1-W7区别、位置与语义分离。对代理把四树命名、字段与revision策略当用户拍板的表述作降格处理，见REQUIREMENTS结尾。

## E01 官网与演示补核：partial

用户明确提供两个入口：

| 实际访问URL | 方式 | 实际结果 |
|---|---|---|
| https://understand-anything.com/ | curl -L，max-time12秒 | curl(7)，约11.33秒，未取得HTTP头/HTML |
| https://understand-anything.com/demo/ | 同上 | curl(7)，约9.34秒，未取得HTTP头/HTML |

未用浏览器，未读取脚本/演示JSON，未再试代理或其他域名。用户能试玩与本执行环境网络失败可以同时成立；不据此判断网站下线。

因此输入类型、实际节点/边、渲染库、2D/3D、手工编辑/位置保存、版本与许可证均保持未核。主控没有重复网络探测；保留执行位报告作为本轮访问证据，不冒称亲自点击界面。

## 可用结论和下一次最小核验

本包的三维/侧栏/稳定ID设计来源于用户需求和本地合同，不声称继承UA实现。重新可访问后，仅沿官网实际链接获取固定版本的README/许可/图schema/渲染与保存入口，交付一条输入→节点边→视图→保存的数据链，再决定“适配UA / 单独渲染器 / 仅借鉴”。未核之前不编写针对UA的补丁路径。

Cognitive Terrain、NotEMD、LearnGraph、graphify、TaskQuay沿用v0.1记录的既有审查边界，本轮没有新核它们的运行/版本，不把旧静态能力当已接入。
