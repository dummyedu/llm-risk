# Review：Palantir 实战（一）：构建第一个本体

## 结论

这篇来源从抽象工具链转向具体操作。它不是解释 Palantir 底层架构，而是跟随
Palantir Learn 课程《Deep Dive: Creating Your First Ontology》，演示如何在
Foundry 中安装课程环境、用 Object Explorer 浏览已有航空公司本体、用 Data
Lineage 追溯对象类型背后的数据集和转换逻辑，并用 Ontology Manager 扩展一个
新的 `Flight Alert` 对象类型、链接类型和 action。

本 review 的判断是：这篇非常适合验证我们刚才讨论的“对象、关系、映射、action”
在实操层面的样子。它清楚展示了对象类型、对象实例、对象集合、链接遍历、数据血缘、
主键/标题键、外键链接和 action 参数表单。但它仍然是教程型材料，重点是“如何点出来
一个最小本体扩展”，还没有回答更复杂的问题：业务规则从哪里来、如何治理审批、如何
测试回滚、如何把多个业务闭环沉淀成可复用模板。

## 来源文件或来源包

- 来源文件：`Palantir实战（一）：手把手教你构建第一个本体（Ontology）.mhtml`
- 来源路径：`/Users/ningl/work/risk/palantir/Palantir实战（一）：手把手教你构建第一个本体（Ontology）.mhtml`
- Manifest 条目：`raw/palantir/MANIFEST.md` 第 48 行
- Manifest 主题：`ontology / semantic layer`
- MHTML 内容来源：`https://mp.weixin.qq.com/s/EuPSyj20Yjlxmiu2EvscTQ`
- 参考课程 URL：`https://learn.palantir.com/deep-dive-creating-your-first-ontology`
- 本 review 中的来源层级：Tier B/C，二手教程总结；引用 Palantir Learn 课程，但本文本身不是官方文档。

## 来源卡片

- 标题：Palantir实战（一）：手把手教你构建第一个本体（Ontology）
- 来源路径：`/Users/ningl/work/risk/palantir/Palantir实战（一）：手把手教你构建第一个本体（Ontology）.mhtml`
- 文件类型：MHTML，保存的网页文章
- 保存或修改时间：2025-11-20 09:25:25
- 文章内显示发布时间：2025-09-16 00:06
- 表观作者/账号：`小智58` / `智见AI视界`
- 表观主题：跟随 Palantir Learn 课程，使用 Foundry 构建第一个 ontology
- 当前为什么读：上一轮工具链讨论停在抽象层，本篇提供更接近实际操作的对象、链接、数据血缘和 action 示例。
- Review 状态：待用户讨论

## 事实性摘要

- 文章说明，本篇以 Palantir 官方于 2025 年更新的免费在线课程
  `Deep Dive: Creating Your First Ontology` 为蓝本，并跟随前 Palantir 工程师、
  Ontologize 团队专家 Gena 的视角。来源位置：正文行 15-23。
- 文章第一步是在 Foundry 中创建工作目录，并从 Marketplace 安装课程产品包
  `Deep Dive: Creating Your First Ontology`。来源位置：正文行 25-60。
- 课程包包含对象视图模块、对象类型、动作类型、数据处理管道和后端数据集。
  安装时需要勾选 `Prefix ontology entities` 以避免多人学习时命名冲突。来源位置：
  正文行 50-58。
- 文章介绍虚构航空公司 `Fresh Air` 场景，包含 Airline、Route、Aircraft、Flight、
  Flight Alert、Airport、Runway 等对象类型。来源位置：正文行 62-70。
- 文章用 Object Explorer 搜索 `Fresh Air Inc.`，说明对象类型是 `Airline`，
  `Fresh Air Inc.` 是该类型的一个对象实例。来源位置：正文行 71-89。
- 文章通过 `Routes` 标签页打开对象集合，展示可以按 Origin、Destination 等属性
  交互式筛选航线。来源位置：正文行 108-142。
- 文章说明可以从航线对象集合通过 Linked Objects 做链接遍历，例如从 routes
  跳转到 origin airports，再跳转到 runway。来源位置：正文行 143-168。
- 文章介绍 Data Lineage：可从对象类型追溯到直接依赖的数据集、转换逻辑和上游数据。
  来源位置：正文行 169-217。
- 文章指出对象类型本身不属于某个项目，它是更高层次的语义定义；其权限继承自后端
  数据集。来源位置：正文行 198-203。
- 文章以 `OFT Airport` 为例，追溯到后端数据集 `ontology_airport`，并指出该数据集
  由 Pipeline Builder 转换生成。来源位置：正文行 208-216。
