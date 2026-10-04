---
title: "Intermediate Python · Week 1"
nav_order: 3
description: "Build a mission briefing with input, variables, strings and print."
---

# Week 1: Mission briefing generator

Turn a player's answers into a personalised space mission. Today we use **text, variables, `input()` and `print()`**.

**Your main goal:** ask two questions, print three briefing lines, and explain where each answer is used. The other tasks are optional choices once your Mission works.

## Jump to the help you need

- [Starter: Welcome aboard](#starter-welcome-aboard)
- [Theory: how the code works](#theory-how-the-code-works)
- [Mission: three-line briefing](#mission-three-line-briefing)
- [Upgrade: bring a companion](#upgrade-bring-a-companion)
- [Challenge: two briefings](#challenge-two-briefings)
- [Boss: four-input story](#boss-four-input-story)
- [Optional: control punctuation](#optional-control-punctuation)
- [Debugging: find and fix a problem](#debugging-find-and-fix-a-problem)
- [Save your work](#save-your-work)

## Starter: Welcome aboard

Copy these two lines into your Python editor. Run the program, type a fictional pilot name, and submit the answer.

```python
pilot = input("Pilot name: ")
print("Welcome aboard,", pilot)
```

If you enter `Ada`, the greeting is:

```text
Welcome aboard, Ada
```

**Try it:** change `"Welcome aboard,"` to `"Mission control welcomes"`. Run again to see the new greeting.

**Explain it:** which part is fixed text, and which part comes from the player?

## Theory: how the code works

### Follow the answer

For the starter, the journey is:

```text
input("Pilot name: ") → player types Ada → pilot remembers "Ada"
print("Welcome aboard,", pilot) → Welcome aboard, Ada
```

Python runs the statements from top to bottom. Store an answer **before** a later line uses it. Python checks a script's syntax before running it; a missing quote can prevent the whole script from starting.

The **editor** holds your instructions. The **output area** shows what happened during a run. After editing, run again. Each fresh run asks for new answers; saving the code does not automatically save those answers.

### Strings: text inside quotes

A **string** is a text value. Quotes tell Python to treat something as literal text.

```python
destination = "Mars"
print(destination)
print("destination")
```

Output:

```text
Mars
destination
```

`destination` asks Python for the stored value. `"destination"` is just the word itself.

Single or double quotes work, but the opening and closing quotes must match. Use straight quotes in code. To put an apostrophe in a sentence, use double quotes around it:

```python
print("Let's launch!")
print('The robot says "Hello".')
```

### Variables: names that remember values

In `pilot = input("Pilot name: ")`, Python first runs the right side, then assigns the returned answer to the name on the left. Here, **`=` means assignment**.

Use descriptive English names such as `pilot`, `destination`, and `companion`. Start with a letter and use letters, digits or underscores. Avoid spaces and hyphens. Keep the spelling and capitals identical everywhere: `pilot` and `Pilot` are different names. Do not use reserved words such as `class`, or replace built-in names such as `print` and `input`.

Assigning a new value replaces what the variable remembers:

```python
pilot = "Ada"
original_pilot = pilot
pilot = "Sam"
print(original_pilot, pilot)
```

Output: `Ada Sam`. `original_pilot` received the earlier string value; changing `pilot` does not change that other variable or earlier output.

### Input: ask and remember

```python
destination = input("Destination: ")
```

`input()` displays a **prompt**, waits for an answer, and returns it as a string. In a terminal, type the answer and press Enter. If your runner has an input panel, supply one answer per line in question order.

- `Liis Mari`, `Jüri`, and `Planet 42` are all text answers.
- Typing `42` still returns text, not a number. Number conversion is for a later lesson.
- Pressing Enter without typing returns an empty string. Today's tasks do not require checking for empty answers.
- The Enter newline is removed, but other typed spaces can remain.

This asks a question but does **not** keep the answer for later:

```python
input("Pilot name: ")
```

Use a variable assignment when your story needs the answer again. You can reuse a stored answer many times without asking again.

### Output: display values with print

```python
pilot = "Ada"
destination = "Mars"
print("Pilot", pilot, "is going to", destination)
print()
print("Ready for launch")
```

Output:

```text
Pilot Ada is going to Mars

Ready for launch
```

`print()` and `input()` are built-in **functions**: named actions called with parentheses. The values inside the parentheses are **arguments**.

By default, `print()` puts spaces between comma-separated arguments and finishes the line. `print()` with no arguments makes a blank output line. Use round parentheses, not square brackets. In a script, a variable name alone does not display its value: use `print()`.

### Comments and layout

```python
# Collect the answers
pilot = input("Pilot name: ")

# Display the greeting
print("Welcome,", pilot)
```

A `#` outside quotes starts a comment for humans; Python ignores the rest of that line. A `#` inside quotes is ordinary text. Blank lines in the code help separate sections; they do not print blank output lines.

For today's programs, put each statement on its own line, starting at the left edge. No semicolons are needed. Do not copy the interactive prompt `>>>` into a `.py` file.

### Vocabulary

| English | Estonian | Meaning today |
|---|---|---|
| String | sõne | A text value |
| Variable | muutuja | A name that remembers a value |
| Assignment | omistamine | Give a value to a variable |
| Input | sisend | An answer supplied to the program |
| Output | väljund | A result displayed by the program |
| Function | funktsioon | A named action, such as `print()` |
| Argument | argument | A value passed to a function |
| Bug | viga | An error in code or behaviour |

## Mission: three-line briefing

**Task:** ask for a pilot name and destination, then print three briefing lines using both answers. Invent your own wording.

Build and run one milestone at a time:

1. Ask for the pilot and print a greeting.
2. Ask for the destination and print where the pilot is going.
3. Add a third line explaining the mission.

### Complete example

```python
pilot = input("Pilot name: ")
destination = input("Destination: ")

print("Welcome aboard,", pilot)
print("Your destination is", destination)
print(pilot, "must rescue the missing space hamster.")
```

With answers `Ada` and `Mars`, the briefing is:

```text
Welcome aboard, Ada
Your destination is Mars
Ada must rescue the missing space hamster.
```

The question prompts may appear too. Count **three briefing output lines after the questions**.

**Why it works:** two variables remember two answers. The quoted story text stays fixed, while the variables supply the changing details. `pilot` is used twice; printing it does not consume or erase its value.

**Check:** run again with `Liis Mari` and `Moon`. The new answers should appear in the same places, with no old `Ada` or `Mars` left in the briefing.

**If stuck:** start with the two input lines above and add only the greeting. Run it before adding the next output line.

## Upgrade: bring a companion

**Task:** add a third question for a companion. Keep the pilot and destination working, and add a sentence using the companion.

### Complete example

```python
pilot = input("Pilot name: ")
destination = input("Destination: ")
companion = input("Companion name: ")

print("Welcome aboard,", pilot)
print("Your destination is", destination)
print(pilot, "must rescue the missing space hamster.")
print("Your companion", companion, "will help with the rescue.")
```

With `Ada`, `Mars`, and `Bolt`:

```text
Welcome aboard, Ada
Your destination is Mars
Ada must rescue the missing space hamster.
Your companion Bolt will help with the rescue.
```

**Why it works:** a new changing detail gets its own variable. Each question is asked once, and each output uses the correct stored answer.

**Check:** run with `Ada` / `Mars` / `Bolt`, then `Ada` / `Mars` / `Pip`. Only the companion sentence should change.

## Challenge: two briefings

**Task:** ask for the pilot, destination and companion once. Produce an official notice and a silly news report, each with a title. Both versions must use all three answers.

### Complete example

```python
pilot = input("Pilot name: ")
destination = input("Destination: ")
companion = input("Companion name: ")

print("OFFICIAL BRIEFING")
print("Pilot:", pilot)
print("Travel to", destination, "with", companion)
print("Recover the missing space hamster.")

print()
print("BREAKING NEWS")
print(pilot, "and", companion, "are heading to", destination)
print("The hamster has requested extra snacks.")
```

With `Ada`, `Mars`, and `Bolt`:

```text
OFFICIAL BRIEFING
Pilot: Ada
Travel to Mars with Bolt
Recover the missing space hamster.

BREAKING NEWS
Ada and Bolt are heading to Mars
The hamster has requested extra snacks.
```

**Why it works:** both output sections read the same variables. There are exactly three `input()` calls. `print()` between the sections creates the blank line.

**Check:** ask a partner to choose three unexpected answers. Find all three values in each version. If the program asks six questions, remove the repeated input section and reuse the original variables.

## Boss: four-input story

**Task:** collect four answers before telling the story. Choose a fourth detail such as cargo, a villain or a lost object. Use every answer meaningfully and reuse at least one answer in more than one sentence.

### Complete example

```python
pilot = input("Pilot name: ")
destination = input("Destination: ")
companion = input("Companion name: ")
cargo = input("Strange cargo: ")

print("Welcome aboard,", pilot)
print("Your companion", companion, "has packed", cargo)
print("Together you must deliver it to", destination)
print(pilot, "suspects that", cargo, "may be alive.")
```

With `Ada`, `Mars`, `Bolt`, and `a singing potato`:

```text
Welcome aboard, Ada
Your companion Bolt has packed a singing potato
Together you must deliver it to Mars
Ada suspects that a singing potato may be alive.
```

**Why it works:** all four inputs happen before the story. Every answer is used, and both `pilot` and `cargo` appear in two sentences. No conditions or loops are needed.

**Check:** try `Sam` / `Underwater City` / `Pip` / `a glowing suitcase`. Can your partner identify the variable behind every changing detail?

**If stuck:** write four question labels and four sentences with blanks on paper. Give each blank the name of its variable, then turn the sentences into `print()` calls.

## Optional: control punctuation

Comma-separated arguments are enough for all the main tasks. They add spaces, so this produces `Welcome, Ada !`:

```python
pilot = "Ada"
print("Welcome,", pilot, "!")
```

For `Welcome, Ada!`, choose either of these alternatives:

```python
pilot = "Ada"
print("Welcome, " + pilot + "!")
print(f"Welcome, {pilot}!")
```

- **Concatenation:** `+` joins strings. Include spaces inside the quoted pieces where needed.
- **F-string:** the `f` before the quote makes `{pilot}` insert the variable's value. Without `f`, the braces and name print literally.

Because `input()` returns text, `"3" + "4"` gives `"34"`. The numeric expression `3 + 4` gives `7`. You do not need numeric conversion for this project.

## Debugging: find and fix a problem

**Expected result → actual result → inspect → change one thing → run again.**

Read the final error line. Check the indicated code line and the line above it. Error wording can vary between runners.

| What you see | What to check |
|---|---|
| `SyntaxError` | Matching quotes and parentheses; a comma between arguments; an unfinished previous line |
| `NameError` | Exact variable spelling and capitals; assignment before use |
| `IndentationError` | Remove accidental leading spaces from today's top-level statements |
| `TypeError` | Did you assign a value to `print` or `input`, or try to join incompatible values? |
| `EOFError` | Supply one input line for every `input()` call in the runner |
| Waiting with no error | Find the input prompt or panel and supply the next answer |
| Literal word `pilot` appears | Use `pilot`, not `"pilot"`, to print the value |
| Wrong answer appears in a line | Trace the variable back to the question that assigned it |
| Old output remains after editing | Rerun the edited file; check that you are running the correct file |
| Typed answer disappears | Look for a later assignment that replaces the answer |

### Common repairs

These are **incorrect snippets**, not a program to copy:

| Incorrect line | Correct line | Reason |
|---|---|---|
| `pilot = input("Pilot name: )` | `pilot = input("Pilot name: ")` | Close the string before closing the call |
| `print("Welcome,", Pilot)` | `print("Welcome,", pilot)` | Names are case-sensitive |
| `print("Welcome,", "pilot")` | `print("Welcome,", pilot)` | Read the variable instead of literal text |
| `print("Welcome," pilot)` | `print("Welcome,", pilot)` | Separate the arguments with a comma |

For **used too early**, put the assignment first:

```python
pilot = input("Pilot name: ")
print("Welcome,", pilot)
```

For **lost answer**, remove the line that overwrites it:

```python
pilot = input("Pilot name: ")
# Do not put pilot = "Captain Nobody" here.
print("Welcome,", pilot)
```

Test in a fresh run. A console with old variables can hide an assignment-order mistake.

### It runs, but is it correct?

A program can run without an error and still use the wrong variable or print an old name. Run twice with different answers. Predict which output lines should change before testing.

An empty answer may make the story awkward without crashing. Today's task does not require rejecting it. If an unrelated exercise judge rejects your creative briefing, check that you are using the project's runner rather than a judge expecting another exercise's exact output.

## Save your work

1. Save your latest code as a plain-text Python file: `I_W01_MissionBriefing_ID.py`. Replace `ID` with your school-approved identifier.
2. Upload or sync the file to your school cloud course folder. Sandbox code is not automatically saved.
3. Reopen the uploaded copy and find your latest change. Run that copy too if time allows.
4. Record one sentence: “I changed …” or “I fixed …”. Sign out of a shared computer.

**Before you finish, explain:**

- Which variable remembers one of your answers?
- Which output line uses it?
- What changes when you choose another destination?

A working Mission that you can explain and have saved is enough. You do not need to finish every extension.
