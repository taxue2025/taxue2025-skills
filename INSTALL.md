# 安装指南

本文档将指导你将 Taxue2025 Skills 安装到你的 AI 编程助手中。

## 环境要求

- 已安装 Node.js 16+
- 已安装支持 Skills 的 AI 编程助手（Claude Code、Cursor 等）

## 快速安装

使用 Vercel 的 skills CLI 工具一键安装：

```bash
npx skills add taxue2025/taxue2025-skills
```

## 安装选项

### 查看可用 Skill

安装前可以查看本仓库包含的所有 skill：

```bash
npx skills add taxue2025/taxue2025-skills --list
```

### 安装特定 Skill

如果只想安装特定的 skill：

```bash
npx skills add taxue2025/taxue2025-skills --skill ultimate-problem-solver
npx skills add taxue2025/taxue2025-skills --skill 哲思伙伴
```

### 全局安装

安装到全局目录（所有项目都可用）：

```bash
npx skills add taxue2025/taxue2025-skills -g
```

### 安装到特定 Agent

如果你安装了多个 AI 编程助手：

```bash
# 只安装到 Claude Code
npx skills add taxue2025/taxue2025-skills -a claude-code

# 只安装到 Cursor
npx skills add taxue2025/taxue2025-skills -a cursor

# 安装到多个 Agent
npx skills add taxue2025/taxue2025-skills -a claude-code -a cursor
```

### 非交互式安装

适用于 CI/CD 环境或自动化脚本：

```bash
npx skills add taxue2025/taxue2025-skills --all -y
```

---

## 手动安装

如果你无法使用 `npx skills` 命令，可以手动安装：

### 1. 克隆仓库

```bash
git clone https://github.com/taxue2025/taxue2025-skills.git
cd taxue2025-skills
```

### 2. 复制 Skill 文件

根据你使用的 AI 编程助手，将 skill 文件复制到对应目录：

**Claude Code**:
```bash
mkdir -p ~/.claude/skills
cp -r skills/* ~/.claude/skills/
```

**Cursor**:
```bash
mkdir -p ~/.cursor/skills
cp -r skills/* ~/.cursor/skills/
```

**其他 Agent**:
请参考对应 Agent 的文档，找到 skills 目录位置。

### 3. 重启 Agent

安装完成后，重启你的 AI 编程助手，或等待其自动加载新 skill。

---

## 验证安装

安装完成后，可以通过以下方式验证：

1. **查看已安装 skill 列表**：
   ```bash
   npx skills list
   ```

2. **测试触发词**：
   在对话中输入触发词，如「帮我解决这个问题」，看是否能激活对应 skill。

---

## 更新 Skill

### 使用 CLI 更新

```bash
# 检查更新
npx skills check

# 更新所有 skill
npx skills update
```

### 手动更新

```bash
# 进入仓库目录
cd taxue2025-skills

# 拉取最新代码
git pull origin main

# 重新复制 skill 文件
cp -r skills/* ~/.claude/skills/
```

---

## 卸载 Skill

### 使用 CLI 卸载

```bash
# 卸载特定 skill
npx skills remove ultimate-problem-solver

# 卸载所有 skill
npx skills remove --all
```

### 手动卸载

直接删除对应 skill 目录：

```bash
rm -rf ~/.claude/skills/ultimate-problem-solver
rm -rf ~/.claude/skills/哲思伙伴
# ... 其他 skill
```

---

## 故障排除

### 问题：Skill 没有触发

**可能原因**：
1. Skill 文件没有正确复制到目录
2. Agent 没有重新加载
3. 触发词不匹配

**解决方法**：
1. 检查 skill 文件是否在正确的目录
2. 重启 Agent
3. 尝试使用更精确的触发词

### 问题：安装时出现权限错误

**解决方法**：
```bash
# 使用 sudo（不推荐，除非必要）
sudo npx skills add taxue2025/taxue2025-skills

# 或更改目录权限
sudo chown -R $(whoami) ~/.claude
```

### 问题：Windows 系统安装失败

**解决方法**：
1. 确保已安装 Git for Windows
2. 使用 PowerShell 或 Git Bash 运行命令
3. 手动复制文件到 `%USERPROFILE%\.claude\skills\`

---

## 支持的 Agent

本 skill 库支持以下 AI 编程助手：

| Agent | 安装路径 |
|-------|----------|
| Claude Code | `~/.claude/skills/` |
| Cursor | `~/.cursor/skills/` |
| OpenCode | `~/.config/opencode/skills/` |
| Codex | `~/.codex/skills/` |
| Cline | `~/.cline/skills/` |
| Roo Code | `~/.roo/skills/` |
| Continue | `~/.continue/skills/` |
| Windsurf | `~/.codeium/windsurf/skills/` |

更多 Agent 支持请参考 [Vercel Skills CLI 文档](https://github.com/vercel-labs/skills)。

---

## 获取帮助

- **GitHub Issues**: [https://github.com/taxue2025/taxue2025-skills/issues](https://github.com/taxue2025/taxue2025-skills/issues)
- **文档**: [README.md](./README.md)
- **English Guide**: [INSTALL_EN.md](./INSTALL_EN.md)
