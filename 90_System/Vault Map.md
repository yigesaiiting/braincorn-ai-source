---
title: Vault Map
type: guide
domain: all
status: active
created: 2026-05-08
updated: 2026-05-08
source: 90_System/CODEX.md
tags: [guide, system, vault]
aliases: ["Vault Map"]
---

# Vault Map

## Layering

- `00_Inbox/`: 临时收集箱，先收后分流。
- `10_Raw/`: 原始资料层，只收集，不改写。
- `20_Wiki/`: 可复用知识层，概念 / 公司 / 人物 / 方法论 / 产品。
- `30_Projects/`: 正在推进的项目工作台。
- `40_Decisions/`: 关键决策与复盘。
- `50_Outputs/`: 研究、报告、PRD、文案、周报等输出沉淀。
- `90_System/`: 规则、模板、prompt、导航页。

## Recommended Flow

1. 资料先进 `00_Inbox/` 或 `10_Raw/`。
2. 通过 prompt 编译成 wiki / project / decision / output。
3. 所有重要输出都回链到相关 wiki。
4. 定期跑 `Wiki Lint` 检查断链和空页。

## Naming

- 正式 wiki 页面尽量带 frontmatter。
- 索引页统一叫 `Index.md`。
- 系统说明页放在 `90_System/`。
