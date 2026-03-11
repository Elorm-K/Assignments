---
marp: true
theme: default
paginate: true
style: |
  section {
    font-size: 28px;
  }
  code {
    font-size: 24px;
  }
  h1 { color: #2c3e50; }
  h2 { color: #34495e; }
---

<!-- Slide 1: Title -->
# Conditionals in Python

### Introduction to Programming — CS1

`if` · `else` · `elif` · Boolean Expressions

---

<!-- Slide 2: Roadmap -->
## Today's Roadmap

| Time | Topic |
|------|-------|
| 0–5 min | Hook: Real-world decisions |
| 5–17 min | Direct Instruction: `if`, `else`, `elif` |
| 17–27 min | Guided Practice |
| 27–42 min | Main Activity: Day Planner |
| 42–47 min | Closing + Exit Ticket |
| 47–50 min | Preview of next class |

---

<!-- Slide 3: Learning Objectives -->
## Learning Objectives (SWBAT)

By the end of class, you will be able to:

1. **Explain** what a conditional statement is
2. **Write** `if` statements using Boolean conditions
3. **Write** `if`/`else` statements for two branches
4. **Write** `if`/`elif`/`else` chains for multiple conditions
5. **Trace** code and predict output before running it

---

<!-- Slide 4: Hook — Real-World Decisions -->
## Every Decision Is a Conditional

*"If it is raining, I will take an umbrella. Otherwise, I will wear sunscreen."*

```
        [Is it raining?]
               |
           YES   NO
          /         \
    [Take            [Wear
   umbrella]       sunscreen]
```

Computers make decisions like this **millions of times per second**.

---

<!-- Slide 5: What Is a Conditional? -->
## What Is a Conditional?

A **conditional statement** tells the program:
> *"Only run this code if a certain condition is true."*

Key vocabulary:

| Term | Meaning |
|------|---------|
| **Condition** | An expression that is `True` or `False` |
| **Boolean** | A type with only two values: `True` / `False` |
| **Branch** | A path the program takes based on the condition |

---

<!-- Slide 6: `if` Statement Syntax -->
## The `if` Statement

```python
if condition:
    # code block
    # runs only if condition is True
```

**Example:**
```python
temperature = 35

if temperature > 30:
    print("It's hot outside!")
```

- Indentation (4 spaces) defines the code block
- If condition is `False` → block is skipped entirely

---

<!-- Slide 7: Comparison Operators -->
## Comparison Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | equal to | `age == 18` |
| `!=` | not equal to | `day != "Monday"` |
| `>` | greater than | `score > 90` |
| `<` | less than | `temp < 0` |
| `>=` | greater than or equal | `grade >= 60` |
| `<=` | less than or equal | `speed <= 100` |

> ⚠️ `=` assigns a value. `==` compares two values.

---

<!-- Slide 8: `else` Clause -->
## Adding `else`

```python
if condition:
    # runs if condition is True
else:
    # runs if condition is False
```

**Example:**
```python
temperature = 20

if temperature > 30:
    print("It's hot outside!")
else:
    print("Enjoy the cool weather.")
```

**Q:** What prints when `temperature = 20`? When `temperature = 35`?

---

<!-- Slide 9: `elif` — Multiple Branches -->
## `elif` — More Than Two Options

```python
if condition1:
    # runs if condition1 is True
elif condition2:
    # runs if condition1 False AND condition2 True
else:
    # runs if none of the above are True
```

Python checks conditions **top to bottom** and stops at the first `True`.

---

<!-- Slide 10: `elif` — Grade Classifier -->
## `elif` Example — Grade Classifier

```python
score = 78

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("Below C")
```

**Q:** What prints for `score = 78`? For `score = 91`? For `score = 55`?

---

<!-- Slide 11: Guided Practice — Temperature Advisor -->
## Guided Practice — Temperature Advisor

Type this along with me:

```python
temp = int(input("What is the temperature today? "))

if temp >= 35:
    print("Wear light clothing and stay hydrated.")
elif temp >= 20:
    print("Great weather for a walk!")
elif temp >= 10:
    print("Bring a jacket.")
else:
    print("Bundle up — it's cold!")
```

**Predict first:** What prints for `temp = 40`? `temp = 22`? `temp = 5`?

---

<!-- Slide 12: Guided Practice — Even or Odd -->
## Guided Practice — Even or Odd

```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(number, "is even.")
else:
    print(number, "is odd.")
```

**New operator:** `%` is **modulo** — gives the remainder after division.

- `10 % 2` → `0` (even)
- `7 % 2` → `1` (odd)

---

<!-- Slide 13: Main Activity -->
## Main Activity — Day Planner

**Task (15 minutes):** Write a program that recommends an activity based on the day of the week.

**Requirements:**
- Use at least one `if`, one `elif`, and one `else`
- Handle at least 4 different days
- Output must be a complete sentence

```python
day = input("What day is it? ")

if day == "Monday":
    print("Start the week strong — review your notes!")
elif day == "___":
    print("___")
# ... continue
else:
    print("Enjoy your ___!")
```

---

<!-- Slide 14: Extension Challenge -->
## Finished Early? Try This!

**Level 1:** Make your program case-insensitive
```python
day = input("What day is it? ").lower()
```

**Level 2:** Add a second input for time of day
```python
time = input("Morning or afternoon? ")
if day == "monday" and time == "morning":
    print("Perfect time to plan your week!")
```

**Level 3:** Write a number guessing game using conditionals

---

<!-- Slide 15: Common Mistakes -->
## Watch Out For These!

**Mistake 1: Using `=` instead of `==`**
```python
# Wrong — this is assignment, not comparison
if age = 18:

# Correct
if age == 18:
```

**Mistake 2: Missing indentation**
```python
if score > 90:
print("A")    # IndentationError!

if score > 90:
    print("A")  # Correct
```

---

<!-- Slide 16: Tracing Code -->
## Tracing — Predict Before You Run

```python
x = 15

if x > 20:
    print("Big")
elif x > 10:
    print("Medium")
else:
    print("Small")
```

Walk through step by step:
1. Is `x > 20`? → `15 > 20` → **False** → skip
2. Is `x > 10`? → `15 > 10` → **True** → print `"Medium"` → stop

---

<!-- Slide 17: Exit Ticket -->
## Closing — Exit Ticket

Before you leave, answer **one** of these:

**Option A:** Write the first line of an `if` statement that checks if a variable `age` is greater than or equal to 18.

**Option B:** What is the difference between `if`/`else` and `if`/`elif`/`else`? Give one example of when you'd use each.

---

<!-- Slide 18: Summary -->
## Summary

✅ Conditionals let programs make decisions

✅ `if` runs a block only when the condition is `True`

✅ `else` provides a fallback when the condition is `False`

✅ `elif` handles multiple branches — checked top to bottom

✅ Use `==` to compare, `=` to assign

✅ Trace code step by step to predict what it does

---

<!-- Slide 19: Homework -->
## Homework — Due Next Class

Post on Gradescope:

1. Write a program that tells the user if a number is **positive**, **negative**, or **zero**
2. Write a **grade classifier** that outputs letter grades A through F
3. Write a simple **chatbot** that responds differently to at least 4 different user inputs

---

<!-- Slide 20: What's Next -->
## What's Next

**Next class: Loops**
> *What if you want to repeat an action 100 times?*
> You'll see how conditionals and loops work together to build real programs.

**Resources:**
- [Python 3 Docs — Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- [Automate the Boring Stuff — Chapter 2](https://automatetheboringstuff.com/2e/chapter2/)
- Office hours: [Day / Time / Location]
