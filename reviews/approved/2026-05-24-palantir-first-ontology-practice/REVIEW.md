# Review：Palantir 实战（一）：构建第一个本体

## 当前状态

已讨论并应用到正式 wiki。

正式更新位置：

- `wiki/sources/palantir-first-ontology-practice.md`
- `wiki/concepts/ontology.md`
- `wiki/concepts/ontology-relation-types.md`
- `wiki/mechanisms/data-to-ontology-mapping.md`
- `wiki/mechanisms/governed-action.md`
- `wiki/concepts/palantir-dynamic-ontology.md`
- `wiki/questions.md`

## 先讲清楚：这篇到底举了什么例子

这篇文章讲的是一个虚构航空公司 `Fresh Air` 的教程。

它不是从零解释 Palantir 的完整架构，而是跟着一个 Palantir Learn 课程，在 Foundry
里做一个很小的 ontology 扩展。

这个例子里已经有一些业务对象：

- `Airline`：航空公司，例如 `Fresh Air Inc.`
- `Route`：航线
- `Airport`：机场
- `Runway`：跑道
- `Flight`：航班

教程先让读者在 Object Explorer 里看这些已有对象，然后做一件新事：

```text
给航班增加一种新的业务对象：Flight Alert
```

`Flight Alert` 可以理解为“航班告警”：

- 某个航班延误了；
- 某个航班取消了；
- 某个航班改道了；
- 需要有人记录原因。

所以这篇文章最核心的例子其实是：

```text
已有对象：Flight
新增对象：Flight Alert
新增关系：一个 Flight 可以有多个 Flight Alert
新增动作：给 Flight Alert 填写 root cause
```

## 这个例子里，本体到底是什么

在这篇教程里，本体不是一个抽象哲学词，也不是一个“知识图谱文件”。

更直接地说，Palantir 这里的 ontology 是一套把底层数据变成业务世界的结构：

```text
底层数据表 / pipeline
-> 对象类型
-> 对象实例
-> 对象之间的链接
-> 用户或系统可以执行的动作
```

放到这个例子里：

| Foundry 里的东西 | 在例子里是什么 | 它在 ontology 中的意义 |
| --- | --- | --- |
| 数据集 `flight_alerts` | 一张航班告警数据表 | 原始或处理后的数据来源 |
| Object Type `Flight Alert` | 航班告警这种业务对象 | 把表变成业务概念 |
| `flight_alert_id` | 告警 ID | 用来识别一个具体告警对象 |
| `alert_title` | 告警标题 | 用来显示对象名称 |
| `flight_id` | 指向航班的外键 | 用来把告警连到航班 |
| Link Type `Flight Alert -> Flight` | 告警属于哪个航班 | 业务关系 |
| Action `Assign Root Cause` | 填写告警根因 | 受控业务动作 |
| Data Lineage | 追溯对象来自哪个 dataset/pipeline | 可追溯性 |

所以，从实际 Palantir 行为看，这里的 ontology 至少包括五件事：

1. **对象定义**：什么叫一个 `Flight`，什么叫一个 `Flight Alert`。
2. **对象身份**：哪一列是唯一 ID，哪一列是标题。
3. **对象关系**：`Flight Alert` 怎么连到 `Flight`。
4. **数据来源**：这些对象背后来自哪个 dataset 和 pipeline。
5. **可执行动作**：用户可以对对象做什么，例如填写 `root_cause`。

## 这篇文章中的操作流程

文章按这个顺序走：

1. 安装 Palantir Learn 的课程包。
2. 在 Object Explorer 里搜索 `Fresh Air Inc.`。
3. 看到 `Fresh Air Inc.` 是一个 `Airline` 对象实例。
4. 进入它关联的 `Route`、`Airport`、`Runway` 等对象。
5. 用 Data Lineage 查看这些对象背后来自哪些 dataset 和 pipeline。
6. 在 Ontology Manager 里新建 `Flight Alert` 对象类型。
7. 选择已有数据源 `flight_alerts`。
8. 设置主键 `flight_alert_id` 和标题键 `alert_title`。
9. 创建 `Flight Alert -> Flight` 的 link type。
10. 创建 action：`Assign Root Cause`。
11. 在 Object Explorer 中执行 action，把 `root_cause` 写回到 `Flight Alert`。

## 从这个例子看，Palantir 的 ontology 更像什么

这篇给出的最有用理解是：

```text
ontology = 业务对象层 + 关系层 + 动作层 + 数据血缘层
```

它不是单纯的数据建模，因为它不只是告诉你表结构。

它也不是单纯的应用 UI，因为它不只是显示页面。