- 文章进入 Ontology Manager，任务是创建新的 `Flight Alert` 对象类型，用来记录航班
  延误、取消或改道等事件。来源位置：正文行 218-227。
- 创建对象类型时，文章选择已有数据源 `flight_alerts`，设置主键 `flight_alert_id`
  和标题键 `alert_title`。来源位置：正文行 231-263。
- 保存后，Foundry 会将后端数据集中的数据索引到 Object Storage V2；同步可能因主键
  不唯一、数据类型不匹配或缺少依赖列失败。来源位置：正文行 265-267。
- 文章创建链接类型，将 `Flight Alert` 与 `Flight` 关联。一个 Flight 可对应多个
  Alert，一个 Alert 只对应一个 Flight；系统识别 `flight_id` 外键与 Flight 主键匹配。
  来源位置：正文行 268-289。
- 文章创建 action type `Assign Root Cause`，只允许用户修改 `Flight Alert` 的
  `root_cause` 属性，并通过参数表单收集用户输入。来源位置：正文行 290-327。
- 最后，文章在 Object Explorer 中执行该 action，提交后 `root_cause` 属性被更新。
  来源位置：正文行 328-348。
- 文章总结称，本体为 AI 提供语义丰富的输入，也为 AI 输出提供写回目的地，例如建议、
  预测或修复方案可以写回相应对象属性。来源位置：正文行 356-369。

## 重要来源主张

| 主张 | 来源位置 | Review 状态 |
| --- | --- | --- |
| 本体不仅是数据集合，也是业务实体、关系和互动方式的建模。 | 正文行 10-14 | 作者 framing；与前文一致但仍需官方验证 |
| Object Explorer 可让用户像搜索引擎一样探索 ontology 数据。 | 正文行 62-65 | 教程描述；需与实际 Foundry 功能验证 |
| 对象类型是业务实体蓝图，对象实例是该类型下的具体数据。 | 正文行 85-89、231-233 | 教程描述；可作为学习框架 |
| 对象集合是动态查询结果，可用于交互式筛选和分析。 | 正文行 116-142 | 教程描述；可作为学习框架 |
| 链接遍历可从一个对象集合跳转到关联对象集合。 | 正文行 143-168 | 教程描述；可作为关系/链接学习材料 |
| Data Lineage 能追溯对象类型背后的数据集、转换逻辑和上游数据。 | 正文行 169-217 | 教程描述；重要但需实际平台验证 |
| 对象类型不属于项目，权限继承自后端数据集。 | 正文行 198-203 | 作者/教程描述；需官方验证 |
| 创建对象类型时，主键必须唯一且稳定。 | 正文行 248-267 | 教程描述；工程上重要 |
| Link Type 可通过外键把新对象类型与已有对象类型连接。 | 正文行 268-289 | 教程描述；直接回应关系/映射讨论 |
| Action 是 ontology 的动词，提供受控和可审计的交互方式。 | 正文行 290-293 | 作者 framing；有价值但仍需官方验证 |
| AI 输出可以写回本体对象属性，让建议、预测、修复方案进入业务场景。 | 正文行 361-369 | 作者观点；需后续 AIP/action 来源验证 |

## 使用的正文块索引

- 正文行 10-24：文章定位，从理论转向 Foundry 实操。
- 正文行 25-60：安装课程环境和 Marketplace 产品包。
- 正文行 62-168：用 Object Explorer 探索 Fresh Air 本体、对象实例、对象集合和链接遍历。
- 正文行 169-217：用 Data Lineage 追溯对象类型、数据集、转换逻辑和 Pipeline Builder。
- 正文行 218-267：用 Ontology Manager 创建 `Flight Alert` 对象类型。
- 正文行 268-289：创建 `Flight Alert -> Flight` 链接类型。
- 正文行 290-348：创建并执行 `Assign Root Cause` action。
- 正文行 356-369：总结 ontology 对 AI 输入和输出写回的价值。

## 作者观点或 framing

- 作者把本体构建描述为“从理解到创造”的全过程，强调从浏览已有 ontology、追溯数据血缘，到创建对象、链接和 action。
- 作者把 action 称为本体的“动词”，对象和链接是“名词”。这个隐喻与前几篇 Data/Logic/Action 框架一致，但本篇只演示了简单属性修改动作。
- 作者认为 ontology 为 AI 提供干净、可用、语义丰富的输入，并为 AI 输出提供写回目的地。这是重要方向，但本篇没有实际演示 AIP/agent。
- 文章是教程复述，操作细节价值高，但不应把教程场景直接推论为企业级复杂治理能力。

