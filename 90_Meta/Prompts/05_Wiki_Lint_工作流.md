---
title: Wiki Lint 工作流
type: prompt
domain: system
status: active
created: 2026-05-08
updated: 2026-05-08
source: 90_Meta/Prompts/05_Wiki_Lint_工作流.md
tags: [prompt, workflow]
aliases: ["Wiki Lint 工作流"]
---
# Wiki Lint 工作流

请对整个 Braincorn vault 做一次 wiki lint。

检查：
1. 有没有孤立页面。
2. 有没有没有 YAML frontmatter 的页面。
3. 有没有断掉的 Obsidian 双链。
4. 有没有重复概念，比如 “AI基础设施” 和 “AI Infra” 是否应合并。
5. 有没有股票页面缺少风险项。
6. 有没有星与产品页面缺少用户场景。
7. 输出一份 `50_Outputs/Weekly_Reviews/wiki_lint_YYYY-MM-DD.md`。
8. 不要自动删除文件，只提出修改建议。
