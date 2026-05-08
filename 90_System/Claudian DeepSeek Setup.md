---
title: Claudian DeepSeek Setup
type: system
domain: ai_tools
status: active
created: 2026-05-08
updated: 2026-05-08
source: .obsidian/plugins/claudian/data.json
tags: [claudian, deepseek, codex]
---

# Claudian DeepSeek Setup

Claudian 已通过 Codex provider 接入 DeepSeek 的 OpenAI-compatible API。

## 当前配置

配置文件：`.obsidian/plugins/claudian/data.json`

```text
OPENAI_BASE_URL=https://api.deepseek.com
OPENAI_API_KEY=YOUR_DEEPSEEK_API_KEY
OPENAI_MODEL=deepseek-v4-flash
```

## 启用步骤

1. 打开 DeepSeek 控制台，创建 API key。
2. 在 Obsidian 中打开 Settings -> Community plugins -> Claudian -> Codex。
3. 找到 Codex provider 的 Environment variables。
4. 把 `YOUR_DEEPSEEK_API_KEY` 替换成真实 key。
5. 重启 Obsidian，或禁用再启用 Claudian。
6. 新建 Claudian tab，provider 选择 Codex，模型应显示 `deepseek-v4-flash`。

## 可选模型

- `deepseek-v4-flash`: 默认，速度和成本更适合日常 wiki 编译。
- `deepseek-v4-pro`: 更适合复杂推理、长文重写、代码和结构设计。

切换到 pro 时，把环境变量改为：

```text
OPENAI_MODEL=deepseek-v4-pro
```

## 注意

不要把真实 API key 写进公开 Git 仓库。如果之后要同步这个 vault，建议把 `.obsidian/plugins/claudian/data.json` 从 Git 中移除或改成私有仓库。
