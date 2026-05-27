# 应用已批准 Review

只有当用户明确批准 review package 后，才使用本流程。

## 共享方法来源

本流程是 `ei-wiki` 的项目封装。通用 approved-review 应用方法以
`/Users/ningl/work/llm-lining/skills/wiki-review/`、
`/Users/ningl/work/llm-lining/skills/wiki-maintain/` 和
`/Users/ningl/work/llm-lining/docs/workflows/wiki-review.md` 为准。

这里仅补充本仓库的批准门槛、ledger、review 目录和本地来源边界。若通用 wiki
组织原则需要调整，应更新 `llm-lining` 的 shared skill，再让本流程引用它。

## 输入

- `reviews/pending/` 下已批准的 package
- `reviews/pending/<slug>/proposed/wiki/` 下的拟议文件，如有
- 正式 wiki：`wiki/`
- Ledger：`meta/INGEST_LEDGER.md`

## 步骤

1. 重新阅读 `REVIEW.md`。
2. 确认用户已经批准该 package。
3. 对照现有 `wiki/` 页面，判断应该更新哪里。
4. 优先更新已有页面，再考虑创建新页面。
5. 在 review 和追溯区保留 claim 标签：
   - 来源事实（Source fact）
   - 作者观点（Author opinion）
   - 用户判断（User judgment）
   - LLM 推断（LLM inference）
   - 应用假设（Application hypothesis）
6. 如需保留单篇来源分析，创建或更新 `references/source-notes/<slug>.md`。
   来源笔记是证据和备份层，不属于正式 wiki。
7. 创建或更新至少一个综合判断位置，除非该来源明确不适合进入综合层。
8. 如果没有更新综合页，必须在 `meta/INGEST_LEDGER.md` notes 中说明原因。
9. 只有当批准内容改变耐久导航或耐久问题时，才更新 `wiki/index.md`、
   `wiki/map.md`、`wiki/synthesis.md` 或 `wiki/questions.md`。
10. 更新 `meta/INGEST_LEDGER.md`。
11. 将 package 移动或复制到 `reviews/approved/`。

## 输出层次

应用 approved review 时，按共享 wiki skill 的知识对象网络原则组织：

1. **正式 wiki 页**：跨来源或可复用的概念、机制、方法、判断框架、应用假设。
2. **问题页**：尚未定论、需要继续验证的问题。
3. **来源笔记**：单篇来源的分析、引用和备份，放在 `references/source-notes/`。

来源笔记是证据层，不是 wiki 层。浏览器 wiki 的主体只能是正式知识对象。

正式 wiki 正文应先表达结论和理解，不应在每句话前铺 `Source fact`、
`Author opinion`、`LLM inference` 等标签。标签用于 review、ledger 或页面底部
“来源与追溯”，避免破坏阅读。

## 停止条件

以下情况先停止，不应用：

- review package 存在未解决的来源追溯问题；
- 拟议更新把推断当作事实；
- 拟议更新创建没有证据支持的跨来源链接；
- 拟议更新把 `risk` 应用假设变成实施要求。
