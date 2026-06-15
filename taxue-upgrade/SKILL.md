---
name: taxue-upgrade
version: "2.8"
description: |
  升级 taxue 系列 skills 到最新版本。
  触发：/taxue-upgrade、升级到最新版本、检查skill更新、更新、版本、taxue升级。
  EN: "upgrade taxue", "check for updates", "update skills", "latest version".
---

# taxue-upgrade：版本管理

> 一键同步，永不过时。

---

## 核心流程

### Step 1：检测本地版本

扫描 `~/.claude/skills/` 目录下所有 taxue 系列 skill。

### Step 2：对比远程版本

```
本地版本 == 远程版本 → 已是最新
本地版本 < 远程版本  → 可升级
本地版本 > 远程版本  → 🔔 本地修改（询问是否覆盖）
```

### Step 3：交互式升级

列出可升级清单，用户选择升级全部或指定 skill。

### Step 4：执行升级

备份当前版本 → 下载新版本 → 验证 → 完成。

---
---

*taxue-upgrade v2.8*
