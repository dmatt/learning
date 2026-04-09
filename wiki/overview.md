---
title: "Overview"
type: synthesis
tags: []
sources: [bubble-sort, trees, linked-list, oop-inheritance, oop-game, oop-flash-cards, oop-basics, abstraction-todo]
last_updated: 2026-04-09
---

# Overview

*This page is maintained by the LLM. It is updated on every ingest to reflect the current synthesis across all sources.*

This knowledge base tracks a personal learning journey focused on **Python programming fundamentals**, with heavy emphasis on data structures, algorithms, and object-oriented design. Sources come from "Learn Python the Hard Way" exercises and self-directed coding projects.

## Current Coverage

### Data Structures
- **[[LinkedList]]** — full singly linked list with append, prepend, insert-after, delete, and iterative reverse ([[linked-list]])
- **[[BinaryTree]]** — binary tree with three depth-first traversal methods using [[Recursion]] ([[trees]])

### Algorithms
- **[[BubbleSort]]** — O(n^2) comparison sort with visual terminal animation and tail optimization ([[bubble-sort]])

### Programming Paradigms
- **[[ObjectOrientedProgramming]]** — the dominant theme across all 8 sources. Progresses from basics (`Song` class) through [[Inheritance]] hierarchies (Animal Kingdom) to full architectural patterns (Engine/Map/Scene game).
- **[[Inheritance]]** — explored in depth: abstract base classes, multi-level chains, scene hierarchies, and planned Document/JournalEntry architecture.

### Design & Architecture
- **Journal app design** ([[abstraction-todo]]) — plans a layered architecture with configuration, generic FileHandler, templates, and prompt sessions. Most architecturally mature thinking in the knowledge base.

## Learning Progression
The sources show a clear progression: basic class syntax ([[oop-basics]]) -> drilling vocabulary ([[oop-flash-cards]]) -> data structure implementations ([[linked-list]], [[trees]]) -> inheritance patterns ([[oop-inheritance]]) -> full application architecture ([[oop-game]], [[abstraction-todo]]).

## Known Issues
- **Bug in trees.py:** `postorder_print` incorrectly calls `inorder_print` for child traversal
- **Syntax error in oop_flash_cards.py:** Line 41 has `other_names = )` — incomplete code
- **Python 2 vs 3:** `oop.py` uses Python 2 `print` syntax while other files use Python 3

## Themes
The learning approach emphasizes **hands-on implementation** — building visual, interactive programs rather than abstract study. OOP is the connecting thread across nearly every source.
