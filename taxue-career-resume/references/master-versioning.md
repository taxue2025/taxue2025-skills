# 简历母版与投递版本管理（产出层）

> 母版是唯一的简历数据真源，所有投递版本从母版派生。改简历只改母版，投递只动版本——避免「一份简历改 50 次，每份都不一样」。

## 1. 核心模型

```
母版（master）—— 完整、未裁剪、覆盖全部经历与量化成果的数据源
   │  派生（渲染时裁剪/排序/覆盖，母版不动）
   ▼
投递版本（version）—— 针对某一 JD 的定制输出：HTML + ATS 文本 + 匹配报告
```

- **母版只增不减**：真实经历全部保留，不因某个岗位不合适就删母版内容，只在该岗位的定制版里排除。
- **定制只发生在版本层**：任何针对具体 JD 的措辞、排序、裁剪都写进 `custom.json`，不回写母版。这样同一个母版可以派生任意多版本，互不污染。

## 2. 简历工作区（目录约定）

用户未指定时，默认在 `<工作目录>/resume-workspace/` 下创建：

```
resume-workspace/
├── master/
│   ├── master.json          # 母版数据（真源，字段见 assets/master-template.json）
│   └── master-notes.md      # 母版变更记录（每次更新记一行：日期 + 改了什么 + 为什么）
├── versions/
│   └── YYYY-MM-DD_公司_岗位/
│       ├── custom.json      # 该版本的定制配置（order/exclude/overrides）
│       ├── resume.html      # 独立 HTML（浏览器打开 → 打印为 PDF）
│       ├── resume.txt       # ATS 纯文本（渲染脚本自动生成）
│       └── match-report.md  # jd_resume_match.py 自检结果 + 投放备注
└── README.md                # 版本索引：每个版本一行（日期/公司/岗位/版本号/状态）
```

版本目录命名 `YYYY-MM-DD_公司_岗位` 保证按时间排序、不覆盖历史版本。同一天投同一家公司多个岗位时，岗位名区分。

## 3. 建立母版

两条路径，二选一或组合：

### 路径 A：从已有简历解析
1. 读入现有简历（文本/PDF 提取/旧 HTML）。
2. 按 `assets/master-template.json` 的字段结构整理成 `master.json`。
3. 解析时只转写不评判；缺量化数字的经历，采访用户补数字，补不上则如实保留描述并标记「待量化」。

### 路径 B：从真实经历采访（模式 D 的产出层）
1. 走 SKILL.md 模式 D 的 9 模块问答收集（基本信息 → 教育 → 补充 → 工作 → 项目 → 实习 → 竞赛 → 技能 → 其他）。
2. 每段经历按 STAR 追问：情境 / 任务 / 动作 / 结果（结果必须给数字或量级）。
3. 收集完直接填入 `master.json`，无需中间格式。

**证据硬门**：用户没提供的经历、数字、案例不得编造；补数字必须来自用户口述并标注。

## 4. 派生投递版本

拿到目标 JD 后，一个版本的生产流程：

1. **JD 解码**：用 `references/jd-decoding.md` 四步法提取硬门槛 / 核心要求 / 加分项 / 关键词。
2. **写 custom.json**（字段见 render_resume.py 头部示例）：
   - `order`：把和目标岗位最相关的 section 提前（如技术岗把 projects 提到 experience 前）。
   - `exclude`：排除与岗位无关的经历/项目（`{"experience": ["e3"]}`）。
   - `overrides.summary`：按 JD 重写价值主张，植入硬门槛关键词。
   - `overrides.skills.hard`：只留与 JD 匹配的技能，按 JD 出现顺序排列。
3. **渲染**：
   ```bash
   python3 <skill目录>/scripts/render_resume.py master/master.json \
     --custom versions/YYYY-MM-DD_公司_岗位/custom.json \
     --out versions/YYYY-MM-DD_公司_岗位/resume.html
   ```
   同时产出 `resume.txt`（ATS 纯文本）和打印页数估算。
4. **ATS 自检**：对 `resume.txt` 跑 `scripts/jd_resume_match.py`（硬门槛 / 技能覆盖 / 量化指标 / 匹配分），结果写 `match-report.md`。硬门槛缺失 → 回第 2 步补关键词或如实接受；技能覆盖 < 70% → 检查是否投错岗。
5. **交付**：打开 `resume.html` 确认版式 → 浏览器打印为 PDF（A4、边距默认）→ 按 `姓名-岗位-手机号.pdf` 命名投递。

**版本不可变**：一旦投出，该版本目录不再修改；要改就新建一个版本（新日期目录）。历史版本是投递记录，不是草稿区。

## 5. 版本维护操作

| 操作 | 做法 |
|------|------|
| 新增版本 | 按第 4 节建新目录，README 加一行 |
| 更新母版（涨经历/改数字） | 只改 `master/master.json` + `master-notes.md` 记一笔；已投版本不动 |
| 重投旧岗位 | 基于母版重新派生（旧版本可能已过时），不直接改旧版本目录 |
| 清理 | 确认已失效的版本目录整体移入 `.trash/`，命名 `YYYY-MM-DD_原名` |
| 复盘 | 看 `README.md` + 各版本 `match-report.md`，统计哪类岗位匹配分高、回复率高 |

## 6. 与技能现有能力的衔接

- 模式 A（简历+JD 改写）、模式 B（仅简历）、模式 C（仅 JD）的输出落点统一为 **custom.json + 渲染**，不再输出散装文本简历。
- 模式 D（从零创建）的终点是 **master.json**，而不是一次性简历文本。
- `jd_resume_match.py`（ATS 匹配）是版本生产的质检步骤，不是可选动作。
- 诊断规则（ATS 关键词、STAR、10 秒测试、Summary 三要素）全部适用于母版和版本两层：母版保证每条经历达标，版本保证与 JD 对齐。

## 7. 边界与禁忌

- 母版 JSON 是机读真源，不要手工排版；排版交给模板。
- 不要在 `resume.html` 里堆自定义 CSS——模板样式是唯一样式，改样式改 `assets/resume-template.html`，版本里不动。
- 简历 HTML 是独立单文件：无外部 CDN、无网络依赖、无 JS 依赖，离线也能打开打印。
- 禁止把定制版内容合并回母版（污染真源）；禁止删母版里的「没用上」的经历（用 exclude 而不是删除）。
