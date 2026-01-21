# P03: Utility Toolkit 🛠️

> **"This is where sloppy thinkers fail."**

## 🎯 The Objective
Create a library of reusable tools. This is not a "script" that runs from top to bottom. It’s a box of functions.

## 🛑 Strict Constraints
1.  **NO Global State**. Functions cannot rely on variables defined outside them.
2.  **Docstrings MANDATORY**. Every function must explain Inputs, Outputs, and Purpose.
3.  **Type Hinting**. Use `def func(a: int) -> int:` syntax.

## 🔨 Tools to Build
### Math Tools
- `is_prime(n)`: Returns bool. Efficiently.
- `factorial(n)`: Recursive or iterative. Handle negatives.
- `stats(numbers_list)`: Returns a dict with max, min, avg.

### Text Tools
- `word_count(text)`: Returns dictionary of word frequencies.
- `clean_text(text)`: Removes punctuation, lowercases everything.

## 💡 Hints
- Test your tools by creating a `__main__` block that calls them.
- `clean_text("Hello!")` should return `"hello"`.
