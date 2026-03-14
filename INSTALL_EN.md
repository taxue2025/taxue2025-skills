# Installation Guide

This guide will help you install Taxue2025 Skills into your AI coding assistant.

## Prerequisites

- Node.js 16+ installed
- An AI coding assistant that supports skills (Claude Code, Cursor, etc.)

## Quick Install

The simplest way to install using Vercel's skills CLI:

```bash
npx skills add taxue2025/taxue2025-skills
```

## Installation Options

### View Available Skills

Before installing, you can view all available skills in this repository:

```bash
npx skills add taxue2025/taxue2025-skills --list
```

### Install Specific Skills

If you only want to install specific skills:

```bash
npx skills add taxue2025/taxue2025-skills --skill ultimate-problem-solver
npx skills add taxue2025/taxue2025-skills --skill 哲思伙伴
```

### Global Installation

Install to global directory (available across all projects):

```bash
npx skills add taxue2025/taxue2025-skills -g
```

### Install to Specific Agent

If you have multiple AI coding assistants installed:

```bash
# Install only to Claude Code
npx skills add taxue2025/taxue2025-skills -a claude-code

# Install only to Cursor
npx skills add taxue2025/taxue2025-skills -a cursor

# Install to multiple agents
npx skills add taxue2025/taxue2025-skills -a claude-code -a cursor
```

### Non-Interactive Installation

For CI/CD environments or automated scripts:

```bash
npx skills add taxue2025/taxue2025-skills --all -y
```

---

## Manual Installation

If you cannot use the `npx skills` command, you can install manually:

### 1. Clone the Repository

```bash
git clone https://github.com/taxue2025/taxue2025-skills.git
cd taxue2025-skills
```

### 2. Copy Skill Files

Copy skill files to the appropriate directory based on your AI coding assistant:

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

**Other Agents**:
Please refer to your Agent's documentation to find the skills directory location.

### 3. Restart Agent

After installation, restart your AI coding assistant or wait for it to auto-load the new skills.

---

## Verify Installation

After installation, you can verify by:

1. **List installed skills**:
   ```bash
   npx skills list
   ```

2. **Test trigger words**:
   Enter trigger words in conversation, such as "Help me solve this problem", to see if the corresponding skill activates.

---

## Update Skills

### Update Using CLI

```bash
# Check for updates
npx skills check

# Update all skills
npx skills update
```

### Manual Update

```bash
# Enter repository directory
cd taxue2025-skills

# Pull latest code
git pull origin main

# Re-copy skill files
cp -r skills/* ~/.claude/skills/
```

---

## Uninstall Skills

### Uninstall Using CLI

```bash
# Uninstall specific skill
npx skills remove ultimate-problem-solver

# Uninstall all skills
npx skills remove --all
```

### Manual Uninstall

Simply delete the corresponding skill directories:

```bash
rm -rf ~/.claude/skills/ultimate-problem-solver
rm -rf ~/.claude/skills/哲思伙伴
# ... other skills
```

---

## Troubleshooting

### Issue: Skill Not Triggering

**Possible Causes**:
1. Skill files not copied to the correct directory
2. Agent not reloaded
3. Trigger words don't match

**Solutions**:
1. Check if skill files are in the correct directory
2. Restart the Agent
3. Try using more precise trigger words

### Issue: Permission Error During Installation

**Solution**:
```bash
# Use sudo (not recommended unless necessary)
sudo npx skills add taxue2025/taxue2025-skills

# Or change directory permissions
sudo chown -R $(whoami) ~/.claude
```

### Issue: Installation Fails on Windows

**Solutions**:
1. Ensure Git for Windows is installed
2. Use PowerShell or Git Bash to run commands
3. Manually copy files to `%USERPROFILE%\.claude\skills\`

---

## Supported Agents

This skill library supports the following AI coding assistants:

| Agent | Installation Path |
|-------|-------------------|
| Claude Code | `~/.claude/skills/` |
| Cursor | `~/.cursor/skills/` |
| OpenCode | `~/.config/opencode/skills/` |
| Codex | `~/.codex/skills/` |
| Cline | `~/.cline/skills/` |
| Roo Code | `~/.roo/skills/` |
| Continue | `~/.continue/skills/` |
| Windsurf | `~/.codeium/windsurf/skills/` |

For more Agent support, please refer to [Vercel Skills CLI Documentation](https://github.com/vercel-labs/skills).

---

## Get Help

- **GitHub Issues**: [https://github.com/taxue2025/taxue2025-skills/issues](https://github.com/taxue2025/taxue2025-skills/issues)
- **Documentation**: [README_EN.md](./README_EN.md)
- **中文指南**: [INSTALL.md](./INSTALL.md)
