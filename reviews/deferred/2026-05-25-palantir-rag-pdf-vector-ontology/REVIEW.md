# Review：Palantir 实战（二）：从 PDF 到向量化本体

## 当前状态

已讨论，转为 deferred / discarded，不进入正式 wiki 主线。

原因：这篇主要是 RAG 数据准备，把 PDF 切成 chunk、计算 embedding，再包装成
`FAA Chunk` object type。它解释了实战（三）的前置对象从哪里来，但和前面讨论的业务
ontology 建模不是同一类东西。当前只把它保留为理解实战（三）的背景，不把它吸收进正式
wiki 的核心结论。

## 先讲清楚：这篇到底举了什么例子

这篇文章接在 `Palantir 实战（一）` 后面，但它不是继续做航班告警对象，也不是讲 agent
怎么对话。

它举的是一个 FAA 飞行员手册的 RAG 数据准备例子：

```text
FAA 飞行员手册 PDF
-> 上传到 Foundry Pipeline Builder
-> 抽取 PDF 文本
-> 合并页文本为长文本
-> 按语义分块
-> 每个 chunk 展平成一行
-> 为每个 chunk 计算 embedding
-> 发布成 ontology 里的 FAA Chunk object type
```

这篇的核心不是“问答效果”，而是“怎么把一个非结构化 PDF 变成 AI 可以检索、引用、
复用的 ontology 对象”。

## 这个例子里，本体到底是什么

在这篇文章里，ontology 不是传统业务对象，而是知识对象：

```text
Object Type: FAA Chunk
Object: FAA 手册里的一个文本块
Primary Key: chunk_number
Title: extracted_text
Important properties:
- extracted_text
- embedding
- media_reference
- path
- timestamp
```

所以，本篇扩展了我们对 ontology 的理解：

```text
ontology 里不只可以放 Airline、Flight、Flight Alert 这类业务对象，
也可以放文档片段、证据材料、知识 chunk 这类知识对象。
```

这也解释了为什么 `实战（三）` 不能跳着读：第三篇里的 AIP Agent 不是凭空读 PDF，
而是读取第二篇已经创建好的 `FAA Chunk` 对象。

## 这篇文章中的操作流程

文章按这个顺序走：

1. 选择 FAA 的 `Pilot's Handbook of Aeronautical Knowledge` 作为示例 PDF。
2. 在 Pipeline Builder 里创建一个新 batch pipeline。
3. 直接在 pipeline 界面上传 PDF，并存成一个新的 Media Set。
4. 将资源重命名为 `FAA Document`。
5. 检查 PDF 是机器可读文本还是扫描件；本例选择可读文本路径。
6. 使用 `Extract text from PDF` 转换。
7. 设置提取方法为 `Raw text`，选择 `media_reference`，从第 16 页到第 513 页抽取核心内容。
8. 因抽取结果按页形成数组，先用 `Join array` 把页文本合并为一个连续文本流。
9. 用 `Chunk string` 分块，设置 chunk size 为 512，chunk overlap 为 50，并按段落、换行、空格等分隔符切分。
10. 用 `Explode array with position` 把 chunk 数组展平成多行，并保留 position。
11. 用 `Extract many struct fields` 抽出 `chunk_number` 和 `extracted_text` 两列。
12. 使用 `Text to embeddings`，选择 `extracted_text` 作为输入。
13. 选择 embedding 模型，例如文章中使用 OpenAI `text-embedding-ada-002`。
14. 把输出列命名为 `embedding`，避免覆盖原始文本列。
15. 在 pipeline 末端 `Add output -> New object type`，创建 `FAA Chunk` 对象类型。
16. 将主键手动设置为 `chunk_number`，标题键设置为 `extracted_text`。
17. 检查 `embedding` 属性的 base type 是 `Vector`，并确认 embedding model 与 pipeline 中使用的模型一致。
18. 部署 pipeline，并在 Ontology Manager 中验证 `FAA Chunk` 已生成。

