---
title: 受治理的行动
type: mechanism
status: active
sources:
  - reviews/approved/2026-05-24-palantir-first-ontology-practice/REVIEW.md
  - reviews/approved/2026-05-25-palantir-aip-process-mining/REVIEW.md
updated: 2026-05-26
---

# 受治理的行动

## 是什么

受治理的行动是动态本体进入真实业务的方式。行动不等于自动执行；它可以是建议、模拟、
暂存、审批、通知、写回或生成审计记录。

## 为什么重要

企业 AI 的风险通常出现在行动层。查询错了可以纠正，行动错了可能影响客户、供应链、
财务、合规和责任边界。

因此 action 必须和权限、审批、审计、回滚、测试一起理解。

第一个 Palantir ontology 实操中的 `Assign Root Cause` 是一个最小 action：用户在
`Flight Alert` 对象上填写 `root_cause`。它证明 action 可以挂在对象上并写回对象属性，
但它还只是受控字段编辑，不能直接外推为复杂业务执行闭环。

流程挖掘案例中的 `AIP Logic` 更像一个业务判断函数：它读取销售订单项、客户信用、历史订单、
准时付款率等对象属性，输出“维持冻结 / 解除冻结”的建议和理由，并把结果写回 ontology。
这比字段编辑更接近业务决策，但仍然不是完整 action。真正的 action 还需要回答谁批准、
是否写回 SAP、如何审计、如何回滚。

## 行动成熟度

```text
解释 / 建议
-> 沙盒推演
-> 受控字段写回
-> AI 建议写回 ontology
-> 暂存动作
-> 审批后执行
-> 有边界的自动执行
-> 反馈和回滚
```

## 和 agent 的关系

企业级 agent 不应只由 prompt 定义边界。它能做什么，应由 ontology、rules、permissions、
logic tools 和 action types 一起约束。
