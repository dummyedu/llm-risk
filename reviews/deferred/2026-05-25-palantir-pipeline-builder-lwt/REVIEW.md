# Review：Palantir 实战（五）：Pipeline Builder 的轻量级转换

## 当前状态

已讨论，暂不进入正式 wiki 主线。

原因：这篇主要是数据工程执行引擎性能贴，说明同一个 Pipeline Builder 管道可以用
Spark 或 LWT 执行，影响成本、速度和开发反馈。它和 ontology 模型只有间接关系：
ontology 需要 clean dataset，而 Pipeline Builder 可能生产这些 dataset。

保留为 deferred review，后续如果研究数据管道、执行引擎或更新延迟问题，再回看。

## 先讲清楚：这篇到底举了什么例子

这篇文章不是继续创建 ontology 对象，也不是讲 action/workflow。

它讲的是：在 Palantir Foundry 里，数据进入 ontology 之前，通常需要先经过
Pipeline Builder 做清洗、join、字段规范化、字符串处理等转换。过去这些管道默认跑在
Spark 上，现在文章介绍一种新的执行方式：轻量级转换，英文是 Lightweight Transforms，
简称 LWT。

文章举的核心例子是一个中等规模数据管道：

```text
输入三个数据集：
- 7700 万行
- 2000 万行
- 20 万行

处理动作：
- 两次 inner join
- 列规范化
- 字符串清理

输出：
- 一个清洗后的结果数据集
```

然后作者比较两种执行方式：

| 执行方式 | 资源 | 时间 | 文章结论 |
| --- | --- | --- | --- |
| Spark | 16 个 executor，总计约 33 CPU，超过 100GB 内存 | 约 9 分钟 | 能跑，但对这种任务偏重 |
| LWT / Data Fusion | 8 CPU，60GB 内存 | 约 6 分 30 秒 | 更便宜、更快，适合中等规模常见管道 |

这篇的例子不是“如何建对象”，而是“如何更高效地产生对象背后的数据集”。

## 它和 ontology 的关系是什么

如果沿用我们刚才形成的工程理解：

```text
Palantir ontology
= 基于表数据的面向对象业务表达
```

那么 Pipeline Builder 处在更靠下的一层：

```text
原始数据
-> Pipeline Builder 清洗 / join / 转换
-> 输出干净 dataset
-> mapping 到 Object Type / Property / Link Type
-> 运行时对象
```

所以 Pipeline Builder 不是 ontology 本体本身。

它更像是 ontology 的数据准备层：

```text
Pipeline Builder = 生产对象属性和关系所需 dataset 的加工管道
```

上一篇讲：

```text
flight_alerts dataset
-> Flight Alert object type
```

这篇补的是更前一步：

```text
flight_alerts dataset 这种数据集，可能是由 Pipeline Builder 通过 join、filter、select、
字段清洗等转换做出来的。
```

## 这篇支持我们刚才理解的哪一部分

它支持：

```text
ontology 的对象世界不是凭空来的，而依赖底层数据管道产出的 dataset。
```

更具体地说：

- Object Type 的属性不是只靠人手写定义，还需要有稳定、干净、可更新的数据源。
- Mapping 能否成立，取决于底层 dataset 有没有被加工成合适形状。
- 如果对象背后的 dataset 来自复杂 join 和清洗，那么 Pipeline Builder 就是对象世界的前置生产线。
- Data Lineage 之所以重要，是因为它让我们可以从对象类型反查到这些 pipeline。

所以它强化了一个判断：

```text
ontology 不是独立于数据工程存在的。
ontology 上层看起来像对象模型，下层必须依赖数据管道把表数据加工成对象可用的形态。
```

## 这篇不能证明什么

这篇没有证明：

- Object Type 具体怎么定义；
- dataset 字段如何 mapping 到属性；
- 外键如何 mapping 到 link type；
- action 如何修改对象属性；
- workflow 如何基于对象状态触发 action；
- AI 输出如何进入对象/action/workflow。

所以它不能直接回答“本体到底是什么”，但它能回答：

```text
本体背后的数据集是如何被准备、转换和优化执行的。
```

## 它的关键概念

### Pipeline Builder

文章把 Pipeline Builder 描述为 Palantir 平台中用于构建数据管道的无代码/低代码可视化工具。
用户可以拖拽和配置数据源、转换节点、清洗逻辑，最后产出服务上层应用和 ontology 的数据集。

来源位置：正文行 15-20。

### Spark

文章说过去 Pipeline Builder 的批处理管道默认跑在 Spark 上。Spark 适合 TB/PB 级数据和复杂
shuffle，但启动重、资源消耗大、开发反馈慢。

来源位置：正文行 21-36。

### Lightweight Transforms / LWT

LWT 是文章介绍的新执行方式。它不走 Spark 的分布式模型，而是使用 Data Fusion 的单节点执行模型。
文章认为很多企业管道其实没有大到必须用 Spark，LWT 对这些中等规模转换更便宜、更快。

来源位置：正文行 37-54。

### 一键切换执行引擎

文章最重要的产品点是：用户可以把一个 Spark 管道在设置中点击“转换为轻量级管道”。
系统会做兼容性检查。如果 Join、Filter、Select 等节点被 LWT 支持，就可以切换。

来源位置：正文行 69-75。

### 不兼容节点

