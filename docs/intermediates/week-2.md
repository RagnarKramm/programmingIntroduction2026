---
title: "Intermediate Python · Week 2"
nav_order: 5
description: "Pass a keyboard answer into a reusable greeting function and trace its value."
---

# Week 2: Interactive greeting

Continue the greeting function you explored in Lesson 1. Make it welcome a name typed by the player, rather than a name fixed in the code.

**Your main goal:** ask one question, store the answer, pass it to a greeting function, and explain the result using two test names. Extensions are optional. You do not need to have completed Week 1's mission briefing.

## Jump to the help you need

- [Starter: recover your greeting](#starter-recover-your-greeting)
- [Theory: follow the answer](#theory-follow-the-answer)
- [Mission: ask for a name](#mission-ask-for-a-name)
- [Upgrade: greet two people](#upgrade-greet-two-people)
- [Challenge: give the pilot a destination](#challenge-give-the-pilot-a-destination)
- [Boss: two travellers, one briefing](#boss-two-travellers-one-briefing)
- [Extra practice](#extra-practice)
- [Debugging](#debugging)
- [Save your work](#save-your-work)

## Starter: recover your greeting

Open your Lesson 1 file in the classroom Python editor and run it. Change its fixed name and run again. Keep familiar function and variable names if your starter differs from this example.

If your file is unavailable, ask for help and use this recovery starter:

```python
def greet(name):
    print("Hello,", name)

player_name = "Ada"
greet(player_name)
```

Output:

```text
Hello, Ada
```

**Try it:** replace `"Ada"` with `"Sam"`. Predict the greeting, then run the edited file. Point to the function definition and the line that calls it.

## Theory: follow the answer

### Define an action, then call it

```python
def greet(name):
    print("Hello,", name)

greet("Ada")
greet("Sam")
```

Output:

```text
Hello, Ada
Hello, Sam
```

`def` defines a function: a named action you can reuse. Defining it does not print a greeting. Each `greet(...)` **call** runs the indented body once.

The definition ends with a colon. Use four spaces before its body. Put the calls at the left edge, after the definition. A call inside its own function would keep calling itself instead of running just once.

`name` is a **parameter**: a local name that receives the supplied value during a call. `"Ada"` is an **argument**: the value supplied by that call. Two calls reuse one definition with different values.

### Keyboard input and function input

```python
def greet(name):
    print("Hello,", name)

player_name = input("Your name: ")
greet(player_name)
```

`input()` displays a question and returns the player's answer as text. `=` assigns that answer to `player_name`. The function call then supplies the stored value to `greet`.

| Step | If the player types `Liis Mari` |
|---|---|
| Define `greet` | The function is available; no greeting yet |
| Run `input(...)` | Ask the question and read the answer |
| Assign to `player_name` | Store the text `"Liis Mari"` |
| Call `greet(player_name)` | Pass that value into parameter `name` |
| Run the body | Print `Hello, Liis Mari` |

The greeting function does not ask the question itself. Keyboard input collects the answer; the argument passes that answer into a function. The caller's variable and the parameter may have different names. Use `name` inside the body and `player_name` outside it.

In a terminal, type your answer and press Enter. If your runner has an input panel, provide one answer per line in question order. After editing, run again; each fresh run starts from the beginning and asks again.

### Text, quotes and variables

| Call | What it supplies |
|---|---|
| `greet("Ada")` | Fixed text `Ada` |
| `greet(player_name)` | The value stored in the variable |
| `greet("player_name")` | The literal text `player_name` |

Quotes mark a **string**, or text value. Use matching straight quotes. Names are case-sensitive: `player_name` and `Player_name` differ. Avoid using `input` or `print` as variable names.

`print("Hello,", name)` separates its arguments with a space and ends the output line. A later assignment changes what a variable stores for future calls; it does not change output already printed.

Today's function prints a greeting. You do not need to add `return` or store the result of `greet(...)` in another variable.

| English | Estonian | Meaning today |
|---|---|---|
| Function | funktsioon | A reusable named action |
| Definition | definitsioon / funktsiooni loomine | Code that defines the action |
| Call | väljakutse | Run the action |
| Parameter | parameeter | A name receiving a supplied value |
| Argument | argument | A value supplied in a call |
| Variable | muutuja | A name storing a value |
| String | sõne | A text value |
| Input / output | sisend / väljund | An answer supplied / a result displayed |

## Mission: ask for a name

**Task:** keep a function with one parameter. Ask for a name, store the answer and call the function with it. Personalise the fixed greeting wording; use the parameter for the changing name.

Build one milestone at a time: run fixed-name greeting → replace the fixed assignment with `input()` → run and trace the typed answer.

### Complete example

```python
def greet(name):
    print("Welcome aboard,", name)

player_name = input("Your name: ")
greet(player_name)
```

With answer `Ada`, the greeting is:

```text
Welcome aboard, Ada
```

The question prompt may appear too. Count one question and one greeting per run.

**Test:** run with `Ada`, then in a fresh run with `Liis Mari`. Each greeting must use the latest answer, with no old name left in it. Explain answer → `player_name` → argument → `name` → printed greeting.

**If stuck:** first get the recovery starter working. Replace only its fixed-name assignment with the input line. Keep the call after that assignment.

## Upgrade: greet two people

**Task:** ask separately for two names and call the same function once for each. Define it only once.

```python
def greet(name):
    print("Welcome aboard,", name)

first_name = input("First pilot: ")
second_name = input("Second pilot: ")
greet(first_name)
greet(second_name)
```

With answers `Ada` and `Sam`:

```text
Welcome aboard, Ada
Welcome aboard, Sam
```

**Why it works:** separate variables preserve both answers; each call passes one value into the same parameter.

**Test:** keep the first answer and change only the second. Predict which greeting changes. Then edit the greeting wording in the function once and check that both greetings use the new wording.

## Challenge: give the pilot a destination

Try this after your teacher demonstrates two parameters.

**Task:** define `briefing(name, destination)`, ask for both values and print two lines from the function. Match argument order to parameter order.

```python
def briefing(name, destination):
    print("Pilot:", name)
    print("Travel to", destination)

pilot = input("Pilot name: ")
planet = input("Destination: ")
briefing(pilot, planet)
```

With `Ada` and `Mars`:

```text
Pilot: Ada
Travel to Mars
```

**Why it works:** first argument `pilot` supplies `name`; second argument `planet` supplies `destination`. Both print lines belong inside the function.

**Test:** run with Ada/Mars, then Sam/Moon. Check each value under its correct label. If the destination appears as the pilot, inspect argument order.

## Boss: two travellers, one briefing

**Task:** reuse one two-parameter function for two travellers. Collect each name and destination separately. Predict all four briefing lines before running.

```python
def briefing(name, destination):
    print("Pilot:", name)
    print("Travel to", destination)

first_pilot = input("First pilot: ")
first_planet = input("First destination: ")
second_pilot = input("Second pilot: ")
second_planet = input("Second destination: ")
briefing(first_pilot, first_planet)
briefing(second_pilot, second_planet)
```

With Ada/Mars/Sam/Moon:

```text
Pilot: Ada
Travel to Mars
Pilot: Sam
Travel to Moon
```

**Test:** change only the second destination. Only the second travel line should change. Explain which argument supplied it. Four questions belong to this optional task; the Mission needs only one.

## Extra practice

Choose one after the Mission works:

- **Literal or variable?** Predict `greet("player_name")` versus `greet(player_name)`, test, then restore the version using the answer.
- **Rename safely:** change the caller variable to `pilot_name` and update its uses. Keep parameter `name`; explain why it still works.
- **Definition only:** in a copy, remove the call. Predict the output, run, then restore the call.
- **Theme remix:** welcome a robot or fantasy hero. Keep one input and one parameter; ask a partner for an unexpected name.
- **One-change tester:** include a name with spaces or Estonian characters. Empty answers may make an awkward greeting; input validation is not required today.

Record a prediction before a test:

| Answer | Expected greeting | Actual greeting |
|---|---|---|
| Ada | ___ | ___ |
| Liis Mari | ___ | ___ |

## Debugging

**Expected result → actual result → inspect → change one thing → rerun.** Read the final error line, then check the indicated line and the line above it.

| Symptom | First check or repair |
|---|---|
| Nothing prints | Call the function after defining it |
| Greeting says `player_name` | Remove quotes around the variable in the call |
| Greeting always says Ada | Print the parameter rather than a fixed name in the body |
| `NameError` | Check spelling, capitals and definition/assignment before use; use caller variable outside the function |
| `TypeError` about arguments | Supply one argument to `greet`, two to `briefing` |
| `SyntaxError` | Check colon, matching quotes and parentheses |
| `IndentationError` | Use four spaces inside the body and put outside calls at the left edge |
| Calls repeat until `RecursionError` | Move the call outside its own function body |
| Waiting or `EOFError` | Find the prompt or provide enough input lines in the runner |
| Old name after an edit | Run the edited file again; check the file you are running |

### Repair a quoted variable

This call is incorrect if you want the stored name:

```python
def greet(name):
    print("Hello,", name)

player_name = "Ada"
greet("player_name")
```

It prints `Hello, player_name`. Change only the last line to:

```python
greet(player_name)
```

Now it prints `Hello, Ada`. Explain why removing quotes changes the supplied value.

## Save your work

1. Save the latest plain-text Python file as `I_W02_InteractiveGreeting_ID.py`, replacing `ID` with your approved identifier.
2. Upload or sync it to your school-approved course folder using the classroom workflow. Sandbox code is not automatically preserved.
3. Reopen the saved copy and find your latest personalised greeting. Run that copy if time allows.
4. Each partner keeps and checks their own copy. Record “I changed …” or “I fixed …” and sign out of shared computers.

If using a judged exercise platform, run this creative project in the teacher's demonstrated runner; an unrelated exercise may expect different exact output.

**Before you finish, point to:** the definition, the call, the variable storing keyboard input, and the parameter receiving its value. Explain what changes when you run with another name. You may explain in Estonian.

A working Mission that you can explain and have saved is enough. Next lesson uses numbers and calculations; today's answers stay as text.
