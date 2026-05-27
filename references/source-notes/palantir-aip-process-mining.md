---
title: 使用 AIP 构建 AI 驱动的流程挖掘与自动化系统
type: source
status: reviewed
sources:
  - reviews/approved/2026-05-25-palantir-aip-process-mining/REVIEW.md
updated: 2026-05-26
---

# 使用 AIP 构建 AI 驱动的流程挖掘与自动化系统

## 这篇文章在讲什么

这篇文章用虚构公司 `Titan Industries` 的 `Order-to-Cash` 流程说明一个信用冻结场景。
信用冻结本来是为了避免给高风险客户发货，但也可能误伤按时付款的优质客户。人工审核解冻
速度慢，会影响订单履行。

文章展示的链路是：

```text
SAP 数据
-> HyperAuto 同步源系统
-> Pipeline Builder 形成流程对象和流程日志
-> Ontology 连接销售订单项、客户、产品、生产线等对象
-> Machinery 做流程挖掘
-> Workshop 搭建业务界面
-> AIP Logic 生成信用冻结建议和理由
-> Automate 触发判断函数
```

## 我读完后的理解

这篇比 RAG 问答类文章更接近业务 ontology 主线。它想表达的是：治理后的 ontology 对象模型，
比临时拼接数据更适合承载反复发生的业务决策。

关键不是 AI 本身突然更聪明，而是 AI 看到的业务上下文更好：

```text
Customer
Sales Order
Sales Order Item
Payment History
Credit Hold
Product
Production Line
```

当这些对象和关系稳定存在时，AI 判断信用冻结不再只是读一包临时字段，而是在业务对象世界里读取
客户信用、历史付款、订单金额、流程状态和影响范围。

## 最有用的部分

文章把 AIP Logic 描述成作用在对象上的判断函数。它读取销售订单项及其相关属性，例如信用状态、
订单 ID、客户信用额度、过去 12 个月历史订单量和准时付款率，然后输出：

```text
recommendation = 维持冻结 / 解除冻结
reasoning = 为什么给出该建议
```

建议和推理过程会写回 ontology。这一点重要，因为判断结果变成了业务对象上的新状态，
后续可以被界面、流程、审计或自动化继续使用。

## 需要警惕的地方

这篇还没有证明无人值守 action 闭环。它没有讲清楚：

- 解除冻结是否真的写回 SAP；
- AI 建议是否需要人审批；
- Automate 触发的是判断函数还是实际业务动作；
- 错误建议如何追责、回滚和审计；
- AIP Logic 规则如何测试和版本化。

因此，本篇适合进入 wiki 的结论是“业务流程 AI 副驾”，不是“自动执行业务系统”。

## 对综合页的影响

这篇已补入 [[concepts/ontology]]、[[mechanisms/ontology-runtime-loop]]、
[[mechanisms/governed-action]] 和 [[questions]]。

它支持的阶段性判断是：对高价值、反复运行、需要治理的业务流程，先把数据建成 ontology
对象和关系，比用时临时拼数据给 AI 更适合承载决策。

## 来源与追溯

- 原始文件：`/Users/ningl/work/risk/palantir/Palantir实战：使用AIP构建AI驱动的流程挖掘与自动化系统.mhtml`
- Review：`reviews/approved/2026-05-25-palantir-aip-process-mining/REVIEW.md`
- 可靠性：二手教程/解读；文章称跟随 Palantir 部署策略师 Ruben Stroh 的业务场景演示，但本文本身不是官方文档。
