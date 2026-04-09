---
title: "Binary Tree"
type: concept
tags: [data-structures, trees, traversal]
sources: [trees]
last_updated: 2026-04-09
---

# Binary Tree

A hierarchical data structure where each node has at most two children (left and right). The topmost node is the root. Binary trees are foundational to search algorithms, expression parsing, and hierarchical data representation.

## Traversal Orders (Depth-First)
- **Preorder:** Root -> Left -> Right
- **Inorder:** Left -> Root -> Right (produces sorted order for BSTs)
- **Postorder:** Left -> Right -> Root

## Implementation Notes
In [[trees]], the tree is built manually by assigning `Node` objects to `.left` and `.right`. Traversals use [[Recursion]] with string accumulation.

## Connections
- [[Recursion]] — traversals are inherently recursive
- [[ObjectOrientedProgramming]] — `Node` and `BinaryTree` class design
