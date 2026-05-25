# 研究单个来源

当用户要求研究一个来源、继续 Palantir 研究，或处理
`raw/palantir/MANIFEST.md` 中的一个文件时，使用本流程。

## 共享方法来源

本流程是 `ei-wiki` 的项目封装。通用 review/ingest 方法以
`/Users/ningl/work/llm-lining/skills/wiki-review/` 和
`/Users/ningl/work/llm-lining/docs/workflows/wiki-review.md` 为准。

这里仅补充本仓库的来源边界、Palantir manifest、review gate 和应用限制。
如果通用 wiki 组织原则有更新，应优先更新 `llm-lining` 的 shared skill，而不是
在本文件复制一套新规则。

## 输入

- 来源 manifest：`raw/palantir/MANIFEST.md`
- 来源家族：`/Users/ningl/work/risk/palantir`
- 现有 wiki 页面：`wiki/`
- Ledger：`meta/INGEST_LEDGER.md`

## 步骤

1. 选择一个来源文件，除非用户明确选择一个小的连贯来源包。
2. 阅读足够内容，创建来源卡片。
3. 创建 review package：

```text
reviews/pending/YYYY-MM-DD-<slug>/
  REVIEW.md
  proposed/
    wiki/
```

4. 在 `REVIEW.md` 中包含：
   - 来源文件或来源包；
   - 来源卡片；
   - 事实性摘要；
   - 重要来源主张；
   - 作者观点或 framing；
   - LLM 推断；
   - 用户讨论记录；
   - 拟议 wiki 更新；
   - 待讨论问题；
   - 应用笔记，如有。
5. 和用户讨论 review。
6. 在用户批准 review package 前，不写正式 wiki 页面。

## 来源卡片

使用以下形状：

```markdown
## 来源卡片

- 标题：
- 来源路径：
- 文件类型：
- 保存或修改时间：
- 表观主题：
- 当前为什么读：
- Review 状态：
```

## 拟议 wiki 更新要求

`REVIEW.md` 的“拟议 wiki 更新”不能只写“更新 questions”。必须明确回答：

- 是否创建或更新 `wiki/sources/<slug>.md` 来源页。
- 是否更新已有综合页，例如 `wiki/concepts/`、`wiki/methods/` 或
  `wiki/applications/` 下的页面。
- 如果需要新建综合页，说明它为什么是可复用概念、方法或判断框架。
- 哪些内容只进入 `wiki/questions.md`，因为它们尚未定论。
- 哪些内容只留在来源页，因为它们不足以支撑综合结论。

## 综合优先原则

正式 wiki 的主体遵循共享 wiki skill 的“知识对象网络”原则：学习后的内容应更新
概念、机制、方法、问题等可复用知识对象，而不是把文章平铺成列表。

- 来源页用于追溯证据和可信度。
- 综合页用于后续查阅和引用。
- 问题页用于保留未定论问题。
- 每篇来源批准后，都必须判断它对现有综合页的影响。
- 阅读顺序、队列规划、来源清单整理不放入 `reviews/pending/`。这类材料应放入
  `meta/` 或 `docs/`，避免和待批准的单篇文章 review 混淆。

## 停止条件

以下情况先停下并询问：

- 修改外部来源文件；
- 复制大型原始文件；
- 对私有材料使用外部服务；
- 在用户批准前应用拟议 wiki 更新；
- 将应用假设变成项目实施要求。
