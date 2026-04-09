---
title: "OOP Inheritance — Animal Kingdom"
type: source
tags: [oop, inheritance, polymorphism, abstraction]
date: 2026-04-09
source_file: raw/OOP_inheritance.py
---

## Summary
Demonstrates Python inheritance chains using a Lion King theme. An `Animal` base class defines an abstract `vocalize()` method (raises `NotImplementedError`). `Lion` and `Zazu` override it differently. `Mufasa` extends `Lion` with a status attribute, and `Simba` extends `Mufasa` with different defaults — showing multi-level inheritance.

## Key Claims
- Abstract methods can be simulated by raising `NotImplementedError` in the base class
- Subclasses override methods to provide specific behavior (polymorphism)
- Multi-level inheritance chains (Animal -> Lion -> Mufasa -> Simba) share and specialize behavior
- `get_status()` is overridden at the `Mufasa` level but inherited by `Simba`

## Key Quotes
> No prose — key design: `vocalize()` dispatches to species-specific methods (`roar()`, `squawk()`) demonstrating the template method pattern.

## Connections
- [[Inheritance]] — multi-level class hierarchy
- [[ObjectOrientedProgramming]] — polymorphism, abstraction, method overriding

## Contradictions
- None identified
