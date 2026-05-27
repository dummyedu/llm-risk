---
title: 语义编译与业务实现讨论纪要
type: concept
status: reviewed
sources:
  - conversation:2026-05-24
  - reviews/approved/2026-05-20-palantir-semantic-compiler-engine-1/REVIEW.md
updated: 2026-05-24
---

# 语义编译与业务实现讨论纪要

## 背景

本页记录围绕 approved review
`reviews/approved/2026-05-20-palantir-semantic-compiler-engine-1/REVIEW.md`
的讨论。讨论重点不是复述文章，而是澄清：如果把文章里的
`Define -> Compile -> Execute -> Govern -> Evolve` 放到真实业务实现中，
到底要做哪些显式步骤，哪些地方最难，系统如何避免发散，以及关系类型到底是否
只是给人看的标签。

## 文章想讲什么

LLM 推断（LLM inference）：这篇文章想表达的不是普通软件分层，而是：

```text
先把业务含义定义成可执行的语义结构，
再把规则、函数、权限和动作组织成运行时可以执行的计划。
```

文章中的生命周期可以暂时理解为：

```text
Define -> Compile -> Execute -> Govern -> Evolve
```

但用户判断（User judgment）：文章仍然没有充分讲清楚“怎么做出来”，尤其是
data preparation、derived dataset、entity alignment、key logic、testing、
rollback 等实际工程路径。

## 一个业务的显式实现步骤

以“供应商延迟交付导致生产和客户订单风险”为例，一个最小闭环可以拆成：

```text
1. 定义业务目标
2. 定义业务对象
3. 接入和整理数据
4. 定义关键业务逻辑
5. 编译成执行计划
6. 运行时触发和执行
7. 贯穿式治理、权限和审计
8. 暴露给用户或 AI agent
9. 记录反馈并演化
```

### 1. 定义业务目标

先不要建大而全 ontology，而是定义一个具体闭环：

```text
当供应商延迟交付关键物料时，
系统识别受影响订单，
计算影响程度，
推荐替代供应商或生产调整方案，
并在审批后触发采购或计划动作。
```

### 2. 定义业务对象

可能涉及：

```text
Supplier
Part
PurchaseOrder
Inventory
ProductionPlan
CustomerOrder
RiskEvent
MitigationAction
ApprovalTask
```

### 3. 接入和整理数据

真实实现必须处理：

```text
ERP 采购订单、供应商、价格
MES 生产计划
WMS 库存
CRM 客户订单
外部物流或供应商通知
字段映射
实体对齐
口径治理
派生数据集
数据版本
```

这是文章中相对缺失、但工程上很关键的一段。

### 4. 定义关键业务逻辑

逻辑不是 LLM 自己生成，而是从业务专家、制度、历史案例和系统约束中抽取。

可能的函数包括：

```text
calculate_shortage(part, date)
find_affected_orders(part, shortage_date)
rank_alternative_suppliers(part, quantity, deadline)
calculate_customer_impact(order)
recommend_mitigation(risk_event)
```

可能的规则包括：

```text
如果 A 类客户订单预计延迟超过 24 小时，则升级。
如果替代供应商价格高于原供应商 15%，需要采购经理审批。
如果物料是安全关键物料，不允许未经认证替换供应商。
如果库存覆盖大于 7 天，不立刻升级为高风险。
```

### 5. 编译成执行计划

这可以理解为文章中的 `Compile` 或 `Logic Plan`。示例：

```text
Trigger:
  SupplierDelayEvent

Inputs:
  supplier_id
  delayed_part_id
  promised_date
  new_estimated_date

Execution:
  1. 查询相关采购订单
  2. 查询当前库存
  3. 计算缺口
  4. 找出受影响生产计划
  5. 找出受影响客户订单
  6. 计算影响等级
  7. 查询替代供应商
  8. 生成推荐应对动作

Governance:
  - 成本数据仅采购和财务可见
  - 自动创建建议，但不自动下单
  - 高影响订单必须人工审批

Outputs:
  - RiskEvent
  - AffectedOrderList
  - MitigationRecommendation
  - ApprovalTask
```

LLM 推断（LLM inference）：这里的“语义编译”不是把自然语言编译成代码，
而是把业务对象、关系、函数、规则、权限和动作组织成可执行计划。

### 6. 执行运行时动作

当事件发生：

```text
SupplierDelayEvent
-> 执行 Logic Plan
-> 更新 RiskEvent
-> 生成受影响订单列表
-> 推荐替代供应商
-> 创建审批任务
-> 通知采购/计划/客户成功团队
```

这一步把系统从 dashboard 推进到行动闭环。

### 7. 治理贯穿全过程

用户判断（User judgment）：`Govern` 不应被理解为最后附加的权限层，而应横切
data、ontology、logic、action、LLM/agent 调用和审计。

需要回答：

```text
谁能看供应商价格？
谁能看到客户优先级？
谁能触发替代采购？
谁能批准生产计划调整？
哪些动作只能建议，不能自动执行？
每次推荐和审批如何留痕？
```

### 8. 暴露给用户或 AI agent

用户可以问：

```text
这次供应商延迟会影响哪些客户订单？
有没有替代供应商？
如果改生产计划，哪个方案损失最小？
```

但 LLM 不应凭空回答，而应调用受控工具：

```text
find_affected_orders()
rank_alternative_suppliers()
simulate_production_plan_change()
create_approval_task()
```

