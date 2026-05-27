---
title: 综合索引
type: concept
status: reviewed
sources: []
updated: 2026-05-24
---

# 综合索引

## 本 wiki 的阅读方式

本 wiki 的主体不是“每篇文章一篇读书笔记”，而是学习后形成的可查阅、
可引用、可继续扩展的综合理解。

因此，内容分三层：

1. **综合页**：按概念、方法、判断框架组织，是主要阅读入口。
2. **来源页**：按单篇来源保留证据、上下文和可信度判断，用于追溯。
3. **问题页**：记录尚未定论、需要后续来源继续验证的问题。

## 当前主体综合

- [[concepts/palantir-dynamic-ontology]]
- [[concepts/semantic-compiler-implementation-notes]]
- [[concepts/ontology-relation-types]]
- [[methods/ontology-centered-delivery]]

## 当前来源追溯

- [[sources/palantir-eleven-part-preface]]
- [[sources/palantir-decision-paradigm]]
- [[sources/palantir-ontology-foundation]]
- [[sources/palantir-dynamic-ontology-core]]
- [[sources/palantir-toolchain-dynamic-ontology-1]]
- [[sources/palantir-fde-deep-dive]]
- [[sources/palantir-fde-day]]
- [[sources/palantir-baseline-fdie]]
- [[sources/palantir-ontology-oriented-software-dev]]

## 后续阅读规则

- 每读一篇来源，先创建 review package，不直接写入正式 wiki。
- 用户批准后，必须创建或更新对应来源页。
- 用户批准后，还必须判断是否更新已有综合页，或是否需要新建综合页。
- 如果一篇来源只适合进入来源页和问题页，不适合进入综合页，必须在 ledger
  或 review 中说明原因。
- `wiki/questions.md` 只放尚未定论的问题，不应替代综合页。

## 判断标准

一条内容适合进入综合页，当它满足至少一个条件：

- 能帮助定义一个反复出现的概念。
- 能补强一个方法或判断框架。
- 能改变现有综合页中的阶段性理解。
- 能形成后续可引用的用户判断、LLM 推断或应用假设。

一条内容只适合留在来源页，当它满足以下情况：

- 只描述单篇文章结构或作者叙述。
- 可信度不足，尚不能支持跨来源综合。
- 属于背景材料、阅读顺序或单篇来源的局部细节。
- 目前只能作为开放问题，不能形成阶段性结论。
