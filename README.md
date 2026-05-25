# ei-wiki

独立企业智能研究 wiki。

## 目的

本仓库支持一种慢速、保留来源上下文的企业 AI 系统研究循环。第一组来源是
当前存放在以下路径的 Palantir 材料：

```text
/Users/ningl/work/risk/palantir
```

目标是在把研究转成项目决策前，先理解方法、概念、案例和设计原则。本地
`risk` 项目未来可以引用本 wiki，但本 wiki 不是 `risk` 的一部分。

## 研究循环

1. 选择一个来源文件，或一个小的连贯来源包。
2. 在 `reviews/pending/` 下创建 review package。
3. 讨论来源、主张、疑点和有用想法。
4. 批准 review package。
5. 将耐久综合写入 `wiki/`。
6. 更新 `meta/INGEST_LEDGER.md`。

## 主要区域

- `raw/`：来源索引和未来来源收件箱。
- `reviews/`：写入 wiki 前的草稿/review 层。
- `wiki/`：已审核综合层。
- `meta/`：schema、来源政策、研究原则和 ledger。
- `docs/workflows/`：可重复执行的研究流程。

## 阅读 Wiki

### Obsidian

把这个仓库目录作为 Obsidian vault 打开：

```text
/Users/ningl/work/ei-wiki
```

本 wiki 使用普通 Markdown 和 Obsidian 风格链接，例如 `[[map]]`。

### 浏览器预览

运行本地零依赖预览服务器：

```bash
python3 tools/wiki_preview.py
```

然后打开：

```text
http://127.0.0.1:8765/
```

预览服务器只渲染 `wiki/` 中的正式阅读内容，并把简单的 `[[wiki links]]`
转成浏览器链接。如果 `8765` 端口被占用，它会自动尝试后续可用端口。

### GitHub Pages

生成静态站点：

```bash
python3 tools/wiki_static.py
```

本地查看静态站点：

```bash
python3 -m http.server 8780 -d site
```

然后打开：

```text
http://127.0.0.1:8780/
```

`site/` 是构建产物，已被 `.gitignore` 忽略。GitHub Actions 会在 push 到
`main` 后自动重新构建并发布 GitHub Pages。静态站点只发布 `wiki/` 中的内容，
不会复制 `reviews/`、`raw/`、`meta/` 或 `tools/` 目录。

## V0 边界

- 不批量 ingest。
- 默认不复制原始来源文件。
- 不建向量数据库。
- 不做浏览器 app。
- 不直接写入 `risk` 项目。

## 起始提示词

开始研究 session 时可以使用：

```text
请从 raw/palantir/MANIFEST.md 里选一个 Palantir 文件，按 docs/workflows/research-one-source.md 和我边读边讨论。
```
