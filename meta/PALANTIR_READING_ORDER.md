# Palantir 阅读顺序

## 说明

这不是单篇来源 review，不占用 `reviews/pending/` 队列。它只是根据
`raw/palantir/MANIFEST.md` 的文件名、粗分类和当前研究目标形成的第一轮阅读顺序。

真正的 review 仍然按“一次一篇文章”推进：

1. 单篇来源进入 `reviews/pending/<date>-<slug>/REVIEW.md`。
2. 用户讨论并批准。
3. 应用到 `wiki/sources/` 和相关综合页。
4. 移入 `reviews/approved/`。

## 来源包

- Manifest：`raw/palantir/MANIFEST.md`
- 外部来源家族：`/Users/ningl/work/risk/palantir`
- 外部文件数量：101
- 文件目的：在正式创建 wiki 页面前，先建立第一轮系统阅读顺序。
- 范围边界：本包只基于 manifest 元数据和文件名排序，不总结具体来源内容，也不把任何来源结论当作事实。

## 来源卡片

- 标题：Palantir 来源家族阅读顺序
- 来源路径：`raw/palantir/MANIFEST.md`；外部来源文件位于 `/Users/ningl/work/risk/palantir`
- 文件类型：manifest，以及外部 `mhtml`、`pdf` 混合来源
- 保存或修改时间：本包未逐一检查
- 表观主题：企业 AI 系统、Palantir ontology、AIP、FDE 交付、OSDK、案例、战略及相邻背景
- 当前为什么读：先建立共同的概念骨架，再逐文件 review，最后再进入 wiki 综合
- 状态：阅读顺序参考；不是文章 review

## 排序原则

1. 先读能说明企业 AI 问题、Palantir 系统观、决策/行动闭环的导论性材料。
2. 再读 ontology 和 semantic layer，因为后面的 AIP、agent、OSDK、交付主张都依赖这套词汇。
3. 概念性 ontology 之后再读 RAG、搜索、工具链和实战材料，让实现细节有上下文。
4. ontology 之后再读 AIP 和 agent 材料，避免把 AIP 当作普通 LLM workflow 来理解。
5. 平台机制之后再读 FDE/交付/文化，因为交付模型要放在产品模型之后才容易判断。
6. 客户案例和生态集成放在机制与交付模型之后，作为检验材料，而不是直接当作营销证明。
7. 市场、领导层、公司叙事和相邻背景最后读，因为它们有解释价值，但不应定义技术 wiki 的主结构。

## 事实性摘要

- `raw/palantir/MANIFEST.md` 索引了 101 个文件。
- 101 个条目当前全部标记为 `unreviewed`。
- `meta/INGEST_LEDGER.md` 暂无已记录 ingest。
- 创建本包前，`reviews/pending/` 下没有已有 review package。
- 当前 `wiki/` 仍是骨架状态；尚无通过该流程批准的 Palantir source-derived wiki 页面。

## 重要来源主张

本包不评估来源主张。后续需要按单篇 source review 逐条抽取和验证。

## 作者观点或 framing

本包不评估具体作者观点。许多标题包含较强 framing，如“护城河”“终极”“革命”“霸主”“无法被复制”；在具体来源 review 前，这些都只能视为作者 framing。

## LLM 推断

- 下方阅读顺序是根据文件名、manifest 粗分类和项目工作流约束形成的 LLM 推断。
- 该顺序不是关于来源质量或正确性的事实判断。
- 部分文件可能是外围材料或重复材料，但需要在逐文件 review 时确认。

## 拟议 wiki 更新

暂无。本包只提出 review 顺序。每篇来源的 wiki 更新应等待对应 source-specific review package 被批准后再进行。

## 推荐第一篇来源

从这篇开始：

1. `从Palantir看_企业级AI的十一部曲(总序）.mhtml`

理由：标题显示它是更大企业 AI 阅读框架的总序或导言，适合先定义问题地图，而不是直接进入技术结论。

## 完整拟议阅读顺序

### 阶段 1：导论与企业 AI 问题框架

