---
title: 从数据到 Ontology
type: mechanism
status: active
updated: 2026-05-25
---

# 从数据到 Ontology

## 是什么

从数据到 ontology，核心不是简单同步字段，而是把底层系统中的数据转成业务对象、属性和关系。

例如 ERP、MES、WMS、CRM 中的数据，经过清洗、对齐和口径治理后，才可能成为 ontology 中的
Supplier、Part、Order、Inventory、RiskEvent 等对象。

## 关键步骤

- 数据准备和预处理；
- derived dataset；
- 实体对齐；
- 字段到属性的 mapping；
- 表关系到业务关系类型的 mapping；
- 数据版本和口径治理。

## 和关系类型的关系

关系类型不是底层 join 的别名。它只有被规则、权限、动作或 agent 工具选择读取时，
才成为动态本体的一部分。参见 [[concepts/ontology-relation-types]]。

## 尚不清楚的地方

当前已读材料还没有充分说明 Palantir 工具链如何处理实体对齐、版本迁移和失败恢复。
