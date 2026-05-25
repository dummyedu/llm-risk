---
title: Palantir 动态本体
type: concept
status: reviewed
sources:
  - reviews/approved/2026-05-18-palantir-eleven-part-preface/REVIEW.md
  - reviews/approved/2026-05-18-palantir-decision-paradigm/REVIEW.md
  - reviews/approved/2026-05-18-palantir-ontology-foundation/REVIEW.md
  - reviews/approved/2026-05-19-palantir-dynamic-ontology-core/REVIEW.md
  - reviews/approved/2026-05-20-palantir-toolchain-dynamic-ontology-1/REVIEW.md
  - reviews/approved/2026-05-20-palantir-semantic-compiler-engine-1/REVIEW.md
updated: 2026-05-25
---

# Palantir 动态本体

## 当前理解

Palantir 动态本体可以暂时理解为一种**以决策和行动为中心的企业运行模型**。
它不是普通数据模型、知识图谱、BI 语义层或文档检索层。它试图把业务对象、业务状态、
关键逻辑、权限边界和受控行动放进同一个可运行的世界里。

这个理解目前来自 6 篇二手评论来源，还没有经过 Palantir 官方材料或一手案例交叉验证。
因此它是当前研究结论，不是最终事实。它的价值在于帮助我们组织后续阅读：每篇新材料
都要检验、修正或拆解这个理解。

## 核心判断

动态本体的关键不是一开始建完整企业世界，而是围绕高价值场景，把关键数据、关键逻辑
和受控行动接成闭环。

这意味着“好 ontology”的标准不是覆盖面大，也不是术语完整，而是：

- 是否抓住关键业务对象和状态；
- 是否承载关键业务逻辑；
- 是否能驱动或约束行动；
- 是否具备权限、审计、测试、回滚和反馈机制；
- 是否能在后续场景中复用和扩展。

小本体不是目标，而是路径。它的作用是降低起步复杂度，用一个关键场景验证 Data、
Logic、Action 是否真的能跑通。最终目标仍然是满足业务预期并产生价值。

## Data、Logic、Action

目前最有用的分析框架是 Data、Logic、Action。

Data 不只是原始数据，也包括业务状态、上下文、历史判断、备选方案、最终行动和后续影响。
如果系统只保存事实数据，却不保存决策过程，它很难从组织经验中学习。

Logic 是业务专家真正掌握的核心。它可以是规则、模型、优化器、仿真、质量标准、审批条件
或场景判断。企业 AI 如果只接入数据而不接入关键 logic，就容易停留在查询和解释层。

Action 是系统进入真实运营的方式。Action 不应该理解为无约束自动执行，而应该包括建议、
沙盒推演、暂存、审批、写回、审计和回滚等不同成熟度。越靠近真实行动，越需要权限和治理。

## 运行时闭环

当前可以用下面这条路径理解动态本体的运行目标：

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

这不是 Palantir 官方架构图，而是我们目前用来阅读和追问后续材料的工作模型。
如果一篇工具链文章只讲 Semantic OS、Logic Plan、Runtime Engine 等抽象词，却不能解释
这条路径如何落地，就只能作为概念材料，不能作为工程方法论。

## OAG 与 RAG

当前理解中，RAG 更像“检索材料后让模型回答”，OAG 更像“先把业务对象、关系、规则和行动
组织成语义世界，再让模型在这个世界中工作”。

这个区分有用，但不能绝对化。说“LLM 完全不参与推理”可能过强。更稳妥的理解是：
高治理场景中的最终判断和行动应受 ontology、rules、permissions、logic tools 和
action types 约束；LLM 仍然可以参与解释、候选方案生成、工具选择和流程编排。

## 语义编译和治理

“语义编译”可以作为学习隐喻：把业务对象、关系、规则、函数、权限和上下文组织成可执行计划。
这个隐喻有助于理解为什么动态本体不只是建模，而是要进入运行时。

但目前读到的材料仍然偏抽象。`Ontology Service -> Logic Service -> Runtime Engine`
这类说法已经被来源作者说明为抽象分层，不是 Palantir 官方命名。它们可以帮助学习，
不能直接写成产品事实。

Govern 应该被理解为贯穿机制，而不是最后附加的权限层。对象定义、逻辑编译、运行执行、
反馈演化都需要治理，否则企业级 agent 和 action 很难承担责任。

## 尚未定论

- Palantir 官方材料如何定义 ontology、AIP、Action Types、Logic、OSDK 与权限边界？
- 动态本体是否必须包含语义编译层，还是语义编译只是理解工具链的一种隐喻？
- 企业级 agent 的边界应由 ontology、rules、permissions、action types 定义，还是由 prompt、workflow 或代码服务定义？
- 自演化 ontology 在企业治理中需要哪些测试、审批、审计和回滚条件？
- 工具链如何具体完成数据准备、实体对齐、对象建模、关键逻辑实现、action 写回和版本迁移？

## 来源与依据

主要来源页：

- [[sources/palantir-eleven-part-preface]]
- [[sources/palantir-decision-paradigm]]
- [[sources/palantir-ontology-foundation]]
- [[sources/palantir-dynamic-ontology-core]]
- [[sources/palantir-toolchain-dynamic-ontology-1]]
- [[sources/palantir-semantic-compiler-engine-1]]

可靠性说明：以上来源均为二手评论材料。当前页面表达的是本 wiki 的阶段性学习结果，
不是 Palantir 官方定义。
