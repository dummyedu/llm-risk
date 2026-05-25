# Review：Palantir 实战（三）：构建你的第一个 AIP 智能体

## 当前状态

已讨论，转为 deferred / discarded，不进入正式 wiki。

说明：这篇文章明确承接 `Palantir 实战（二)`。实战（二）已经判断为 RAG 数据准备旁支，
不进入 wiki 主线。本文进一步把该旁支包装成 AIP Agent 问答应用，本质仍是
`对象检索 + LLM 回答`，没有补充业务 ontology、action 或 workflow 闭环。

用户判断：这篇对当前主线价值很低，废弃。

## 先讲清楚：这篇到底举了什么例子

这篇文章举的是一个 FAA 飞行训练手册问答智能体。

前置假设是：上一篇已经把 FAA 飞行员手册 PDF 处理成了 ontology 里的对象：

```text
Object Type: FAA Chunk
Object: 每一个手册文本片段
Property:
- extracted_text：片段原文
- embedding：片段向量
```

这篇要做的是把这些 `FAA Chunk` 对象接到 AIP Agent Studio，做成一个聊天式专家：

```text
用户提问：
What are hazardous attitudes and their antidotes?

系统做：
1. 根据问题去 FAA Chunk.embedding 做语义搜索
2. 找出相关 FAA Chunk 对象
3. 把这些对象的 extracted_text 放进 LLM 上下文
4. LLM 生成回答
5. 回答下方显示引用，能追溯到具体 FAA Chunk
```

所以这篇最核心的例子不是“agent 自己懂飞行”，而是：

```text
agent 使用 ontology 中已有的 FAA Chunk 对象作为检索上下文，生成可追溯回答。
```

## 它和我们当前模型理解的关系

我们当前的阶段性理解是：

```text
ontology = 基于表数据的面向对象业务表达
```

这篇把 AI/agent 放到了这个对象世界之上：

```text
PDF 文档
-> 切片、抽取、embedding
-> FAA Chunk Object Type
-> FAA Chunk runtime objects
-> Agent Studio 配置 Ontology Context
-> 用户对话时检索相关对象
-> LLM 基于对象内容生成回答
-> 回答带引用，回到对象
```

这说明 agent 不是直接面对一堆散乱 PDF，也不是只靠 prompt。

它面对的是已经被组织成 ontology object 的知识资产。

## 这篇里的本体到底是什么

在这个例子中，本体不是航空知识的抽象概念图，而是一个可被检索和复用的对象集合：

```text
FAA Chunk = 飞行手册文本片段对象
```

每个 `FAA Chunk` 至少有：

- 文本内容：`extracted_text`
- 向量表示：`embedding`

所以这里的本体对象很朴素：

```text
一个文档片段
被做成一个对象
对象上挂着原文和 embedding
agent 可以检索这些对象
```

这和上一篇 `Flight Alert` 的例子不同：

| 文章 | Object Type | 对象代表什么 | 主要用途 |
| --- | --- | --- | --- |
| 实战（一） | `Flight Alert` | 航班告警 | 业务对象、关系、action |
| 实战（三） | `FAA Chunk` | 文档片段 | 语义检索、问答上下文、引用追溯 |

这说明 ontology 里的对象不一定都是传统业务实体，也可以是知识片段、文档块、证据材料。

## Document Context 和 Ontology Context 的区别

这篇最有用的区别是：

```text
Document Context = 临时上传文件给这个 agent 用
Ontology Context = 连接到已经建好的 ontology object type
```

文章对两者的取向很明确：

- Document Context 配置快，但更像一次性知识，和平台其他对象隔离。
- Ontology Context 复用性强，因为 `FAA Chunk` 对象可以被多个 agent、AIP Logic、Workshop 应用共享。
- Ontology Context 未来还可以把文本块和结构化对象建立链接，例如飞行课程、飞机型号、证书要求等。

这对我们理解 Palantir 很关键：

```text
Palantir 不希望每个 agent 都自己上传一份知识。
它倾向于先把知识沉淀成 ontology object，再让多个 AI 应用复用。
```

## Agent 在这里到底是什么

从这篇行为看，AIP Agent 更像一个被配置出来的“对象检索 + LLM 回答”的交互入口。

它包含：

- 一个底层 LLM，例如 GPT-4.1 或类似模型；
- 一段系统指令，例如“你是友好且知识渊博的飞行教官”；
- 温度等生成参数；
- Retrieval Context，尤其是 Ontology Context；
- 起始提示；
- 发布版本；
- 可嵌入 Workshop 的交互控件。

所以这个 agent 不是新的业务对象模型，而是一个使用对象模型的 AI 交互层：

```text
Agent = LLM + instructions + retrieval context + UI/deployment wrapper
```

## 它和 action/workflow 的关系

这篇主要讲问答，不讲 action。

它展示的是：

```text
用户问题
-> agent 检索 ontology objects
-> LLM 生成答案
-> 返回引用
```

还没有展示：

```text
agent 调用 action 修改对象
agent 触发 workflow
agent 进入审批链
agent 执行业务操作
```

所以这篇支持的是“AI 如何读取对象世界”，还不支持“AI 如何改变对象世界”。

这点非常重要：

```text
本篇证明 agent 可以基于 ontology 做可追溯问答。
本篇没有证明 agent 可以安全执行业务 action。
```

## 来源文件或来源包

