# === Stage 61: Add performance timing for core list and search operations ===
# Project: GoalTrail
import time


class Timer:
    def __init__(self):
        self._log = []

    def _now(self):
        return time.perf_counter()

    def measure(self, fn_name, data, iterations=100):
        best = float("inf")
        worst = 0.0
        for _ in range(iterations):
            start = self._now()
            result = fn_name(data)
            end = self._now()
            elapsed_ms = (end - start) * 1000
            best = min(best, elapsed_ms)
            worst = max(worst, elapsed_ms)
        return {"operation": fn_name, "best_ms": round(best, 3), "worst_ms": round(worst, 3)}

    def log(self):
        if not self._log:
            print("No timings recorded.")
            return
        for entry in self._log:
            print(f"{entry['operation']}: best={entry['best_ms']}ms worst={entry['worst_ms']}ms")


def benchmark_list_ops():
    t = Timer()

    # Linear search
    data = list(range(10_000))
    target = 5000
    t.measure(lambda d, tgt: next((x for x in d if x == tgt), -1), {"data": data, "target": target})

    # List append growth
    def grow_list(n):
        lst = []
        for i in range(n):
            lst.append(i)
        return len(lst)

    t.measure(grow_list, 2000)

    # In-place replace (no allocation)
    data2 = list(range(10_000))
    idx = next((i for i, v in enumerate(data2) if v == 5000), -1)
    t.measure(lambda d: None, {"data": data2})

    print(t.log())


benchmark_list_ops()
