# Review：Palantir 揭秘：OSDK 深度解析，重新定义企业级应用开发的未来

## 当前状态

待讨论。

这篇接着上一篇 `Ontology-Oriented Software Development`，但比上一篇具体。它讲的是：

```text
当 ontology 已经定义了对象、关系、action、function 和权限后，
Palantir 如何把这些东西生成成开发者可用的 SDK，
让外部应用围绕业务对象读写和调用能力。
```

它的关键词是：

```text
OSDK
Developer Console
Application Type
User permissions / Application permissions
Ontology and Resource Scoping
Object Types / Links / Actions / Functions
TypeScript / Python / cURL SDK
React application
write back to ontology
```

## 先讲清楚：这篇到底举了什么例子

文章使用虚构公司 `Titan Industries` 的供应链应急场景。

前置场景是：

```text
Titan Industries 的配送中心发生火灾。
已有 AIP 应用能展示受火灾影响的客户订单，并找到替代配送中心。
```

新的需求是：

```text
管理层需要评估火灾损失；
希望调用公共卫星拍摄火场；
希望 LLM 自动找到合适卫星；
希望在新的 React 应用中完成卫星任务创建。
```

为此，文章说需要扩展 Titan ontology：

```text
Plant Events：记录火灾等事件；
Sensor Task：定义需要拍摄的位置和图像类型；
Satellite：可执行拍摄任务的卫星实体；
LLM Function：寻找合适卫星的 Sat Helper function；
Action：创建任务或事件等写回操作。
```

然后通过 Developer Console 生成一个面向这个业务范围的 OSDK 包。

## OSDK 到底是什么

这篇把 OSDK 说成：

```text
your ontology's SDK = your business's SDK
```

更克制地说，OSDK 是：

```text
把 ontology 中被授权暴露的对象、关系、action 和 function，
生成成开发者可调用的软件开发接口。
```

它不是自动写应用，也不是消除所有开发工作。它是让开发者不再每次从底层数据库/API 开始，而是从已经建好的业务对象层开始。

## 深入研究：为什么 OSDK 是关键工具

用户判断：

```text
OSDK 很重要，因为它介绍的是最关键的工具。工具可以衍生出一切，因为工具是载体。
```

这个判断应该进入 review。前面几篇讲 ontology、FDE、交付、平台可部署性，还是偏方法和组织；OSDK 这篇开始触及“能力如何被开发者拿到手”的载体。

更准确地说：

```text
ontology 是模型层；
OSDK 是模型层向应用开发、AI 调用、低代码扩展和外部系统集成开放的开发者边界。
```

如果没有 OSDK 或类似接口，ontology 可能主要停留在 Palantir 内部应用、Workshop、Object Explorer 等平台内工具里。
有了 OSDK，开发者可以把 ontology 里的对象、action、function 和权限边界带进自己的前端、后端、移动端、边缘应用或自动化服务。

所以 OSDK 的关键性不在于“又多了一个 SDK”，而在于：

```text
它决定了 ontology 能否从平台内部模型，变成可被持续扩展的业务开发接口。
```

## 官方资料校正

我查了 Palantir 官方文档和公开代码仓库，当前 pending review 的核心判断基本成立，但需要补强几个边界。

### 1. OSDK 的官方定位

Palantir 官方 OSDK overview 明确说，OSDK 让开发者在开发环境中访问 Foundry Ontology；支持 TypeScript 的 NPM、Python 的 Pip/Conda、Java 的 Maven，以及通过 OpenAPI 支持其他语言。官方也把它描述为把 Foundry 当作后端，用 ontology 查询、Foundry writeback 和治理控制来构建应用。

来源：

- https://www.palantir.com/docs/foundry/ontology-sdk/overview

这支持我们的判断：

```text
OSDK 是 ontology 的开发者接口层，不是单纯前端 SDK。
```

### 2. OSDK 不是暴露整个 ontology，而是暴露选定范围

官方文档说，OSDK 的类型和函数基于“与你相关的 ontology 子集”生成；token 也只 scoped 到应用被允许访问的 ontology entities，并叠加用户本身的数据权限。

Developer Console 文档进一步说明：添加 object types、link types、action types、functions 到 SDK 配置时，这些资源和依赖会加入应用的 resource access restrictions。依赖变化、移除资源、旧客户端兼容都需要手动管理或通过 Developer Console 修正。

来源：

- https://www.palantir.com/docs/foundry/ontology-sdk/overview
- https://www.palantir.com/docs/foundry/developer-console/permissions
- https://www.palantir.com/docs/foundry/developer-console/create-application

这让“工具可以衍生一切”更精确：

