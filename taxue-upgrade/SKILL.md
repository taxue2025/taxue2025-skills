---
name: taxue-upgrade
description: |
  升级 taxue 系列 skills 到最新版本
  触发：/taxue-upgrade、/升级taxue、「升级踏雪技能」
---

# taxue-upgrade

升级 taxue 系列 skills 到最新版本，显示更新内容和版本变化。

## 支持的 Skills

taxue 系列核心 skills：
- `taxue` —— 问题解决入口
- `taxue-build` —— 系统构建
- `taxue-learn` —— 学习方法
- `taxue-roundtable` —— 圆桌讨论

## 升级流程

### Step 1: 检测安装位置

```bash
SKILL_DIRS=""
for dir in "$HOME/.config/agents/skills" "$HOME/.claude/skills" "$HOME/.agents/skills"; do
  if [ -d "$dir/taxue" ]; then
    SKILL_DIRS="$dir"
    echo "Install location: $dir"
    break
  fi
done

if [ -z "$SKILL_DIRS" ]; then
  echo "ERROR: taxue skills not found in standard locations"
  echo "Searched: ~/.config/agents/skills, ~/.claude/skills, ~/.agents/skills"
  exit 1
fi
```

### Step 2: 获取当前版本

```bash
OLD_VERSION="unknown"
VERSION_FILE="$SKILL_DIRS/taxue/README.md"

if [ -f "$VERSION_FILE" ]; then
  # 从 README.md 中提取版本号（格式：踏雪问题解决系统 vX.Y）
  OLD_VERSION=$(grep -oE 'v[0-9]+\.[0-9]+' "$VERSION_FILE" | head -1 || echo "unknown")
fi

echo "Current version: $OLD_VERSION"
```

### Step 3: 获取远程版本

```bash
REMOTE_VERSION=""
REMOTE_URL="https://raw.githubusercontent.com/taxueseek/taxueskills/main/VERSION"

# 尝试从 GitHub 获取版本
REMOTE_VERSION=$(curl -sL --connect-timeout 5 "$REMOTE_URL" 2>/dev/null || echo "")

if [ -z "$REMOTE_VERSION" ]; then
  echo "INFO: Cannot fetch remote version from GitHub"
  echo "Remote repository: https://github.com/taxueseek/taxueskills"
  echo ""
  echo "Possible reasons:"
  echo "  - Network connection issue"
  echo "  - Repository not yet published"
  echo "  - GitHub API rate limit"
  echo ""
  echo "You can manually check for updates at:"
  echo "  https://github.com/taxueseek/taxueskills/releases"
  exit 0
fi

echo "Remote version: $REMOTE_VERSION"
```

### Step 4: 比较版本

如果 `OLD_VERSION` 等于 `REMOTE_VERSION`：

```
taxue skills 已是最新版本（REMOTE_VERSION）！

当前安装的 skills：
- taxue (OLD_VERSION)
- taxue-build
- taxue-learn
- taxue-roundtable

无需升级。
```

否则继续升级。

### Step 5: 备份当前版本

```bash
BACKUP_DIR="$SKILL_DIRS/.taxue-backup-$(date +%Y%m%d-%H%M%S)"
mkdir -p "$BACKUP_DIR"

# 备份所有 taxue* 目录
for skill_dir in "$SKILL_DIRS"/taxue*; do
  if [ -d "$skill_dir" ]; then
    skill_name=$(basename "$skill_dir")
    if [ "$skill_name" != "taxue-upgrade" ]; then
      cp -r "$skill_dir" "$BACKUP_DIR/" 2>/dev/null || true
    fi
  fi
done

echo "Backup created: $BACKUP_DIR"
```

### Step 6: 下载最新版本

```bash
TMP_DIR=$(mktemp -d)
REPO_URL="https://github.com/taxueseek/taxueskills.git"

echo "Cloning from $REPO_URL..."
git clone --depth 1 "$REPO_URL" "$TMP_DIR/taxueskills" 2>&1

if [ $? -ne 0 ]; then
  echo "ERROR: Failed to clone repository"
  echo ""
  echo "Troubleshooting:"
  echo "  1. Check your internet connection"
  echo "  2. Verify the repository exists: $REPO_URL"
  echo "  3. Try running: git clone $REPO_URL"
  exit 1
fi

echo "Downloaded to: $TMP_DIR/taxueskills"
```

### Step 7: 验证下载内容

```bash
# 检查下载的内容结构是否正确
if [ ! -d "$TMP_DIR/taxueskills/skills" ] && [ ! -d "$TMP_DIR/taxueskills/taxue" ]; then
  echo "ERROR: Downloaded repository has unexpected structure"
  echo "Expected: skills/ or taxue/ directory"
  echo ""
  echo "Contents of downloaded directory:"
  ls -la "$TMP_DIR/taxueskills/"
  exit 1
fi
```

### Step 8: 替换旧版本