它更像一个夹在数据、应用和 AI 之间的业务运行层：

```text
数据表告诉系统有什么数据
ontology 告诉系统这些数据在业务里是什么
link type 告诉系统业务对象之间怎么连
action 告诉系统哪些变化是允许发生的
lineage 告诉系统这些对象从哪里来
```

如果把它翻译成更普通的软件语言：

- Object Type 有点像业务实体类型；
- Object Instance 有点像实体对象；
- Link Type 有点像显式命名的业务关系；
- Action 有点像受权限和表单约束的业务命令；
- Data Lineage 有点像从业务对象回看数据管道的可追溯机制。

## 这篇能说明什么

这篇能说明：

- Palantir 的 ontology 不是只写概念图，而是能落到 Foundry UI 的对象、关系和 action。
- 一个对象类型可以由 dataset 创建出来。
- 对象之间的关系可以通过外键匹配形成 link type。
- action 可以把用户输入写回对象属性。
- Data Lineage 能让对象类型追溯到底层数据和 pipeline。

这对我们之前讨论的“关系和映射”很关键：

```text
关系：Flight Alert 和 Flight 在业务上有关联
映射：用 flight_id 外键把 Flight Alert 数据行连到 Flight 对象
```

也就是说，关系不是凭空写一句“它们有关”；它要落到可识别的键、对象类型和 link type。

## 这篇不能说明什么

这篇不能证明 Palantir 已经解决了复杂企业治理问题。

原因是它的 action 很简单：

```text
Assign Root Cause = 给 root_cause 字段填一个值
```

这更像“受控编辑字段”，还不是复杂业务动作。例如它没有展示：

- 多步骤审批；
- 复杂规则判断；
- action 的测试和回滚；
- AI 建议如何进入审批链；
- 多对象、多部门、多权限的协同治理；
- action 执行后的审计和异常处理。

所以这篇的价值是“看见最小 ontology 操作单元”，不是证明企业级闭环已经完整成立。

## 来源文件或来源包

- 来源文件：`Palantir实战（一）：手把手教你构建第一个本体（Ontology）.mhtml`
- 来源路径：`/Users/ningl/work/risk/palantir/Palantir实战（一）：手把手教你构建第一个本体（Ontology）.mhtml`
- Manifest 条目：`raw/palantir/MANIFEST.md` 第 48 行
- Manifest 主题：`ontology / semantic layer`
- MHTML 内容来源：`https://mp.weixin.qq.com/s/EuPSyj20Yjlxmiu2EvscTQ`
- 参考课程 URL：`https://learn.palantir.com/deep-dive-creating-your-first-ontology`
- 来源层级：Tier B/C，二手教程总结；引用 Palantir Learn 课程，但本文本身不是官方文档。

## 来源卡片

- 标题：Palantir实战（一）：手把手教你构建第一个本体（Ontology）
- 文件类型：MHTML，保存的网页文章
- 保存或修改时间：2025-11-20 09:25:25
- 文章内显示发布时间：2025-09-16 00:06
- 表观作者/账号：`小智58` / `智见AI视界`
- 表观主题：跟随 Palantir Learn 课程，使用 Foundry 构建第一个 ontology
- 当前为什么读：前几篇停留在 ontology、semantic compiler、toolchain 的抽象层，本篇提供对象、链接、数据血缘和 action 的最小实操例子。
- Review 状态：已讨论并应用到正式 wiki

## 来源事实摘要

- 文章说明，本篇以 Palantir 官方免费在线课程 `Deep Dive: Creating Your First Ontology`
  为蓝本。来源位置：正文行 15-23。
- 文章第一步是在 Foundry 中创建工作目录，并从 Marketplace 安装课程产品包。
  来源位置：正文行 25-60。
- 课程包包含对象视图模块、对象类型、动作类型、数据处理管道和后端数据集。
  来源位置：正文行 50-58。
- 教程场景是虚构航空公司 `Fresh Air`，包含 Airline、Route、Aircraft、Flight、
  Flight Alert、Airport、Runway 等对象类型。来源位置：正文行 62-70。
- 文章用 Object Explorer 搜索 `Fresh Air Inc.`，说明它是 `Airline` 类型下的一个对象实例。
  来源位置：正文行 71-89。
- 文章展示可以从航线对象集合通过 Linked Objects 跳转到 origin airports 和 runway。
  来源位置：正文行 143-168。
- 文章介绍 Data Lineage，可从对象类型追溯到直接依赖的数据集、转换逻辑和上游数据。
  来源位置：正文行 169-217。
- 文章以 `OFT Airport` 为例，追溯到后端数据集 `ontology_airport`，并指出该数据集由
  Pipeline Builder 转换生成。来源位置：正文行 208-216。