### 9. 反馈和演化

系统记录：

```text
推荐了什么方案
人选择了什么方案
实际是否解决问题
预测影响是否准确
哪些规则失效
需要新增哪些对象属性或逻辑
```

然后进入演化：

```text
新增 Supplier.reliability_score
调整 high_priority_order 规则
增加物流延迟预测模型
修改审批阈值
重新编译 Logic Plan
```

## 规则从哪里来

用户问题（User question）：规则怎么来？谁拆解这些规则？

LLM 推断（LLM inference）：规则通常来自四类材料：

```text
1. 显性制度：SOP、审批制度、合同条款、合规要求、SLA。
2. 业务专家经验：采购、计划、风控、运营负责人脑中的判断。
3. 历史案例：过去类似事件如何处理，哪些方案有效或失败。
4. 系统约束：ERP/MES/WMS/CRM 中已有状态机、字段、接口和权限限制。
```

拆解规则通常需要多角色协作：

```text
业务负责人：定义目标和价值。
业务专家：解释真实判断逻辑。
数据/系统专家：说明数据位置、字段含义和接口限制。
产品/分析人员：拆对象、状态、规则和动作。
工程师/FDE：把这些内容转成模型、函数、权限和界面。
合规/管理者：确认哪些动作可自动化，哪些必须审批。
```

Palantir 语境中的 FDE，可以暂时理解为现场翻译和落地角色：同时理解业务、
数据、系统限制和工程实现，推动最小可运行闭环。

## 关系与映射

用户问题（User question）：关系和映射分别是什么？

LLM 推断（LLM inference）：

```text
关系：业务语义层的问题，描述两个对象在业务世界中如何相连。
映射：数据落地层的问题，说明对象属性和关系从哪些底层字段或表生成。
```

示例：

```text
关系：
Supplier supplies Part

映射：
erp_purchase_orders.vendor_code -> Supplier.id
erp_purchase_orders.item_code   -> Part.id
vendor_code + item_code         -> Supplier supplies Part
```

进一步讨论见 [[concepts/ontology-relation-types]]。

## 系统如何收敛

用户问题（User question）：如果每个业务都这么复杂，系统怎么收敛？

LLM 推断（LLM inference）：系统不能靠每个业务从零建模来收敛。它必须把一次业务实现沉淀到共享层：

```text
稳定层：
对象类型、关系类型、规则模板、Action 类型、权限模型、审计机制、执行引擎。

变化层：
具体业务场景、参数、阈值、对象组合、特殊规则、页面和流程。
```

收敛机制包括：

```text
核心对象收敛
关系模式收敛
规则模式收敛
Action 类型收敛
业务流程骨架收敛
治理机制收敛
```

例如多个供应链场景都可能复用：

```text
Supplier
Part
Inventory
ProductionPlan
CustomerOrder
RiskEvent
Task
Approval
```

多个业务闭环也可能复用同一骨架：

```text
Detect -> Assess -> Recommend -> Approve -> Act -> Learn
```

关键判断：

> 业务实现可以从具体场景开始，但产物必须回流到共享对象、关系、规则、
> Action 和治理能力中，否则系统不会收敛。

## 关系类型到底有什么用

用户问题（User question）：从实现角度看，关系类型是不是只有对人有用？

讨论后的结论：

```text
存储层：关系大多都是边。
运行时解释层：关系类型会影响规则、权限、查询、动作和解释。
```

关系类型只有在被系统作为可执行配置读取时，才不只是给人看的标签。它应该能定义：

```text
允许连接哪些对象
方向和基数
需要哪些属性
能被哪些规则使用
能触发哪些动作
是否承载权限或责任含义
```

简化判断：

> 关系类型是有限、受控、可被运行时逻辑引用的语义边类型。

如果某种连接不会被规则、权限、动作、查询或解释使用，它可能只是备注或搜索标签，
不一定需要进入核心 ontology。

专题见 [[concepts/ontology-relation-types]]。

## 本轮讨论形成的关键判断

- 用户判断（User judgment）：文章里的语义编译框架有帮助，但实际难点在规则来源、业务拆解、映射、治理、测试和系统收敛。
- 用户判断（User judgment）：如果每个业务都从零建模，系统会发散；必须把具体业务产物回流到共享对象、关系、规则、Action 和治理能力。
- LLM 推断（LLM inference）：`Govern` 应横切整个生命周期，而不是事后附加。
- LLM 推断（LLM inference）：`Logic Plan` 可作为学习隐喻，但不能直接当成 Palantir 官方产品事实。
- LLM 推断（LLM inference）：关系类型的实现价值在运行时解释层；如果不被规则、权限、动作或查询使用，它就只是文档标签。
- LLM 推断（LLM inference）：后续继续阅读工具链材料时，应重点追问实际路径：

```text
业务目标
-> 数据准备
-> 实体对齐
-> 对象和关系建模
-> 关键规则与函数
-> 执行计划
-> 受控 action
-> 权限审计
-> 测试回滚
-> 反馈演化
```

## 对已批准 review 的影响

这轮讨论表明，该 review 不应只把语义生命周期记为问题清单。它已经推动更新：

- [[concepts/palantir-dynamic-ontology]]
- [[concepts/ontology-relation-types]]
- 本页
- [[questions]]

同时需要在来源笔记中明确：该文章提供的是概念框架和学习隐喻，仍未充分回答
“如何做出来”的工程路径。
