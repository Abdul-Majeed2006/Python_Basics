# P11: Function Monitoring Toolkit 🕵️‍♀️

> **"If you use decorators just to feel advanced, you failed."**

## 🎯 The Objective
Create a set of decorators that you can slap onto any function to monitor its behavior in production.

## 🛑 Strict Constraints
1.  **Usage**. The decorators must be reusable. `@timer` on one function, `@log_args` on another.
2.  **`functools.wraps`**. You must preserve the metadata of the original function.
3.  **Real Value**. Don't make a decorator that prints "Hello". Make one that saves your bacon during a crash.

## 🔨 Requirements
- [ ] **`@execution_time`**: Prints (or logs) how long the function took.
- [ ] **`@validate_positive`**: (Example) raises Error if argument is negative.
- [ ] **`@simulated_auth`**: Checks a global variable `USER_ROLE`. If not "ADMIN", raising PermissionError.

## 💡 Hints
- `time.time()`
- `args` and `kwargs` mastery is required here.
