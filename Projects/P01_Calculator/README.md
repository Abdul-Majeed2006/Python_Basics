# P01: Terminal-Based Calculator + Analyzer 🧮

> **"If this feels too simple, you’re lying to yourself."**

## 🎯 The Objective
Build a terminal app that takes two numbers and an operator, performs the calculation, and prints a "statistical analysis" of the result (even/odd, positive/negative).

## 🛑 Strict Constraints (The "Brutal" Part)
1.  **NO FUNCTIONS**. Everything must run in the global scope (for now). You need to feel the pain of spaghetti code to appreciate functions later.
2.  **No `eval()`**. If you use `eval()`, you fail immediately.
3.  **Handle Bad Input**. If the user enters "two" instead of "2", the program must not crash. It should scold them and exit or ask again.
4.  **No Copy-Pasting**. Write every line.

## 🔨 Requirements
- [ ] Ask for Number 1.
- [ ] Ask for Number 2.
- [ ] Ask for Operator (+, -, *, /).
- [ ] Perform calculation.
- [ ] Print Result.
- [ ] Print "Analysis":
    - Is it an integer or float?
    - Is it even or odd? (Careful with floats!)
    - Is it positive, negative, or zero?

## 💡 Hints (No Code)
- `input()` returns a string. You can't multiply strings.
- Division by zero crash is a classic rookie mistake.