1. `从Palantir看_企业级AI的十一部曲(总序）.mhtml`
2. `Palantir 架构深度解析：从数据集成到应用落地.mhtml`
3. `从 Palantir 看决策范式的演进：数据时代的答案与 AI 时代的挑战.mhtml`
4. `AI革命的最大障碍，不是算法，而是“数据集成”.mhtml`
5. `AI+软件产业_从代码革命到系统革命.mhtml`
6. `智能型企业：面向人工智能未来的IT架构（一）.mhtml`
7. `智能型企业：面向人工智能未来的IT架构（二）.mhtml`
8. `智能型企业：面向人工智能未来的IT架构（三）.mhtml`
9. `为什么软件吞噬了世界，却没有把蛋糕做大？.mhtml`
10. `万物皆可Palantir？警惕AI初创公司的“服务化陷阱”与“伪平台”幻觉.mhtml`

### 阶段 2：Ontology 与语义层核心

11. `连接AI与决策：深度解析Palantir的“基石”：本体（Ontology）.mhtml`
12. `解构Palantir的核心：Ontology如何为海量数据注入灵魂.mhtml`
13. `Palantir揭秘：为什么说“本体”是AI时代的真正护城河？.mhtml`
14. `Palantir CTO重磅解读：将你的业务编译成代码，“本体论”才是数字时代的终极武器.mhtml`
15. `AI时代的语义驱动_Palantir基于OODA的产品逻辑.mhtml`
16. `从 Palantir看_动态本体如何成为企业级AI的核心范式.mhtml`
17. `从洞察到行动：Palantir的“本体”如何将数据真正转化为企业行动力？.mhtml`
18. `在“最优复杂性”中寻找极简之道——解读Palantir 本体论的实战哲学.mhtml`
19. `Palantir的“语言隐喻”：AI如何像人类一样理解业务现实？.mhtml`
20. `计算范式的断层_从通用计算到语义计算.mhtml`
21. `当本体（Ontology）遇上AI，如何重塑企业主数据管理的未来？.mhtml`
22. `本体管道：秘制语义知识库AI引擎 - 极道.mhtml`
23. `AI 基础设施与本体论的深度融合：解构 NVIDIA 与 Palantir 的全栈野心.mhtml`
24. `从a16z的“AI软件开发栈”看_碎片化生态的逻辑断层与语义统一之路.mhtml`
25. `从企业制度与生产力出发_Agent-Centric与Ontology-Centric架构的融合逻辑(Agent Skills的行动语义编译).mhtml`
26. `智能体无界：利用Ontology-MCP构建全域连接的AI生态系统.mhtml`
27. `Palantir发布的“本体驱动的智能体”，是AI迈向自主决策的终极形态？.mhtml`
28. `Palantir首席架构师深度对话：AI与工作的未来，从“替代”到“本体融合”的架构重构.mhtml`
29. `[必收藏] Palantir大模型平台深度解析：从本体论到企业AI决策实战_palantir本体论-CSDN博客.mhtml`

### 阶段 3：Ontology 实践、搜索、RAG 与工具链

30. `Palantir AIP 深度解析（一）：超越 RAG，用本体增强生成（OAG）重塑企业决策.mhtml`
31. `Palantir AIP 深度解析（二）：为 RAG_OAG 注入“逻辑”之魂，让大模型不再“纸上谈兵”.mhtml`
32. `Palantir AIP 深度解析（三）：跨越关键词的鸿沟，七步构建企业级语义搜索应用.pdf`
33. `深度解析（三）：跨越关键词的鸿沟，七步构建企业级语义搜索应用（2）.pdf`
34. `Palantir AIP 深度解析（四）：超越关键词与向量，本体驱动的搜索如何实现真正的“理解”？.mhtml`
35. `Palantir实战（一）：手把手教你构建第一个本体（Ontology）.mhtml`
36. `Palantir实战（二）：为RAG工作流赋能，从PDF到向量化本体的全流程解析.pdf`
37. `Palantir实战（四）：从零开始构建企业级RAG智能应用.pdf`
38. `Palantir实战（六）：防御性数据库之优化索引刷新语义.mhtml`
39. `从Palantir看_工具链如何支撑动态本体的构建和运行(一).mhtml`
40. `从Palantir看_工具链如何支撑动态本体的构建和运行(二)_语义编译_从定义到执行的语义引擎(上).mhtml`

