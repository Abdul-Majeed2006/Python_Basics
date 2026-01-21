# P13: Optimize a Slow Script 🏎️

> **"Speed without clarity is useless."**

## 🎯 The Objective
Write a script that is intentionally slow (O(n²) or worse). Then refactor it to O(n) or O(log n).

## 🛑 Strict Constraints
1.  **Measure First**. Use `time.time()` or `cProfile` to prove it is slow.
2.  **No Logic Change**. The output must remain exactly the same.
3.  **Big O Analysis**. You must write a comment explaining WHY the new version is faster.

## 🔨 The Challenge
- **Scenario**: Finding duplicates in a list of 100,000 random numbers.
- **Slow Way**: Nested loops (compare every number to every other number). ~Wait seconds/minutes.
- **Fast Way**: Use a Set. ~Instant.

## 💡 Hints
- See `Phase 13: Performance` in the roadmap.