## LLM 推断

- 这篇补足了我们刚才讨论的“关系和映射”中最具体的一环：`Flight Alert` 与 `Flight`
  的 link type 来自 `flight_id` 外键匹配。关系在 ontology 层被命名和浏览，映射在数据源/键匹配层实现。
- `Data Lineage` 是连接语义层与数据工程层的重要工具：它让对象类型不只是业务词汇，而能追溯到后端 dataset、转换逻辑和 pipeline。
- 这篇的 action 示例很小，只是修改 `root_cause` 属性，但它很好地说明 action 的基本形态：受控字段、参数表单、提交后写回对象属性。
- 这篇仍未充分解释规则从哪里来。`Assign Root Cause` 基本没有复杂业务规则；它更像“受控编辑动作”，不是完整的 Logic Plan。
- 本篇适合推动我们把 `对象类型 / 对象实例 / 对象集合 / link type / data lineage / action type`
  这些操作性概念写入综合页，但暂不适合证明 Palantir 已经解决复杂业务规则收敛问题。

## 与前几篇的关系

- 前几篇讲 Data/Logic/Action、动态本体和语义编译，本篇第一次具体展示对象、链接和 action 如何在 Foundry UI 中被创建和执行。
- 它对 [[concepts/ontology-relation-types]] 有直接补充：link type 在工具里有明确创建流程，并依赖外键匹配。
- 它对 [[concepts/semantic-compiler-implementation-notes]] 有直接补充：文章展示了“对象/链接/action”的最低限度实操路径，但仍没有进入复杂规则拆解和系统收敛。

## 用户判断记录

暂无新的用户判断。本篇 review 应等待用户讨论。

## 拟议 wiki 更新

若用户批准，建议：

- 创建 `wiki/sources/palantir-first-ontology-practice.md`。
- 更新 [[concepts/semantic-compiler-implementation-notes]]，补入“实操路径：Object Explorer -> Data Lineage -> Ontology Manager -> Action”。
- 更新 [[concepts/ontology-relation-types]]，补入 `Flight Alert -> Flight` link type 与 `flight_id` 外键匹配示例。
- 更新 [[concepts/palantir-dynamic-ontology]]，补入“Data Lineage 让对象类型可追溯到 dataset / pipeline”的阶段性结论。
- 更新 [[questions]]，保留“教程式 action 与复杂业务规则/Logic Plan 之间的差距”。

## 待讨论问题

1. 这篇是否回答了你对“关系和映射分别是什么”的疑问，尤其是 link type 与外键匹配？
2. `Assign Root Cause` 这种 action 是否只能说明受控字段编辑，还不能说明复杂业务 action？
3. Data Lineage 是否应作为我们理解 ontology 收敛的关键机制：对象类型必须能追溯到 dataset 和 pipeline？
4. 本篇是否说明 Foundry 的入门路径是：先看已有对象和关系，再追溯数据血缘，最后扩展对象、链接和 action？
5. 下一篇是否继续读 `Palantir实战（二）：为RAG工作流赋能，从PDF到向量化本体的全流程解析.pdf`，还是先读更贴近 Pipeline Builder 的 `Palantir实战（五）：Pipeline Builder 的轻量级转换.mhtml`？

## 应用笔记

暂无正式应用假设。

保留一个 **Application hypothesis / LLM inference**：如果未来应用到本地 `risk`
项目，入门闭环不应先做复杂 agent，而可以先做：

```text
一个对象类型
一个与既有对象的 link type
一个可追溯的数据源或派生数据集
一个受控 action
一个对象视图或审计记录
```

该假设未在 `risk` 中验证，不能作为实施要求。

## 建议下一篇来源

有两个合理方向：

1. `Palantir实战（二）：为RAG工作流赋能，从PDF到向量化本体的全流程解析.pdf`
   - 优点：延续“实战”系列顺序。
   - 风险：可能转向 RAG/PDF，不一定继续回答 ontology 构建细节。

2. `Palantir实战（五）：Pipeline Builder 的轻量级转换.mhtml`
   - 优点：更贴近本轮关心的数据准备、mapping、pipeline 和对象来源。
   - 风险：跳过实战（二）（三）（四）的上下文。

基于当前研究问题，推荐下一篇优先读 `Palantir实战（五）：Pipeline Builder 的轻量级转换.mhtml`，因为它更可能回答“对象类型背后的 dataset/pipeline 怎么做出来”。
