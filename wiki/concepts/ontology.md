---
title: Ontology
type: concept
status: active
sources:
  - reviews/approved/2026-05-24-palantir-first-ontology-practice/REVIEW.md
  - reviews/approved/2026-05-25-palantir-aip-process-mining/REVIEW.md
updated: 2026-05-26
---

# Ontology

## 是什么

在当前 wiki 中，ontology 暂时不是指普通知识图谱，也不是单纯的数据字典。
它更接近一种业务世界模型：用对象、属性、关系、状态、规则、权限和行动来表达企业如何运行。

读完第一个 Palantir ontology 实操例子后，可以把它说得更工程化一些：

```text
ontology = 基于表数据的面向对象业务表达
```

底层数据表提供事实和字段；ontology 把这些数据解释成业务对象、对象属性、对象关系和
对象上的受控行动。运行时再把具体数据、具体用户、具体事件填进这些模型。

读完流程挖掘和信用冻结案例后，这个理解可以再补一层：ontology 的价值不只是把表包装成对象，
而是让反复发生的业务决策拥有稳定、可治理的上下文模型。AI 面对治理后的对象和关系时，
更容易做出可解释、可复用、可追踪、可接入流程的判断。

这个定义还在演化。当前材料主要来自 Palantir 二手评论和教程总结，因此这里表达的是
研究中的工作理解。

## 解决什么问题

企业 AI 如果只面对数据库、文档和接口，很难知道一个数据点在业务中意味着什么。
它也很难判断哪些动作可做、谁有权做、做完以后如何追踪。

Ontology 试图把这些分散信息组织成一个可被人、应用和 AI 共同使用的业务世界。

## 由哪些部分组成

当前最有用的组成是：

- 对象类型：业务世界中的模型，如供应商、订单、物料、风险事件、航班告警。
- 对象实例：运行时里的具体对象，由数据行、标识键和上下文形成。
- 属性：对象的状态和描述，由字段映射而来，也可能被 action 更新。
- 关系：对象之间的业务连接，通常需要通过外键、主键或其他匹配规则落地，参见 [[concepts/ontology-relation-types]]。
- 流程对象和流程日志：描述哪个对象处在什么流程状态、何时进入该状态。
- 逻辑：作用在对象和关系上的规则、模型、函数和判断。
- 行动：可被建议、模拟、审批或执行的业务动作。在最小实操例子里，action 先表现为对象上的受控字段写回。
- 治理：权限、审计、测试、回滚和责任边界。

第一个实操例子把这件事落到了一个很小的航空场景：

```text
flight_alerts dataset
-> Flight Alert object type
-> flight_alert_id / alert_title / root_cause properties
-> Flight Alert 与 Flight 通过 flight_id 形成 link type
-> Assign Root Cause action 更新 root_cause
```

它说明 ontology 不是只画概念图，而是把 dataset、对象模型、关系、action 和 data lineage
连在一起。

流程挖掘案例把它放进一个信用冻结决策中：

```text
SAP tables
-> sales order item / customer / product / production line
-> process object dataset / log object dataset
-> credit hold decision context
-> AIP Logic recommendation and reasoning
-> recommendation written back to ontology
```

这支持一个阶段性判断：对高价值、反复运行、需要权限和追溯的业务流程，提前把数据建成
ontology 对象和关系，比每次临时拼数据给 AI 更适合承载决策。

## 和其他概念的关系

- [[concepts/palantir-dynamic-ontology]] 关注 ontology 如何进入运行时。
- [[concepts/data-logic-action]] 提供理解 ontology 的核心框架。
- [[mechanisms/data-to-ontology-mapping]] 解释底层数据如何进入 ontology。
- [[mechanisms/governed-action]] 解释 ontology 如何约束行动。

## 尚不清楚的地方

Palantir 官方材料如何精确定义 ontology，目前还需要后续来源验证。

第一个实操例子只证明了最小对象、关系和字段写回链路。它还不能证明复杂 workflow、
多步骤审批、AI 建议进入执行链、回滚和跨部门治理已经完整成立。

流程挖掘案例证明的是 AI 建议层：治理后的对象模型更适合承载业务判断。它还没有证明
建议如何进入审批、action、SAP 写回和回滚链路。