### 阶段 4：OSDK 与应用开发

41. `Palantir揭秘：OSDK 深度解析，重新定义企业级应用开发的未来.mhtml`
42. `从数据底座到全栈应用：Palantir OSDK与PACK如何重塑前端开发的“广度”与“深度”.mhtml`
43. `Palantir如何用「本体SDK」实现Vibe Coding？.mhtml`

### 阶段 5：AIP、Agents、Evals 与 AI 工作流

44. `Palantir揭秘：如何通过AIP平台将AI转化为真正的生产力.mhtml`
45. `从 Palantir AIP 看_下一代企业级 AI 系统 —— 从 AIP 到语义自治系统架构(Part 1).mhtml`
46. `Palantir CEO AIPCon主旨演讲：破除硅谷大模型迷思，揭示AI革命的真正前景.mhtml`
47. `Palantir AIP Evals如何将生成式AI安全带入企业核心.mhtml`
48. `Palantir AIP 深度解析（七）：AIP平台的可观测性.mhtml`
49. `Palantir AIP 深度解析（五）：构建企业级AI客户服务引擎——从自动化到知识沉淀.mhtml`
50. `Palantir AIP 深度解析（六）：解锁工业AI——从沉睡的图纸到鲜活的数字孪生.mhtml`
51. `Palantir的终极野心：用AIP重塑未来的企业级“智能体操作系统”.mhtml`
52. `Palantir AIP 驱动医疗行业变革，HCA的AI医院管理实践启示.mhtml`
53. `First Solar 与 Palantir 如何重新定义 AI Agent：基于“知识节点”的专家级推理进阶.mhtml`
54. `Palantir实战（三）：构建你的第一个AIP智能体——从结构化知识到智能对话.mhtml`
55. `Palantir实战：使用AIP构建AI驱动的流程挖掘与自动化系统.mhtml`
56. `AI智能体的新范式？摩根士丹利研究员深度解析：为什么强化学习（RL）是关键的下一步.mhtml`
57. `谷歌DeepMind大神深度解读：大模型推理的“黑魔法”——从思维链到自我进化.mhtml`

### 阶段 6：FDE、交付模型与工程文化

58. `Palantir FDE 深度解析：是一场营销游戏，还是软件工程的革命？.mhtml`
59. `Palantir FDE的一天：我们不仅仅是工程师，更是问题的解决者.mhtml`
60. `Dev vs. Delta：深度解析Palantir两大核心工程角色，揭秘其独特的工程师文化.mhtml`
61. `FDE已成过去式？揭秘Palantir的下一个“超级士兵”：全栈工程师.mhtml`
62. `Palantir 的“反销售”革命：揭秘其征服AI时代的秘密武器——软件训练营.mhtml`
63. `从 Palantir 看_下一代企业级AI系统规模化交付_业务结果_落地路径探讨—— 工程机制篇.mhtml`
64. `从概念验证到生产力革命：Palantir AI FDE如何让工业巨头实现“代码自由”？.mhtml`
65. `揭秘Palantir的灵魂：为什么FDE模式的模仿者都只学到了皮毛？.mhtml`
66. `揭秘Palantir FDE 团队的另一面：部署策略师 “Echo” 的一天.mhtml`
67. `揭秘 Palantir 的基线团队和前沿部署基础设施工程.mhtml`
68. `Palantir CIO深度揭秘，如何用自家软件重塑内部IT.mhtml`
69. `Palantir CIO深度揭秘，如何颠覆传统的内部IT组织？.mhtml`
70. `Palantir首席营收官（CRO）深度专访：解构“反咨询”模式、Karp的长期主义与Thiel的“压力测试”文化.mhtml`
71. `超越“创始人模式”：Palantir 实战启示录——为何“使命模式”才是硬科技的终极解法？.mhtml`

### 阶段 7：客户案例与生态集成

