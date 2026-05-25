---
title: Ontology
type: concept
status: active
updated: 2026-05-25
---

# Ontology

## 是什么

在当前 wiki 中，ontology 暂时不是指普通知识图谱，也不是单纯的数据字典。
它更接近一种业务世界模型：用对象、属性、关系、状态、规则、权限和行动来表达企业如何运行。

这个定义还在演化。当前材料主要来自 Palantir 二手评论，因此这里表达的是研究中的工作理解。

## 解决什么问题

企业 AI 如果只面对数据库、文档和接口，很难知道一个数据点在业务中意味着什么。
它也很难判断哪些动作可做、谁有权做、做完以后如何追踪。

Ontology 试图把这些分散信息组织成一个可被人、应用和 AI 共同使用的业务世界。

## 由哪些部分组成

当前最有用的组成是：

- 对象：业务世界中的实体，如供应商、订单、物料、风险事件。
- 属性：对象的状态和描述。
- 关系：对象之间的业务连接，参见 [[concepts/ontology-relation-types]]。
- 逻辑：作用在对象和关系上的规则、模型、函数和判断。
- 行动：可被建议、模拟、审批或执行的业务动作。
- 治理：权限、审计、测试、回滚和责任边界。

## 和其他概念的关系

- [[concepts/palantir-dynamic-ontology]] 关注 ontology 如何进入运行时。
- [[concepts/data-logic-action]] 提供理解 ontology 的核心框架。
- [[mechanisms/data-to-ontology-mapping]] 解释底层数据如何进入 ontology。
- [[mechanisms/governed-action]] 解释 ontology 如何约束行动。

## 尚不清楚的地方

Palantir 官方材料如何精确定义 ontology，目前还需要后续来源验证。
