# ei-wiki

Independent enterprise-intelligence research wiki.

## Purpose

This repo supports a slow, source-aware research loop for enterprise AI systems.
The first source family is the Palantir material currently stored under:

```text
/Users/ningl/work/risk/palantir
```

The goal is to understand methods, concepts, cases, and design principles before
turning them into project decisions. The local `risk` project may later cite
this wiki, but this wiki is not part of `risk`.

## Research Loop

1. Select one source file, or one small coherent bundle.
2. Create a review package under `reviews/pending/`.
3. Discuss the source, claims, doubts, and useful ideas.
4. Approve the review package.
5. Apply durable synthesis into `wiki/`.
6. Update `meta/INGEST_LEDGER.md`.

## Main Areas

- `raw/`: source indexes and future source inboxes.
- `reviews/`: draft/review layer before wiki updates.
- `wiki/`: reviewed synthesis layer.
- `meta/`: schema, source policy, research principles, and ledger.
- `docs/workflows/`: repeatable research workflows.

## V0 Boundary

- No bulk ingest.
- No raw source copying by default.
- No vector database.
- No browser app.
- No direct writes into the `risk` project.

## Starter Prompt

Use this when beginning a research session:

```text
请从 raw/palantir/MANIFEST.md 里选一个 Palantir 文件，按 docs/workflows/research-one-source.md 和我边读边讨论。
```