- 文章进入 Ontology Manager，创建新的 `Flight Alert` 对象类型，用来记录航班延误、
  取消或改道等事件。来源位置：正文行 218-227。
- 创建对象类型时，文章选择已有数据源 `flight_alerts`，设置主键 `flight_alert_id`
  和标题键 `alert_title`。来源位置：正文行 231-263。
- 文章创建链接类型，将 `Flight Alert` 与 `Flight` 关联：一个 Flight 可对应多个 Alert，
  一个 Alert 只对应一个 Flight；系统识别 `flight_id` 外键与 Flight 主键匹配。
  来源位置：正文行 268-289。
- 文章创建 action type `Assign Root Cause`，只允许用户修改 `Flight Alert` 的
  `root_cause` 属性，并通过参数表单收集用户输入。来源位置：正文行 290-327。
- 最后，文章在 Object Explorer 中执行该 action，提交后 `root_cause` 属性被更新。
  来源位置：正文行 328-348。

## Review 判断

这篇应该作为“ontology 最小实操例子”来吸收，而不是作为 Palantir 全部 ontology
能力的证明。

可以进入 wiki 的主要内容是：

- 对象类型如何从 dataset 建出来；
- 主键、标题键如何让数据行变成对象；
- link type 如何通过外键连接对象；
- Data Lineage 如何让对象类型可追溯；
- action 如何成为对象上的受控写回入口。

暂时不能进入正式结论的是：

- Palantir 是否已经完整解决复杂业务规则编译；
- action 是否能自然覆盖复杂业务流程；
- AI 输出进入 ontology 后如何治理。

这些应保留为问题。

## 用户判断记录

用户提出一个更适合后续验证的工程化理解：

```text
Palantir ontology
= 基于表数据的面向对象业务表达
```

其中：

- 类 / Object Type 是模型；
- 实例 / Object 是运行时里的具体业务对象；
- mapping 把表、字段、外键映射成对象、属性和关系；
- action 像作用在对象上的受控业务函数；
- workflow 是基于对象状态、关系和事件推进的流程；
- 运行时会把具体数据、具体用户、具体事件填进这些模型。

本篇支持其中一部分：

- `flight_alerts` 数据集到 `Flight Alert` 对象类型，支持“表数据变成对象模型”；
- `flight_alert_id`、`alert_title`、`root_cause` 支持“字段映射成属性”；
- `flight_id` 支持“外键映射成对象关系”；
- `Assign Root Cause` 支持“action 是对象上的受控业务函数”。

本篇尚未充分支持：

- workflow 如何系统性地基于对象状态和事件触发 action；
- action 在复杂业务中如何审批、回滚、审计和编排；
- AI 输出如何进入 action/workflow。

后续阅读应围绕这些未验证点继续修正该理解。

## 拟议 wiki 更新

若用户批准，建议：

- 创建 `wiki/sources/palantir-first-ontology-practice.md`，用本文这种“例子先行”的方式写。
- 更新 [[concepts/ontology]]，补入“从 Foundry 行为看 ontology 是对象、关系、动作、血缘的业务运行层”。
- 更新 [[concepts/ontology-relation-types]]，补入 `Flight Alert -> Flight` link type 与 `flight_id` 外键匹配示例。
- 更新 [[concepts/palantir-dynamic-ontology]]，补入 Data Lineage 让对象类型可追溯到 dataset / pipeline。
- 更新 [[concepts/semantic-compiler-implementation-notes]]，说明本篇只展示最小 action，不足以证明复杂 Logic Plan。
- 更新 [[questions]]，保留“受控字段编辑 action 与复杂业务 action 的差距”。

## 待讨论问题

1. 这个 `Flight Alert -> Flight` 例子，是否回答了你对“关系和映射分别是什么”的疑问？
2. 你是否同意：本篇里的 action 更像受控字段编辑，还不能代表复杂业务 action？
3. Data Lineage 是否应该成为我们理解 Palantir ontology 的关键机制之一？
4. 批准后，正式 wiki 是否应该把这篇作为“最小 ontology 操作单元”的例子来吸收？

## 建议下一篇来源

基于当前问题，下一篇建议读：

```text
Palantir实战（五）：Pipeline Builder 的轻量级转换.mhtml
```

理由：这篇更可能继续解释对象类型背后的 dataset/pipeline 怎么做出来。

如果想按实战系列顺序，也可以读：

```text
Palantir实战（二）：为RAG工作流赋能，从PDF到向量化本体的全流程解析.pdf
```

但它可能转向 RAG/PDF，不一定继续回答 ontology 构建细节。