```text
OSDK 是有范围的工具载体。
它不是把企业全部 ontology 打开，而是为一个应用选择必要对象、关系、action、function 和依赖资源。
```

### 3. 权限模型是 OSDK 的核心，不是附属功能

官方 Developer Console 权限文档区分：

```text
User permissions：由当前用户权限决定可读写什么，使用 authorization code grant。
Application permissions：应用使用 generated service user，使用 client credentials grant。
```

client-facing 应用必须使用 user permissions；backend service 可以使用服务用户。官方文档也提醒 service user 需要被授予具体项目、object types、datasets 等权限。

来源：

- https://www.palantir.com/docs/foundry/developer-console/permissions
- https://www.palantir.com/docs/foundry/consumer-mode/client-credentials-setup/

这说明 OSDK 的本质不是“绕过权限快速开发”，而是：

```text
把 ontology 权限模型、OAuth 应用边界、资源范围和 SDK 生成绑在一起。
```

### 4. OSDK 能读写 ontology，但 action/writeback 仍然有严格边界

官方 Action 文档说明，action type 定义的是一次对 objects、properties、links 的变更，也可以有 side effects。Action rules 可以编辑 ontology，也可以触发 Foundry 中的其他效果；webhook 可在 action 被应用时请求外部系统。

但官方 Apply Action API 文档也明确提醒：HTTP 200 只表示服务器收到并处理请求，要看 response body 里的 validation result 才知道 action 是否成功。Action 权限文档还说明，不同 writeback 设置下，提交 action 的用户需要不同权限；“only allow edits via actions” 是推荐方向，以避免为了直接编辑底层 writeback dataset 暴露过多数据。

来源：

- https://www.palantir.com/docs/foundry/action-types/overview
- https://www.palantir.com/docs/foundry/action-types/rules
- https://www.palantir.com/docs/foundry/action-types/permissions
- https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/actions/apply-action

这支持我们之前的警惕：

```text
写回 ontology 不等于外部业务系统已经完成执行。
action 是否触发外部系统、是否有 webhook、是否审批、是否回滚，仍要看 action 配置和治理边界。
```

### 5. OSDK 的工程边界真实存在

官方 `Unsupported types for OSDK` 文档列出不同语言 SDK 不支持的 object property、action parameter、function input/output 类型；还说明 OAuth 2.0 webhook action types 不支持通过 SDK 应用使用，除非用户先通过 Foundry 授权 outbound application。

TypeScript OSDK migration guide 显示 OSDK 版本迁移会带来类型兼容、对象包装、日期类型、action 调用等变化。Palantir 公开的 `osdk-ts` 仓库也表明 TypeScript OSDK 是一组真实维护的包，包括 `@osdk/client`、`@osdk/api`、`@osdk/foundry-sdk-generator`、`@osdk/oauth`。

来源：

- https://www.palantir.com/docs/foundry/ontology-sdk/unsupported-types
- https://www.palantir.com/docs/foundry/ontology-sdk/typescript-osdk-migration
- https://github.com/palantir/osdk-ts

这进一步说明：

```text
OSDK 是强工具，但不是无成本工具。
它会带来版本、类型、兼容性、权限、scope、unsupported types、客户端升级等工程问题。
```

## 工具链分层理解

基于文章和官方资料，可以把 OSDK 放进当前 wiki 的工具链位置：

```text
现有系统 / 数据源
-> Foundry 数据层与治理
-> Ontology：对象、关系、action、function、权限
-> Developer Console：选择应用、权限、资源范围
-> OSDK：生成语言绑定和访问 token 边界
-> 应用：React / Python / Java / 后端服务 / AI 工具
-> Action / Function：读写 ontology 或触发受控副作用
```

OSDK 的关键作用在中间：

```text
把 ontology 中已经被建模和授权的能力，变成应用开发可以直接使用的接口。
```

所以它确实是载体，但这个载体的前提是 ontology 已经被认真开发。OSDK 本身不能替代对象建模、关系设计、权限治理、action 设计和性能判断。

## 和“工具可以衍生一切”的关系

可以吸收成一个更稳的判断：

```text
OSDK 是 ontology 能力外溢的关键工具。
它让一个已建好的局部模型不只服务于一个 Palantir 内部页面，而是能衍生出多个应用、服务、AI workflow 和外部集成。
```

但这个“衍生”不是无限自动生成，而是受几个边界限制：

```text
模型边界：ontology 里有没有对应对象、关系、action、function。
权限边界：用户权限或 service user 能否访问。
资源边界：SDK scope 是否包含对应资源和依赖。
类型边界：OSDK 是否支持对应数据类型和 function/action 参数。
执行边界：action 是只改 ontology，还是触发外部系统。
版本边界：ontology / SDK / 客户端是否同步升级。
治理边界：审批、审计、action log、失败处理是否完整。
```

