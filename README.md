# 🤖 Agentic AI Cohort

A hands-on learning journey through Python and Agentic AI concepts — one day at a time.

---

## 📁 Project Structure

```
Agentic-AI-Cohort/
├── DAY_01/
│   ├── test.py          # Python basics — input/output practice
│   └── Assingment.py   # Day 01 assignments (Calculator, Guessing Game, Grade Calculator)
├── main.py              # Project entry point
├── .gitignore           # Ignores .venv and other unnecessary files
└── README.md            # You're here!
```

---

## 📅 Day 01 — Python Basics & Problem Solving

### 🧪 `test.py` — Input/Output Basics
Practice script covering:
- Taking **string input** from the user
- Taking **integer input** using `int(input(...))`

```python
name = input("Enter your name: ")
print(name)

a = int(input("Enter your number: "))
print(a)
```

---

### 📝 `Assingment.py` — Assignments

#### ✅ Assignment 1 — Calculator
A basic calculator that:
- Takes two numbers and an operator (`+`, `-`, `*`, `/`) as input
- Handles **division by zero** gracefully
- Outputs the computed result

#### ✅ Assignment 2 — Number Guessing Game
An interactive guessing game that:
- Generates a **random number between 1 and 100**
- Gives hints: *"Too High"* or *"Too Low"*
- Loops until the user guesses correctly

#### ✅ Assignment 3 — Student Grade Calculator
Calculates a student's grade based on marks across 5 subjects:
- Takes marks for each subject via a loop
- Computes **total** and **percentage**
- Assigns grade based on the following scale:

| Percentage  | Grade |
|-------------|-------|
| ≥ 90%       | A     |
| ≥ 75%       | B     |
| ≥ 60%       | C     |
| ≥ 40%       | D     |
| < 40%       | F     |

---

## ⚙️ Setup & Run

```bash
# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate

# Run any script
python DAY_01/test.py
python DAY_01/Assingment.py
```

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Environment:** Virtual environment (`.venv`)
- **Version Control:** Git
