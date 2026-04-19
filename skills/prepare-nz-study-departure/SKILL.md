---
name: prepare-nz-study-departure
description: Build and tailor a pre-departure checklist for Chinese students heading to New Zealand for undergraduate, master's, or PhD study. Use when Codex needs to organize what to pack, what documents to print, payment and phone setup, electronics and adapters, optional kitchen or office items, and last-mile departure reminders for NZ study abroad. Triggers include "新西兰留学行李", "NZ 留学 checklist", "赴新留学出发前准备", "新西兰留学带什么", or similar requests.
metadata:
  author: Pengqian Han
  package: nz-life-skills
  bundle: nz-pre-departure
  geography: nz
  audience:
    - international-students
    - newcomers
  policy_sensitive: true
  official_sources_required: true
---

# Prepare NZ Study Departure

## Overview

Turn a rough packing list or student profile into a practical pre-departure checklist for Chinese students going to New Zealand. Keep recommendations conservative, portable, and easy to scan.

## Workflow

1. Infer or ask only for the factors that materially change the list: degree level, city, accommodation type, baggage allowance, whether the student expects to drive, whether they cook, and device ecosystem.
2. Start from the baseline list in [references/current-guidance.md](references/current-guidance.md).
3. Reorganize the output into `必带` / `优先建议带` / `按需带` / `出发前确认`.
4. Add only short explanations that reduce confusion, cost, or risk.
5. Keep the answer concise. Do not turn the output into a travel blog or a generic "study abroad tips" article.

## Adaptation Rules

- Treat undergraduates, taught master's students, research master's students, and PhD students as sharing the same baseline. Degree level mainly changes school paperwork and research or office gear.
- If the student does not plan to drive soon after arrival, move the licence item to `按需带`.
- If accommodation is furnished or baggage is tight, downgrade bulky kitchen appliances to `按需带` and note that they can be bought after arrival.
- If the student uses Apple devices, mention ecosystem convenience briefly. If the student uses Android, focus on app availability and Google Play setup. Mention HarmonyOS friction only as a practical compatibility note.
- If the user appears to rely on an outdated rule, correct it with a concrete date or current wording instead of repeating the outdated claim.
- If a recommendation depends on regulation or policy, avoid absolute wording and point to the official source when precision matters.

## Output Style

- Default to Chinese unless the user asks otherwise.
- Keep bullets short, direct, and actionable.
- Prefer practical caveats over broad lifestyle advice.
- Separate universal essentials from optional items.
- When mentioning driving eligibility or cash declaration thresholds, note that the student should verify current NZTA or NZ Customs guidance if they need a precise rule.

## Reference

Use [references/current-guidance.md](references/current-guidance.md) as the primary source for the baseline packing list, explanations, and official check points.