## 这篇最有用的理解

这篇把 RAG 的“文档处理”放进了 ontology 工程里。

普通 RAG 很容易被理解为：

```text
上传文档
-> 向量化
-> 检索
-> 回答
```

但这篇展示的 Palantir 路径更像：

```text
文档
-> pipeline 中的可追溯数据处理
-> chunk dataset
-> embedding vector
-> ontology object type
-> 后续被 AIP Logic / AIP Agent Studio 使用
```

关键变化在于：文本块不是临时塞进某个 agent 的私有知识库，而是被资产化成可治理、
可追溯、可被多个应用复用的对象。

## 它和第一篇 ontology 实战的关系

第一篇：

```text
flight_alerts dataset
-> Flight Alert object type
-> Flight Alert 与 Flight 的 link
-> Assign Root Cause action
```

第二篇：

```text
FAA PDF
-> extracted text
-> chunks
-> embeddings
-> FAA Chunk object type
```

两篇共同支持一个更稳的理解：

```text
Palantir ontology = 把不同来源的数据加工成可运行、可检索、可治理的对象世界。
```

第一篇偏业务对象和 action，第二篇偏知识对象和检索。

## 它和第三篇 AIP Agent 的关系

第三篇里 agent 用的是 `FAA Chunk` 或类似对象类型。第二篇解释了这些对象怎么来的：

```text
PDF 内容不是直接给 agent。
PDF 先被切成 chunk，每个 chunk 成为 ontology object，并带有 extracted_text 和 embedding。
Agent 后续通过 Ontology Context 检索这些对象，再把相关文本交给 LLM 回答。
```

所以第三篇应该等第二篇 review 完成后再恢复。

## 这篇能说明什么

这篇能说明：

- Palantir 可以把非结构化 PDF 通过 pipeline 转成结构化 chunk 数据。
- 文本分块不是小技术细节，而直接影响检索精度和 embedding 质量。
- `chunk_number` 这种人工构造的稳定编号可以成为知识 chunk 对象的主键。
- `embedding` 被作为 Vector 类型属性挂到对象上。
- embedding 模型在数据准备阶段和查询阶段必须一致，否则向量距离没有意义。
- 文档片段可以进入 ontology，成为后续 agent 和应用共享的知识资产。

## 这篇不能说明什么

这篇不能证明：

- AIP Agent 的回答质量一定好。
- Ontology Context 的检索排序、过滤和引用机制具体如何实现。
- PDF chunk 对象如何和传统业务对象建立关系。
- agent 是否能根据这些知识对象安全执行 action。
- 复杂文档、表格、图片、扫描件、跨页段落在真实企业场景中是否稳定处理。

它展示的是“准备可检索知识对象”的数据工程链路，不是完整 RAG 应用，也不是行动闭环。

## 来源文件或来源包

- 来源文件：`Palantir实战（二）：为RAG工作流赋能，从PDF到向量化本体的全流程解析.pdf`
- 来源路径：`/Users/ningl/work/risk/palantir/Palantir实战（二）：为RAG工作流赋能，从PDF到向量化本体的全流程解析.pdf`
- Manifest 条目：`raw/palantir/MANIFEST.md` 第 50 行
- Manifest 主题：`ontology / semantic layer`
- 文件大小：4531979 bytes
- 保存或修改时间：2025-11-12 03:14:50
- 文章内显示发布时间：2025-09-21 14:00
- 表观作者/账号：`小智58` / `智见AI视界`
- 来源层级：Tier B/C，二手教程总结；疑似微信文章导出的 PDF，不是 Palantir 官方文档。

## 来源卡片

