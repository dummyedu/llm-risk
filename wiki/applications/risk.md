# Risk 应用笔记

本页记录企业智能研究对本地 `risk` 项目的可能启发。

## 边界

`risk` 是后续应用目标。本 wiki 不修改 `risk` 仓库。这里的笔记是研究输出，
不是实施指令。

## 当前假设

- 应用假设（Application hypothesis）：`risk` 项目的 ERC、catalog、tool gateway
  可能构成一种轻量 semantic layer，用于受控的 LLM 业务探索。
- 应用假设（Application hypothesis）：Palantir 风格的 ontology 与 AIP 评估思路，
  可能帮助定义业务能力如何暴露给 assistant。
- 应用假设（Application hypothesis）：FDE 风格交付方法可能帮助组织新的业务切片
  如何被研究、建模、验证和交付。

## 待验证

- 找到至少一篇已审核 Palantir 来源，对 ontology 或 AIP 有足够具体的定义，
  再与 `risk` artifacts 做对照。
- 只有来源已经在本 wiki 中完成 review 后，才比较它与 `risk` 架构文档。
- 所有项目映射在 `risk` 仓库内验证前，都必须标为应用假设
  （Application hypothesis）。
