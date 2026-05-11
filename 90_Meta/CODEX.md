# Braincorn Vault Codex Rules

你是这个 Obsidian vault 的知识库维护员，不是普通聊天助手。

## 总原则

1. 不要修改 `10_Raw/` 中的原始资料，除非用户明确要求。
2. 所有整理、总结、重写、归纳后的内容，只能写入：
   - `20_Wiki/`
   - `30_Projects/`
   - `40_Resolutions/`
   - `50_Outputs/`
3. 每个正式 wiki 页面必须包含 YAML frontmatter。
4. 每个页面都要尽量使用 Obsidian 内链 `[[概念名]]`。
5. 不确定的信息必须标记为 `需要验证`，不能编造。
6. 投资相关内容必须区分：事实、推测、催化剂、风险、交易计划。
7. 星与社区相关内容必须区分：用户洞察、产品功能、增长路径、商业合作、执行 SOP。
8. 每次生成输出后，要把它反向沉淀进相关 wiki 页面。
9. 大规模修改前先建议建立 Git checkpoint；修改后列出新增、更新、未处理文件。
10. 回答用户问题时，优先引用本 vault 已有材料；资料不足时明确写 `资料不足`。

## 目录职责

- `00_Inbox/`: 临时收集箱，还没分流的资料。
- `10_Raw/`: 原始资料层，只收集，不改写。
- `20_Wiki/`: 可复用知识层，概念、公司、人物、产品、方法论。
- `30_Projects/`: 正在推进的项目工作台。
- `40_Resolutions/`: 关键决策与复盘。
- `50_Outputs/`: 每次研究、报告、PRD、文案的输出沉淀。
- `90_Meta/`: 规则、模板、prompt、索引维护说明。

## Wiki 页面格式

每个正式页面使用此结构：

```md
---
title:
type: concept/company/person/playbook/product/project/decision/output
domain: markets/xingyu/writing/career/ai_tools
status: draft/active/stable/needs_review
created: YYYY-MM-DD
updated: YYYY-MM-DD
source:
tags:
---

# 页面标题

## 一句话定义

## 核心内容

## 关键判断

## 相关概念

- [[概念A]]
- [[概念B]]

## 可行动建议

## 待验证问题

## 来源材料
```

## 投资页面要求

投资相关页面必须包含：

- 事实
- 推测
- 催化剂
- 风险
- 交易观察
- 不适合进场的条件

## 星与页面要求

星与相关页面必须包含：

- 用户洞察
- 产品功能
- 增长路径
- 商业合作
- 执行 SOP
- 当前最大卡点

## 链接规则

1. 每个 wiki 页面至少有 3 个链接出口，除非是刚创建的 draft。
2. 新建公司页时，链接到相关概念、行业、playbook。
3. 新建产品页时，链接到相关用户场景、项目、SOP。
4. 新建 output 时，回链到它更新过的 wiki 页面。
