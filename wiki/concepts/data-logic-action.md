---
title: Data / Logic / Action
type: concept
status: active
updated: 2026-05-25
---

# Data / Logic / Action

## 是什么

Data / Logic / Action 是当前理解 Palantir ontology 最有用的框架。

Data 提供业务状态和决策依据。Logic 承载规则、模型、优化器、仿真和业务判断。
Action 让判断进入业务现实，包括建议、模拟、审批、写回和审计。

## 为什么重要

很多企业 AI 系统停在 Data 层：能查数据、总结文档、回答问题，但不能进入真实运营。
如果没有 Logic，系统不知道如何判断；如果没有 Action，系统无法形成闭环。

因此，企业 AI 的关键不只是“知道什么”，而是能否把知道的内容转成受治理的判断和行动。

## 三者如何连接

```text
Data    -> 描述世界发生了什么
Logic   -> 判断这些事实意味着什么
Action  -> 在权限和审计约束下推动下一步
```

这个框架直接连接 [[mechanisms/ontology-runtime-loop]]。

## 当前理解

Data 不只是原始数据，也包括历史决策、备选方案、上下文和后续影响。
Logic 是业务专家最关键的资产，不一定完整，但必须抓住关键判断。
Action 不应被理解成自动化按钮，而是一个从建议到写回的成熟度谱系。

## 尚不清楚的地方

后续需要验证 Palantir 官方材料是否也以类似方式组织 ontology、logic 和 action。
