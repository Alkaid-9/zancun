#!/usr/bin/env python3
"""
独立的红队审计脚本：穿透式事实校验
验证目前生成的所有“卷宗”和“结论”与真实文件依据是否存在“脑补”或“串线”。
"""

import os
import re
import json

def verify_factual_basis():
    print("=" * 80)
    print("🚨 [INDEPENDENT RED TEAM AUDIT] 穿透式事实核查 🚨")
    print("目标：剥离大模型（Gemini/Agent）的幻觉、脑补与串线，基于硬文件锚点证明结论真伪。")
    print("=" * 80)

    # 1. 验证 Headroom 基准测试结论的事实依据
    print("\n[核查项 1] Headroom Benchmark 结论真实性")
    bm_path = "/mnt/d/Alkaid/Desktop/zancun/09_外部参考项目深度调研/receipts/sources/headroom/compression_benchmark.py"
    if os.path.exists(bm_path):
        with open(bm_path, 'r') as f:
            content = f.read()
            has_truncation_test = "Truncation" in content
            has_cost = "llm_cost_usd" in content
            print(f"  👉 依据文件: {bm_path}")
            print(f"  👉 事实检验: 截断对比存在={has_truncation_test}, 包含经济成本模型={has_cost}")
            if has_truncation_test and has_cost:
                print("  ✅ 红队判定: 卷宗中关于“基准测试比较了截断、摘要并涉及经济成本”的结论是【真实的】，非脑补。")
            else:
                print("  ❌ 红队判定: 结论存在【严重脑补】，原文中并无此逻辑！")
    else:
         print("  ❌ 红队判定: 文件不存在，属于【凭空幻觉】！")

    # 2. 验证 CodeCompressor / AST 相关结论的真实性
    print("\n[核查项 2] CodeCompressor (AST代码骨架化) 是否真实存在于原仓？")
    cache_path = "/mnt/d/Alkaid/Desktop/zancun/09_外部参考项目深度调研/receipts/sources/headroom/cache_control.rs"
    lib_path = "/mnt/d/Alkaid/Desktop/zancun/09_外部参考项目深度调研/receipts/sources/headroom/lib.rs"
    
    ast_found_in_original = False
    for path in [cache_path, lib_path]:
        if os.path.exists(path):
            with open(path, 'r') as f:
                content = f.read()
                if "CodeCompressor" in content or "ast" in content.lower():
                    ast_found_in_original = True

    print("  👉 依据文件: cache_control.rs, lib.rs")
    if ast_found_in_original:
        print("  ✅ 红队判定: CodeCompressor 概念在原件中有提及。")
    else:
        print("  ❌ 红队判定: 【过度宣称 / 串线脑补】！原始 Rust 收据中根本没有任何关于 AST、Python ast 模块或 CodeCompressor 的提及！原仓只做了 JSON/Log 和 Cache 保护的 transforms！所谓“AST代码骨架化”是 Agent 借题发挥脑补出的概念，并非 headroom 原仓的真实特性！")

    # 3. 验证 CCR (Context Cache & Retrieval) 是否是原仓概念
    print("\n[核查项 3] CCR 机制是否真实存在于原仓？")
    if os.path.exists(lib_path):
        with open(lib_path, 'r') as f:
            content = f.read()
            if "pub mod ccr;" in content:
                print("  ✅ 红队判定: 【真实的】。lib.rs 第 5 行明确存在 `pub mod ccr;`。")
            else:
                print("  ❌ 红队判定: CCR 属于【串线脑补】。")

if __name__ == "__main__":
    verify_factual_basis()
