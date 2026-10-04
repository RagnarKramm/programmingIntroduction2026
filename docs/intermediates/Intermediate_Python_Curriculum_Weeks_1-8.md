# Intermediate Python Curriculum Weeks 1 to 8

Editable teacher planning document · Version 1.0 · 4 October 2026

This document plans the first eight lessons of a 32-lesson after-school programming course for 12 students aged 10–13. Lessons last 60 minutes and happen weekly. Students previously learned block programming with another teacher; their individual confidence with variables, conditions and loops is not yet known. We teach in Estonian, write code in English, and use short interactive programs to connect familiar ideas to Python.

By the end of this module, students should be able to build and test a small text game using input, output, variables, arithmetic, conditions, loops and simple functions. Lists, dictionaries, broader string processing and larger projects follow in later modules. No required homework or formal exams are planned. Weeks 4 and 8 provide evidence for adjusting the course.

## How to use and revise this document

- Rehearse each demo in the selected Python environment. Publish the Mission, Upgrade, Challenge and Boss tasks before class so students can continue independently.
- Every task should produce a visible result within a few minutes of a small code change. Pause explanations to let students run and modify code.
- After each meeting, fill in its teaching record and adjust future lessons. Keep completed plans as a record of what was taught.
- Suggested adjustment rule: if fewer than about 9 of 12 students finish the Mission and explain the key idea, reserve the first 10 minutes of the next lesson for a repair/remix and remove an extension. This is a planning signal, not a student pass mark.
- Lesson numbers are meetings, not calendar dates. Absence or cancellation should not force a student to skip a prerequisite; give them the recovery starter and one short catch-up task.

## Platform choice and persistence

**Current decision:** Trial Dodona for browser-based Python and selected exercises. Keep the lessons portable to PyCharm with school cloud storage. The specific school login, course access and saving process have not been tested yet. PythonAnywhere remains an alternative to investigate if the trial fails; this document does not assume accounts there exist.

Dodona's [Python sandbox documentation](https://docs.dodona.be/en/guides/students/scratchpad/) says that sandbox code is not saved automatically. Students must copy/finalize their code into the exercise editor and submit it to retain a submission. A browser runner and a persistent project workspace are different things. The sandbox is opened from a Python exercise; do not assume an independent cloud project editor is available.

### Preflight before Week 1

