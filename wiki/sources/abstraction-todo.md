---
title: "Abstraction Todo — Journal App Design"
type: source
tags: [design, abstraction, architecture, journal]
date: 2026-04-09
source_file: raw/abstraction_todo.md
---

## Summary
A design document outlining the architecture for a journaling application. Plans a layered design with configuration, file handling, templates, and prompt sessions. Proposes using [[Inheritance]] with a `Document` base class that `JournalEntry` extends, and a separate `Quotes` feature pulling from an API.

## Key Claims
- Configuration should be externalized (JOURNAL_FOLDER, FILE_PREFIX, FILE_EXTENSION)
- `FileHandler` should be generic read/write, not journal-specific
- `JournalEntry` should inherit from a generic `Document` class
- Prompt sessions come in types: freeform, Q&A-freeform, Q&A-integer
- Quotes feature: API data -> template -> document

## Key Quotes
> "JournalEntry could inherit a Document (which handles generic things, date setter, template, creations with FileHandler)" — key architectural decision favoring composition via inheritance

## Connections
- [[Inheritance]] — proposed Document -> JournalEntry hierarchy
- [[ObjectOrientedProgramming]] — class design, separation of concerns, abstraction layers

## Contradictions
- None identified
