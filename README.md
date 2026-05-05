# 🧩 Sudoku Validator

## 📌 Overview
This project implements a Sudoku Validator in Python that verifies whether a given 9x9 Sudoku grid is valid. It checks rows, columns, and 3x3 subgrids to ensure they contain all digits from 1 to 9 without duplication.

## 🧠 Key Highlights
- Implemented a complete validation system for Sudoku grids
- Used efficient set-based comparisons for validation
- Covered all constraints: rows, columns, and 3x3 subgrids
- Achieved full test coverage using Pytest
- Wrote clean and readable Python code

## ⚙️ Features
- Validates all rows contain digits 1–9
- Validates all columns contain digits 1–9
- Validates each 3x3 subgrid contains digits 1–9
- Handles invalid grids correctly

## 🛠️ Tech Stack
- Python
- Pytest (unit testing)
- Pylint (code quality)

## 🧪 Example

```python
grid = [
    [7,8,4,1,5,9,3,2,6],
    [5,3,9,6,7,2,8,4,1],
    [6,1,2,4,3,8,7,5,9],

    [9,2,8,7,1,5,4,6,3],
    [3,5,7,8,4,6,1,9,2],
    [4,6,1,9,2,3,5,8,7],

    [8,7,6,3,9,4,2,1,5],
    [2,4,3,5,6,1,9,7,8],
    [1,9,5,2,8,7,6,3,4]
]

sudoku_validator(grid)
# Output: True
```

## 🧩 How It Works
- Each row is checked using set comparison
- Each column is extracted and validated
- Each 3x3 subgrid is iterated and validated
- If any condition fails → returns False
- If all checks pass → returns True

## 🧪 Testing
Run all tests:

```bash
pytest -v
```

✔️ All tests pass  
✔️ Code quality validated with Pylint  

## 📚 What I Learned
- Working with nested data structures (list of lists)
- Using sets for efficient validation
- Iterating over 2D data structures
- Writing clean and testable logic
- Validating complex constraints step by step

## 💡 Why This Project Matters
This project demonstrates strong problem-solving skills, logical thinking, and the ability to validate structured data efficiently. It reflects real-world scenarios where data integrity and validation are critical.

## 🔗 Author
Yağmur Güner
