# P04: Student / Cadet Record System 🗃️

> **"If your data structure changes every 5 minutes, you failed."**

## 🎯 The Objective
Build a CRUD (Create, Read, Update, Delete) system for managing student records in memory.

## 🛑 Strict Constraints
1.  **Data Structure**: You MUST use a Dictionary of Dictionaries (or List of Dictionaries).
    - Example: `students = { "id_101": { "name": "Alice", "grades": [90, 85] } }`
2.  **No Parallel Lists**. If you have `names = []` and `grades = []`, delete your code.
3.  **Idempotency**: Updating a record that doesn't exist should inform the user, not crash.

## 🔨 Requirements
- [ ] **Create**: Add new student (ID must be unique).
- [ ] **Read**: View a student's full profile by ID.
- [ ] **Update**: Add a grade to a student's record.
- [ ] **Delete**: Remove a student.
- [ ] **Search**: Find all students with average grade > 85.

## 💡 Hints
- The ID is the primary key.
- Calculating average grade is a perfect candidate for a helper function from P03.
