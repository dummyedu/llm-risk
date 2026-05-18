# Source Policy

## External Source Family

The initial source family is:

```text
/Users/ningl/work/risk/palantir
```

In v0, this repository indexes those files but does not copy them by default.

## Rules

- Do not modify external source files.
- Do not move or delete external source files.
- Do not bulk-copy `.mhtml` or `.pdf` files into this repository.
- Record source paths in `raw/palantir/MANIFEST.md`.
- Record reviewed processing state in `meta/INGEST_LEDGER.md`.
- If a source is sensitive, stop before using external tools or network
  services.
- If a source is copyrighted public material, do not save full text or full
  translation unless allowed.

## Allowed In V0

- Read local source files.
- Extract short source cards.
- Summarize and discuss.
- Create review packages.
- Write reviewed synthesis after user approval.

## Not Allowed In V0

- Automatic full-folder ingest.
- Automatic raw source copying.
- Direct source-derived writes into `wiki/`.
- Direct writes into `/Users/ningl/work/risk`.
