# 🐍 Python Basics Learning Environment ✨

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

*(More advanced topics like Files, Testing, and Type Hints are in the `Notes/` folder)*

## 🧠 Learning Outcomes & Engineering Thinking

### 🔹 Lesson 01: Variables
- **Concept**: Storing data types (strings, integers).
- **Skill**: Basic state management.
- **Engineering Mindset**: Naming variables descriptively (`user_age` vs `x`) prevents bugs later.

### 🔹 Lesson 06: Loops
- **Concept**: Iteration and control flow.
- **Skill**: Automating repetitive tasks.
- **Common Mistake**: modifying a list while iterating over it (causes skipped items).

## 📂 Repository Structure

- **`src/`**: reusable code modules (The "Product").
- **`tests/`**: automated verification (The "Proof").
- **`exercises/`**: your workspace.
- **`solutions/`**: the answer key.
- **`Notes/`**: the textbook.
