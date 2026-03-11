# Lesson Plan: Conditionals in Python

---

## Header

| | |
|--|--|
| **Course** | Introduction to Programming (CS1) |
| **Topic** | Conditional Statements — `if`, `else`, `elif` |
| **Grade / Level** | Undergraduate (introductory) |
| **Duration** | 50 minutes |
| **Class Number** | 1 of [n] |
| **Date** | [Date] |
| **Instructor** | [Name] |

---

## Standards Alignment

| Standard | Description |
|----------|-------------|
| CSTA 3A-AP-15 | Justify the selection of specific control structures when tradeoffs involve implementation, readability, and program performance |
| CSTA 2-AP-10 | Use flowcharts and/or pseudocode to address complex problems as algorithms |
| CSTA 2-AP-12 | Design and iteratively develop programs that combine control structures |

---

## Learning Objectives (SWBAT)

By the end of this lesson, **Students Will Be Able To:**

1. **Explain** what a conditional statement is and describe a real-world situation where one is needed
2. **Write** an `if` statement that executes a code block only when a Boolean condition is `True`
3. **Write** an `if`/`else` statement to handle two mutually exclusive branches
4. **Write** an `if`/`elif`/`else` chain to handle three or more conditions
5. **Trace** through conditional code mentally and predict its output before running it

---

## Materials

- Student laptops with Python 3 installed, or browser-based interpreter (e.g., [repl.it](https://replit.com))
- Projector / screen share for instructor demos
- Slide deck (projected)
- Printed or digital "Day Planner" activity handout (Main Activity)
- Whiteboard / markers for the Hook activity

---

## Hook / Introduction — 5 minutes

**Activity: "What Would You Do?"**

Write the following on the board and ask students to complete the sentence out loud:

> *"If it is raining outside, I will ___. Otherwise, I will ___."*

Take 3–4 student responses. Then ask:

> *"Notice anything? You just described an* if*–*else *decision. Computers make these same kinds of decisions millions of times per second."*

Draw a simple flowchart on the board:

```
[Is it raining?]
      |
   YES / NO
    /      \
[Take      [Wear
umbrella]  sunscreen]
```

**Transition:** *"Today we'll write Python code that makes decisions exactly like this."*

---

## Direct Instruction — 12 minutes (5–17 min)

### 1. What Is a Conditional? (2 min)

A conditional statement tells the program: *"only run this code if a certain condition is true."*

Key vocabulary:
- **Condition** — an expression that evaluates to `True` or `False`
- **Boolean** — a data type with only two possible values: `True` / `False`
- **Branch** — a path the program can take depending on the condition

### 2. The `if` Statement (3 min)

**Syntax:**
```python
if condition:
    # code block — runs only if condition is True
```

**Example:**
```python
temperature = 35

if temperature > 30:
    print("It's hot outside!")
```

Walk through:
- The condition `temperature > 30` → evaluates to `True`
- Python executes the indented block
- Indentation (4 spaces) is required — it defines the block

### 3. The `else` Clause (3 min)

**Syntax:**
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

Ask students: *"What prints when temperature is 20? What about 35?"*

### 4. The `elif` Clause (3 min)

Use `elif` when there are more than two possible branches.

**Syntax:**
```python
if condition1:
    # runs if condition1 is True
elif condition2:
    # runs if condition1 is False AND condition2 is True
else:
    # runs if none of the above are True
```

**Example — Grade Classifier:**
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

Ask students: *"What grade prints for score = 78? score = 91?"*

### 5. Comparison Operators Quick Reference (1 min)

| Operator | Meaning |
|----------|---------|
| `==` | equal to |
| `!=` | not equal to |
| `>` | greater than |
| `<` | less than |
| `>=` | greater than or equal to |
| `<=` | less than or equal to |

---

## Guided Practice — 10 minutes (17–27 min)

Instructor live-codes the following on the projector while students type along on their own machines.

### Exercise A — Temperature Advisor
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

**Ask students to predict output before running** for: temp = 40, temp = 22, temp = 5.

### Exercise B — Even or Odd
```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(number, "is even.")
else:
    print(number, "is odd.")
```

Introduce `%` (modulo) briefly: *"The remainder when you divide by 2."*

---

## Main Activity — 15 minutes (27–42 min)

### "Day Planner" Coding Challenge

Students work **independently** (or in pairs if needed). Instructor circulates to assist.

**Task:** Write a Python program that acts as a simple day planner. Given a day of the week entered by the user, print a recommended activity.

**Requirements:**
- Use at least one `if`, one `elif`, and one `else`
- Handle at least 4 different days
- Output must be a complete sentence

**Starter template (on board / handout):**
```python
day = input("What day is it? ")

if day == "Monday":
    print("Start the week strong — review your notes!")
elif day == "___":
    print("___")
elif day == "___":
    print("___")
else:
    print("Enjoy your ___!")
```

**Challenge extension** (for students who finish early):
- Make the program case-insensitive using `.lower()`
- Add a second `input()` for time of day (`"morning"` / `"afternoon"`) and use nested conditionals

---

## Closing — 5 minutes (42–47 min)

### Objective Recap
Return to the slide with the 5 learning objectives. Ask students to give a thumbs up / thumbs down for each one — quick self-assessment.

### Exit Ticket (written or verbal)
Ask students to answer **one** of the following on a slip of paper or in a chat message:

1. *"Write the first line of an `if` statement that checks if a variable `age` is greater than or equal to 18."*
2. *"What is the difference between `if`/`else` and `if`/`elif`/`else`? Give one example of when you'd use each."*

Collect exit tickets to inform the next lesson.

---

## Preview — 3 minutes (47–50 min)

*"Great work today. Next class we'll tackle **loops** — what happens when you want to repeat an action 100 times? You'll see how conditionals and loops work together to build real programs."*

Assign homework (below) and remind students of office hours.

---

## Assessment

| Type | Description | Graded? |
|------|-------------|---------|
| **Formative — Exit Ticket** | Written response to one conceptual question | No |
| **Formative — Guided Practice** | Participation in live coding | No |
| **Formative — Main Activity** | Day Planner program (circulate and observe) | No |
| **Summative — Homework** | 3 conditional problems on Gradescope, due next class | Yes |

**Homework problems:**
1. Write a program that tells the user if a number is positive, negative, or zero
2. Write a grade classifier that outputs letter grades A–F
3. Write a simple chatbot that responds differently to at least 4 different user inputs

---

## Differentiation

### Support (for students who struggle)
- Provide a printed reference card with `if`/`elif`/`else` syntax and comparison operators
- Allow pair work during the main activity
- Reduce the Day Planner requirement to 2 days + `else` (one `if` and one `else`)
- Pre-fill more of the starter template

### Extension (for students who finish early)
- Add `.lower()` to handle case-insensitive input
- Use `and` / `or` to combine conditions: `if age >= 13 and age <= 17:`
- Write a number guessing game using nested conditionals
- Research: What is a `match` statement in Python 3.10+? How does it relate to `if`/`elif`?

---

## Instructor Notes

- **Common misconception:** Students often confuse `=` (assignment) with `==` (comparison). Address this explicitly when introducing comparison operators.
- **Indentation errors** are the #1 syntax mistake in Python. Walk through one intentional indentation error and its error message during Direct Instruction.
- If time is short, the `elif` section of Direct Instruction can be moved to the start of the next class.
