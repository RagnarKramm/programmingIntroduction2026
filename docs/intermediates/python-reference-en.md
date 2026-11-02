---
title: "Python reference · English"
nav_order: 1
permalink: /
lang: en
description: "A short Python reference for the concepts in script.py."
---

# Python quick reference

[Eesti keeles]({{ '/intermediates/python-reference-et.html' | relative_url }})

Only the concepts used in `script.py`. Find a concept, compare the example with your code, then change one thing and run again. Each code block is a separate example.

## Variables and data types

`=` stores a value in a variable. A later assignment replaces it. Names are case-sensitive: `age` and `Age` are different.

```python
name = "Alice"       # str: text (use quotes)
age = 25             # int: whole number
price = 19.99        # float: decimal number (use a dot)
is_active = True     # bool: True or False (no quotes)
```

**Check:** `"25"` is text; `25` is a number. A comment starts with `#`; Python ignores the rest of that line.

## Output: print and f-strings

`print()` displays a value. In an f-string, `{name}` inserts the variable's value into text.

```python
name = "Ragnar"
print("Today is a good day!")
print(f"Hi, {name}!")  # Hi, Ragnar!
```

**Check:** use the `f` before the opening quote and braces `{}` around the variable. `print("name")` displays the word; `print(name)` displays its value.

## Input: ask and store

`input()` asks a question and returns **text**, even when you type digits. Type an answer and press Enter.

```python
friendName = input("What is your name: ")
print(f"Hi, {friendName}!")
```

**Check:** use the same variable name when reading the answer. In `script.py`, `friendName` is stored but never used in a greeting.

## Numbers: int and subtraction

`int()` converts whole-number text to an integer. `-` subtracts numbers.

```python
age = input("How old are you: ")
birth_year = 2026 - int(age)
print(birth_year)
```

**Check:** type `12`, not `twelve` or `12.5`. Do not put `age = 25` after the question unless you want to replace the answer (as `script.py` currently does). This estimate uses the fixed year 2026; the actual birth year may be one year earlier if the birthday is still ahead.

## Functions: define and call

`def` defines a reusable action. A **call** runs it. A **parameter** receives the value passed in the call.

```python
def print_hi(name):          # name is the parameter
    print(f"Hi, {name}!")

def tell_story():            # no parameter
    print("Today is a good day!")

print_hi("Alice")           # pass one value
tell_story()                # parentheses still needed
```

**Check:** end the definition with `:`. Indent its body consistently (use four spaces). Define the function before calling it; put these calls outside its body.

## Return: send a result back

`return` ends the function and sends a value back to the caller. Store or use that value. `print()` only displays it.

```python
def ask_age():
    return input("How old are you: ")

def calculate_birthday_year(age):
    return 2026 - int(age)

age = ask_age()
birth_year = calculate_birthday_year(age)
print(birth_year)
```

**Check:** `return print(...)`, as used in `print_age` in the script, displays text but returns `None` (no value). Use `return year` to send a year back, or just `print(...)` to display it.

## Decisions: if, elif, else

`==` compares values. Python runs the first matching branch; `else` handles the remaining answers.

```python
answer = input("Do you like programming (yes/no): ")
if answer == "yes":
    print("Nice, me too!")
elif answer == "no":
    print("No problem!")
else:
    print("Only 'yes' and 'no' are valid answers!")
```

**Check:** `=` assigns; `==` compares. Keep `if`, `elif` and `else` aligned, add each `:`, and indent each body. `Yes` and `yes ` do not equal `yes`.

## Starting the script: main guard

The indented code runs when you run this file directly. It does not run when another file imports it. Keep the special names exactly as shown.

```python
def tell_story():
    print("Today is a good day!")

if __name__ == "__main__":
    tell_story()
```

## When your code does not work

Read the last error line; check the indicated code line and the line above it.

| Symptom | First check |
|---|---|
| `SyntaxError` | Matching quotes and parentheses; missing `:`; `==` in conditions |
| `IndentationError` | Consistent spaces inside functions and branches; no mixed tabs/spaces |
| `NameError` | Spelling and capitals; assign variables and define functions before use |
| `TypeError` | Convert input before subtraction; pass the right number of function arguments |
| `ValueError` from `int()` | Enter whole-number digits, such as `12` |
| Nothing prints | Call the function; use `print()` to display a returned value |
| Wrong name or age | Check which variable you use and whether a later assignment replaces the answer |

Save the file, run it again, and compare the result with what you expected.
