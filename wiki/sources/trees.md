---
title: "Binary Tree Traversals"
type: source
tags: [trees, data-structures, recursion, traversal]
date: 2026-04-09
source_file: raw/trees.py
---

## Summary
A binary tree implementation in Python with three depth-first traversal methods: preorder (root-left-right), inorder (left-root-right), and postorder (left-right-root). Uses a `Node` class with label/left/right pointers and a `BinaryTree` class that dispatches traversal by name.

## Key Claims
- Preorder visits root first, then left subtree, then right subtree
- Inorder visits left subtree, then root, then right subtree
- Postorder visits left subtree, then right subtree, then root
- All three traversals use recursion with string accumulation
- Comments note breadth-first traversal as a future topic

## Key Quotes
> `"""Root -> Left -> Right"""` — docstring pattern used to document each traversal order

## Connections
- [[BinaryTree]] — the core data structure implemented here
- [[Recursion]] — all traversal methods are recursive
- [[ObjectOrientedProgramming]] — uses `Node` and `BinaryTree` classes

## Contradictions
- **Bug:** `postorder_print` calls `self.inorder_print` for left and right children instead of `self.postorder_print` — this produces incorrect postorder output
