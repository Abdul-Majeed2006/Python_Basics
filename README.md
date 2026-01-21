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

## 📚 Engineering Roadmap (Lesson Flow)

> **No Hype. Pure Engineering.**
>
> 🏆 **[START THE PROJECT-DRIVEN ROADMAP HERE (PROJECTS.md)](PROJECTS.md)** 🏆

| Phase | Topic | Engineering Grade Notes | Practice |
| :--- | :--- | :--- | :--- |
| **00** | Mental Setup | [Phase 00 Mental Setup](Notes/Phase_00_Mental_Setup.ipynb) | Trace code manually |
| **01** | Absolute Core | [Phase 01 Absolute Core](Notes/Phase_01_Absolute_Core.ipynb) | `exercises/ex01_variables.py` |
| **02** | Control Flow | [Phase 02 Control Flow](Notes/Phase_02_Control_Flow.ipynb) | `exercises/ex02_loops.py` |
| **03** | Functions | [Phase 03 Functions](Notes/Phase_03_Functions.ipynb) | - |
| **04** | Data Structures | [Phase 04 Data Structures](Notes/Phase_04_Data_Structures.ipynb) | - |
| **05** | File Handling | [Phase 05 File Handling](Notes/Phase_05_File_Handling.ipynb) | - |
| **06** | Exceptions | [Phase 06 Exceptions](Notes/Phase_06_Exceptions.ipynb) | - |
| **07** | Modules | [Phase 07 Modules](Notes/Phase_07_Modules.ipynb) | - |
| **08** | OOP | [Phase 08 OOP](Notes/Phase_08_OOP.ipynb) | - |
| **09** | Comprehensions | [Phase 09 Comprehensions](Notes/Phase_09_Comprehensions.ipynb) | - |
| **10** | Iterators | [Phase 10 Iterators](Notes/Phase_10_Iterators.ipynb) | - |
| **11** | Decorators | [Phase 11 Decorators](Notes/Phase_11_Decorators.ipynb) | - |
| **12** | Debugging | [Phase 12 Debugging](Notes/Phase_12_Debugging.ipynb) | - |
| **13** | Performance | [Phase 13 Performance](Notes/Phase_13_Performance.ipynb) | - |
| **14** | Applications | [Phase 14 Applications](Notes/Phase_14_Applications.ipynb) | Build something |

*Legacy notes have been archived in `Notes/legacy_v1/`*

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
