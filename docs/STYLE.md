# Writing and Evidence Style Guide

Every page in this project must be readable by a curious 10-year-old **and** trustworthy to a working astrophysicist. These rules make that possible. Contributors, please follow them.

## 1. The two-layer rule

Each page has a simple layer and an expert layer.

1. **Simple layer (top of the page).** Short sentences. Everyday words. One idea per sentence. Aim for about a 4th–6th grade reading level. Use a picture-in-words (a metaphor) when it helps.
2. **Expert layer (lower on the page).** Equations, data sources, methods, uncertainties and references. Put it under a heading such as "For experts" so younger readers know they can stop.

Never put an equation in the simple layer. Never leave the expert layer without references.

## 2. Plain-language rules

- Prefer short words: "use" not "utilize", "show" not "demonstrate".
- Explain every technical word the first time it appears, in brackets or a short sentence. Example: "a **transit** (when a planet passes in front of its star and blocks a little light)".
- Keep sentences under about 20 words in the simple layer.
- Use "we" for the project and "you" for the reader.
- Give numbers people can picture: "about 4 times the distance from the Sun to Neptune", not only "120 au".
- Use SI units in the expert layer. Add familiar units (miles, km/h) in the simple layer where helpful.

## 3. Tone rules

- **Respect professionals.** Never say scientists or agencies are "foolish", "blind", "idiots" or "hiding" things. Real reasons explain why some signals are not followed up yet: limited time, limited telescope access, noise, and the cost of false alarms.
- **No hype.** Do not say "proves", "confirmed", "guaranteed" or "instant discovery" unless an independent, published result says so.
- **No science fiction framing.** No "timelines", "matrices", "non-local telemetry", "scalar" anything, code names, or secret-mission language. This is an open science project.
- **"Alien planets" means exoplanets** (planets around other stars). We make no claims about alien life or alien technology. If a reader asks, say so kindly and clearly.
- **Health claims are out of scope.** This project does not give medical, wellness or "frequency healing" advice.

## 4. Evidence levels

Every claim in a disclosure gets one of these labels. Always write the words, not only the color, so the label works for screen readers and in black-and-white print.

| Label | Name | Meaning (simple) | Meaning (expert) |
|---|---|---|---|
| 🟢 **Level 1** | **Confirmed** | Scientists have seen it and checked it more than once. | Published in peer-reviewed literature and independently confirmed. |
| 🔵 **Level 2** | **Strong evidence** | There are good published results, but experts still discuss them. | Peer-reviewed evidence exists; confirmation or interpretation is still debated. |
| 🟡 **Level 3** | **Testable idea** | It follows the normal rules of physics. Nobody has shown it yet. You can help test it. | Physically well-motivated hypothesis with a concrete, falsifiable test using public data. |
| 🟠 **Level 4** | **Long shot** | The physics is fine, but today's tools may be too weak to find it. | Physically allowed, but expected signal is at or below current sensitivity, or prior searches have already constrained it strongly. |

Ideas that conflict with well-tested physics are **not** given a level. They are left out of the disclosures and listed in [about/editorial-notes.md](about/editorial-notes.md) with the reason.

## 5. Page template for a disclosure

```
# Dxx — Plain-language title

> **In one sentence:** ...
> **Evidence level:** 🟡 Level 3 — Testable idea (main claim). See the table below for each part.

## For young readers
3–8 short sentences and one picture-in-words.

## The big idea
Plain explanation for adults (2–4 paragraphs).

## What we already know
Bulleted, each with an evidence label and a reference.

## What is still open
The specific, testable question.

## How you could test it
Numbered steps using public data. Name the archive and the tool.

## How we could be wrong
Known false positives, and what result would show the idea is wrong.

## For experts
Equations, methods, sensitivities, and numbers with uncertainties.

## Try it
Links to tutorials, lessons and code modules.

## References
Author(s), year, title, journal or archive, and a DOI/arXiv/URL if known.
```

## 6. Facts, numbers and references

- Check every specific number, date and name against a primary source (paper, archive, agency page). If you cannot check it, leave it out or say "about" and give a range.
- Never invent a reference. If you are unsure a paper exists, do not cite it.
- Give a date for anything that changes ("as of November 2026").
- When a claim is new (for example, a 2026 result), cite the paper, not only news stories.

## 7. Code in documentation

- Code examples must run against the `fdastro` package in this repository.
- Tutorials live in `docs/tutorials/`. Other pages should link to tutorials rather than repeat long code.

## 8. Accessibility

- Every image needs alt text that explains what it shows.
- Do not rely on color alone.
- Use real headings in order (`#`, `##`, `###`).
- Write link text that makes sense alone ("the TESS archive", not "click here").
