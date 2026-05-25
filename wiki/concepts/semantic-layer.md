---
title: 语义层
type: concept
status: active
updated: 2026-05-25
---

# 语义层

## 是什么

语义层把底层数据解释成业务对象、属性、关系和口径。它让上层应用不必直接面对杂乱的表、
字段和系统差异。

## 和 ontology 的关系

语义层更偏解释数据；ontology 如果要成为动态本体，还需要进一步连接 logic、action、
governance 和 runtime feedback。

所以当前理解中：

```text
语义层是 ontology 的必要部分，但不是完整动态本体。
```

## 解决什么问题

语义层解决的是同一个业务概念在不同系统中的口径不一致、字段不一致、上下文不一致。
它让“客户”“订单”“风险”“库存”等概念可被统一查询和解释。

## 尚不清楚的地方

Palantir Foundry 中 dataset、ontology、mapping、materialization 的实际边界仍需验证。