- 来源文件：`Palantir实战（三）：构建你的第一个AIP智能体——从结构化知识到智能对话.mhtml`
- 来源路径：`/Users/ningl/work/risk/palantir/Palantir实战（三）：构建你的第一个AIP智能体——从结构化知识到智能对话.mhtml`
- Manifest 条目：`raw/palantir/MANIFEST.md` 第 49 行附近
- Manifest 主题：`AIP / agents / evals`
- 文件大小：5069478 bytes
- 保存或修改时间：2025-11-12 03:44:39
- 文章内显示发布时间：2025-09-22 00:12
- 表观作者/账号：`小智58` / `智见AI视界`
- 来源层级：Tier B/C，二手教程总结；文章依赖前一篇 PDF-to-ontology/RAG 教程，但本文本身不是官方文档。

## 来源事实摘要

- 文章承接实战（二），说明前序工作已经把 FAA 飞行员手册 PDF 切片，并生成 embedding，形成可搜索的 ontology 资产。来源位置：正文行 8-12。
- 本文目标是用 AIP Agent Studio，基于前序 ontology 资产，构建 FAA 专家智能体。来源位置：正文行 11-16。
- 文章要求 Foundry 环境中已有 `FAA Chunk` 或类似对象类型，每个对象实例代表手册文本片段。来源位置：正文行 17-23。
- `FAA Chunk` 至少需要 `extracted_text` 和 `embedding` 属性：前者供 LLM 阅读，后者供语义搜索。来源位置：正文行 24-33。
- 文章介绍 AIP Agent Studio 是用于构建、配置和部署对话式 AI 应用的环境，并和 AIP Logic 区分。来源位置：正文行 34-36。
- 创建 agent 时选择 Standard Agent，配置名称、描述和存储位置。来源位置：正文行 37-50。
- 配置 agent 时选择模型、系统指令和温度。来源位置：正文行 59-65。
- 文章将 Retrieval Context 描述为让系统在处理用户消息时自动检索并附加相关背景信息的机制。来源位置：正文行 66-71。
- 文章区分 Document Context 和 Ontology Context。Document Context 是直接上传 PDF；Ontology Context 是链接到已有对象类型。来源位置：正文行 72-87。
- 配置 Ontology Context 时，选择 `FAA Chunk` 对象类型，Object Set 设为 Relevant objects，Search Property 选择 `embedding`。来源位置：正文行 88-107。
- 测试时可以询问 PAVE checklist、hazardous attitudes、carburetor icing 等问题。来源位置：正文行 108-115。
- 回答下方会显示引用，可追溯到用于生成答案的 FAA Chunk 对象。来源位置：正文行 113-115。
- 文章最后将 agent 保存发布，并嵌入 Workshop 应用的 AIP Agent interactive widget。来源位置：正文行 126-144。
- 文章总结称，将非结构化知识本体化，再通过 Agent Studio 赋予对话能力，可以让 AI 与组织数据和业务流程集成。来源位置：正文行 145-149。

## Review 判断

这篇应作为“AI 如何读取 ontology 对象世界”的例子来吸收。

它补上了当前理解中的一层：

```text
模型 / 对象 / mapping
-> ontology 中形成可检索对象
-> agent 把对象作为 retrieval context
-> LLM 生成带引用回答
```

它没有补上 action/workflow 的执行层。

所以本篇适合形成一个阶段性结论：

```text
Palantir 的 agent 首先不是自主行动者，而是一个可以连接 ontology context 的对话入口。
当 ontology 中的对象带有 embedding 和可追溯文本时，agent 可以把它们作为检索上下文，生成可引用回答。
```

## 和当前工作理解的关系

用户当前理解：

```text
ontology = 基于表数据的面向对象业务表达
```

本篇扩展为：

```text
ontology 不只容纳传统业务对象，也可以容纳文档切片、知识片段、证据对象。
agent 通过 Ontology Context 使用这些对象，而不是每次临时上传文件。
```

所以当前整体链路可以扩展为：

```text
PDF / raw data
-> pipeline / extraction / embedding
-> knowledge object type, such as FAA Chunk
-> runtime knowledge objects
-> ontology context
-> agent retrieval
-> grounded answer with citation
```

## 拟议 wiki 更新

若用户批准，建议：

- 创建 `wiki/sources/palantir-aip-agent-faa.md`，作为可读文章分析页。
- 新建或更新 `wiki/concepts/aip-agent.md`，把 agent 定义为 `LLM + instructions + retrieval context + deployment wrapper` 的阶段性理解。
- 更新 [[concepts/ontology]]，补入 ontology object 可以是知识片段，不只传统业务实体。
- 更新 [[concepts/oag]] 或新建机制页，说明 Ontology Context 如何让 agent 使用 ontology objects。
- 更新 [[questions]]，保留：agent 如何从“读取对象世界”走向“修改对象世界/action/workflow”。

## 待讨论问题

1. 你是否同意：这篇只证明了 agent 读取 ontology objects，不证明 agent 执行业务 action？
2. `FAA Chunk` 这种文档片段对象，是否可以纳入我们对 ontology 的理解：ontology 中不只有业务实体，也有知识对象/证据对象？
3. Document Context vs Ontology Context 的区别，是否说明 Palantir 的主张是“先资产化知识，再让 AI 复用”？
4. 下一篇是否应该读 `Palantir AIP 深度解析（二）：为 RAG/OAG 注入“逻辑”之魂，让大模型不再“纸上谈兵”`，继续追 action/logic？
