---
title: 动态本体如何成为企业级 AI 核心范式
type: source
status: reviewed
sources:
  - reviews/approved/2026-05-19-palantir-dynamic-ontology-core/REVIEW.md
updated: 2026-05-25
---

# 动态本体如何成为企业级 AI 核心范式

## 这篇文章在讲什么

这篇文章把前面较抽象的 ontology 概念接成一个运行时结构。它讨论 Dataset、
Pipeline、Mapping、Ontology、Action、API、安全和 OAG/RAG 的关系，试图说明：
动态本体不是静态模型，而是可以被数据更新、规则触发、行动写回和治理约束的运行层。

文章中最重要的结构是：底层数据先通过 pipeline 加工成 dataset，再通过 mapping
投射到 ontology 的对象、属性、关系和状态；对象状态变化可以触发 logic 和 action；
action 的结果又可能写回 dataset 或外部系统，形成下一轮反馈。

## 我读完后的理解

这篇文章把“动态”讲得更清楚了。动态本体不是把 ER 图、知识图谱或 BI 语义层搬到
AI 时代，而是让对象、状态、逻辑、权限和行动形成可运行闭环。

但更关键的是用户判断：小本体不是目标，只是路径。研究或交付时不应该追求一次性建出
完整企业世界，而应该围绕高价值场景，选择关键数据、关键逻辑和可控行动，先把闭环跑通。
最终目标不是建模本身，而是满足业务预期并产生价值。

## 最有用的部分

文章对 Dataset 和 Ontology 的区分有用。Dataset 更像事实数据层，回答“发生了什么”；
Ontology 则把这些事实放进业务语义里，回答“这些事实对业务对象和行动意味着什么”。

文章对 OAG 和 RAG 的对比也有用。RAG 更依赖临时检索片段和模型生成，OAG 则强调先把
知识、关系、规则和行动沉淀进业务世界，再让 LLM 在这个世界上工作。这个对比不应绝对化，
但它能解释为什么企业 AI 不能只停留在文档问答。

## 需要警惕的地方

文章对 Palantir 产品细节的描述仍需验证，尤其是 action 类型、安全机制、OAG 中 LLM
是否“不参与推理”等说法。

“真正推理发生在 ontology 内部，LLM 只是自然语言生成层”这个说法可能过强。更合理的
理解是：高风险判断应受 ontology、rules、permissions 和 action types 约束，但 LLM
仍可能参与解释、候选方案生成、工具选择和流程编排。

## 对综合页的影响

这篇文章是 [[concepts/palantir-dynamic-ontology]] 的核心来源之一。它让综合页从
Data / Logic / Action 进一步扩展到 runtime：dataset、mapping、ontology、logic、
action、governance、feedback。

## 来源与追溯

- 原始文件：`/Users/ningl/work/risk/palantir/从 Palantir看_动态本体如何成为企业级AI的核心范式.mhtml`
- Review：`reviews/approved/2026-05-19-palantir-dynamic-ontology-core/REVIEW.md`
- 可靠性：二手评论来源；结构有启发，产品细节和 OAG/RAG 对比需后续验证。
