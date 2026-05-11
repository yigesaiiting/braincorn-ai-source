---
title: Vault Map
type: guide
domain: all
status: active
created: 2026-05-08
updated: 2026-05-08
source: Meta/CODEX.md
tags: [guide, system, vault]
aliases: ["Vault Map"]
---

# Vault Map

## Layering

- `Inbox/`: 临时收集箱，先收后分流。
- `Raw/`: 原始资料层，只收集，不改写。
- `Wiki/`: 可复用知识层，概念 / 公司 / 人物 / 方法论 / 产品。
- `Projects/`: 正在推进的项目工作台。
- `Resolutions/`: 关键决策与复盘。
- `Outputs/`: 研究、报告、PRD、文案、周报等输出沉淀。
- `Meta/`: 规则、模板、prompt、导航页。

## Recommended Flow

1. 资料先进 `Inbox/` 或 `Raw/`。
2. 通过 prompt 编译成 wiki / project / decision / output。
3. 所有重要输出都回链到相关 wiki。
4. 定期跑 `Wiki Lint` 检查断链和空页。

## Naming

- 正式 wiki 页面尽量带 frontmatter。
- 索引页统一叫 `Index.md`。
- 系统说明页放在 `Meta/`。
