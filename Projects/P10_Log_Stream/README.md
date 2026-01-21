# P10: Log File Stream Processor 🌊

> **"If you don’t feel the memory advantage, redo it."**

## 🎯 The Objective
Simulate processing a massive (e.g., 1GB) log file. You need to read it line-by-line, filter for "ERROR", and count them, without crashing your RAM.

## 🛑 Strict Constraints
1.  **Usage of `yield`**. You must write a generator function.
2.  **No `readlines()`**. Reading the whole file at once is forbidden.
3.  **Pipeline**. Chain generators (one reads, one filters, one counts).

## 🔨 Requirements
- [ ] **Generator 1**: `read_logs(filename)` yields one line at a time.
- [ ] **Generator 2**: `filter_errors(log_stream)` yields only lines containing "ERROR".
- [ ] **Consumer**: Loop through the filter generator and print/count.

## 💡 Hints
- You can test this with a small file, but design it as if the file is 100TB.
