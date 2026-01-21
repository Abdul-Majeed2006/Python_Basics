# P12: Break & Fix Challenge 🐛

> **"Engineers debug. Typists rewrite."**

## 🎯 The Objective
Go back to P01 (Calculator) or P04 (Record System). INTENTIONALLY break it. Introduce subtle bugs. Then fix them using **Tools**, not guess-and-check.

## 🛑 Strict Constraints
1.  **No `print()` Debugging**. You must use `pdb` or logging.
2.  **Reproduction Script**. Write a script (or test) that triggers the bug reliably.
3.  **The Fix**. Fix the bug without rewriting the whole logic.

## 🔨 Workflow
1.  **Sabotage**: Change a `+` to `*` in a rare edge case. Or make a variable global that shouldn't be.
2.  **Hunt**: Use `import pdb; pdb.set_trace()` to find the state corruption.
3.  **Test**: Write a `unittest` case that fails (Red).
4.  **Repair**: Fix the code so the test passes (Green).

## 💡 Hints
- `n` (next), `s` (step), `p` (print variable) in pdb.