72. `Palantir Foundry：AI赋能RaceTrac革新便利店体验.mhtml`
73. `Palantir HyperAuto如何颠覆SAP数据壁垒，让业务人员成为AI应用的构建者.mhtml`
74. `Palantir如何驱动采购领域的AI自动化变革？.mhtml`
75. `Palantir 驱动 AI 招聘革命：每天为每位顾问节省1小时，这家巨头如何凭空“创造”56名员工？.mhtml`
76. `巨头联手，重塑企业大脑：深度解析SAP与Palantir如何开启认知数字孪生新纪元.mhtml`
77. `深度解析：SAP与Palantir战略集成的技术架构与运营逻辑.mhtml`
78. `双剑合璧：Palantir与Databricks集成的战略图谱与技术架构.mhtml`
79. `深度对决：Palantir vs. Databricks，谁是 AI 时代的数据终局？.mhtml`
80. `动态关税冲击下,Palantir的答案_企业供应链敏捷闭环决策是出路.mhtml`

### 阶段 8：市场、公司、领导层与战略叙事

81. `AI时代的“数字孪生”霸主：深度解析Palantir无法被复制的护城河.mhtml`
82. `从项目到产品：深度拆解Palantir的万亿市值转型之路.mhtml`
83. `Palantir Q4 2025财报深度解析：业绩炸裂，这已不仅仅是增长，而是代际跨越.mhtml`
84. `Palantir揭秘：单季营收破10亿美金，股价狂飙后，用“封神”业绩回答一切质疑.mhtml`
85. `Palantir 2026年展望：AI软件霸主的67倍市销率神话能否延续？.mhtml`
86. `一个“局内人”的深度反思：Palantir究竟是一家怎样的公司？.mhtml`
87. `数据霸权下的哲学幽灵：解构 Palantir 的崛起与野心.mhtml`
88. `揭开神秘面纱：Palantir官方回应，一次性说清所有争议.mhtml`
89. `Alex Karp的达沃斯启示录：AI时代的权力位移与真实性革命.mhtml`
90. `Palantir深度解码：一个“硅谷异类”CEO与他眼中的AI未来.mhtml`
91. `Palantir的“怪咖军团”：深度解码千亿AI帝国背后的“精神内核”.mhtml`
92. `深度 _ Palantir CTO万字实录：解构一个硅谷“异端”的国防、AI与价值观.mhtml`
93. `换个视角看Palantir：前员工揭秘“杀伤链”与“政府操作系统”的背后.mhtml`

### 阶段 9：相邻 AI、政策与外围背景

94. `AI推理新范式_Prefill→Decode解耦推动智能云发展.mhtml`
95. `从 Groq 看：软硬融合一体推理系统的“性能确定性”设计逻辑及工具链探讨.mhtml`
96. `深度对话 DeepMind CEO Demis Hassabis：AGI前夜的战略蓝图与技术沉思.mhtml`
97. `警钟长鸣：在AI“军备竞赛”的狂热中，职场菜鸟正成为牺牲品！.mhtml`
98. `政府工作报告2026.pdf`
99. `CNCA-C18-02：2024强制性产品认证实施规则 灭火器.pdf`

### 阶段 10：暂存，等待去重或重分类

100. `Palantir揭秘：软件开发的终局，是被“本体”统一？.mhtml`
101. `Palantir实战（五）：Pipeline Builder 的轻量级转换.mhtml`

说明：本阶段保存的是需要在内容 review 后确认最佳归类的条目。后续它们可能移动到 ontology/工具链或应用开发阶段。

## 待讨论问题

1. source-level review 是否从推荐第一篇开始，还是先读更技术性的 ontology primer？
2. 看起来重复的 PDF 和文章，如果确认内容高度一致，是否作为小 bundle 一起 review？
3. 明显外围的材料，例如并非直接讨论 Palantir 的监管 PDF，是否继续留在 Palantir 来源家族，还是移入后续外部背景队列？

## 下一步 review 动作

创建第一篇 source-specific review package：

`从Palantir看_企业级AI的十一部曲(总序）.mhtml`

该 package 应遵循 `docs/workflows/research-one-source.md`，从实际来源中抽取主张，并在写入任何正式 wiki 页面前停下来与用户讨论。
