---
name: kiwi-access-card
description: Answer questions about New Zealand Kiwi Access Card eligibility, online versus in-person application, required documents, fees, processing times, and form interpretation. Use when Codex needs to explain Kiwi Access Card rules from AA, Kiwi Access official pages, or the official PDF form, especially for international students, overseas passport holders, or users asking whether they can apply and how. For any request involving current policy, latest rules, current fees, or live application support, verify against official websites first before answering and update the skill references if the policy has changed.
---

# Kiwi Access Card

## Overview

Use this skill to answer Kiwi Access Card questions with an official-source-first workflow. Focus on separating stable guidance from policy details that may change, and explicitly distinguish general eligibility from online-system constraints.

## Workflow

1. Determine whether the user is asking about:
   - general eligibility
   - online application
   - in-person application
   - required documents
   - timing, fees, or shipping
   - interpretation of the official PDF form
2. Read [references/current-policy.md](references/current-policy.md) for the current baseline.
3. If the user asks for anything current, latest, today, now, fee-sensitive, policy-sensitive, or process-sensitive, verify the relevant official pages on the web before answering.
4. If the live official policy differs from the reference file, update the skill reference before finishing the task.
5. Answer in plain language, and clearly call out any gap between:
   - overall eligibility to apply
   - what the current online portal appears to support
   - what can be done in person at AA or NZ Post

## Source Order

Use sources in this order unless the user asks otherwise:

1. AA official Kiwi Access page
2. Kiwi Access official site
3. Kiwi Access official FAQ
4. Kiwi Access online application portal
5. Official PDF application form supplied by the user or linked from official sites

Do not rely on forum posts, blogs, or third-party summaries when an official source exists.

## Policy Freshness Rule

Treat Kiwi Access rules as temporally unstable. The skill is based on the policy summarized in [references/current-policy.md](references/current-policy.md), but if the policy, fee, required documents, application channel, or online portal behavior may have changed, search the official sites first and then update the reference file so the skill stays current.

## Answering Rules

When answering:

- State eligibility first, then process details.
- Separate `can apply in general` from `can use the online portal`.
- For overseas passport holders or international students, explicitly mention that foreign nationals and visitors can apply in general when the official sources support that.
- If online eligibility is unclear or appears narrower than the general FAQ, say so directly and recommend in-person application as the reliable fallback.
- Include exact fees and timing only after checking current official sources when the user asks for operational details.
- If interpreting the PDF form, distinguish:
  - form instructions
  - in-store handling steps
  - online-only limitations that are not visible in the PDF
- If the user provides a downloaded PDF, inspect the PDF itself instead of assuming it matches the website.

## PDF And Form Handling

When working from a user-supplied Kiwi Access PDF form:

- Check whether the PDF is a fillable AcroForm or just a printable form.
- Read the visible instructions on the form, especially photo handling, capital-letter requirements, and store submission notes.
- Do not assume a fillable PDF means digital submission is accepted. Confirm submission rules from the form and official site.
- If the user asks whether they must print the form, answer from both the PDF design and the official submission workflow.

## References

- Read [references/current-policy.md](references/current-policy.md) for the current known policy baseline and source links.
- Update that reference whenever official rules materially change.
