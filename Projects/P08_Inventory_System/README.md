# P08: Inventory / Equipment Management System 🏭

> **"OOP is about design, not syntax."**

## 🎯 The Objective
Model a warehouse using Class-based structures. Manage items, categories, and stock levels.

## 🛑 Strict Constraints
1.  **Encapsulation**. Attributes like `stock_level` should not be accessed directly (use methods like `add_stock()`).
2.  **Reprs**. Every class must have a `__repr__` method so `print(item)` looks good.
3.  **No God Classes**. Don't put everything in one `Warehouse` class. Items should be their own class.

## 🔨 Requirements
- [ ] **Item Class**: Name, Price, Quantity. Method `update_stock()`.
- [ ] **Category Class**: Holds a list of items.
- [ ] **Warehouse Class**: Holds categories.
- [ ] **Interaction**: Create items, move them between categories, check total value.

## 💡 Hints
- `f"Item({self.name}, {self.price})"`
- Composition: A Warehouse *has* Categories. A Category *has* Items.
