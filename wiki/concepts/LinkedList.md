---
title: "Linked List"
type: concept
tags: [data-structures, linked-list]
sources: [linked-list]
last_updated: 2026-04-09
---

# Linked List

A linear data structure where each element (node) contains data and a pointer to the next node. Unlike arrays, elements are not stored contiguously in memory — traversal is sequential from the head.

## Key Operations
- **Append:** O(n) — traverse to tail, add node
- **Prepend:** O(1) — reassign head pointer
- **Insert after:** O(n) — find target, splice in new node
- **Delete:** O(n) — find node, update pointers to skip it
- **Reverse (iterative):** O(n) — flip all next pointers using prev/curr/next

## Implementation Notes
In [[linked-list]], the `LinkedList` class uses a sentinel `empty = ()` tuple instead of `None` for the empty state. The `Node` class stores `data` and `next`.

## Connections
- [[ObjectOrientedProgramming]] — `LinkedList` and `Node` classes
- [[BinaryTree]] — both are pointer-based data structures, but trees branch