- 标题：Palantir实战（二）：为RAG工作流赋能，从PDF到向量化本体的全流程解析
- 来源路径：`/Users/ningl/work/risk/palantir/Palantir实战（二）：为RAG工作流赋能，从PDF到向量化本体的全流程解析.pdf`
- 文件类型：PDF，图片型网页导出；本地 `pdftotext` 无法抽出正文，已按页图核读
- 保存或修改时间：2025-11-12 03:14:50
- 表观主题：把 FAA 手册 PDF 转成可向量检索的 ontology object type
- 当前为什么读：`实战（三）` 明确依赖本文创建的 `FAA Chunk` 对象；需要补齐顺序
- Review 状态：pending，等待用户讨论和批准

## 来源事实摘要

- 文章说明上一篇讨论了如何定义和创建 ontology，本篇转向如何为 RAG 工作流准备数据。
  来源位置：PDF 第 1 页。
- 文章选择 FAA 的 `Pilot's Handbook of Aeronautical Knowledge` 作为示例文档。
  来源位置：PDF 第 1-2 页。
- 文章目标是把该手册转化为智能问答系统可以理解和检索的知识库。
  来源位置：PDF 第 2 页。
- 文章在 Foundry Pipeline Builder 中创建 batch pipeline，并命名为类似
  `Compute Embeddings from FAA Handbook` 的管道。来源位置：PDF 第 2-3 页。
- 文章说明可以直接在 pipeline 界面上传 PDF，并将其存储为 Media Set。
  来源位置：PDF 第 3 页。
- 文章将上传后的资源重命名为 `FAA Document`。来源位置：PDF 第 3 页。
- 文章检查 PDF 是否可选中文本，并说明若是扫描件则需要 OCR；本例是机器可读 PDF。
  来源位置：PDF 第 4 页。
- 文章使用 `Extract text from PDF` 转换，提取方法选择 `Raw text`，媒体引用列选择
  `media_reference`。来源位置：PDF 第 4-5 页。
- 文章设置抽取页码范围为第 16 页到第 513 页，以跳过封面、目录、致谢、索引等噪声内容。
  来源位置：PDF 第 5 页。
- 文章说明初始 `extracted_text` 是数组，每个元素对应一页文本。来源位置：PDF 第 5 页。
- 文章选择先合并页文本再分块，使用 `Join array` 把数组合并成连续长文本，分隔符为空。
  来源位置：PDF 第 5-6 页。
- 文章说明分块的原因包括模型输入限制、检索精度和 embedding 质量。来源位置：PDF 第 6 页。
- 文章使用 `Chunk string`，输入列为 `extracted_text`，chunk size 设置为 512，
  chunk overlap 设置为 50。来源位置：PDF 第 7 页。
- 文章说明分隔符按段落、换行、空格等顺序尝试，以尽可能保持语义完整。
  来源位置：PDF 第 7 页。
- 文章使用 `Explode array with position` 将 chunk 数组展平成多行，并保留 position。
  来源位置：PDF 第 8 页。
- 文章说明 position 可作为每个文本块的唯一编号，并在后续创建对象时作为理想主键。
  来源位置：PDF 第 8 页。
- 文章使用 `Extract many struct fields`，将 position 和 element 抽取为 `chunk_number`
  和 `extracted_text`。来源位置：PDF 第 8-9 页。
- 文章使用 `Text to embeddings`，选择 `extracted_text` 作为输入列。来源位置：PDF 第 9-10 页。
- 文章选择 embedding 模型，提到 OpenAI `text-embedding-ada-002` 和 `text-embedding-3-small`
  等示例，并在本例中选择 `text-embedding-ada-002`。来源位置：PDF 第 10 页。
- 文章强调 output column 需要设为新列，例如 `embedding`，不能覆盖原始 `extracted_text`。
  来源位置：PDF 第 10-11 页。
- 文章说明转换后数据新增 `embedding` 列，Pipeline Builder 识别为 embedding vector 类型。
  来源位置：PDF 第 11 页。
- 文章在管道末端选择 `Add output -> New object type`，创建 `FAA Chunk` 对象类型。
  来源位置：PDF 第 11-12 页。
