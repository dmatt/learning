---
title: "OOP Flash Cards Drill"
type: source
tags: [oop, learning-tool, drills]
date: 2026-04-09
source_file: raw/oop_flash_cards.py
---

## Summary
A CLI flash card tool for drilling OOP syntax from "Learn Python the Hard Way" exercise 41. Uses template patterns with `%%%`, `***`, `@@@` placeholders that get filled with random words from a URL. Shows code snippets and their English translations to build OOP vocabulary (is-a, has-a, instance, parameter).

## Key Claims
- OOP concepts are mapped to English phrases: "class X(Y)" = "Make a class named X that is-a Y"
- Drilling both directions: code-to-English and English-to-code (via `--english` flag)
- Random word generation from external URL fills placeholders for variety

## Key Quotes
> `"class %%%(%%%): Make a class named %%% that is-a %%%."` — the core mapping between code syntax and natural language

## Connections
- [[ObjectOrientedProgramming]] — the subject matter being drilled

## Contradictions
- **Syntax error on line 41:** `other_names = )` is invalid Python — file appears to be incomplete/broken
