---
title: "Inheritance"
type: concept
tags: [oop, inheritance, polymorphism]
sources: [oop-inheritance, oop-game, abstraction-todo]
last_updated: 2026-04-09
---

# Inheritance

An OOP mechanism where a child class inherits attributes and methods from a parent class, enabling code reuse and specialization. Python supports single and multiple inheritance.

## Key Patterns in Sources
- **Abstract base class:** `Animal` raises `NotImplementedError` to enforce override ([[oop-inheritance]])
- **Multi-level chain:** Animal -> Lion -> Mufasa -> Simba, each level adding/overriding behavior ([[oop-inheritance]])
- **Scene hierarchy:** `Scene` base class with `enter()` overridden by each game room ([[oop-game]])
- **Planned hierarchy:** `Document` -> `JournalEntry` for generic vs. specific file handling ([[abstraction-todo]])

## Connections
- [[ObjectOrientedProgramming]] — inheritance is a core OOP pillar
