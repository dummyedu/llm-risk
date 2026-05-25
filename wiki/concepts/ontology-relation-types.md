---
title: Ontology 关系类型
type: concept
status: reviewed
sources:
  - conversation:2026-05-24
  - reviews/approved/2026-05-24-palantir-first-ontology-practice/REVIEW.md
updated: 2026-05-25
---

# Ontology 关系类型

## 核心结论

从映射和存储角度看，关系本质上都是两个实体之间的连接，例如一对一、一对多、多对多。

关系类型的价值不在存储层，而在运行时解释层。存储层里边就是边；运行时里，不同关系类型
会影响规则、权限、查询、动作和解释。

因此，关系类型应该是有限、受控、可被运行时逻辑引用的语义边类型，而不是业务人员随手起的描述性标签。

## 三层区分

### 关系实例

关系实例是具体业务事实：

```text
SupplierA supplies PartX
SupplierB supplies PartX
ProductionPlan1 depends_on PartX
DepartmentA owns AssetY
RiskEvent1 affects CustomerOrder9
```

从底层实现看，它们都可以存成类似结构：

```text
from_entity_id
relation_type
to_entity_id
properties
```

### 关系类型

关系类型是受控定义：

```text
supplies
depends_on
owns
contains
affects
fulfills
approved_by
mitigates
```

每一种关系类型都应该说明：

```text
允许连接哪些对象
方向是什么
基数是什么
需要哪些属性
可以被哪些规则使用
可以触发哪些动作
是否承载权限或责任含义
```

### 映射

映射是把底层数据字段变成对象、属性和关系。

例如第一个 Palantir ontology 实操中，`flight_alerts` 数据集里有：

```text
flight_alert_id
alert_title
flight_id
root_cause
```

它们被解释为：

```text
Flight Alert object
Flight Alert.title
Flight Alert -> Flight link
Flight Alert.root_cause
```

这里的关系是：

```text
一个 Flight 可以有多个 Flight Alert。
一个 Flight Alert 只属于一个 Flight。
```

映射则是：

```text
用 flight_alerts.flight_id 匹配 Flight 的主键，生成 Flight Alert -> Flight 这条 link。
```

另一个通用例子是 ERP 里有：

```text
erp_purchase_orders.vendor_code
erp_purchase_orders.item_code
```

可以映射为：

```text
Supplier supplies Part
```

所以：

```text
关系：业务语义层的问题，说明两个对象在业务世界中如何相连。
映射：数据落地层的问题，说明这条业务关系从哪些字段或表生成。
```

## 对实现有什么用

如果系统只把关系类型当字符串标签，关系类型主要对人有用。但如果系统读取关系类型定义，它就会影响运行时行为。

例如 `supplies` 可以定义为：

```text
from: Supplier
to: Part
required_properties:
  - lead_time_days
  - unit_price
  - certification_status
allowed_rules:
  - supplier_substitution
  - supply_risk_analysis
allowed_actions:
  - recommend_alternative_supplier
  - create_purchase_order_draft
```

`owns` 可以定义为：

```text
from: Department
to: Asset
required_properties:
  - owner_role
  - cost_center
  - effective_date
allowed_rules:
  - responsibility_lookup
  - permission_resolution
allowed_actions:
  - approve_asset_change
  - transfer_ownership
```

这时二者在存储上都是边，但运行时含义不同：

```text
supplies  -> 供应风险、替代推荐、采购动作
owns      -> 责任归属、权限推导、成本归属
depends_on -> 影响传播、关键路径分析
contains  -> 汇总、组成结构、生命周期级联
affects   -> 风险事件、缓解动作、状态跟踪
```

## 规则如何使用关系类型

规则可以显式引用关系类型：

```text
沿 depends_on 传播风险。
沿 owns 找责任人。
沿 supplies 找替代供应商。
沿 contains 做金额或数量汇总。
沿 affects 生成缓解动作。
```

如果没有关系类型，这些逻辑会散落在代码里：

```text
如果 A 是 Supplier 且 B 是 Part，就当作供应关系处理。
如果 A 是 Department 且 B 是 Asset，就当作归属关系处理。
```

这不是不能做，但它把业务语义藏进了代码，业务专家很难审查，跨业务复用也更难。

## 什么时候关系类型有价值

关系类型值得建模，当它会影响至少一种系统行为：

```text
规则判断
权限推导
动作约束
图遍历路径
风险传播
推荐排序
审计解释
agent 工具选择
UI 或查询入口生成
```

如果一个关系类型不会被规则、权限、动作、查询或解释使用，它可能只是备注或搜索标签，不一定需要进入核心 ontology。

## 什么时候可以不用复杂关系类型

如果系统只做：

```text
展示
简单 join
固定报表
所有逻辑都写死在 service 代码里
```

那么普通表、外键、join 和 service 代码就足够。此时关系类型主要是帮助人理解，工程价值有限。

Ontology 关系类型的价值，只有在系统希望把一部分业务逻辑从硬编码服务中抽出来，变成可配置、可审查、可复用、可被 agent 查询和调用的语义层时，才开始显现。

## 判断标准

可以用一句话判断：

> 只要某种连接会影响系统行为，就应该成为明确、受控、可测试的关系类型；如果它只用于说明或展示，就不必过度建模。

## 与动态本体的关系

在 [[concepts/palantir-dynamic-ontology]] 中，关系类型属于 ontology 层的核心元素之一。它连接 Data、Logic、Action：

```text
Data    -> 通过映射生成对象和关系实例
Logic   -> 根据关系类型选择规则、路径和约束
Action  -> 根据关系类型决定允许动作、审批和审计
```

因此，关系类型不是单纯业务词汇表。它只有被运行时读取时，才成为动态本体的一部分。
