---
title: Banners Assets
type: system
domain: all
status: active
created: 2026-05-14
updated: 2026-05-14
source: user request
tags: [meta, banners, assets]
aliases: ["Banner Assets", "封面图资源"]
---

# Banners Assets

用于 Obsidian Banners 插件的封面图资源目录。

## 素材来源

- [[90_Meta/Banners/Typographic Posters Archive|Typographic Posters Archive]]

## 批量拉取

如果你想把这个站点的海报图批量拉到本地素材库，可以运行：

```bash
python3 90_Meta/Banners/scripts/download_typographicposters.py
```

默认会把前 200 张海报下载到：

```text
90_Meta/Banners/Typographic Posters Archive/
```

如需更多，可调整参数：

```bash
python3 90_Meta/Banners/scripts/download_typographicposters.py --max-items 500 --items-per-page 100 --variant poster
```

如果你想要更小的素材库，可以把 `--variant poster` 改成 `--variant thumb`。
默认文件会保存为 `.jpg`。

## 使用规则

- 只放适合做笔记封面的图片
- 优先使用横向图片
- 文件命名尽量简短、可识别
- 不要把日常截图和临时素材混进来

## 推荐用途

- `README` / `INDEX` 入口页
- `Projects` 主项目页
- `Outputs` 主要成果页
- 重点 `Wiki` 页面
