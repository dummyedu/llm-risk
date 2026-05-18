# Review Package

Review packages are the required intermediate layer between source reading and
formal wiki updates.

## Location

```text
reviews/pending/YYYY-MM-DD-<slug>/
  REVIEW.md
  proposed/
    wiki/
```

After approval, the package may be moved or copied to:

```text
reviews/approved/
```

## REVIEW.md Template

```markdown
# Review: <source title>

## Source Card

- Title:
- Source path:
- File type:
- Saved or modified date:
- Apparent topic:
- Why study now:
- Review status: pending

## Factual Summary

- Source fact:

## Important Source Claims

- Source fact:

## Author Opinions Or Framing

- Author opinion:

## LLM Inferences

- LLM inference:

## User Discussion Notes

- User judgment:

## Proposed Wiki Updates

- Create:
- Update:

## Possible Links

- Link candidate:
- Evidence:

## Open Questions

- Question:

## Application Notes

- Application hypothesis:
```

## Rules

- Keep evidence close to each claim.
- Do not include full copyrighted source text unless allowed.
- Do not promote the proposed files to `wiki/` until the user approves.
