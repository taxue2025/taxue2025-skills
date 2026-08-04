# TaxueSkills README 视觉蓝图

**Visual thesis**：夜色雪径——深底上的清晰路径，决策像脚印一样可跟、可收敛。  
**Content plan**：先看清是什么 → 职业产出层实证 → 怎么装 → 怎么用 → 版本。  
**Interaction thesis**：静态纯 SVG，GitHub 暗/亮均可读；Markdown 承载正文与命令。

## Color Palette

| Token | Hex | Role |
|-------|-----|------|
| night | `#0B0F14` | 画布底 |
| snow | `#F4F1EA` | 主文字 |
| ice | `#8EC8D6` | 强调 / 路径节点 |
| trail | `#3D5A66` | 次级线 / 静默结构 |
| mist | `#8B919A` | 元信息 / 说明 |

## Typography

- 系统无衬线：`-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif`
- 等宽元信息：`ui-monospace, SFMono-Regular, Menlo, monospace`
- 层级：Hero 标题 ≥48 / 副标 20 / 节点标签 ≥18

## Shape & Motif

- 圆角 26；描边 1.2；间距 8 的倍数
- **Motif**：雪迹点列（step trail）——每一步决策一个节点
- 密度：技术编辑风，留白优先于装饰

## Do's / Don'ts

- Do：用真实链路（career pipeline）作 proof
- Do：第一屏说清「决策系统，不是 prompt 箱」
- Don't：紫渐变 SaaS 模板、假截图、无证据的数字
- Don't：远程字体 / foreignObject / SVG 内动画

## Decision Trace

| Decision | Chose | Rejected | Why |
|----------|-------|----------|-----|
| 实现 | 纯 SVG | Hybrid/ImageGen | 确定性强、易维护、主题是路径而非角色 |
| 主色 | 夜底 + 冰蓝 | 纯黑白 / 品牌黄 | 踏雪语义：冷、清晰、可跟 |
| Hero proof | 求职七步链路 | 26 skill 全表 | v3.4.2 主卖点是职业产出层 |
| 动效 | 静态 | GIF | 未授权动效；默认静态 |
| 归因徽标 | 暂不加 | MADE WITH | 先交付主体，满意后再议 |
