# Intermediate Python Week 2 Teacher Reference

Editable lesson companion · Version 1.0 · 13 October 2026

For 12 students aged 10–13, a 60-minute lesson taught in Estonian with English code. Companion to the revised [Weeks 1–8 curriculum](Intermediate_Python_Curriculum_Weeks_1-8.md).

**Today's project:** An interactive greeting. **Minimum success:** Reopen/run a script, read one keyboard name, pass it to a function and explain the greeting using two test names. Optional tasks deepen the same ideas; arithmetic is Week 3.

## Starting point from Lesson 1

The teacher reports that students opened their first script and edited the initial Hello World function to say their name. They encountered function creation, calls, function inputs and variable assignment. The original Week 1 briefing was not reached. Individual independence, keyboard input and saving success have not been confirmed. Check these through small actions rather than treating exposure as mastery.

Use the actual Lesson 1 file where available. The model below represents the reported concepts; it does not reproduce an unseen starter. Keep familiar function/variable names initially if students' files differ.

```python
def greet(name):
    print("Hello,", name)

player_name = "Ada"
greet(player_name)
```

## At a glance

| Need | Quick action |
|---|---|
| First win | Reopen file, change the stored name, run and see it |
| Core new idea | Keyboard `input()` supplies text instead of a fixed quoted name |
| Function vocabulary | Definition gives the action a name; call runs it; argument supplies a value; parameter receives it |
| Mission | One question, one greeting function, one call, two tested names |
| Scope | One parameter first; two parameters only after a demonstration |
| Main checks | Definition before call, colon, indentation, quotes and consistent spelling |
| Exit evidence | Student traces answer → variable → argument → parameter → printed name |
| Save | `I_W02_InteractiveGreeting_ID.py`; reopen the saved copy |

## Preparation

1. Retrieve the actual Lesson 1 starter and check whether students can reopen their saved versions. Record the working environment; do not change it just to match earlier platform suggestions.
2. Test keyboard input in that runner. In a terminal, answer the prompt and press Enter. A runner with an input panel may require answers supplied ahead of time, one per line.
3. Prepare a fixed-name recovery starter and an interactive copy. Keep bug examples separate from working starters.
4. Confirm the school-approved save destination and how to reopen it. Keep teacher backup copies for students who cannot retrieve their file.
5. Put the Mission and optional briefs somewhere students can see them. Teach task prose in Estonian; leave code keywords in English.

## The 60-minute lesson

| Time | Teacher action | Student action / evidence |
|---|---|---|
| 0–10 | Help reopen Lesson 1; show which file is running | Run, change fixed name, run again; first visible win |
| 10–20 | Trace the fixed-name model; distinguish definition and call | Identify both; predict a second call with another name |
| 20–30 | Replace fixed assignment with one `input()` line; run after the change | Type an answer and locate it in output; explain where it was stored |
| 30–45 | Release Mission; offer extensions only after the core trace works | Complete one-input greeting, then choose an optional task |
| 45–52 | Pair test with two different names; show one small bug | Predict, run, compare and repair one issue |
| 52–57 | Ask each student for a short trace; record independent/support evidence | Point to definition, call, variable and parameter |
| 57–60 | Stop features and guide saving/reopening | Preserve latest code and find a distinctive change in saved copy |

Pairs switch driver/navigator about every 7–8 minutes; each student explains and saves a copy. If access takes too long, remove extensions. If the fixed-name trace remains unclear at minute 20, spend the next block on two calls, provide the input line with help and reduce the Mission to one successful run. Record that support; protect the save time. If saving needs more than three minutes in the actual environment, begin it earlier.

## Python explanations for live teaching

### Creating versus calling a function

```python
def greet(name):
    print("Hello,", name)

greet("Ada")
greet("Sam")
```

`def` creates the function. It does not run the body immediately. Each `greet(...)` call runs that body with the supplied value. Here output is `Hello, Ada`, then `Hello, Sam`. The definition ends with a colon. Use four spaces for the body; the calls are outside the definition at the left edge. Avoid putting a call to `greet` inside its own body.

The parameter `name` is a local name for the supplied value during the call. Use it inside the body; outside, use the caller's `player_name` variable. The caller and parameter do not need the same spelling. Avoid a full scope lecture; trace one concrete value.

### A function input and keyboard input are different steps

