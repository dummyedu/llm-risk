---
title: 从数据到 Ontology
type: mechanism
status: active
sources:
  - reviews/approved/2026-05-24-palantir-first-ontology-practice/REVIEW.md
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

第一个 Palantir ontology 实操给出了一个最小例子：

| 数据层 | Ontology 层 | 作用 |
| --- | --- | --- |
| `flight_alerts` dataset | `Flight Alert` object type | 把表解释为业务对象类型 |
| `flight_alert_id` | object primary key | 识别一个具体告警对象 |
| `alert_title` | title property | 用于对象显示和识别 |
| `root_cause` | editable property | action 可以写回的业务属性 |
| `flight_id` | link mapping to `Flight` | 把告警对象连到航班对象 |

这说明 mapping 不是简单复制字段。它要决定哪些字段形成对象身份，哪些字段成为属性，
哪些字段支撑对象关系，哪些字段允许被 action 更新。

## 和关系类型的关系

关系类型不是底层 join 的别名。它只有被规则、权限、动作或 agent 工具选择读取时，
才成为动态本体的一部分。参见 [[concepts/ontology-relation-types]]。

在 `Flight Alert -> Flight` 的例子中，底层落地依赖 `flight_id` 匹配；但进入 ontology 后，
它表达的是“告警属于航班”的业务关系。后续如果有规则、查询、权限或 action 沿这条关系运行，
它才真正成为运行时可用的关系类型。

## 尚不清楚的地方

当前已读材料还没有充分说明 Palantir 工具链如何处理实体对齐、版本迁移和失败恢复。