文章举了一个不能直接转换的例子：`repartition`。因为 repartition 是 Spark 分布式数据分片概念，
在单节点 LWT 中没有意义。系统会高亮不兼容节点，让用户删除或改回 Spark。

来源位置：正文行 104-114。

## 来源文件或来源包

- 来源文件：`Palantir实战（五）：Pipeline Builder 的轻量级转换.mhtml`
- 来源路径：`/Users/ningl/work/risk/palantir/Palantir实战（五）：Pipeline Builder 的轻量级转换.mhtml`
- Manifest 条目：`raw/palantir/MANIFEST.md` 第 51 行附近
- Manifest 主题：`enterprise intelligence context`
- 文件大小：4416314 bytes
- 保存或修改时间：2025-11-13 06:08:03
- 文章内显示发布时间：2025-11-03 07:59
- 表观作者/账号：`小智58` / `智见AI视界`
- 来源层级：Tier B/C，二手教程/解读；文章声称基于 Palantir 技术主管 Xander Bailey 和架构师 Chad Wahlquist 的演示，但本文本身不是官方文档。

## 来源事实摘要

- 文章承接前一篇 RAG 应用，转向 Palantir 平台中的数据工程组件 Pipeline Builder。
  来源位置：正文行 6-14。
- 文章描述 Pipeline Builder 是无代码/低代码可视化数据管道工具，用于集成、清洗、转换数据，并最终构建服务上层应用的 ontology。
  来源位置：正文行 15-20。
- 文章称 Pipeline Builder 过去的批处理默认在 Spark 上执行。来源位置：正文行 21-24。
- 文章列出 Spark 的成本：启动 Driver/Executor、JVM、Jar、Spark Context，资源消耗和启动延迟较大。
  来源位置：正文行 25-36。
- 文章认为很多企业管道没有达到必须使用分布式集群的规模。来源位置：正文行 34-36。
- 文章介绍 LWT，引入 Data Fusion 单节点执行模型。来源位置：正文行 37-45。
- 文章举例说一个 LWT 管道初始化时间为 7 秒。来源位置：正文行 49-52。
- 文章的 A/B 测试处理三个数据集，规模分别为 7700 万行、2000 万行、20 万行，进行两次 inner join、列规范化和字符串清理。
  来源位置：正文行 55-60。
- Spark 基准配置使用 16 个 executor，总计 33 CPU、超过 100GB 内存，约 9 分钟完成。
  来源位置：正文行 61-68。
- LWT 配置使用 8 CPU、60GB 内存，约 6 分 30 秒完成。来源位置：正文行 69-92。
- 文章强调 LWT 改善开发体验：启动快、预览快，开发者能更频繁测试管道逻辑。
  来源位置：正文行 93-103。
- 文章说明 LWT 不是替代 Spark。遇到不支持操作或大规模 shuffle 时仍可使用 Spark。
  来源位置：正文行 104-128。
- 文章建议默认先用 LWT，只有当数据规模或操作复杂度压垮单节点时再升级到 Spark。
  来源位置：正文行 129-136。

## Review 判断

这篇文章应该作为“ontology 下方的数据管道层”来吸收。

它对当前 wiki 的贡献不是新增一个 ontology 定义，而是补上这条链路：

```text
对象模型依赖 dataset
dataset 依赖 pipeline
pipeline 需要选择合适执行引擎
执行引擎影响成本、延迟、开发反馈和可维护性
```

这对我们理解 Palantir 有帮助：Palantir 的 ontology 如果要成为运行时对象世界，它下方必须有持续更新的数据工程系统。Pipeline Builder 就是这套系统里更接近业务用户的一层。

## 与当前工作理解的关系

用户当前阶段性理解是：

```text
ontology = 基于表数据的面向对象业务表达
```

本篇对这句话的补充是：

```text
表数据不是天然适合进入对象世界。
它需要先经过 pipeline 清洗、join、规范化和转换。
Pipeline Builder 是这个前置加工层。
```

所以可以把整体理解扩展为：

```text
raw tables
-> pipeline transforms
-> clean datasets
-> mapping
-> object types / properties / links
-> runtime objects
-> actions / workflows
```

## 拟议 wiki 更新

若用户批准，建议：

- 创建 `wiki/sources/palantir-pipeline-builder-lwt.md`，作为可读文章分析页。
- 新建或更新 `wiki/mechanisms/data-pipeline-to-ontology.md`，解释从 raw tables 到 clean datasets 再到 object mapping 的链路。
- 更新 [[concepts/ontology]]，补一句：ontology 的对象模型依赖底层数据管道产出可映射的数据集。
- 更新 [[mechanisms/data-to-ontology-mapping]]，补入 Pipeline Builder 的位置：它更偏 mapping 之前的数据准备层。
- 更新 [[questions]]，保留：Pipeline Builder 到 Object Type mapping 的边界在哪里？哪些字段/关系在 pipeline 层处理，哪些在 ontology mapping 层处理？

## 待讨论问题

1. 你是否同意把 Pipeline Builder 放在 ontology 的下游数据准备层，而不是 ontology 本体层？
2. 这篇是否让“基于表数据的面向对象表达”更完整：表数据先要被 pipeline 加工成 clean dataset？
3. 我们是否需要单独建一个机制页：`从数据管道到 Ontology`？
4. 下一篇是否继续读 `Palantir实战（六）：防御性数据库之优化索引刷新语义.mhtml`，顺着数据管道和更新语义往下看？
