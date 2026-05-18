# Apply Approved Review

Use this workflow only when the user explicitly approves a review package.

## Inputs

- Approved package under `reviews/pending/`
- Proposed files under `reviews/pending/<slug>/proposed/wiki/`
- Formal wiki under `wiki/`
- Ledger under `meta/INGEST_LEDGER.md`

## Steps

1. Re-read `REVIEW.md`.
2. Confirm the user approved this package.
3. Compare proposed wiki updates with existing wiki pages.
4. Prefer updating existing pages over creating new pages.
5. Preserve labels:
   - Source fact
   - Author opinion
   - User judgment
   - LLM inference
   - Application hypothesis
6. Apply approved changes to `wiki/`.
7. Update `wiki/index.md`, `wiki/map.md`, or `wiki/questions.md` only when the
   approved content changes durable navigation or durable questions.
8. Update `meta/INGEST_LEDGER.md`.
9. Move or copy the package to `reviews/approved/`.

## Stop Conditions

Stop before applying if:

- the review package contains unresolved source-trace issues;
- the proposed update treats inference as fact;
- the proposed update creates unsupported cross-source links;
- the proposed update turns a `risk` application hypothesis into a requirement.
