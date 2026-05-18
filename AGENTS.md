# AGENTS.md

## Project Purpose

This repository is an independent enterprise-intelligence research wiki. It is
for gradual reading, discussion, and synthesis around enterprise AI systems,
ontology-centered software, agent workflows, delivery methods, and related
cases.

Palantir is the first source family, but this repository is not limited to
Palantir. The local `risk` project is a later application target, not the owner
of this research system.

## Operating Rules

- Research stays research. Do not force every source into a project decision.
- Do not modify `/Users/ningl/work/risk/palantir`.
- Do not modify `/Users/ningl/work/risk` unless the user explicitly switches to
  that project and asks for implementation there.
- Do not bulk-ingest all sources. Process one source file, or one small coherent
  source bundle, at a time.
- New research output must first create a review package under
  `reviews/pending/`.
- Do not write new source-derived conclusions directly into `wiki/` unless the
  user explicitly approves the review package.
- Preserve source references close to the claims they support.
- Distinguish source facts, author opinions, user judgments, LLM inferences, and
  application hypotheses.
- Do not present Palantir marketing, commentary, or secondary analysis as
  verified fact.
- Do not connect unrelated sources because of topical similarity. Cross-source
  links require explicit overlap, a reviewed bridge page, or user confirmation.
- Prefer updating existing wiki pages before creating new pages.

## Source Boundaries

The initial source family is external:

```text
/Users/ningl/work/risk/palantir
```

In v0, `raw/palantir/MANIFEST.md` indexes that folder. The source files remain
in place and are not copied by default.

## Application Notes

`wiki/applications/risk.md` may record possible implications for the local
`risk` project. These notes must be labeled as `Application hypothesis` or
`LLM inference` unless validated in `risk`.

Application notes are research outputs, not implementation instructions.

## Research Commands

When the user asks to study one source, research one file, or continue Palantir
research, follow:

```text
docs/workflows/research-one-source.md
```

When the user approves a review package, follow:

```text
docs/workflows/apply-approved-review.md
```
