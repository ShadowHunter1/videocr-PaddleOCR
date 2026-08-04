# CLAUDE.md

## Project Overview

This project extracts subtitles from hard-subbed videos and generates subtitle files (e.g. SRT).

The OCR pipeline is already implemented and working correctly. The primary focus of this project is **performance optimization**, not feature development.

---

## Primary Goal

Improve the overall processing speed of the subtitle extraction pipeline while maintaining the current level of subtitle accuracy.

When making changes, prioritize execution time and resource efficiency.

---

## Scope

Focus on:

* Performance optimization
* Profiling bottlenecks
* Algorithm improvements
* Memory optimization
* CPU utilization
* Parallelization where appropriate
* Reducing unnecessary computation

Avoid changing project behavior unless required for performance improvements.

---

## Development Principles

* Keep changes as small and isolated as possible.
* Prefer incremental improvements over large refactors.
* Preserve existing functionality.
* Maintain backward compatibility whenever possible.
* Avoid introducing unnecessary complexity.
* Reuse existing components before introducing new ones.

---

## Performance First

Before implementing a change:

1. Identify the bottleneck.
2. Explain why the proposed change improves performance.
3. Describe any trade-offs.
4. Keep the implementation measurable and benchmarkable.

Do not optimize based on assumptions alone.

---

## Code Quality

* Write clean and maintainable code.
* Prefer readability unless there is a measurable performance benefit.
* Avoid duplicated logic.
* Keep functions focused on a single responsibility.
* Follow the existing project style and architecture.
* Keep implementations simple whenever possible.

---

## Benchmarking

Performance-related changes should be measurable whenever possible.

Consider tracking:

* Total processing time
* CPU usage
* Memory usage
* Throughput
* Number of processed frames
* Number of OCR operations

---

## Context Management

Work in a context-efficient manner.

* Read only the files necessary for the current task.
* Avoid loading or analyzing the entire codebase unless required.
* Prefer targeted searches over broad exploration.
* Reuse previously gathered context whenever possible.
* Make the smallest possible code changes to accomplish the task.
* Avoid repeatedly reading the same files.
* Minimize unnecessary reasoning and keep responses focused.
* When additional context is required, inspect only the relevant modules or files.
* Do not rewrite existing code unless it is necessary for the current task.

---

## Collaboration Guidelines

When working on a task:

1. Understand the existing implementation first.
2. Identify the actual bottleneck.
3. Propose one or more possible approaches.
4. Explain the trade-offs.
5. Recommend the best approach.
6. Wait for approval before making significant architectural changes.
7. Implement the smallest effective solution.
8. Preserve existing behavior unless explicitly requested otherwise.

If requirements are unclear, ask for clarification instead of making assumptions.

---

## Important

The project already has a working OCR pipeline.

Your responsibility is to improve the existing implementation, not redesign or rewrite it.

Always prioritize:

* Performance
* Small, safe changes
* Maintainability
* Measurable improvements
* Efficient use of context

Avoid unnecessary refactoring or architectural changes unless explicitly requested.
