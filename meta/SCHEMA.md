# Schema

## Claim Labels

Use these labels whenever a research note makes a durable claim.

### Source fact

A statement directly supported by the source.

Required evidence:

- source path or URL;
- section, title, page, or nearby quote location when available.

### Author opinion

The source author's framing, interpretation, recommendation, or critique.

Required evidence:

- source path or URL;
- short description of the author's position.

### User judgment

The user's interpretation, correction, priority, or disagreement.

Required evidence:

- discussion note or explicit user statement.

### LLM inference

An assistant-generated synthesis, analogy, abstraction, or implication.

Required evidence:

- source facts or author opinions that motivated the inference;
- explicit label `LLM inference`.

### Application hypothesis

A possible implication for a target project, especially `risk`.

Required evidence:

- reviewed source basis;
- target project artifact, if inspected;
- explicit label `Application hypothesis`.

## Wiki Page Frontmatter

Use this frontmatter for formal wiki pages when useful:

```yaml
---
title:
type: concept | method | case | source | application | question
status: stub | active | reviewed
sources: []
updated:
---
```

## Review Package Fields

Each `reviews/pending/<date>-<slug>/REVIEW.md` should include:

- source file or bundle;
- source card;
- factual summary;
- important source claims;
- author opinions or framing;
- LLM inferences;
- user discussion notes;
- proposed wiki updates;
- possible links;
- open questions;
- application notes.

## Ledger Fields

`meta/INGEST_LEDGER.md` uses:

```text
| Date | Source | Size | Modified | Status | Review | Notes |
```
