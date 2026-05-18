# Research One Source

Use this workflow when the user asks to study one source, continue Palantir
research, or process a file from `raw/palantir/MANIFEST.md`.

## Inputs

- Source manifest: `raw/palantir/MANIFEST.md`
- Source family: `/Users/ningl/work/risk/palantir`
- Existing wiki pages under `wiki/`
- Ledger: `meta/INGEST_LEDGER.md`

## Steps

1. Select one source file, unless the user explicitly selects a small coherent
   source bundle.
2. Read enough of the source to create a source card.
3. Create a review package:

```text
reviews/pending/YYYY-MM-DD-<slug>/
  REVIEW.md
  proposed/
    wiki/
```

4. In `REVIEW.md`, include:
   - source file or bundle;
   - source card;
   - factual summary;
   - important source claims;
   - author opinions or framing;
   - LLM inferences;
   - proposed wiki updates;
   - open questions;
   - application notes, if any.
5. Discuss the review with the user.
6. Do not write formal wiki pages until the user approves the review package.

## Source Card

Use this shape:

```markdown
## Source Card

- Title:
- Source path:
- File type:
- Saved or modified date:
- Apparent topic:
- Why study now:
- Review status:
```

## Stop Conditions

Stop and ask before:

- modifying external source files;
- copying large raw files;
- using external services for private material;
- applying proposed wiki updates;
- turning an application hypothesis into a project requirement.
