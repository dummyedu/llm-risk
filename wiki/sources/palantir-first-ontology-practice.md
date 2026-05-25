---
title: Palantir 实战（一）：构建第一个本体
type: source
status: reviewed
sources:
  - reviews/approved/2026-05-24-palantir-first-ontology-practice/REVIEW.md
updated: 2026-05-25
---

# Palantir 实战（一）：构建第一个本体

## 这篇文章在讲什么

这篇文章跟随 Palantir Learn 的课程，用一个虚构航空公司 `Fresh Air` 做最小 ontology
扩展。教程里已经有 `Airline`、`Route`、`Airport`、`Runway`、`Flight` 等对象，
文章要新增的是 `Flight Alert`。

`Flight Alert` 表示航班延误、取消、改道等告警。它来自底层数据集 `flight_alerts`，
用 `flight_alert_id` 作为对象主键，用 `alert_title` 作为显示标题，再通过 `flight_id`
连回已有的 `Flight` 对象。

最后，文章创建了一个 `Assign Root Cause` action，让用户给 `Flight Alert.root_cause`
填写根因。

## 我读完后的理解

这篇最有价值的地方，是把之前抽象的 ontology 拉回到一个可操作的最小单元：

```text
dataset
-> object type
-> object identity
-> property mapping
-> link type
-> action
-> data lineage
```

因此，本 wiki 当前可以把 Palantir ontology 暂时理解为：

```text
基于表数据的面向对象业务表达
```

Object Type 像类，Object 像运行时实例，mapping 把表、字段和外键连到对象、属性和关系。
Action 像作用在对象上的受控业务函数。在本篇里，这个函数还很简单，只是把用户输入写回
`root_cause` 字段。

## 最有用的部分

这篇帮我们区分了关系和映射：

```text
关系：Flight Alert 属于某个 Flight。
映射：用 flight_alerts.flight_id 匹配 Flight 的主键，生成这条 link。
```

也就是说，业务关系不是一句自然语言声明。它需要对象类型、键、字段和 link type 一起支撑。

文章也说明了 Data Lineage 的位置：从对象类型可以追溯到底层 dataset 和 pipeline。
这让 ontology 不是脱离数据工程的概念层，而是能回到底层数据生产过程。

## 需要警惕的地方

这篇不能证明复杂企业闭环已经成立。`Assign Root Cause` 只是一个最小 action，更像受控字段编辑。
它没有展示多步骤审批、复杂规则判断、AI 建议如何进入审批链、多对象协同、回滚和异常处理。

所以它适合进入 wiki 的位置是“最小 ontology 操作单元”，不是“Palantir 已解决复杂治理”的证明。

## 对综合页的影响

这篇已经补入 [[concepts/ontology]]、[[concepts/ontology-relation-types]]、
[[mechanisms/data-to-ontology-mapping]] 和 [[mechanisms/governed-action]]。

它让当前本体理解更具体：ontology 不是只有对象名和关系名，还需要主键、标题键、字段映射、
关系映射、动作入口和数据血缘。

## 来源与追溯

- 原始文件：`/Users/ningl/work/risk/palantir/Palantir实战（一）：手把手教你构建第一个本体（Ontology）.mhtml`
- Review：`reviews/approved/2026-05-24-palantir-first-ontology-practice/REVIEW.md`
- MHTML 内容来源：`https://mp.weixin.qq.com/s/EuPSyj20Yjlxmiu2EvscTQ`
- 参考课程：`https://learn.palantir.com/deep-dive-creating-your-first-ontology`
- 可靠性：二手教程总结；引用 Palantir Learn 课程，但本文本身不是官方文档。
