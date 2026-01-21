# P09: Data Cleaner 🧹

> **"Readability is non-negotiable."**

## 🎯 The Objective
Take a list of messy, unformatted strings (e.g., "  john.DOE@email.com ", "Jane-doe@GMAIL.com") and transform them into a standardized, usable dataset using List Comprehensions.

## 🛑 Strict Constraints
1.  **Comprehensions Only**. Logic like filtering and mapping must use `[x for x in data]`.
2.  **No Unreadable One-Liners**. If it's too complex, break it down or use a normal loop.
3.  **Transformation Pipeline**. Normalize -> Filter -> Structure.

## 🔨 Requirements
- [ ] **Input**: A list of raw records (dicts with bad keys/values).
- [ ] **Filter**: different criteria (e.g. active users only).
- [ ] **Transform**: standardizing names, changing string numbers to ints.
- [ ] **Load**: Result into a new clean list.

## 💡 Hints
- `cleaned = [process(x) for x in raw_data if is_valid(x)]`