```python
def greet(name):
    print("Hello,", name)

player_name = input("Your name: ")
greet(player_name)
```

`input()` asks for keyboard text and returns that answer. Assignment stores it under `player_name`. The call passes that stored value as an argument to `greet`; `name` receives it as its parameter, then `print` displays it. The greeting function itself does not ask a question.

| Step | With keyboard answer `Liis Mari` |
|---|---|
| Define `greet` | Function available; no greeting printed yet |
| `input(...)` | Prompt shown, answer read as text |
| Assignment | `player_name` refers to `"Liis Mari"` |
| `greet(player_name)` | That value is passed; local `name` refers to it |
| Body runs | `Hello, Liis Mari` prints |

Do not require a custom `return` today. `input` returns text, while this greeting function's job is to print. Adding `result = greet(player_name)` is unnecessary for this project.

### Quotes, variables and reassignment

`greet("Ada")` passes fixed text. `greet(player_name)` reads a variable. `greet("player_name")` passes the literal word `player_name`. Commas in `print("Hello,", name)` separate arguments and add a space by default.

```python
player_name = "Ada"
greet(player_name)
player_name = "Sam"
greet(player_name)
```

The first greeting stays Ada; the later assignment affects the second call. A fresh script runs from the start every time; editor changes need a new run. Do not name a variable `input` or `print`.

## Student task ladder and teacher solutions

### Warm-up — recover the greeting

**About 10 minutes.** Open your Lesson 1 file, run it, change the fixed name and run again. Point to the definition and the call. If your file is unavailable, use the recovery starter above. **Check:** The latest name appears; you can identify the running file. **Hint:** Changing the editor does not change earlier output.

### Mission — ask for a name

**About 12–15 minutes after the demo.** Keep a function with one parameter. Ask the player for a name, store the answer and call the function with it. Change the greeting message to your own wording. Do not type your name directly into the greeting body.

**Success:** One question per run; the typed answer appears in the greeting; the student explains the value's path. **Tests:** Run with `Ada`, then `Liis Mari`; no old name should remain. **Hint ladder:** Which value changes? → Replace the fixed-name assignment with `input(...)`. → Supply `player_name = input("Your name: ")` and ask the student to write the call.

**Reference solution:** The interactive example in the explanation section is complete. Output wording is flexible.

### Upgrade — greet two people

**About 4–6 minutes.** Ask separately for two names, store each in its own variable and call the same function once for each. **Check:** Ada/Sam gives two greetings in that order; change only the second answer and predict which line changes.

```python
def greet(name):
    print("Welcome aboard,", name)

first_name = input("First pilot: ")
second_name = input("Second pilot: ")
greet(first_name)
greet(second_name)
```

**Hint:** Reuse the definition; write another call. No second greeting function is needed.

### Challenge — give the pilot a destination

**About 6–10 minutes, after a two-parameter demo.** Define `briefing(name, destination)`. Ask for both values and pass them in matching order. Print two lines from the function.

```python
def briefing(name, destination):
    print("Pilot:", name)
    print("Travel to", destination)

pilot = input("Pilot name: ")
planet = input("Destination: ")
briefing(pilot, planet)
```

**Check:** Ada/Mars, then Sam/Moon; correct value under each label. **Hint:** Two parameter names need two arguments. Label the argument order before running.

### Boss — two travellers, one reusable briefing

**About 8–12 minutes; completion is optional.** Reuse the Challenge definition for two travellers. Ask for each name and destination separately. Predict the output before running. Change just one destination and explain why only its travel line changes.

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

**Check:** Ada/Mars/Sam/Moon produces four briefing lines with correct pairings. The function is defined once. Four inputs are required only for this optional task.

## Extra practice menu

Choose one when the Mission works; these use existing syntax.

- **Two calls, one edit · 3–5 minutes:** Change the greeting body once. Predict how both calls change. Explain why copying the whole function is unnecessary.
- **Literal or variable? · 3–5 minutes:** Predict `greet("player_name")` versus `greet(player_name)`, test and explain. Restore the desired version.
- **Rename safely · 4–6 minutes:** Rename the caller's variable to `pilot_name` and update its uses. Leave the function's parameter as `name`; explain why it still works.
- **Reassignment detective · 4–6 minutes:** Use the two-assignment example above. Predict each line before running and explain why earlier output stays unchanged.
- **One-change tester · 4–6 minutes:** Keep a test table of answer, expected greeting and actual greeting. Include a name with spaces or Estonian characters. Empty names may produce awkward output; validation is not required.
- **Definition only · 3–5 minutes:** Temporarily remove the call. Predict the absence of a greeting, run, then restore the call.
- **Theme remix · 4–6 minutes:** Make the function welcome a robot or fantasy hero. Keep one input and one parameter; a partner supplies an unexpected name.

