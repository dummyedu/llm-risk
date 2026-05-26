# 问题

## 耐久研究问题

- Palantir 在运营系统里说的 ontology 到底是什么？
- OAG（ontology-augmented generation）和 RAG 的实质差异在哪里？
- AIP 中哪些部分属于模型能力，哪些属于治理能力，哪些属于交付方法？
- FDE、bootcamp 和客户部署实践如何改变软件产品化？
- OSDK 对企业应用开发意味着什么？
- 哪些 Palantir 思想是通用 enterprise-intelligence 方法，哪些只是 Palantir 产品与销售模型的特定结果？

## 工具链问题

- 来源事实（Source fact）：`语义编译：从定义到执行的语义引擎（上）` 明确说明
  `Ontology Service / Logic Service / Runtime Engine` 是作者抽象，不是 Palantir
  官方命名。
- 用户判断（User judgment）：研究整体架构时，小样本/小本体只是研究方法和路径的一环，不能和最终目标混淆；最终目标是满足预期并产生价值。
- 用户判断（User judgment）：Data 很重要；Logic 是业务专家真正要把握的核心，不需要完整但要关键；Action 的价值在于行为闭环；模型贵精不贵多，应优先把重要功能的完整闭环做完。
- LLM 推断（LLM inference）：`Dataset / Mapping / Ontology / Logic / Action` 目前只作为逐步学习的工作框架，不应过早定论为最终架构。
- LLM 推断（LLM inference）：高质量 derived dataset 已经承载大量决策 Data；ontology 的增量价值必须来自 logic、action、权限、审计、复用和 AI/agent 边界，而不只是 mapping。
- LLM 推断（LLM inference）：动态本体工具链不能只停留在 `Semantic OS`、`Semantic Compiler`、`Logic Plan` 等抽象词，必须解释从业务目标到可运行闭环的实际构建路径。
- LLM 推断（LLM inference）：后续工具链研究应按这条路径追问：业务目标 / 预期价值 -> pipeline / preprocessing -> derived dataset / entity alignment / 口径治理 -> object / property 抽象 -> key logic 实现 -> controlled action / writeback -> governance / permission / audit -> testing / rollback / feedback。
- LLM 推断（LLM inference）：`Logic Plan` 可以暂时作为理解关键业务 logic 如何被执行、审计和复用的中间概念，但不能过早假设 Palantir 产品中一定以该名称或该结构实现。
- 研究问题（Research question）：动态本体是否需要一个“语义编译”层，才能从对象建模进入可执行运行时？
- 研究问题（Research question）：`Govern` 是否应被理解为贯穿 ontology、logic、
  runtime 的横切机制，而不是独立阶段？
- 研究问题（Research question）：作者抽象出的
  `Ontology Service / Logic Service / Runtime Engine` 与 Palantir 官方产品模块之间
  是否存在可验证对应关系？
- 研究问题（Research question）：企业级 agent 的边界是否应由 ontology、rules、permissions 和 action types 定义，而不是由 prompt 或硬编码流程定义？
- 研究问题（Research question）：“自演化 ontology”在企业治理中必须满足哪些测试、审批、审计和回滚条件？
- 研究问题（Research question）：工具链评价标准应是术语完整性，还是关键场景闭环是否产生价值？

## 本体与决策问题

- 来源事实（Source fact）：`连接AI与决策：深度解析Palantir的“基石”：本体（Ontology）` 将决策拆为 Data、Logic、Action 三个要素；该来源是二手评论，不是官方材料。
- 来源事实（Source fact）：`Palantir 实战（一）：构建第一个本体` 展示了 `flight_alerts`
  dataset 到 `Flight Alert` object type、属性、link type 和 `Assign Root Cause` action 的最小链路；该来源是二手教程总结，不是官方材料。
- 来源事实（Source fact）：`使用 AIP 构建 AI 驱动的流程挖掘与自动化系统` 展示了
  SAP 数据到流程对象、流程日志、ontology、Machinery、Workshop、AIP Logic 和 Automate
  的信用冻结建议链路；该来源是二手教程总结，不是官方材料。
- LLM 推断（LLM inference）：ontology 可以暂时理解为以决策为中心的业务运行模型，而不只是数据语义层；但该理解仍需后续来源验证。
- 用户判断（User judgment）：当前更工程化的阶段理解是：ontology 是基于表数据的面向对象业务表达；类是 Object Type，实例是运行时 Object，mapping 把表和字段连到对象、属性和关系，action 像对象上的受控函数。
- 用户判断（User judgment）：治理后的 ontology 对象模型比临时拼接数据更适合承载反复发生的业务决策；它提高的不是 LLM 本身智力，而是业务上下文的表达力、可复用性和可治理性。
- 研究问题（Research question）：企业 AI 的关键资产是否不只是业务数据，还包括历史决策过程、被评估选项、最终行动和下游影响？
- 研究问题（Research question）：LLM/AIP 在 ontology 中到底应承担自然语言入口、解释、方案生成、工具选择、动作编排中的哪些角色？
- 研究问题（Research question）：OAG 中“LLM 不是推理主体，真正推理发生在 ontology 内部”这个说法是否过强？
- 研究问题（Research question）：ontology 与更强 LLM/agent 的关系是替代关系，还是“治理化理性系统 + 生成式直觉系统”的组合关系？
- 研究问题（Research question）：`Assign Root Cause` 这种最小 action 和复杂企业 workflow 之间缺哪些环节：审批、权限、测试、回滚、异常处理、审计和多对象协同分别在哪里发生？
- 研究问题（Research question）：Palantir 官方材料如何定义 Object Type、Object、Link Type、Action Type、Ontology Context，和当前“面向对象业务表达”的类比是否一致？
- 研究问题（Research question）：`AIP Logic` 的输出是只写回 ontology 的建议字段，还是能直接触发受控 action？
- 研究问题（Research question）：`Automate` 触发的是判断函数、暂存动作，还是实际业务写回？如果能写回 SAP，审批、审计和回滚在哪里？

## `risk` 应用问题

- 应用假设（Application hypothesis）：`risk` 项目的 ERC/catalog/tool gateway 是否能成为轻量 ontology-like semantic layer？
- 应用假设（Application hypothesis）：哪些 Palantir-style eval 或 guardrail 思路可以在不采用 Palantir 完整模型的前提下，用 `risk` assistant 测试？
- 应用假设（Application hypothesis）：哪些 FDE 或 bootcamp 交付实践有助于把新的业务切片接入 `risk` assistant？
