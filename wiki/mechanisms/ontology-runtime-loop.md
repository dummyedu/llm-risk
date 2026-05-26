---
title: Ontology 运行时闭环
type: mechanism
status: active
sources:
  - reviews/approved/2026-05-25-palantir-aip-process-mining/REVIEW.md
updated: 2026-05-26
---

# Ontology 运行时闭环

## 是什么

Ontology 运行时闭环描述的是动态本体如何从数据进入业务语义，再从业务语义进入逻辑和行动。

当前工作模型是：

```text
业务目标 / 预期价值
-> 数据准备 / pipeline / preprocessing
-> derived dataset / entity alignment / 口径治理
-> object / property / relation 抽象
-> key logic 实现
-> controlled action / writeback
-> governance / permission / audit
-> testing / rollback / feedback
```

## 为什么重要

如果没有闭环，ontology 只是描述世界；有了闭环，它才可能驱动业务。

这个闭环也提供了判断工具链文章的标准：如果一篇文章只讲抽象层次，却不能说明这条路径
如何实现，它就还不是可执行方法论。

## 信用冻结例子

流程挖掘案例可以作为当前最具体的候选闭环：

```text
SAP 数据
-> HyperAuto 同步源系统
-> Pipeline Builder 形成流程对象和流程日志
-> Ontology 连接销售订单项、客户、产品、生产线和信用冻结状态
-> Machinery 观察真实流程路径和异常
-> Workshop 给业务人员查看和操作
-> AIP Logic 基于对象属性生成维持冻结 / 解除冻结建议
-> 建议和推理写回 ontology
-> Automate 按事件或定时触发判断函数
```

这个例子支持“业务流程 AI 副驾”，还不支持“无人值守执行闭环”。目前清楚的是：
AI 可以在治理后的对象模型上生成建议，并把建议写回 ontology；尚不清楚的是建议如何变成
受控 action，以及是否写回 SAP。

## 相关页面

- [[concepts/data-logic-action]]
- [[mechanisms/data-to-ontology-mapping]]
- [[mechanisms/logic-execution]]
- [[mechanisms/governed-action]]
- [[mechanisms/feedback-and-evolution]]
