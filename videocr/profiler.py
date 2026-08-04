"""
Lightweight performance profiler for the videocr pipeline.

This module is purely additive: it measures execution time and counts
events for each major stage of subtitle extraction without altering any
existing behavior or algorithm.
"""
from __future__ import annotations

import time
from collections import defaultdict
from contextlib import contextmanager


class Profiler:
    def __init__(self):
        self._stage_total_time: dict[str, float] = defaultdict(float)
        self._stage_call_count: dict[str, int] = defaultdict(int)
        self._counters: dict[str, int] = defaultdict(int)
        self._session_start: float | None = None

    def start_session(self) -> None:
        """Reset all measurements and start timing a new run."""
        self._stage_total_time = defaultdict(float)
        self._stage_call_count = defaultdict(int)
        self._counters = defaultdict(int)
        self._session_start = time.perf_counter()

    @contextmanager
    def measure(self, stage_name: str):
        """Context manager that records elapsed time for a pipeline stage."""
        start = time.perf_counter()
        try:
            yield
        finally:
            elapsed = time.perf_counter() - start
            self._stage_total_time[stage_name] += elapsed
            self._stage_call_count[stage_name] += 1

    def increment(self, counter_name: str, amount: int = 1) -> None:
        """Increment a named statistic counter."""
        self._counters[counter_name] += amount

    def _total_runtime(self) -> float:
        if self._session_start is None:
            return sum(self._stage_total_time.values())
        return time.perf_counter() - self._session_start

    def report(self) -> str:
        total_runtime = self._total_runtime()

        lines = []
        lines.append("=" * 78)
        lines.append("PERFORMANCE REPORT".center(78))
        lines.append("=" * 78)
        lines.append(
            "{:<26}{:>8}{:>12}{:>14}{:>12}".format(
                "Stage", "Calls", "Total (s)", "Avg (s)", "% Total"
            )
        )
        lines.append("-" * 78)

        # sort stages by total time descending -> easiest way to spot bottlenecks
        sorted_stages = sorted(
            self._stage_total_time.items(), key=lambda kv: kv[1], reverse=True
        )
        for stage_name, total_time in sorted_stages:
            call_count = self._stage_call_count[stage_name]
            avg_time = total_time / call_count if call_count else 0.0
            pct = (total_time / total_runtime * 100) if total_runtime > 0 else 0.0
            lines.append(
                "{:<26}{:>8}{:>12.4f}{:>14.6f}{:>11.2f}%".format(
                    stage_name, call_count, total_time, avg_time, pct
                )
            )

        lines.append("-" * 78)
        lines.append("{:<26}{:>60.4f}s".format("TOTAL RUNTIME", total_runtime))
        lines.append("")
        lines.append("STATISTICS".center(78))
        lines.append("-" * 78)
        if self._counters:
            for name in sorted(self._counters.keys()):
                lines.append("{:<50}{:>28}".format(name, self._counters[name]))
        else:
            lines.append("(no counters recorded)")
        lines.append("=" * 78)

        return "\n".join(lines)

    def print_report(self) -> None:
        print(self.report())


# module-level singleton used across the whole pipeline
profiler = Profiler()