这比“OSDK 重新定义企业开发”更适合正式 wiki。

## 校正后的 Review 判断

建议把本篇从普通来源升级为“关键工具页”的依据材料。

正式吸收时，建议新建 `wiki/concepts/osdk.md`，因为 OSDK 已经不是 `ontology.md` 中一段话能容纳的内容。它是一个独立知识对象：

```text
OSDK = ontology 面向开发者和外部应用的受控接口层。
```

该页应回答：

- OSDK 暴露什么：object types、links、action types、functions。
- OSDK 怎么暴露：Developer Console、language bindings、generated docs、OAuth token、resource access restrictions。
- OSDK 权限如何工作：user permissions vs application permissions / service user。
- OSDK 能做什么：query/search/aggregate objects，follow links，apply actions，execute functions，write back to ontology。
- OSDK 不能证明什么：不能证明外部系统已完成执行，不能消除 ontology 建模成本，不能绕过治理。
- OSDK 为什么关键：它是 ontology 从平台模型变成可扩展应用生态的载体。

## Developer Console 提供了哪些边界

这篇最具体的价值，是讲了生成 SDK 时要配置哪些边界。

### 1. 应用类型

文章区分：

```text
Client-side application：前端、桌面、移动端；不应存储敏感 client credentials。
Backend service：后端服务、守护进程、集成任务；可以安全保存服务凭据。
```

这说明 OSDK 不是一个没有边界的万能 SDK。不同应用形态有不同安全假设。

### 2. 权限模式

文章区分：

```text
User permissions：应用继承当前登录用户权限。
Application permissions：应用使用 service user 权限。
```

这对我们很重要，因为它说明：

```text
应用层不应该重新发明一套权限；
OSDK 应该继承或承接 ontology 中已经定义的权限边界。
```

但这也引出问题：service user 的边界、审计和滥用风险必须被治理。

### 3. Ontology and Resource Scoping

文章强调 SDK 只应暴露应用需要的内容：

```text
Object Types
Links
Actions
Functions
LLM functions
```

这意味着 OSDK 的核心不是把整个企业 ontology 一次性暴露出去，而是按应用需求选择范围。

这个点和我们之前说的“小本体 / 局部模型”一致：

```text
不是大而全暴露；
而是围绕当前应用需求，暴露足够对象、关系、action 和 function。
```

## 这篇和我们当前判断的关系

我们刚形成的判断是：

```text
ontology-oriented development 本质仍是开发。
它减少一级临时理解，但增加一级抽象。
```

这篇给出了更具体的形态：

```text
ontology 本身先被开发出来；
然后 Developer Console 把其中一部分对象、action、function 和权限打包成 SDK；
开发者在 React / Python / backend 中使用这个 SDK 构建具体应用。
```

所以 OSDK 是连接 ontology 开发和应用开发的一层接口。

它不是把业务需求自动变成代码，而是把已经建好的业务对象层暴露给代码。

## 最值得吸收的判断

这篇最有价值的判断是：

```text
OSDK 是 ontology 面向开发者的边界。
它把被授权的业务对象、关系、action 和 function 变成可安装、可文档化、可调用的 SDK。
```

这个判断比“重新定义企业级应用开发的未来”更稳。

## 需要警惕的地方

这篇仍然有明显产品宣传口吻。

它不能直接证明：

- OSDK 可以让开发时间从数月缩短到数天；
- 自动文档永远准确；
- SDK 与 ontology 演化不会产生版本兼容问题；
- 权限继承在所有场景中都安全；
- LLM function 可以可靠选择卫星；
- 写回 ontology 后就等于完成真实业务闭环。

尤其要警惕 `write back to ontology`。

文章说 React 应用点击保存后，会通过 LLM function / OSDK 创建新的任务对象，并在 ontology 中可见。
这证明的是：

```text
自定义应用可以通过 OSDK 写入 ontology 对象。
```

但它还没有证明：

```text
该任务是否真的发送给外部卫星系统；
外部卫星系统如何确认；
失败如何回滚；
谁审批；
谁承担责任；
审计如何跨系统闭环。
```

所以这篇支持“应用到 ontology 的双向互动”，但不能直接证明完整外部系统执行闭环。

## 来源文件或来源包

- 来源文件：`Palantir揭秘：OSDK 深度解析，重新定义企业级应用开发的未来.mhtml`
- 来源路径：`/Users/ningl/work/risk/palantir/Palantir揭秘：OSDK 深度解析，重新定义企业级应用开发的未来.mhtml`
- 文件大小：6282276 bytes
- 保存或修改时间：2025-11-10 09:22:47
- 文章内显示发布时间：2025-07-29 08:09，加拿大
- 表观作者/账号：`小智` / `智见AI视界`
- 来源层级：Tier B/C，二手解读/教程式叙事；不是 Palantir 官方文档。

