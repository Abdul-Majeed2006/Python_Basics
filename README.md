# 🐍 Python Basics Learning Environment ✨

[![Python Tests](https://github.com/Abdul-Majeed2006/Python_Basics/actions/workflows/test.yml/badge.svg)](https://github.com/Abdul-Majeed2006/Python_Basics/actions/workflows/test.yml)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Course Objective**: Learn Python from completely zero to intermediate engineering concepts. This course emphasizes not just *syntax*, but *engineering discipline*—teaching you how to write code that is reproducible, testable, and maintainable.

## ⚡ Quick Start

```bash
git clone https://github.com/Abdul-Majeed2006/Python_Basics.git
cd Python_Basics

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt
pytest
```

## 📚 Lesson Flow

| Lesson | Topic | Notes (Theory) | Exercise (Practice) | Solution (Reference) |
| :--- | :--- | :--- | :--- | :--- |
| **01** | Variables | [L01 Variables](Notes/L01%20Variables%20and%20Simple%20Data%20Types.ipynb) | [ex01_variables.py](exercises/ex01_variables.py) | [sol01_variables.py](solutions/sol01_variables.py) |
| **02** | Lists | [L02 Lists](Notes/L02%20introducing%20lists.ipynb) | - | - |
| **03** | Working w/ Lists | [L03 Working With Lists](Notes/L03%20Working%20With%20Lists.ipynb) | - | - |
| **04** | If Statements | [L04 If Statements](Notes/L04%20If%20Statements.ipynb) | - | - |
| **05** | Dictionaries | [L05 Dictionaries](Notes/L05%20Dictionaries.ipynb) | - | - |
| **06** | Loops & Input | [L06 Loops](Notes/L06%20User%20Input%20and%20While%20Loops.ipynb) | [ex02_loops.py](exercises/ex02_loops.py) | [sol02_loops.py](solutions/sol02_loops.py) |
| **07** | Functions | [L07 Functions](Notes/L07%20Functions.ipynb) | - | - |
| **08** | Classes | [L08 Classes](Notes/L08%20Classes.ipynb) | - | - |
| **09** | Comprehensions | [L09 List Comprehensions](Notes/L09%20List%20Comprehensions.ipynb) | - | - |
| **10** | Files & Errors | [L10 Files and Exceptions](Notes/L10%20Files%20and%20Exceptions.ipynb) | - | - |
| **11** | Testing | [L11 Testing Your Code](Notes/L11%20Testing%20Your%20Code.ipynb) | - | - |
| **12** | Standard Library | [L12 The Standard Library](Notes/L12%20The%20Standard%20Library.ipynb) | - | - |
| **13** | Type Hints | [L13 Type Hints](Notes/L13%20Type%20Hints.ipynb) | - | - |
| **14** | Project Setup | [L14 Project Setup](Notes/L14%20Project%20Setup.ipynb) | - | - |

---

## 🧠 Learning Outcomes & Engineering Thinking

### 🔹 Lesson 01: Variables
- **Concept**: Storing data types (strings, integers).
- **Skill**: Basic state management.
- **Engineering Mindset**: Naming variables descriptively (`user_age` vs `x`) prevents bugs later.

### 🔹 Lesson 06: Loops
- **Concept**: Iteration and control flow.
- **Skill**: Automating repetitive tasks.
- **Common Mistake**: modifying a list while iterating over it (causes skipped items).

## 🔧 Engineering Thinking

This section separates this course from basic tutorials—it teaches you **why** things work the way they do.

### Why Python is Dynamically Typed
- **Static typing** (C++, Java): `int x = 5;` — type is declared and enforced.
- **Dynamic typing** (Python): `x = 5` — type is inferred at runtime.
- **Trade-off**: Python is faster to write, but errors appear later (runtime vs compile-time).
- **Professional Fix**: Use Type Hints (`def add(x: int, y: int) -> int:`) and tools like `mypy`.

### Why Loops Can Fail Silently
```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # ❌ DANGEROUS: modifies list during iteration
```
- **Problem**: Removing items shifts indices, causing Python to skip elements.
- **Solution**: Use list comprehensions or iterate over a copy:
  ```python
  numbers = [num for num in numbers if num % 2 != 0]  # ✅ Safe
  ```

### Common Beginner Pitfalls
1. **Mutable Default Arguments**:
   ```python
   def add_item(item, lst=[]):  # ❌ lst is shared across calls
       lst.append(item)
       return lst
   ```
2. **Not Validating Input**: Always check types and ranges before processing.
3. **Hardcoded Values**: Use constants or config files instead of magic numbers.

### Best Practices
- **Naming**: `user_age` > `x`, `calculate_total()` > `calc()`
- **Modularization**: Keep functions under 20 lines; one responsibility per function.
- **Testing**: Write tests **before** you refactor—proves nothing broke.


- **`src/`**: reusable code modules (The "Product").
- **`tests/`**: automated verification (The "Proof").
- **`exercises/`**: your workspace.
- **`solutions/`**: the answer key.
- **`Notes/`**: the textbook.
