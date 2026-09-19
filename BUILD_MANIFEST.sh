#!/usr/bin/env bash
set -euo pipefail

package_root="/mnt/d/workspace/_exports/2026-09_进组计划与产出_按项目与论文归类_截至2026-09-19"
project_root="/mnt/d/MyResearch/MAS_Safety_Project"
snapshot_manifest="/mnt/d/workspace/Desks/vaults/Research-Garden/learning/group-entry/FILES.tsv"
snapshot_sources="$package_root/.snapshot_sources.raw"
raw_list="$package_root/.source_files.raw"
manifest_unsorted="$package_root/.manifest.unsorted.tsv"
manifest="$package_root/00_完整文件清单_时间倒序.tsv"
plans_manifest="$package_root/00_计划与状态文件清单_时间倒序.tsv"
missing_manifest="$package_root/00_未找到或未复制条目.txt"
september_start_epoch="$(date -d '2026-09-01 00:00:00' +%s)"
september_end_epoch="$(date -d '2026-09-20 00:00:00' +%s)"

# Idempotent rebuild of this dedicated staging package only.
find "$package_root" -mindepth 1 -maxdepth 1 ! -name 'BUILD_MANIFEST.sh' -exec rm -rf -- {} +

classify_group() {
  local source_path="$1"
  local lower_path="${source_path,,}"

  case "$lower_path" in
    */research/map/surveys/industry_scan_202609/*)
      printf '%s' '06_九月研究刷新/01_工业界_IND1'
      ;;
    */research/map/surveys/rescan_202609/*)
      printf '%s' '06_九月研究刷新/02_学术增量与被引_RS'
      ;;
    */research/map/proposals/*|*/onboarding_preflight/*|*lu_to_sun_learning_and_portfolio_pack*|*e1_technical_fit_brief*)
      printf '%s' '01_进组总计划_OE1_材料交付'
      ;;
    *controller_synthesis.md|*ex01-hash-status-and-ccf-youbo-intake*|*/edge下载/*|*research-garden/learning/group-entry*)
      printf '%s' '01_进组总计划_OE1_材料交付'
      ;;
    *ownership-v3/crossedgeim*|*crossedgeim*)
      printf '%s' '02_四论文Ownership主线/04_CrossEdgeIM'
      ;;
    *ownership-v3/sigrank*|*sigrank*)
      printf '%s' '02_四论文Ownership主线/02_sigRank'
      ;;
    *ownership-v3/ground-truth*|*ground-truth*|*sommers*)
      printf '%s' '02_四论文Ownership主线/03_GroundTruth_Sommers'
      ;;
    *ownership-v3/edgeim*)
      printf '%s' '02_四论文Ownership主线/01_EdgeIM'
      ;;
    *four-paper*|*ownership-v3*|*manifest_addendum_20260904*|*visual_readings_20260904*|*only_paper_full_session*)
      printf '%s' '02_四论文Ownership主线/00_共享合同_计划_验收'
      ;;
    */teardown-joint-20260813/teaching_paywall3/*)
      printf '%s' '02_四论文Ownership主线/01_EdgeIM/历史联卷'
      ;;
    */teardown-joint-20260813/teaching/*)
      printf '%s' '03_鲁组其他论文与研究谱系/00_鲁组PN四篇联卷'
      ;;
    *sbtpn*)
      printf '%s' '03_鲁组其他论文与研究谱系/01_SBTPN'
      ;;
    *pnulock*|*deadlock-2024-ieeeaccess*)
      printf '%s' '03_鲁组其他论文与研究谱系/02_PNULOCK'
      ;;
    *uaf-pn-vfg*|*uaf_pn_vfg*|*/03_uaf*)
      printf '%s' '03_鲁组其他论文与研究谱系/03_UAF_PN_VFG'
      ;;
    *deadlockseg*|*seglock*)
      printf '%s' '03_鲁组其他论文与研究谱系/04_SEGLOCK_DeadlockSeg'
      ;;
    *sbpn*)
      printf '%s' '03_鲁组其他论文与研究谱系/05_SBPN'
      ;;
    *mhp*)
      printf '%s' '03_鲁组其他论文与研究谱系/06_MHP'
      ;;
    *deadlocklockseggraph*|*jos2021*|*deadlock_jos2021*|*/15_deadlock*)
      printf '%s' '03_鲁组其他论文与研究谱系/07_Deadlock_JOS2021'
      ;;
    *agentproof*)
      printf '%s' '03_鲁组其他论文与研究谱系/09_前沿待跟踪/01_Agentproof'
      ;;
    *causalpastlogic*)
      printf '%s' '03_鲁组其他论文与研究谱系/09_前沿待跟踪/02_CausalPastLogic'
      ;;
    *objectcentricconformance*)
      printf '%s' '03_鲁组其他论文与研究谱系/09_前沿待跟踪/03_ObjectCentricConformance'
      ;;
    *tracecompiler*)
      printf '%s' '03_鲁组其他论文与研究谱系/09_前沿待跟踪/04_TraceCompiler'
      ;;
    *cn119477231b*)
      printf '%s' '03_鲁组其他论文与研究谱系/09_前沿待跟踪/05_CN119477231B'
      ;;
    *ra2716*|*导师画像*|*研究谱系*|*lineage*)
      printf '%s' '03_鲁组其他论文与研究谱系/08_导师画像_谱系_团队'
      ;;
    *ra26-evoagent-toy*)
      printf '%s' '07_专项训练与待学论文包/01_ra26_EvoAgent'
      ;;
    *ra28-mindbridge*)
      printf '%s' '07_专项训练与待学论文包/02_ra28_MindBridge'
      ;;
    *ra30-memory-formal*|*cross-window-memory*)
      printf '%s' '07_专项训练与待学论文包/03_ra30_记忆与Petri网'
      ;;
    *ase2026_probguard*)
      printf '%s' '07_专项训练与待学论文包/04_ProbGuard'
      ;;
    *icse2026_agentspec*)
      printf '%s' '07_专项训练与待学论文包/05_AgentSpec'
      ;;
    *folda_partial_order_alignment*)
      printf '%s' '07_专项训练与待学论文包/06_FoldA'
      ;;
    */teardowns/intima/*)
      printf '%s' '07_专项训练与待学论文包/07_INTIMA'
      ;;
    */teardowns/anchor/*)
      printf '%s' '07_专项训练与待学论文包/08_Anchor'
      ;;
    */teardowns/emoagent/*)
      printf '%s' '07_专项训练与待学论文包/09_EmoAgent'
      ;;
    *best-friends-not-forever*)
      printf '%s' '07_专项训练与待学论文包/09_EmoAgent/相关论文'
      ;;
    */learning/case_studies/evoagent/*)
      printf '%s' '07_专项训练与待学论文包/10_EvoAgent_Phase1历史复习'
      ;;
    *jinzu*|*进组*|*oe1*|*oe-1*|*br1*|*group-entry*|*lu-onboarding*)
      printf '%s' '01_进组总计划_OE1_材料交付'
      ;;
    *research_growth*|*bridge*|*lu-sun*|*transfer*|*研究操作符*|*科研学习与训练体系*)
      printf '%s' '04_Bridge与迁移研究'
      ;;
    *ccf优博*|*博士生科研入门辅导*)
      printf '%s' '08_科研方法与长期成长材料'
      ;;
    *research-desk*|*two-desks*|*three-desks*|*workbench*|*cockpit*|*knowledge-network*|*map-learning*|*research-canvas*|*research-system*|*desks-infrastructure*|*research-inventory*|*rd2-*|*research-copilot*|*learning-feedback*|*correction-notebooks*|*workflow-notes-and-coe*|*reference-evaluation*|*reference-followup*|*reference-integration*)
      printf '%s' '05_科研台_学习台_工作台支撑'
      ;;
    *工作簿1.xlsx)
      printf '%s' '05_科研台_学习台_工作台支撑/原始输入'
      ;;
    */learning/training/lu-edgeim-algo1/*|*/learning/一些讨论.md)
      printf '%s' '02_四论文Ownership主线/01_EdgeIM'
      ;;
    */research/papers_lu/plan-rewrite-inputs-20260906/*|*/research/papers_lu/session-archive-20260906/*|*/edge下载/*重构进组计划*|*/edge下载/*学习与科研体系*|*/edge下载/*鲁组进组准备*|*/edge下载/*第二条研究线*)
      printf '%s' '01_进组总计划_OE1_材料交付'
      ;;
    */learning/modules/*|*/learning/methodology/*|*/learning/00_master_index.md|*/learning/roadmap.md|*/learning/learning_path.md|*learning–research\ os*|*/learning/training/00_system.md|*/learning/training/ledger.md)
      printf '%s' '08_科研方法与长期成长材料/通用学习基础'
      ;;
    */research/papers_lu/*)
      printf '%s' '03_鲁组其他论文与研究谱系/99_其他论文与盘点'
      ;;
    */progress/*)
      printf '%s' '01_进组总计划_OE1_材料交付/99_其他相关计划与状态'
      ;;
    *)
      printf '%s' '99_待人工复核归类'
      ;;
  esac
}

classify_subpath() {
  local relative_path="$1"

  case "$relative_path" in
    progress/decisions/*)
      printf '计划与决策/%s' "${relative_path#progress/decisions/}"
      ;;
    progress/handoff/*)
      printf '交接与恢复/%s' "${relative_path#progress/handoff/}"
      ;;
    progress/task_logs/*)
      printf '任务日志/%s' "${relative_path#progress/task_logs/}"
      ;;
    progress/audits/*)
      printf '审计与核验/%s' "${relative_path#progress/audits/}"
      ;;
    progress/runbooks/*)
      printf '手册/%s' "${relative_path#progress/runbooks/}"
      ;;
    progress/projects/*)
      printf '项目卡/%s' "${relative_path#progress/projects/}"
      ;;
    research/map/proposals/*)
      printf '进组交付材料/%s' "${relative_path#research/map/proposals/}"
      ;;
    learning/training/lu-edgeim-algo1/*)
      printf '学习与课程/%s' "${relative_path#learning/training/lu-edgeim-algo1/}"
      ;;
    learning/*)
      printf '学习与课程/%s' "${relative_path#learning/}"
      ;;
    research/papers_lu/*)
      printf '论文原文与拆解/%s' "${relative_path#research/papers_lu/}"
      ;;
    research/sun/phase1/papers/*)
      printf '学习与课程/%s' "${relative_path#research/sun/phase1/papers/}"
      ;;
    research/map/surveys/*)
      printf '研究刷新/%s' "${relative_path#research/map/surveys/}"
      ;;
    casual/companion-survey/*)
      printf '学习与课程/%s' "${relative_path#casual/companion-survey/}"
      ;;
    OUTER_MyResearch/research_growth/*)
      printf '方法论与反思/%s' "${relative_path#OUTER_MyResearch/research_growth/}"
      ;;
    OUTER_MyResearch/*)
      printf '外层研究材料/%s' "${relative_path#OUTER_MyResearch/}"
      ;;
    Edge下载/*)
      printf '外部输入/%s' "${relative_path#Edge下载/}"
      ;;
    Alkaid_Desktop/*)
      printf '桌面原始输入/%s' "${relative_path#Alkaid_Desktop/}"
      ;;
    xwechat_files/*)
      printf '微信原始材料/%s' "${relative_path#xwechat_files/}"
      ;;
    *)
      printf '其他/%s' "$relative_path"
      ;;
  esac
}

classify_kind() {
  local source_path="$1"
  local lower_path="${source_path,,}"

  case "$lower_path" in
    */progress/decisions/*) printf '%s' '计划或决策' ;;
    */progress/handoff/*) printf '%s' '交接与恢复' ;;
    */progress/task_logs/*) printf '%s' '任务日志' ;;
    */progress/audits/*) printf '%s' '审计与核验' ;;
    */progress/runbooks/*) printf '%s' '手册与规则' ;;
    */progress/projects/*) printf '%s' '项目卡' ;;
    */research/map/proposals/*) printf '%s' '进组交付材料' ;;
    */learning/training/*|*/learning/case_studies/*|*/research/sun/phase1/papers/*|*/casual/companion-survey/*/teaching/*) printf '%s' '学习包与本人作答' ;;
    */research/map/surveys/*) printf '%s' '九月研究刷新' ;;
    */research/papers_lu/*) printf '%s' '论文原文与拆解' ;;
    */research_growth/*) printf '%s' '方法论与研究反思' ;;
    */edge下载/*|*/xwechat_files/*|*/alkaid/desktop/*) printf '%s' '外部原始材料' ;;
    *) printf '%s' '其他相关产出' ;;
  esac
}

{
  awk -F '\t' 'NR > 1 {print $2}' "$snapshot_manifest" > "$snapshot_sources"
  cat "$snapshot_sources"
  rg -l -i '进组|jinzu|鲁组|鲁法明|OE-1|OE1|EdgeIM|ownership-v3|四论文' \
    "$project_root/progress/decisions" \
    "$project_root/progress/handoff" \
    "$project_root/progress/task_logs/2026/09" \
    "$project_root/progress/audits/2026/09" \
    "$project_root/progress/runbooks" \
    "$project_root/progress/projects" \
    | awk '/\/2026\/09\// || /2026-09/ || /jinzu-sprint\.md$/ || /lu-onboarding-and-desks/ || /PENDING\.md$/'
  find "$project_root/progress" -maxdepth 1 -type f -name '*.md'
  find "$project_root/progress/decisions" -type f \( \
    -path '*/rd2-*/*' -o \
    -path '*/three-desks-v0.1/*' -o \
    -path '*/two-desks-delta-20260914/*' -o \
    -name '*rd2-*' -o \
    -name '*research-desk*' -o \
    -name '*three-desks*' -o \
    -name '*two-desks*' -o \
    -name '*knowledge-network*' -o \
    -name '*research-copilot*' -o \
    -name '*learning-feedback*' -o \
    -name '*correction-notebooks*' -o \
    -name '*workflow-notes-and-coe*' -o \
    -name '2026-09-10__research__SOL_START_HERE.md' \
  \)
  find "$project_root/progress/handoff" -type f \( \
    -name '*research-desk*' -o \
    -name '*research-workbench*' -o \
    -name '*research-copilot*' -o \
    -name '*two-desks*' -o \
    -name '*three-desks*' \
  \)
  find "$project_root/progress/task_logs/2026/09" -type f \( \
    -name '*research-desk*' -o \
    -name '*workbench-research-desk*' -o \
    -name '*research-copilot*' -o \
    -name '*two-desks*' -o \
    -name '*three-desks*' -o \
    -name '*knowledge-network*' -o \
    -name '*rd2-*' -o \
    -name '*learning-feedback*' -o \
    -name '*correction-notebooks*' \
    -o -name '*reference-evaluation*' \
    -o -name '*reference-followup*' \
    -o -name '*reference-integration*' \
  \)
  find "$project_root/learning/training/lu-edgeim-algo1" -type f \
    -not -path '*/_sealed/*' \
    -not -path '*/__pycache__/*' \
    -newermt '2026-09-01' ! -newermt '2026-09-20'
  find "$project_root/research/papers_lu" -type f \
    -newermt '2026-09-01' ! -newermt '2026-09-20'
  find "$project_root/research/map/surveys/industry_scan_202609" \
    "$project_root/research/map/surveys/rescan_202609" \
    -type f 2>/dev/null
  find "$project_root/research/map/proposals" -type f
  find "$project_root/research/papers_lu/teardown-joint-20260813/_codex_20260824/onboarding_preflight" -type f
  find "$project_root/progress/audits/2026/09/2026-09-08__research-inventory" -type f
  find "$project_root/progress/audits/2026/09/2026-09-16__jinzu-and-research-infra-landscape" -type f
  find "$project_root/progress/exports/2026-09-08__research-desk-mobile" -type f
  find /mnt/d/MyResearch/research_growth -type f \
    -not -path '*/.git/*' \
    -newermt '2026-09-01' ! -newermt '2026-09-20'
  printf '%s\n' \
    "$project_root/learning/一些讨论.md" \
    "$project_root/research/papers_lu/teardown-joint-20260813/_codex_20260827/CONTROLLER_SYNTHESIS.md" \
    "$project_root/research/papers_lu/teardown-joint-20260813/_codex_20260827/LU_TO_SUN_LEARNING_AND_PORTFOLIO_PACK.md" \
    "$project_root/research/papers_lu/teardown-joint-20260813/_codex_20260827/agent_f_onboarding_learning/E1_TECHNICAL_FIT_BRIEF_20260827.md" \
    "/mnt/d/MyResearch/HANDOFF_2026-09-08__ex01-hash-status-and-ccf-youbo-intake.md" \
    "/mnt/d/Edge下载/学习与科研体系-整合版.md" \
    "/mnt/d/Edge下载/鲁组进组准备-执行细化-v1.0-2026-09-08 (1).md" \
    "/mnt/d/Edge下载/第二条研究线-方向恢复与双入口试探-2026-09-08 (1).md" \
    "/mnt/d/Edge下载/学习科研规划回看与系统性科研补充-2026-09-07.md" \
    "/mnt/d/Edge下载/ChatGPT-分支_·_重构进组计划.md" \
    "/mnt/d/Edge下载/ChatGPT-重构进组计划.md" \
    "/mnt/d/Edge下载/研究操作符与横向迁移案例册.md" \
    "/mnt/d/Edge下载/科研学习与训练体系-v0.1.md" \
    "/mnt/d/Edge下载/博士生科研入门辅导.pdf" \
    "/mnt/d/Alkaid/Desktop/工作簿1.xlsx" \
    "/mnt/d/Alkaid/Desktop/0908最近科研/CCF优博成长.pdf" \
    "/mnt/d/xwechat_files/wxid_74cug3zn6dzm22_1a1d/msg/file/2026-09/CCF优博成长.docx" \
    "/mnt/d/xwechat_files/wxid_74cug3zn6dzm22_1a1d/msg/file/2026-09/ccf优博系列(1).pdf" \
    "$project_root/learning/methodology/RESEARCH_METHODOLOGY.md" \
    "$project_root/progress/handoff/INDEX.md" \
    "$project_root/progress/task_logs/INDEX.md" \
    "$project_root/progress/lines/outreach.md" \
    "$project_root/progress/projects/lu-side.md" \
    "$project_root/progress/runbooks/research-desk-mobile-handoff.md" \
    "$project_root/progress/exports/科研台手机带学包_20260908_v0.1.zip" \
    "$project_root/progress/handoff/2026-09-01__workbench-v2-wp0-codex-execution__handoff.md" \
    "$project_root/progress/task_logs/2026/09/2026-09-01__maintenance__workbench-v2-wp0-codex-execution.md" \
    "$project_root/progress/task_logs/2026/08/2026-08-30__research__bridge-lu-two-week-masterplan-alignment.md" \
    "$project_root/progress/handoff/2026-09-15__ownership-v3-window-archive/WINDOW-ARCHIVE-MANIFEST-20260915.sha256" \
    "/mnt/d/workspace/Desks/vaults/Research-Garden/learning/group-entry/README.md" \
    "/mnt/d/workspace/Desks/vaults/Research-Garden/learning/group-entry/SOURCES.md" \
    "/mnt/d/workspace/Desks/vaults/Research-Garden/learning/group-entry/FILES.tsv" \
    "/mnt/d/workspace/Desks/vaults/Research-Garden/learning/group-entry/LINK_CHECK.md"
} | awk 'NF' | sort -u > "$raw_list"

{
  printf 'project_or_paper\tscope\tkind\tsource_path\tmtime_local\tbytes\tsha256\tpackage_path\tmaterialized_from\n'
  : > "$missing_manifest"
  while IFS= read -r source_path; do
    lower_source_path="${source_path,,}"
    case "$lower_source_path" in
      */_sealed/*|*/answer_key*|*/examiner*|*/final_oral*|*/holdout*|*/exam_sop.md|*/validate_assets.py|*/validate_learning.py|*/light_mode.md|*/08_teaching_pack.md)
        continue
        ;;
    esac
    copy_source="$source_path"
    materialized_from='current_source'
    recorded_mtime=''
    if [[ ! -f "$source_path" ]]; then
      vault_relative="$(awk -F '\t' -v wanted="$source_path" '$2 == wanted {print $3; exit}' "$snapshot_manifest")"
      recorded_mtime="$(awk -F '\t' -v wanted="$source_path" '$2 == wanted {print $5; exit}' "$snapshot_manifest" | tr -d '\r')"
      snapshot_fallback="/mnt/d/workspace/Desks/vaults/Research-Garden/$vault_relative"
      if [[ -n "$vault_relative" && -f "$snapshot_fallback" ]]; then
        copy_source="$snapshot_fallback"
        materialized_from="2026-09-17_snapshot:$snapshot_fallback"
      else
        printf '%s\n' "$source_path" >> "$missing_manifest"
        continue
      fi
    fi
    case "$source_path" in
      "$project_root"/*)
        relative_path="${source_path#"$project_root"/}"
        ;;
      /mnt/d/MyResearch/*)
        relative_path="OUTER_MyResearch/${source_path#/mnt/d/MyResearch/}"
        ;;
      /mnt/d/Edge下载/*)
        relative_path="Edge下载/${source_path#/mnt/d/Edge下载/}"
        ;;
      /mnt/d/Alkaid/Desktop/*)
        relative_path="Alkaid_Desktop/${source_path#/mnt/d/Alkaid/Desktop/}"
        ;;
      /mnt/d/xwechat_files/*)
        relative_path="xwechat_files/${source_path#/mnt/d/xwechat_files/}"
        ;;
      /mnt/d/workspace/Desks/vaults/Research-Garden/learning/group-entry/*)
        relative_path="ResearchGardenSnapshot/${source_path#/mnt/d/workspace/Desks/vaults/Research-Garden/learning/group-entry/}"
        ;;
      *)
        relative_path="External/${source_path#/}"
        ;;
    esac
    group_path="$(classify_group "$source_path")"
    subpath="$(classify_subpath "$relative_path")"
    kind="$(classify_kind "$source_path")"
    destination="$package_root/$group_path/$subpath"
    mkdir -p "$(dirname "$destination")"
    cp -p -- "$copy_source" "$destination"

    if [[ -n "$recorded_mtime" ]]; then
      mtime_local="$recorded_mtime"
      mtime_epoch="$(date -d "$recorded_mtime" +%s)"
    else
      mtime_local="$(stat -c '%y' "$copy_source")"
      mtime_epoch="$(stat -c '%Y' "$copy_source")"
    fi
    bytes="$(stat -c '%s' "$copy_source")"
    sha256="$(sha256sum "$copy_source" | awk '{print $1}')"
    package_path="$group_path/$subpath"
    in_snapshot='no'
    if grep -Fxq -- "$source_path" "$snapshot_sources"; then
      in_snapshot='yes'
    fi
    in_september='no'
    if (( mtime_epoch >= september_start_epoch && mtime_epoch < september_end_epoch )); then
      in_september='yes'
    fi
    case "$in_snapshot:$in_september" in
      yes:yes) scope='九月产出_0917学习包已纳入' ;;
      yes:no) scope='存量学习包_0917整理纳入' ;;
      no:yes) scope='九月新增或相关产出' ;;
      *) scope='进组相关存量材料' ;;
    esac
    printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
      "$group_path" "$scope" "$kind" "$source_path" "$mtime_local" "$bytes" "$sha256" "$package_path" "$materialized_from"

    group_index_tmp="$package_root/$group_path/.INDEX.unsorted.tsv"
    if [[ ! -e "$group_index_tmp" ]]; then
      printf 'scope\tkind\tmtime_local\tsource_path\tpackage_path\n' > "$group_index_tmp"
    fi
    printf '%s\t%s\t%s\t%s\t%s\n' "$scope" "$kind" "$mtime_local" "$source_path" "$package_path" >> "$group_index_tmp"
  done < "$raw_list"
} > "$manifest_unsorted"

{
  head -n 1 "$manifest_unsorted"
  tail -n +2 "$manifest_unsorted" | sort -t $'\t' -k5,5r -k1,1 -k4,4
} > "$manifest"

{
  head -n 1 "$manifest"
  tail -n +2 "$manifest" \
    | awk -F '\t' '$3 == "计划或决策" || $3 == "交接与恢复" || $3 == "任务日志" || $3 == "审计与核验" || $3 == "手册与规则" || $3 == "项目卡"'
} > "$plans_manifest"

while IFS= read -r -d '' group_index_tmp; do
  group_index="${group_index_tmp%/.INDEX.unsorted.tsv}/INDEX_时间倒序.tsv"
  {
    head -n 1 "$group_index_tmp"
    tail -n +2 "$group_index_tmp" | sort -t $'\t' -k3,3r -k4,4
  } > "$group_index"
  rm -f "$group_index_tmp"
done < <(find "$package_root" -name '.INDEX.unsorted.tsv' -print0)

{
  printf 'project_or_paper\tfile_count\n'
  tail -n +2 "$manifest" | awk -F '\t' '{count[$1]++} END {for (name in count) print name "\t" count[name]}' | sort
} > "$package_root/00_按项目与论文计数.tsv"

total_count="$(( $(wc -l < "$manifest") - 1 ))"
plan_count="$(( $(wc -l < "$plans_manifest") - 1 ))"
unclassified_count="$(awk -F '\t' '$1 == "99_待人工复核归类" {count++} END {print count+0}' "$manifest")"
september_count="$(awk -F '\t' 'NR > 1 && $2 ~ /^九月/ {count++} END {print count+0}' "$manifest")"
snapshot_expected_count="$(wc -l < "$snapshot_sources")"
snapshot_copied_count="$(awk -F '\t' 'NR > 1 && ($2 == "九月产出_0917学习包已纳入" || $2 == "存量学习包_0917整理纳入") {count++} END {print count+0}' "$manifest")"
missing_count="$(wc -l < "$missing_manifest")"
printf 'total_files=%s\nseptember_files=%s\nplan_and_status_files=%s\nlearning_snapshot_expected=%s\nlearning_snapshot_copied=%s\nunclassified_files=%s\nmissing_files=%s\n' \
  "$total_count" "$september_count" "$plan_count" "$snapshot_expected_count" "$snapshot_copied_count" "$unclassified_count" "$missing_count" > "$package_root/COUNTS.txt"

rm -f "$raw_list" "$snapshot_sources" "$manifest_unsorted"
