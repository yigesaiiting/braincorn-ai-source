---
title: Git 使用说明
type: guide
domain: all
status: active
created: 2026-05-09
updated: 2026-05-09
source: Meta/README.md
tags: [guide, system, git]
aliases: ["Git 提交流程", "Braincorn Git 使用说明"]
---

# Git 使用说明

这是 Braincorn vault 的推荐 Git 提交流程。

## 仓库根目录

```bash
/Users/yaoyuan/Documents/Braincorn/Braincorn
```

以后所有 Git 操作默认先进入这个目录：

```bash
cd /Users/yaoyuan/Documents/Braincorn/Braincorn
```

## 日常提交流程

### 1. 查看状态

```bash
git status --short --branch
```

重点看：

- 当前分支是否是 `main`
- 有没有不想提交的文件
- 有没有大规模误改

### 2. 查看变更

```bash
git diff --stat
git diff --name-only
```

如果要看某个文件：

```bash
git diff path/to/file.md
```

### 3. 暂存变更

如果确认都要提交：

```bash
git add .
```

如果只提交部分文件，建议显式指定路径：

```bash
git add Wiki/Index.md Meta/README.md
```

### 4. 提交

```bash
git commit -m "your message"
```

推荐提交信息风格：

- `add vault usage guide`
- `update INOD model`
- `refine trading playbook`
- `fix wiki links`

### 5. 推送

```bash
git push
```

首次或重新绑定远端时可用：

```bash
git push -u origin main
```

## 常见问题

### 1. push 失败：认证问题

先检查：

```bash
gh auth status
```

如果没登录：

```bash
gh auth login
```

### 2. push 失败：HTTP/2 framing error

可固定使用 HTTP/1.1：

```bash
git config --global http.version HTTP/1.1
```

然后再推送：

```bash
git push
```

### 3. 远端不存在或仓库名不对

检查 remote：

```bash
git remote -v
```

## 建议的长期配置

```bash
git config --global user.name "yigesaiiting"
git config --global user.email "mgmtape@gmail.com"
```

## 习惯建议

- 大改前先看状态。
- 大改后先提交再继续。
- 尽量按主题提交，不要攒太久。
- 如果不确定是否该提交，先问我。

