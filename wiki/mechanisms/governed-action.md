---
title: 受治理的行动
type: mechanism
status: active
sources:
  - reviews/approved/2026-05-24-palantir-first-ontology-practice/REVIEW.md
updated: 2026-05-25
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

## 行动成熟度

```text
解释 / 建议
-> 沙盒推演
-> 受控字段写回
-> 暂存动作
-> 审批后执行
-> 有边界的自动执行
-> 反馈和回滚
```

## 和 agent 的关系

企业级 agent 不应只由 prompt 定义边界。它能做什么，应由 ontology、rules、permissions、
logic tools 和 action types 一起约束。
