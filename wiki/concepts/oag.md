---
title: OAG
type: concept
status: active
updated: 2026-05-25
---

# OAG

## 是什么

OAG 可以暂时理解为 ontology-augmented generation：先把业务对象、关系、规则和行动
组织成可治理的语义世界，再让 LLM 在这个世界中检索、解释、生成方案或调用工具。

## 和 RAG 的区别

RAG 更像从文档或向量库中检索片段，再让模型生成回答。
OAG 强调模型面对的不是孤立文本片段，而是结构化的业务世界。

这个区别有用，但不能过度绝对化。实际系统可能同时使用 RAG、工具调用、ontology 查询和
agent 编排。

## 当前理解

OAG 的价值在于把企业 AI 从文档问答推向业务语义和行动边界。它让模型生成内容时受到对象、
规则、权限和 action types 的约束。

## 尚不清楚的地方

“LLM 不参与推理，真正推理发生在 ontology 内部”这个说法可能过强。更稳妥的理解是：
LLM 可以参与解释、候选方案生成和工具选择，但高治理判断应受 ontology 和 logic 约束。
