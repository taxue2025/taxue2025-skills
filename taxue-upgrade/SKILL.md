---
name: taxue-upgrade
description: |
  升级 taxue、zaoren、ming 系列 skills 到最新版本。

  触发：/upgrade、更新skill、升级、skill版本、检查更新、
  我的skill是不是过时了、怎么更新到最新版。
---

# taxue-upgrade：版本管理

> 一键同步，永不过时。

---

## 核心流程

### Step 1：检测本地版本

扫描 `~/.claude/skills/` 目录下所有相关 skill：

| 系列 | 匹配模式 |
|:---|:---|
| taxue 系列 | `taxue*` |
| zaoren 系列 | `zaoren*` |
| ming 系列 | `ming*` |

### Step 2：对比远程版本

**版本对比规则**：
```
本地版本 == 远程版本 → ✅ 最新
本地版本 < 远程版本  → ⚠️ 可升级
本地版本 > 远程版本  → 🔔 本地修改
未识别版本           → ❓ 未知
```

### Step 3：交互式升级

```
发现 3 个 skill 可升级：

1. zaoren-boss    本地: v3.1  →  远程: v4.0  [推荐]
2. taxue-build    本地: v2.0  →  远程: v2.1  [推荐]

操作：
- 输入数字升级指定 skill
- 输入 all 升级全部
- 输入 skip 跳过
```

### Step 4：执行升级

**升级前自动备份**：
```
~/.claude/skills/.backup/YYYY-MM-DD-HHMMSS/
```

### Step 5：验证与回滚

**回滚机制**：
```
/upgrade --rollback 2026-04-07-143022
```

---

## 命令列表

| 命令 | 功能 |
|:---|:---|
| `/upgrade` | 检测并列出可升级 skill |
| `/upgrade all` | 升级全部 |
| `/upgrade [name]` | 升级指定 skill |
| `/upgrade --check` | 只检测 |
| `/upgrade --list` | 列出所有已安装版本 |
| `/upgrade --rollback [时间戳]` | 回滚 |
| `/upgrade --clean` | 清理旧备份 |

---

## 版本定义

在 SKILL.md 文件尾部添加：
```
---
*version: v4.0*
*updated: 2026-04-07*
*series: zaoren*
```

当前 taxue 版本：**v2.3**（2026-06）

---

## 备份位置

升级前备份会存放到以下位置（按优先级）：

| 优先级 | 位置 | 说明 |
|--------|------|------|
| 1 | `~/.claude/skills/.backup/YYYY-MM-DD-HHMMSS/` | 默认备份路径 |
| 2 | `.taxue-backups/` | 项目级全量备份 |
| 3 | `.taxue-backups/current/` | 最近一次手动备份 |

---

## 边界

- **不做**：自动更新（需要用户确认）
- **不做**：版本降级（除非 --rollback）
- **不做**：非官方 skill 更新
- **做**：备份、验证、回滚

---

*taxue-upgrade · 一键同步 · 永不过时*
