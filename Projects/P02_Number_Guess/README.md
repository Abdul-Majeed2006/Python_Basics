# P02: Number Guessing Game (But Serious) 🎲

> **"If your loop logic breaks, you don’t move on."**

## 🎯 The Objective
A robust guessing game where the computer picks a number, and you guess it. But with stakes and difficulty settings.

## 🛑 Strict Constraints
1.  **Loop Invariants**. At any point in the loop, your state variables (attempts left, range) must be correct.
2.  **No Infinite Loops**. The game *must* end eventually (Win or Loss).
3.  **Edge Cases**. What if I guess a number outside the valid range? What if I guess the same number twice?

## 🔨 Requirements
- [ ] **Difficulty Modes**:
    - Easy: 1-50 (10 attempts)
    - Hard: 1-100 (5 attempts)
    - Impossible: 1-1000 (3 attempts)
- [ ] **Feedback**: "Too High", "Too Low", "Way Too High" (if > 10 off).
- [ ] **History**: specific list of guesses made so far showed at end.
- [ ] **Replayability**: Ask to play again without restarting script.

## 💡 Hints
- `import random`
- `while True` is powerful but dangerous. Ensure your `break` conditions are bulletproof.
