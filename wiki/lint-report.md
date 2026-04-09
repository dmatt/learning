---
title: "Lint Report"
type: synthesis
tags: [maintenance, health-check]
last_updated: 2026-04-09
---

# Wiki Lint Report — 2026-04-09

## Orphan Pages
None found. All pages have inbound links.

## Broken Links
None found. All `[[wikilinks]]` resolve to existing pages.

## Contradictions
- **Python 2 vs 3:** [[oop-basics]] uses Python 2 `print` statement while all other sources use Python 3

## Stale Summaries
None — all pages created in the same ingest batch.

## Missing Entity Pages
None warranted — no individual entities are referenced across 3+ pages.

## Bugs Found in Source Code
1. **[[trees]]** line 43: `postorder_print` calls `self.inorder_print` instead of `self.postorder_print` — produces incorrect traversal output
2. **[[oop-flash-cards]]** line 41: `other_names = )` is invalid Python syntax — file is incomplete/broken

## Data Gaps
- No hash tables, stacks, queues, heaps, or graph implementations
- `doubly_linked_list.py` exists at repo root but is empty (0 bytes)
- No search algorithms (binary search, DFS, BFS)
- No dynamic programming examples
- No testing/unit test examples for data structures

## Recommendations
1. Fix the `postorder_print` bug in `trees.py`
2. Complete or remove `doubly_linked_list.py`
3. Add stack and queue implementations (natural next steps after linked list)
4. Add a hash table implementation to cover the most important data structures
