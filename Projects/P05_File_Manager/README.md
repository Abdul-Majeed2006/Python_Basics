# P05: Persistent Record Manager 💾

> **"Now your code touches reality."**

## 🎯 The Objective
Take P04 and give it a brain. Save the data to a file so it survives a reboot.

## 🛑 Strict Constraints
1.  **Use `with`**. `open()` without `with` is an automatic fail.
2.  **Format**: Start with `.txt` (manual parsing), then upgrade to `.json`.
3.  **Corruption Proof**: If the file is empty or corrupted, the program must not crash. It should start with a fresh database.

## 🔨 Requirements
- [ ] **Load on Start**: Read data from `database.json`.
- [ ] **Auto-Save**: Save data after every Create/Update/Delete action.
- [ ] **Manual Save**: Option to export to a specific filename.
- [ ] **Reset**: Option to wipe the database (with "Are you sure?" confirmation).

## 💡 Hints
- `import json`
- `json.dump(data, file, indent=4)` makes it readable.
- Validating JSON before loading it is "defensive programming".
