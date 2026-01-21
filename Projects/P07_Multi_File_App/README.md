# P07: Multi-File Python Application 📦

> **"Single-file Python is a dead end."**

## 🎯 The Objective
Refactor one of your previous projects (like P04 or P05) into a professional modular structure.

## 🛑 Strict Constraints
1.  **No Sprawling Code**. `main.py` should be under 50 lines. It just coordinates the other modules.
2.  **No Circular Imports**. If A imports B and B imports A, you fail.
3.  **Virtual Environment**. You must create and activate a `venv`.

## 🔨 Structure
```
project/
 ├── venv/          (Excluded from Git)
 ├── src/
 │    ├── __init__.py
 │    ├── main.py     (Entry point)
 │    ├── logic.py    (Calculations)
 │    ├── storage.py  (File I/O)
 │    └── utils.py    (P03 Helpers)
 ├── requirements.txt
 └── README.md
```

## 💡 Hints
- Use `from src import logic`
- `pip freeze > requirements.txt`
