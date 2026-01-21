# P06: Fault-Tolerant CLI App 🛡️

> **"If your app crashes, you refactor."**

## 🎯 The Objective
Build a command-line tool (e.g., a file downloader or converter) that is bulletproof. It handles network errors, missing files, and user stupidity without showing a Python traceback.

## 🛑 Strict Constraints
1.  **No Bare `except`**. `except:` is illegal. You must catch specific errors (`except ValueError:`).
2.  **Graceful Failure**. If an error occurs, print a friendly message ("Could not find file") and exit with a non-zero status code.
3.  **Log File**. Errors must be silently logged to `errors.log` so you can debug later.

## 🔨 Requirements
- [ ] **Custom Exceptions**: Define at least one exception class (e.g., `InvalidConfigError`).
- [ ] **Logging**: Use the `logging` module.
- [ ] **EAFP**: Use "Easier to Ask Forgiveness than Permission" style.

## 💡 Hints
- `logging.basicConfig(filename='errors.log')`
- `sys.exit(1)` indicates a failure to the OS.