## Debugging and repair answers

Use: expected result → actual result → read final error line → inspect indicated line and the line above → change one thing → rerun. Give one bug at a time.

| Symptom | Likely cause | First check / repair |
|---|---|---|
| Nothing prints | Definition never called | Add a call after the definition |
| Name appears as `player_name` | Quoted variable passed | Remove quotes in the argument |
| `NameError` | Misspelling, call before definition, or local parameter used outside | Compare names and order; use caller variable outside |
| `TypeError` about argument count | Call does not match parameter count | One argument for `greet`, two for `briefing` |
| `SyntaxError` | Missing colon/quote/parenthesis | Inspect punctuation and previous line |
| `IndentationError` | Function body not indented consistently | Four spaces inside; caller at left edge |
| Repeated calls until `RecursionError` | Call accidentally inside its own function | Move call outside definition |
| Waiting / `EOFError` | Missing input in runner | Find prompt or provide enough input lines |
| Old name after edit | Wrong file or no rerun | Change a visible message and run edited file |

**Bug A — quoted variable:** Given `player_name = "Ada"` and `greet("player_name")`, output is `Hello, player_name`. Repair to `greet(player_name)`.

**Bug B — definition without call:** A script containing only `def greet(name):` and its indented print body produces no greeting. Add `greet("Ada")` at the left edge after the body.

**Bug C — missing value:** `greet()` with the one-parameter definition raises `TypeError`. Supply a name argument; do not remove the parameter to hide the mismatch.

**Bug D — hard-coded body:** `def greet(name):` with `print("Hello, Ada")` ignores the supplied name. Repair body to `print("Hello,", name)` and test two calls.

**Bug E — wrong spelling:** `player_name = input("Your name: ")` followed by `greet(Player_name)` raises `NameError`. Use `player_name` consistently.

## Support and outage plan

If overloaded, keep the fixed-name greeting, supply the definition and ask the student to add/change one call. Then provide the input assignment and trace it together. A copied working program needs a student-made change and explanation before extensions.

For an outage, one student reads the input prompt, another stores the answer on a variable card, and a third is the greeting function. Pass the value card into its parameter slot and read the template. Reuse the station with another value. Record a paper design and preserve existing code in approved storage if possible.

## Saving, exit check and next lesson decision

Save the latest plain-text `.py` file as `I_W02_InteractiveGreeting_ID.py` in the school-approved course folder; replace ID with the approved identifier. Reopen the saved copy and locate the personalised latest message. Run that copy if time permits. Each student saves their own copy and signs out of shared terminals. If using the earlier Dodona sandbox route, use the established cloud-file procedure; an unrelated creative script is not a solution submission for an arbitrary judged exercise.

Ask individually: Where is the function created? Which line runs it? Where is the keyboard answer stored? How does that value reach the printed greeting? What changes on a second run with another name? Accept explanations in Estonian.

Date ___ · Present ___/12 · Mission working ___/12 · Independent value trace ___/12

- Needed help reopening/running: ___
- Definition/call or parameter/argument confusion: ___
- Keyboard input versus function input confusion: ___
- Quote/indentation/spelling problems: ___
- Latest file saved and reopened: ___/12 · Workflow issues: ___
- Extensions reached and useful observations: ___
- First 10 minutes of Week 3: ___

If fewer than about 9 of 12 finish the Mission and explain its value flow, begin Week 3 with greeting repair and reduce shop extensions. For students still needing input support, use fixed numeric quantity first, then supply the conversion lines. This is a pacing signal, not a grade. No required homework; optional practice is to predict two greeting calls on paper.

## Revision log

| Version | Date | Change |
|---|---|---|
| 1.0 | 13 October 2026 | Lesson 2 planned from actual Lesson 1 progress; consolidates functions/variables and introduces one keyboard input |