## 来源卡片

- 标题：Palantir揭秘：OSDK 深度解析，重新定义企业级应用开发的未来
- 来源路径：`/Users/ningl/work/risk/palantir/Palantir揭秘：OSDK 深度解析，重新定义企业级应用开发的未来.mhtml`
- 文件类型：MHTML，保存的网页文章
- 保存或修改时间：2025-11-10 09:22:47
- 表观主题：OSDK、Developer Console、ontology scoping、permissions、React 应用、LLM function、写回 ontology
- 当前为什么读：上一篇讨论 ontology-oriented development，本篇具体看 ontology 如何通过 SDK 暴露给开发者
- Review 状态：待讨论

## 来源事实摘要

- 文章以 Titan Industries 配送中心火灾为场景，已有 AIP 应用展示受影响订单和替代配送中心。来源位置：缘起。
- 文章提出新需求：评估火灾损失，并为公共卫星分配拍摄任务。来源位置：缘起。
- 文章将 OSDK 描述为 ontology 的软件开发工具包，并称它让开发者用业务语言与数字业务模型交互。来源位置：核心解密。
- 文章称 OSDK 可用于前端、移动端、桌面、边缘应用和后端服务。来源位置：核心解密。
- 文章称 Developer Console 支持 client-side 和 backend service 两类应用。来源位置：开发驾驶舱。
- 文章称权限模式包括 user permissions 和 application permissions。来源位置：开发驾驶舱。
- 文章称开发者可以在 Developer Console 中选择 SDK 需要暴露的 object types、links、actions 和 functions。来源位置：开发驾驶舱。
- 文章称 actions 可以关联业务逻辑，甚至回写数据到源系统；functions 可以包括 LLM 驱动功能。来源位置：开发驾驶舱。
- 文章称案例中扩展 ontology，增加 Plant Events、Sensor Task、Satellite 等对象。来源位置：实践出真知。
- 文章称 SDK 可生成 TypeScript NPM 包、Python Pip/Conda 包或 cURL 调用。来源位置：生成 SDK 包。
- 文章称 Developer Console 会根据 SDK 选择的 ontology 实体自动生成 API 文档，且会随 ontology 和 SDK 更新。来源位置：自动生成文档。
- 文章称 React 应用可以使用生成的 SDK 加载配送中心、调用 LLM 卫星任务函数，并创建新的任务对象。来源位置：代码时间。
- 文章称点击保存后，任务创建请求写回 Titan ontology，并能立刻查询到新任务对象。来源位置：闭环的魔力。

## Review 判断

这篇值得进入正式 wiki，但建议等用户讨论后再决定是否新建 `wiki/concepts/osdk.md`。

建议吸收的判断：

```text
OSDK 是 ontology 面向开发者的接口层：它把授权范围内的对象、关系、action 和 function 打包成 SDK，
让具体应用围绕业务对象读写和调用能力。
```

不建议吸收的判断：

```text
OSDK 重新定义了企业应用开发的未来；
OSDK 已经消除所有后端集成和权限复杂性；
写回 ontology 等于真实外部业务系统已经执行完成。
```

## 拟议 wiki 更新

如果用户批准，建议：

- 创建来源页：`wiki/sources/palantir-osdk-deep-dive.md`。
- 新建或更新 `wiki/concepts/osdk.md`：
  - OSDK 是 ontology 的开发者接口层。
  - 关键边界：应用类型、权限模式、resource scoping、对象/action/function 选择。
  - 写回 ontology 不等于外部系统完整执行闭环。
- 更新 `wiki/concepts/ontology.md`：
  - 增加 OSDK 作为 ontology 开发者边界的链接。
- 更新 `wiki/questions.md`：
  - SDK 版本如何跟随 ontology 演化？
  - application permissions / service user 如何审计和限制？
  - action 写回 ontology 与写回外部源系统的边界在哪里？

## 待讨论问题

1. 我们是否接受这个判断：OSDK 是 ontology 面向开发者的接口层，而不是自动应用生成器？
2. 是否现在新建 `wiki/concepts/osdk.md`？
3. 这篇的 writeback 是否只能证明“写回 ontology”，不能证明“外部系统完整执行”？

## 应用笔记

Application hypothesis：

如果未来用于本地 `risk` 项目，这篇提示：如果存在稳定的业务对象层，开发者接口不应直接暴露所有底层数据库/API，
而应按应用范围暴露必要对象、action、function 和权限边界。

这只是应用假设，不是对 `risk` 项目的实施指令。
