---
title: "Bubble Sort Visualization"
type: source
tags: [sorting, algorithms, visualization, oop]
date: 2026-04-09
source_file: raw/bubble_sort.py
---

## Summary
A visual bubble sort implementation in Python that uses OOP to represent sortable lines as dashes. The `Line` class wraps a numeric length with a visual string, and `LineList` manages a collection of lines, printing the state to the terminal after every comparison to animate the sort in real time.

## Key Claims
- Bubble sort works by repeatedly comparing adjacent elements and swapping if out of order
- An `ignore_last_n` optimization skips already-sorted tail elements each pass
- Terminal clearing + short sleep creates a real-time animation of the sorting process
- OOP encapsulation separates data representation (`Line`) from collection behavior (`LineList`)

## Key Quotes
> No prose quotes — this is a code file. Key design choice: each `Line` stores both numeric `length` and string `visual` (`length * '-'`), keeping display logic inside the data object.

## Connections
- [[BubbleSort]] — canonical O(n^2) comparison sort algorithm
- [[ObjectOrientedProgramming]] — uses classes to encapsulate sort state and visualization

## Contradictions
- None identified