1. With school IT, verify the actual student authentication path and school approval for the selected platform. Microsoft 365 and Google Workspace login are described in the [teacher getting-started guide](https://docs.dodona.be/en/guides/teachers/getting-started/); school configuration may still need attention.
2. Obtain teacher access, choose an accessible Python exercise and test sandbox input, output, `import random`, the debugger and Stop. Test on a student terminal rather than only the teacher's computer.
3. Submit a small solution, log out of the terminal session, sign back in and retrieve its code from submission history. Separately test uploading and reopening a `.py` file in school cloud storage.
4. Decide the primary route for creative projects. If Dodona is used as a runner, use school cloud files as the authoritative project copy. If this is cumbersome, use the preinstalled PyCharm and the same cloud-save workflow from Week 1.
5. Put resources and starter text in the school learning platform. Keep teacher copies of the short examples and recovery starters in approved persistent storage.
6. Select any existing judged exercises before class. Check language, student access, prerequisites and exact input/output expectations. Custom automatic feedback requires configuring exercises and tests; these original creative tasks are not already published Dodona exercises.

### Two supported workflows

| Route | Build and run | Authoritative copy | End-of-lesson check |
|---|---|---|---|
| Dodona trial | Open a Python exercise's sandbox and run the creative program | `.py` file in school cloud storage; relevant judged work also submitted | Reopen the cloud file and check the latest code; confirm submission history for judged tasks |
| PyCharm fallback | Download/open `.py` locally, edit and run | Updated `.py` uploaded to school cloud storage | Reopen/download the uploaded file and check a distinctive change |

For the Dodona route, test how students will copy code into a plain-text `.py` file using the installed editor, then upload it. Do not submit an unrelated creative game to an exercise and interpret its failed judge tests as a programming failure. Use the sandbox to run it and the cloud file to save it. Judged tasks should be separate short exercises with matching specifications.

Use names such as `I_W06_GuessingGame_A7.py`, with a school-approved identifier. Pair ownership is explicit: one student drives, then both students save their own copy. Avoid two students overwriting the same cloud file. At the next meeting, retrieve the file before starting new work.

### The save ritual

At minute 57, stop adding features. Save the current code as a `.py` file, upload or sync it to the student's course folder, and reopen the remote copy to confirm the latest change. For relevant Dodona exercises, also finalize and submit, then check the code in submission history. Record the filename and one sentence about a change or bug. Sign out of the shared terminal.

During a cloud outage, the teacher must collect the latest code into an approved persistent location before students log out. If the code cannot be preserved, switch to the unplugged activity and record a design to build next time. Files left on the school computer disappear after logout.

## Teaching and feedback routines

Use **Mission → Upgrade → Challenge → Boss** every week. Everyone aims for the Mission; other levels are optional, and students need not finish every level in one meeting. Boss tasks combine taught concepts. A student who finishes quickly should solve a harder reasoning problem, not type a longer version of the same program.

In pairs, the driver types and the navigator predicts, reads the task and checks tests. Switch every 7–8 minutes. Six pairs fit this class when all 12 attend. Use pair work for debugging and tests, while requiring each student to explain a decision and save a copy.

Teach the help request: “I expected …; it did …; I tried …”. Read the last line of an error message and inspect the indicated line, then the line above it. Change one thing, run again, and compare. Treat wrong output as a bug even when no error is printed.

The examples use standard Python 3 syntax and avoid platform-specific packages. Numeric tasks initially assume valid integer input. This is a deliberate scope limit: do not silently require students to handle every invalid input before teaching validation or exceptions. Prompt text and creative output are flexible unless a selected judge exercise requires exact output.

## The eight lesson sequence

| Week | Project | Main idea | Evidence of progress |
|---|---|---|---|
| 1 | Mission briefing generator | Strings, variables, input and print | Traces an input into output |
| 2 | Space shop | Integer conversion and arithmetic | Predicts totals and remaining credits |
| 3 | Airlock security | Comparisons and if elif else | Tests all decision branches |
| 4 | Three-question quiz | Review and debugging | Explains scoring and repairs a bug |
| 5 | Dice arena | for, range and randomness | Predicts loop count and score updates |
| 6 | Guess the number | while and changing loop state | Explains when and why a loop stops |
| 7 | Reusable game tools | Functions, parameters and return | Calls a function with different inputs |
| 8 | Python game showcase | Plan, combine, test and refactor | Demonstrates a game and a tested improvement |

## Week 1 Mission briefing generator

**Learning objective:** Write and modify a short program using `print()`, `input()` and string variables. Connect “set name to …” in blocks to assignment in Python. Assess prior knowledge through predictions rather than a formal test.

**Hook:** Type a player's name and a planet; the program announces a ridiculous space mission. Ask where the typed text appears in the code.

**Prepare:** A working runner, cloud folder and this tiny starter. Keep a second version with one missing quote for debugging after students have a working result.

```python
name = input("Pilot name: ")
print("Welcome aboard,", name)
```

### The 60 minute plan

- **0–5:** Demo the personalised briefing. Ask students to identify an input and an output; note who remembers variables from blocks.
- **5–12:** Students run the starter, then change its message. Explain quotes, parentheses, assignment and commas in `print` through these changes. First win: their own name in the output.
- **12–30:** Build the Mission in stages: one input, two inputs, three-line briefing. Introduce `#` comments only as optional notes, not a separate exercise.
- **30–50:** Ladder work. At minute 40, pairs swap predicted output and test it. Circulate with one variable-tracing question per student.
- **50–57:** Repair the missing-quote example. Show that variable names are case-sensitive and strings need quotes.
- **57–60:** Save and reopen the cloud copy. Resolve access problems before extensions.

### Student challenge ladder

- **Mission:** Ask for a pilot name and destination, then print a three-line briefing using both answers. Success: changing either answer changes the correct part of the briefing.
- **Upgrade:** Ask for a companion's name and include it in another sentence.
- **Challenge:** Create two different briefings from the same three answers. Reuse variables rather than asking the same questions again.
- **Boss:** Build an interactive story introduction with four inputs and a coherent result. A partner should be able to identify which variable produced each personalised detail.

**Tests:** Inputs `Ada` and `Mars` should appear in their intended places. A name containing a space should be accepted as text. Try a different destination and verify that no old destination remains hard-coded.

**Likely mistakes and hints:** `Name` and `name` differ. `print(name)` prints a value; `print("name")` prints the word. A missing quote or parenthesis causes a syntax error. If `input` seems stuck, check the runner's input field rather than repeatedly rerunning.

**Support and backup:** Supply the first two lines and ask the student to add one input and one output. During an outage, one partner acts as the program, collecting input cards and inserting them into a printed briefing.

**Exit evidence:** Explain one assignment and predict the result of changing its input. Save `I_W01_MissionBriefing_ID.py`. Optional mission: invent a new briefing theme.

**Resources:** [Python built-in functions](https://docs.python.org/3/library/functions.html) for teacher reference on `input` and `print`; [Raspberry Pi About Me](https://projects.raspberrypi.org/en/projects/about-me) as an optional related creative project. The Raspberry Pi page needs JavaScript; rehearse access and disregard any legacy environment setup that conflicts with our tested workflow.

**Teaching record:** Date ___ · Mission completed ___/12 · Prior knowledge observed ___ · Access/save issues ___ · Week 2 adjustment ___

## Week 2 Space shop

**Learning objective:** Convert numeric input with `int()` and use variables and arithmetic to calculate a total and remaining balance. Prerequisite: input, output and assignment.

**Hook:** A shop has 20 credits and batteries cost 3 credits each. Ask what happens if the customer buys four. Then show the bug where text `"4"` is repeated rather than multiplied numerically.

**Prepare:** The starter below and one broken version without `int`. Introduce `+`, `-`, `*`, `/`, `//` and `%` with one small result each; the Mission uses only multiplication and subtraction. Explain that `//` and `%` extensions use nonnegative whole numbers here.

```python
credits = 20
price = 3
quantity = int(input("How many batteries? "))
total = price * quantity
remaining = credits - total
print("Total:", total)
print("Credits left:", remaining)
```

### The 60 minute plan

- **0–5:** Demo the space shop and predict a four-item purchase.
- **5–12:** Run with quantity 2, then 4. Compare `input()` text with `int(input())`. First win: a correct calculated bill.
- **12–30:** Mission wins: read quantity, calculate total, calculate balance. Students explain the values after each line.
- **30–50:** Ladder. Partners calculate an expected result on paper before running the same input.
- **50–57:** Fix the missing-conversion bug. Discuss a negative balance as useful information; automatic purchase rejection belongs to next week's conditions.
- **57–60:** Save and reopen.

### Student challenge ladder

- **Mission:** Produce the total and remaining credits for a battery purchase. Success: quantity 4 gives total 12 and balance 8; quantity 0 gives total 0 and balance 20.
- **Upgrade:** Add a second product with its own price and quantity. Print a combined total and balance.
- **Challenge:** For a nonnegative credit amount and positive price, calculate the maximum number of items using `//` and the unused credits using `%`. Test 20 credits at a price of 3: six items and two credits left.
- **Boss:** Create a supply planner for two products and a starting budget supplied by the user. Show both item totals and the remaining budget. Write three tests, including one overspend, and explain all calculations without adding conditions yet.

**Likely mistakes and hints:** Text multiplied by an integer repeats text; check conversion. Negative results are not necessarily a code bug. A string in a numeric calculation can cause `TypeError`. `int("two")` raises `ValueError`; today require integer input and explain that validation comes later.

**Support and backup:** Supply `int(input(...))` and the prices; ask the student to write only total and balance lines. For an outage, calculate bills using variable cards and compare a textual “4” with a numeric 4.

**Exit evidence:** Ask why conversion is needed and trace quantity 3. Save `I_W02_SpaceShop_ID.py`. Optional mission: invent prices and manually check one purchase.

**Resource:** [Python introduction](https://docs.python.org/3/tutorial/introduction.html), specifically numbers and text. Use it for reference and selected examples; it is not a child-facing worksheet to read in full.

**Teaching record:** Date ___ · Mission completed ___/12 · Conversion understood ___ · Arithmetic gaps ___ · Next adjustment ___

## Week 3 Airlock security

**Learning objective:** Compare values and select an outcome with `if`, `elif` and `else`. Use `and` and `or` when combining rules. Prerequisite: strings, integer conversion and variables.

**Hook:** Try to enter a space station with different clearance levels and passwords. Ask why one visitor gets a different message from another.

**Prepare:** This small two-branch starter. Later demonstrate `elif`, `>=`, `and` and `or` through one example each before students use them in extensions. Connect a block-programming if block to Python's colon and indented body.

```python
password = input("Password: ")
if password == "moon":
    print("Door opens")
else:
    print("Access denied")
```

### The 60 minute plan

- **0–5:** Demo the two outcomes and ask for predictions with `moon` and `sun`.
- **5–12:** Run the starter, change the password and trace the selected branch. First win: two correctly different outcomes. Explain `=` versus `==` and four-space indentation.
- **12–30:** Build the Mission; then demonstrate a three-outcome clearance check. Keep guided examples short and let students run after each branch is added.
- **30–50:** Ladder and paired tests covering each branch. Provide a small truth table for the combined condition.
- **50–57:** Bug hunt: an input integer compared with a text number, or a missing colon. Students explain their correction.
- **57–60:** Save with three test inputs noted in comments or the class record.

### Student challenge ladder

- **Mission:** Ask for a password and print exactly one appropriate access message. Success: correct and incorrect passwords take different branches.
- **Upgrade:** Ask for numeric clearance. Permit entry only when clearance is at least 2 **and** password is correct. Test all four combinations of sufficient/insufficient clearance and correct/incorrect password.
- **Challenge:** Make three outcomes: clearance below 2 gives “Training required”; otherwise a correct password opens the door; otherwise say “Wrong password”. Use `if/elif/else` and test each route.
- **Boss:** Design a station rule with a normal-entry route and an emergency route using `and`/`or`, with explicit messages. Write the rule in plain language first, then test cases that prove each route works and an unauthorised visitor is rejected. Use parentheses to show grouping when needed.

**Likely mistakes and hints:** `=` assigns while `==` compares. A branch without indentation cannot form its intended body. Several independent `if` statements may print several outcomes; choose an exclusive chain when only one outcome is intended. Check types before changing the comparison.

**Support and backup:** Use only the two-branch password starter, then add a clearance check with help. In an outage, students sort visitor cards into outcomes and turn the sorting rule into pseudocode.

**Exit evidence:** Trace one allowed and one denied entry. Save `I_W03_AirlockSecurity_ID.py`. Optional mission: invent a security policy and three visitor cards.

**Resource:** [Python control flow tutorial](https://docs.python.org/3/tutorial/controlflow.html), focusing on `if` statements. The airlock brief and test cases are original classroom tasks.

**Teaching record:** Date ___ · Mission completed ___/12 · Branch explanations ___ · Indentation/type issues ___ · Week 4 adjustment ___

## Week 4 Three question quiz

**Learning objective:** Combine inputs, variables, arithmetic and conditions in a complete small program; debug wrong results systematically. No new construct is required. Loops are intentionally not required yet.

**Hook:** Show a quiz that always ends with score 1. Ask what evidence would show that the scoring rule is wrong.

**Prepare:** Three questions with fixed expected answers and a bug version using `score = 1` after each correct answer. Include a second bug where `input()` text is compared with integer 7. Keep a one-question working starter.

```python
score = 0
answer = input("What is 3 + 4? ")
if answer == "7":
    score = score + 1
    print("Correct")
else:
    print("The answer is 7")
print("Score:", score)
```

### The 60 minute plan

- **0–5:** Run the faulty scoring demo. Predict the score for three correct answers.
- **5–12:** Model expected result, actual result, suspect line, one change and retest. Repair assignment versus score increment.
- **12–30:** In pairs, repair one supplied bug, switch roles, then each student builds their own three-question quiz.
- **30–50:** Ladder and teacher checkpoint conversations. Test an all-correct run and an all-wrong run before personalising further.
- **50–57:** Share one bug and its evidence. Ask each student one tracing question, including students who worked with a stronger partner.
- **57–60:** Save code and test notes.

### Student challenge ladder

- **Mission:** Ask three questions, give feedback for each, and show a final score from 0 to 3. Success: all correct gives 3, all wrong gives 0 and a mixed run gives the expected score.
- **Upgrade:** Give a final message for score 3, score 1–2, and score 0 using an exclusive branch chain.
- **Challenge:** Award different points for the questions and show the possible maximum. Update the tests so they reflect the new scoring rule.
- **Boss:** Design a quiz that recommends one of three fictional explorer roles using the score. A partner runs it and you explain the thresholds, including an exact-boundary score.

**Checkpoint questions:** What type does `input()` return? Why initialise score before questions? What is the difference between setting and increasing score? Which test disproved the bug? Record seen, with help, or independent for each student.

**Likely mistakes and hints:** Score is reset between questions; move initialisation before the first. Feedback is outside the intended branch; check indentation. A numeric answer can be compared as text (`"7"`) or converted and compared as a number (7), but not mixed accidentally. Copying a question can leave an old expected answer behind.

**Support and backup:** Supply three question prompts but leave the conditions and updates to the student. During an outage, trace a printed quiz with answer cards and score tokens.

**Exit evidence:** Save `I_W04_Quiz_ID.py` with three input/output test records. Optional mission: create one new question and its expected answer.

**Resources:** [Python input and print reference](https://docs.python.org/3/library/functions.html) and [control flow tutorial](https://docs.python.org/3/tutorial/controlflow.html). If using a judged exercise as a side task, choose and rehearse a relevant accessible input/condition exercise; the creative quiz itself uses manual tests.

**Teaching record:** Date ___ · Mission completed ___/12 · Independent tracing ___ · Concepts to revisit ___ · Week 5 changes ___

## Week 5 Dice arena

**Learning objective:** Use a `for` loop and `range()` for a fixed number of rounds, update an accumulator, and generate random integers. Prerequisite: variables, arithmetic and conditions.

**Hook:** Run a five-round dice duel. Ask whether we need five copies of the same code and why the result changes between runs.

**Prepare:** Starter below. Explain that `import random` makes the module available; `randint(1, 6)` includes both endpoints. The starter's `range(3)` runs three times. Show `round_number + 1` to label rounds without teaching lists.

```python
import random

total = 0
for round_number in range(3):
    roll = random.randint(1, 6)
    total = total + roll
    print("Round", round_number + 1, "roll", roll)
print("Total:", total)
```

### The 60 minute plan

- **0–5:** Demo the duel and ask which statements should repeat.
- **5–12:** Run the starter. Change three rounds to five and predict line count. First win: three visible rolls and their total.
- **12–30:** Build the Mission and verify the final print is outside the loop. Temporarily use `roll = 2` to test the total deterministically, then restore randomness.
- **30–50:** Ladder. Demonstrate a player and computer roll, with `if/elif/else` deciding a win, loss or draw. Partners trace score updates.
- **50–57:** Discuss how to test random programs: fixed temporary values for logic and repeated runs to check allowed ranges. A few runs cannot prove fairness.
- **57–60:** Save the version with randomness restored.

### Student challenge ladder

- **Mission:** Roll a die five times, print each round and print the total once at the end. Success: exactly five round lines; every value is 1–6; total matches their sum.
- **Upgrade:** Roll for player and computer each round; print win, loss or draw for all five rounds.
- **Challenge:** Keep separate win scores for the two players and announce the overall result after five rounds. Draws do not increase either win score.
- **Boss:** Give the user a choice of 3, 5 or 7 rounds. Reject other numeric choices with a message; use the loop only for an allowed value. Test a draw and each overall winning route with fixed temporary rolls, then restore `randint`.

**Likely mistakes and hints:** Score reset inside the loop never accumulates. Final result inside the loop prints repeatedly. `range(5)` yields 0–4, so display `round_number + 1`. Random results make a bug hard to reproduce; replace rolls temporarily with known numbers rather than repeatedly hoping for the right case.

**Support and backup:** Give the loop and random call; ask for accumulator and final output. In an outage, physically roll dice for three rounds and trace the printed starter's variables.

**Exit evidence:** Predict the total after five fixed rolls of 2. Save `I_W05_DiceArena_ID.py`. Optional mission: design a different dice scoring rule using known conditions.

**Resources:** [Python for and range reference](https://docs.python.org/3/tutorial/controlflow.html) and [random module](https://docs.python.org/3/library/random.html). These are teacher references for the original dice task.

**Teaching record:** Date ___ · Mission completed ___/12 · Loop-count predictions ___ · Accumulator problems ___ · Next adjustment ___

## Week 6 Guess the number

**Learning objective:** Use a `while` loop when the number of repetitions depends on a condition. Update the values that control the loop and explain its stopping rule. Prerequisite: integer input, comparisons, random numbers and fixed-count loops.

**Hook:** Guess a secret number until it is found. Ask whether the program knows how many guesses a player will need.

**Prepare:** Start with fixed secret 7 for testing, then switch to `random.randint(1, 10)`. Explain the starter's 0 as an initial value outside the valid guess range. Demonstrate Stop before showing an intentionally non-terminating loop.

```python
secret = 7
guess = 0
while guess != secret:
    guess = int(input("Guess 1 to 10: "))
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print("Correct")
```

### The 60 minute plan

- **0–5:** Demo wrong guesses followed by the correct one. Compare fixed rounds with “until correct”.
- **5–12:** Run the starter and trace `guess` before each loop check. First win: a wrong guess receives a hint and another prompt. Show how Stop handles a loop whose controlling value never changes.
- **12–30:** Mission wins: repeat input, correct hint, stop after success. Add randomness only after fixed-secret tests pass.
- **30–50:** Ladder. Before attempt limits, show the combined condition `guess != secret and attempts < 5` and increment attempts once per submitted guess.
- **50–57:** Bug hunt: input accidentally moved outside the loop. Ask what changes, and whether the stopping condition can become false.
- **57–60:** Save the game and note the tested sequence.

### Student challenge ladder

- **Mission:** Keep asking until the number is correct and print low/high/correct feedback. Success with secret 7: guesses 3, 9, 7 print low, high, correct, then stop.
- **Upgrade:** Count guesses and report how many were needed after success. Verify the sequence above counts 3.
- **Challenge:** Limit the game to five guesses. After the loop, print a win message if correct, otherwise reveal the secret. Success on guess five must still count as a win.
- **Boss:** Add numeric range validation: values outside 1–10 produce a warning and do not use an attempt. Valid wrong guesses still count. Use `if/else` inside the loop; exceptions for nonnumeric input are not required. Test both an out-of-range entry and success on the final allowed attempt.

**Likely mistakes and hints:** The input is outside the loop, so `guess` never changes. Attempts is never incremented. Using `or` instead of `and` may allow the loop to continue after success or exhaustion. Losing is announced even after a correct fifth guess; check success first after the loop. Validation still assumes integer input, as stated in the prompt.

**Support and backup:** Keep secret fixed and omit attempt limits. Trace a three-guess run using a table of guess and condition result. For an outage, play the game with one student as the computer and track its loop state.

**Exit evidence:** Explain which change makes the loop stop. Save `I_W06_GuessingGame_ID.py`. Optional mission: write a test sequence for success on the last allowed guess.

**Resources:** [Python control flow tutorial](https://docs.python.org/3/tutorial/controlflow.html) for conditions and general loop context; [Dodona sandbox guide](https://docs.dodona.be/en/guides/students/scratchpad/) for Stop and stepping through code. Use the guide as environment support, not a project-save guarantee.

**Teaching record:** Date ___ · Mission completed ___/12 · Can explain termination ___ · Off-by-one problems ___ · Week 7 adjustment ___

## Week 7 Reusable game tools

**Learning objective:** Define and call a function, pass values through parameters, and use a returned value. Distinguish printing a result from returning it for further calculation. Prerequisite: expressions, conditions and loops.

**Hook:** Show three copied damage calculations. Change the shield rule and ask how many places would need editing. Then show one function used three times.

**Prepare:** Starter below and a copied-code version for comparison. Keep `max()` out of the initial example; the condition uses familiar syntax. Explain definition, call, argument, parameter and return through the actual values.

```python
def damage_after_shield(damage, shield):
    remaining = damage - shield
    if remaining < 0:
        remaining = 0
    return remaining

hit = damage_after_shield(8, 3)
print("Damage:", hit)
```

### The 60 minute plan

- **0–5:** Compare copied calculations with one reusable rule.
- **5–12:** Run the starter and change the call to `(2, 5)`. First win: two different calls produce correct results. Explain that defining a function alone does not call it.
- **12–30:** Mission wins: define function, call with two inputs, store and print its returned result. Demonstrate replacing `return` with `print` to reveal why the caller no longer receives the numeric value it needs.
- **30–50:** Ladder. Before the Challenge, model a short `show_status(health)` function that prints a label, and call it inside a two-round loop.
- **50–57:** Trace one call, identifying the argument values, local variables and returned number. Avoid introducing global variables as a shortcut.
- **57–60:** Save both the functions and their calls.

### Student challenge ladder

- **Mission:** Write `damage_after_shield(damage, shield)` and use it for at least two calls. Success: `(8, 3)` returns 5; `(2, 5)` returns 0; `(4, 4)` returns 0.
- **Upgrade:** Ask the user for damage and shield values, call the function and print the returned result. Assume nonnegative integer input.
- **Challenge:** Create a three-round battle using random damage, the damage function and a `show_status(health)` function. Start health at 20 and show the health after each hit. Use a condition to keep displayed health at least 0.
- **Boss:** Put a known game rule from Week 5 or 6 into a function with parameters and a returned value. Explain the caller's job and the function's job. Test the function separately with three inputs before running the whole game.

**Likely mistakes and hints:** The definition is never called. A function prints but does not return a usable number, so the caller receives `None`; compare the two versions. Code tries to use `remaining` outside the function; use the returned value instead. Incorrect argument order changes the result; label the two values before calling.

**Support and backup:** Supply the function header and arithmetic line; the student adds the condition, return and two calls. During an outage, treat a function as a station: input cards go in and one result card returns to the caller.

**Exit evidence:** Explain why `return` is useful when health must be updated. Save `I_W07_GameTools_ID.py`. Optional mission: describe another rule that could become a function.

**Resource:** [Python defining functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions), using selected examples for teacher preparation. Our game-tool brief is an original task.

**Teaching record:** Date ___ · Mission completed ___/12 · Parameter/return explanations ___ · Scope confusion ___ · Week 8 changes ___

## Week 8 Python game showcase

**Learning objective:** Plan a small text game, combine taught constructs, test meaningful cases and explain one improvement. No new language construct is required.

**Hook:** Choose “Guessing game with limited attempts” or “Dice arena with a reusable scoring rule”. A student can propose a similarly sized text adventure if it uses only taught ideas and fits the minimum brief.

**Prepare:** Minimal working starters from Weeks 5 and 6 and a blank planning outline. Students can extend their own work; rebuilding from a blank file is optional. Provide test headings: input, expected result, actual result, change needed.

### The 60 minute plan

- **0–5:** Show project choices and the minimum playable brief.
- **5–12:** Students write three rules, choose a starter and plan one small feature. Model how to choose a boundary test. First win: starter runs with one student-made change.
- **12–30:** Build the Mission. Circulate to verify every student can trace a state update, even if working in pairs.
- **30–45:** Ladder and paired tests. Each student owns a test record; reserve five minutes for repairing one issue.
- **45–54:** Three short demos, while other students playtest in pairs. Present a feature and evidence of a repair, not a long code reading.
- **54–57:** Individual reflection and next-module interest survey.
- **57–60:** Save code and test notes, then reopen the remote copy.

### Student challenge ladder

- **Mission:** Finish a game with input, a changing score or attempt value, at least one condition, a loop and a clear ending. Success: a partner can play without coaching and the final result matches the stated rules.
- **Upgrade:** Extract one repeated or clearly separate rule into a named function. Call it from the game and explain its parameter or returned value. Students who still need function support may do this with a provided header.
- **Challenge:** Create three meaningful tests, including a success, a failure or draw, and a boundary case. Repair one issue and rerun the affected test.
- **Boss:** Add a user-chosen difficulty setting that changes a taught parameter such as allowed attempts, number range or round count. Compare both settings using test evidence and avoid new packages or data structures.

**Suggested acceptance tests:** For guessing: correct first guess, all allowed guesses wrong, correct final allowed guess. For dice: player win, computer win, draw using temporary fixed rolls. Restore random rolls afterwards and check their permitted ranges. For an alternative adventure, test every offered choice and at least one invalid text choice with a known `else` response.

**Checkpoint questions:** What enters the program? Which value changes each round? Why does the loop stop? What job does the function do, if included? What did you test, and what changed? If a student omits a function, assess their Week 7 function example separately rather than assuming mastery.

**Likely mistakes and hints:** A large new story consumes the build time; finish three rules before adding content. Moving code into a function can lose access to a value; pass it as a parameter or return it. Test data can remain hard-coded accidentally; check the delivered version after restoring randomness.

**Support and backup:** Use a tested starter and require one independently explained rule change plus three tests. If most students need loop reinforcement, use the whole session as a guessing-game repair workshop and postpone optional features. In an outage, write pseudocode and trace the three tests on paper.

**Exit evidence:** Save `I_W08_Showcase_ID.py` and its test record. Optional mission: write a proposal for one next-module feature.

**Resources:** [Python control flow tutorial](https://docs.python.org/3/tutorial/controlflow.html), [random module reference](https://docs.python.org/3/library/random.html) and [Raspberry Pi Rock Paper Scissors](https://projects.raspberrypi.org/en/projects/rock-paper-scissors) as a related later project. The Raspberry Pi page requires JavaScript; its project can inspire future games, but it is not a required new build in this showcase.

**Teaching record:** Date ___ · Playable projects ___/12 · Independent explanations ___ · Concepts to reinforce ___ · Student interests ___ · Week 9 priority ___

## Progress tracking and future decisions

Use **S** for seen, **H** for can use with help, **I** for independent, and a dash for not yet observed. Add a date and one concrete action or explanation. Duplicate the rows for all 12 students. Pair success alone does not establish independent understanding.

| Student ID | Input and output | Types and arithmetic | Conditions | for loops | while loops | Functions | Debugging and tests | Cloud saving | Evidence and next step |
|---|---|---|---|---|---|---|---|---|---|
| ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ |
| ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ |
| ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ |

At Week 4, decide whether students need more type/condition work before loops. At Week 8:

- If loops remain uncertain, use another short guessing or round-based game and trace its state before adding lists.
- If parameters and return remain uncertain, begin with tiny reusable scoring functions and separate tests.
- If the core constructs are secure, Weeks 9–16 can introduce lists, string methods, dictionaries and decomposition through quizzes, simulations and text adventures.
- Later modules can develop modules, file/data concepts in the tested environment, larger teamwork projects and an independent showcase. Basic object-oriented ideas remain optional and depend on readiness.
- A saving failure is a workflow issue to repair before multiweek projects, not a reason to blame the student.

## Online exercise selection guide

The original projects above are deliberately creative and use manual acceptance tests. Existing online tasks supplement them; automatic judging is useful for short precise problems, while a teacher or partner evaluates open-ended game choices.

When adding a Dodona exercise, record the exact URL here only after reviewing it. Choose a task of roughly 5–10 minutes, with a clear English or translated statement, matching prerequisites and a quick visible success. Prefer deterministic inputs and outputs while students are learning syntax. Read [Solving Exercises](https://docs.dodona.be/en/guides/students/exercises/) to rehearse the student submission route.

| Week | Desired supplement | Selected exercise URL | Access and test checked |
|---|---|---|---|
| 1–2 | Input, output, integer calculation | ___ | ___ |
| 3–4 | Two or three decision outcomes | ___ | ___ |
| 5 | Fixed-count total | ___ | ___ |
| 6 | Condition-controlled repetition | ___ | ___ |
| 7 | Function with parameters and return | ___ | ___ |

This selection is optional preparation, not a dependency for teaching the supplied lessons. The document does not claim that particular custom exercises or a Dodona teacher course have already been created.

## Estonian vocabulary support

| English term | Estonian teaching term |
|---|---|
| input and output | sisend ja väljund |
| variable | muutuja |
| string | sõne |
| integer | täisarv |
| condition | tingimus |
| loop | tsükkel |
| function | funktsioon |
| parameter | parameeter |
| return value | tagastusväärtus |
| debugging | vigade leidmine ja parandamine |

Keep Python keywords in English. Translate task prose as needed, but do not translate code identifiers automatically. Students can explain their reasoning in Estonian while using the English keyword to identify the relevant construct.

## Revision log

| Version and date | Lesson or decision | What changed | Evidence or reason |
|---|---|---|---|
| 1.0 · 4 October 2026 | First eight lessons | Initial plan with Dodona trial and explicit cloud backups | Agreed constraints and verified sandbox saving limitation |
| ___ | ___ | ___ | ___ |
| ___ | ___ | ___ | ___ |

## Resource notes

Official Python, Dodona and Raspberry Pi links were checked during preparation on 4 October 2026 in the teacher's timezone. Raspberry Pi project pages require JavaScript and should be rehearsed before assigning them; their full step-by-step contents were not inspected in this preparation. Core tasks here are self-contained original lesson plans. Timings, challenge levels and adjustment thresholds are teaching recommendations. Platform login and saving must still be tested in the school environment before the course begins.
