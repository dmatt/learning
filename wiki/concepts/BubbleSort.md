---
title: "Bubble Sort"
type: concept
tags: [sorting, algorithms, complexity]
sources: [bubble-sort]
last_updated: 2026-04-09
---

# Bubble Sort

A simple comparison-based sorting algorithm that repeatedly steps through a list, compares adjacent elements, and swaps them if they are in the wrong order. Named for the way smaller elements "bubble" to the top.

## Key Properties
- **Time complexity:** O(n^2) average and worst case, O(n) best case (already sorted)
- **Space complexity:** O(1) — in-place
- **Stable:** Yes — equal elements maintain relative order
- **Adaptive:** Can be optimized to detect already-sorted input

## Implementation Notes
In [[bubble-sort]], an `ignore_last_n` optimization is used: after each full pass, the largest unsorted element is in its final position, so subsequent passes skip the sorted tail.

## Connections
- [[ObjectOrientedProgramming]] — the bubble sort implementation uses OOP for visualization