- 文章将 object type 命名为 `FAA Chunk`，主键设置为 `chunk_number`，标题键设置为
  `extracted_text`。来源位置：PDF 第 12 页。
- 文章提示不要把默认 ID 或 media item RID 当作主键，因为所有 chunk 来自同一个源文件，
  这些值不能唯一标识每个文本块。来源位置：PDF 第 12 页。
- 文章在 Ontology Manager 中验证 `FAA Chunk` 对象类型，并检查 `embedding` 属性的
  base type 为 `Vector`。来源位置：PDF 第 13 页。
- 文章强调 Ontology Manager 中的 Embedding Model 配置必须与 pipeline 中使用的
  embedding 模型一致。来源位置：PDF 第 14 页。
- 文章总结称，经过处理后，静态复杂 PDF 被转为动态、智能、AI 可用的数据资产，
  数千个带唯一标识、可检索的知识片段已融入 Palantir ontology 框架。
  来源位置：PDF 第 15 页。

## Review 判断

这篇应该作为“知识对象进入 ontology”的关键补充，而不是作为 agent 能力证明。

它适合进入 wiki 的内容是：

- 非结构化文档可以通过 pipeline 变成 ontology object type；
- chunk 是知识对象的基本粒度；
- embedding 是对象上的向量属性；
- 主键、标题、文本、向量和媒体引用共同构成可检索知识对象；
- 第三篇 AIP Agent 的 Ontology Context 依赖这些对象。

暂时不能进入正式结论的是：

- Palantir 的 RAG 检索质量；
- AIP Agent 对这些 chunk 的实际推理能力；
- 文档 chunk 和业务对象之间如何建立高质量语义关系；
- 多文档、多版本、权限、引用和更新治理如何处理。

## 和当前工作理解的关系

我们当前阶段性理解是：

```text
ontology = 基于表数据的面向对象业务表达
```

这篇需要把“表数据”放宽一点：进入 ontology 的不一定是传统业务表，也可以是通过 pipeline
从 PDF 生成的派生表。每一行代表一个知识 chunk，每一行再被映射成一个对象。

因此更准确的表达可以变成：

```text
ontology = 把底层数据资产加工成可运行、可检索、可治理对象世界的表达层。
```

其中底层数据资产可以是结构化表，也可以是非结构化文档经过抽取、分块、向量化后形成的
derived dataset。

## 拟议 wiki 更新

若用户批准，建议：

- 创建 `wiki/sources/palantir-rag-pdf-vector-ontology.md`，作为可读文章分析页。
- 更新 [[concepts/ontology]]，补入 ontology object 可以是文档 chunk / 知识对象。
- 更新 [[mechanisms/data-to-ontology-mapping]]，补入 `PDF -> extracted_text -> chunks -> embeddings -> object type` 链路。
- 新建或更新一个机制页，例如 `wiki/mechanisms/document-to-knowledge-object.md`，
  专门描述非结构化文档如何变成知识对象。
- 更新 [[questions]]，保留：chunk 与业务对象如何关联、embedding 模型一致性如何治理、
  文档版本和权限如何进入检索。
- 恢复 `reviews/deferred/2026-05-25-palantir-aip-agent-faa/REVIEW.md` 的后续讨论，
  因为它的前置来源已经补齐。

## 待讨论问题

1. 你是否同意：`FAA Chunk` 是知识对象，不是传统业务对象，但仍可以进入 ontology？
2. 这篇是否让我们把 ontology 理解从“基于表数据的面向对象表达”扩展为
   “基于底层数据资产的对象世界”，其中 PDF 先被 pipeline 变成 derived dataset？
3. `chunk_number` 作为主键这个点是否说明：进入 ontology 前，数据工程必须先构造稳定身份？
4. 第三篇 AIP Agent 是否可以在本文批准后重新 review，并只吸收“agent 读取 ontology objects”
   这一层？