```bash
echo "Upgrading skills..."

# 确定源目录（支持两种结构）
if [ -d "$TMP_DIR/taxueskills/skills" ]; then
  SOURCE_DIR="$TMP_DIR/taxueskills/skills"
else
  SOURCE_DIR="$TMP_DIR/taxueskills"
fi

# 删除旧的 taxue* skills（保留 taxue-upgrade 本身）
for skill_dir in "$SKILL_DIRS"/taxue*; do
  if [ -d "$skill_dir" ]; then
    skill_name=$(basename "$skill_dir")
    if [ "$skill_name" != "taxue-upgrade" ]; then
      rm -rf "$skill_dir"
      echo "  Removed: $skill_name"
    fi
  fi
done

# 复制新版本
cp -r "$SOURCE_DIR"/taxue* "$SKILL_DIRS/" 2>/dev/null || true

# 清理临时目录
rm -rf "$TMP_DIR"

echo "Upgrade completed"
```

如果复制失败，从备份恢复：

```bash
if [ $? -ne 0 ]; then
  echo "ERROR: Upgrade failed, restoring from backup..."
  
  # 恢复备份
  for backup_skill in "$BACKUP_DIR"/taxue*; do
    if [ -d "$backup_skill" ]; then
      skill_name=$(basename "$backup_skill")
      rm -rf "$SKILL_DIRS/$skill_name"
      cp -r "$backup_skill" "$SKILL_DIRS/"
    fi
  done
  
  echo "Restored from backup: $BACKUP_DIR"
  exit 1
fi
```

### Step 9: 显示更新内容

```bash
# 尝试读取新版本号
NEW_VERSION="unknown"
if [ -f "$SKILL_DIRS/taxue/README.md" ]; then
  NEW_VERSION=$(grep -oE 'v[0-9]+\.[0-9]+' "$SKILL_DIRS/taxue/README.md" | head -1 || echo "unknown")
fi
```

输出格式：

```
===================================================
  taxue skills 升级成功！
===================================================

版本：OLD_VERSION -> NEW_VERSION

已更新的 skills：
- taxue —— 问题解决入口
- taxue-build —— 系统构建
- taxue-learn —— 学习方法
- taxue-roundtable —— 圆桌讨论

===================================================

更新要点：
- 从 CHANGELOG 或 git log 提取的更新内容
- 如需查看完整更新日志，访问：
  https://github.com/taxueseek/taxueskills/releases

===================================================

备份位置：BACKUP_DIR
保留 7 天后自动清理，或手动删除：
  rm -rf BACKUP_DIR
```

### Step 10: 验证安装

```bash
# 验证每个 skill 是否正确安装
echo ""
echo "验证安装..."

for skill in taxue taxue-build taxue-learn taxue-roundtable; do
  if [ -f "$SKILL_DIRS/$skill/SKILL.md" ]; then
    echo "  OK: $skill"
  else
    echo "  MISSING: $skill"
  fi
done
```

## 离线升级（手动模式）

如果无法连接 GitHub，支持手动升级：

```bash
# 用户手动下载并指定路径
taxue-upgrade --local /path/to/downloaded/taxueskills
```

流程：
1. 跳过 git clone 步骤
2. 使用用户提供的本地路径作为 SOURCE_DIR
3. 继续执行备份和替换流程

## 错误处理

| 错误场景 | 处理 |
|----------|------|
| 找不到本地 skills | 提示安装位置，退出 |
| 网络失败 | 提示手动下载选项，退出 |
| git clone 失败 | 从备份恢复，提示检查仓库地址 |
| 文件复制失败 | 从备份恢复，提示磁盘空间/权限问题 |
| 版本号无法解析 | 继续升级，但显示 unknown |

## 版本号规则

- 格式：v{major}.{minor}（如 v1.2）
- 从 taxue/README.md 中的版本声明提取
- 远程版本从 GitHub 仓库根目录的 VERSION 文件获取

## 备份策略

- 每次升级自动创建带时间戳的备份
- 备份保留 7 天，自动清理脚本：

```bash
# 添加到 crontab，每天运行
find "$SKILL_DIRS" -name ".taxue-backup-*" -type d -mtime +7 -exec rm -rf {} + 2>/dev/null
```

## 与 dbskill-upgrade 的对比

| 特性 | dbskill-upgrade | taxue-upgrade |
|------|-----------------|---------------|
| 安装路径 | ~/.claude/skills | 多路径支持 |
| 版本管理 | VERSION 文件 | README.md + VERSION |
| 仓库地址 | dontbesilent2025/dbskill | taxueseek/taxueskills |
| 升级范围 | 所有 dbs* skills | 所有 taxue* skills |
| 离线模式 | 不支持 | 支持 --local |
| 备份策略 | 手动清理 | 7天自动清理 |

## 注意事项

1. **只升级 taxue 系列**：不触碰其他 skills（career、dbs 等）
2. **保留 taxue-upgrade**：升级过程中不删除自身
3. **原子操作**：失败时自动回滚到备份版本
4. **GitHub 依赖**：默认从 https://github.com/taxueseek/taxueskills 获取更新

---

*taxue-upgrade v1.0 - 让踏雪 skills 保持最新*
