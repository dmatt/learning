---
title: "OOP Space Adventure Game"
type: source
tags: [oop, game, inheritance, state-machine]
date: 2026-04-09
source_file: raw/oop_game.py
---

## Summary
A text-based space adventure game built with OOP. Uses an Engine/Map/Scene architecture where scenes are subclasses of a base `Scene` class. The `Engine` loops through scenes returned as strings, looked up via a `Map` dictionary. Includes a `Challenge` class for password-guessing mini-games with word generation from a URL.

## Key Claims
- Scene-based game architecture uses inheritance: each room is a `Scene` subclass with an `enter()` method
- The `Map` class acts as a scene registry, mapping string keys to scene instances
- The `Engine` runs a game loop: enter scene -> get result string -> look up next scene
- `Challenge` class implements a guess-the-password mechanic with limited attempts
- Input validation is handled by a recursive `validated_prompt()` helper

## Key Quotes
> `"This base scene not configured. Subclass it and implement enter()"` — base class enforces subclassing

## Connections
- [[Inheritance]] — every game scene inherits from `Scene`
- [[ObjectOrientedProgramming]] — class hierarchies, encapsulation, composition (Engine has-a Map)
- [[Recursion]] — `validated_prompt()` recurses on invalid input

## Contradictions
- None identified
