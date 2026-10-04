# Intermediate Python Week 1 Teacher Reference

Editable lesson companion · Version 1.0 · 4 October 2026

For the teacher of 12 students aged 10–13, teaching in Estonian with English code and materials. This reference expands Week 1 of **Intermediate Python Curriculum Weeks 1 to 8**. Use the first sections to answer questions during class, the exercise briefs to direct students, and the answer notes to give hints without immediately supplying a solution.

**Today’s project:** Mission briefing generator. **Essential learning:** use `print()`, `input()` and string variables to turn a player's answers into personalised output. Success means a student can build a small working briefing, change an answer and explain where that answer appears. Extra tasks are choices, not a completion checklist or a ranking of students.

## At a glance

| Need | Quick answer or action |
|---|---|
| First working program | `name = input("Pilot name: ")` followed by `print("Welcome aboard,", name)` |
| Minimum finished project | Two inputs, three output lines, both answers used |
| Four lesson levels | Mission: briefing; Upgrade: companion; Challenge: two briefings from the same answers; Boss: four-input story |
| Main debugging checks | Matching quotes and parentheses; correct variable spelling; assignment before use |
| Common confusion | `print(name)` prints the stored value; `print("name")` prints the literal word |
| Evidence of understanding | Student points to an input, its variable and the output that uses it |
| Saving | Save `I_W01_MissionBriefing_ID.py` to school cloud storage and reopen the uploaded copy |
| Time limit | Stop features at minute 57; protect saving time even if tasks are unfinished |

## Python essentials for this lesson

### Running code and reading the screen

Python executes statements in order. A program is instructions; the editor is where we write them; the output area is where we see results. Changing the editor does not change an earlier result: run the program again. In an ordinary script, typing a variable or expression alone does not display it; use `print()`.

The interactive Python prompt sometimes shows `>>>`. This is a prompt, not code to copy into a `.py` file. Our examples are scripts and intentionally omit it. A `.py` file is a plain-text Python program, not a Word document.

For this lesson, put each statement on its own line, starting at the left edge. Python uses indentation to group code in later lessons; accidentally indenting a top-level line can produce `IndentationError`. No semicolons are needed.

### Output with print

```python
print("Mission control online")
print("Pilot:", "Ada")
print()
print("Ready for launch")
```

`print()` is a built-in function: a named action we call using parentheses. The items inside the parentheses are its arguments. By default, commas between arguments produce spaces, and each call ends the output line. `print()` with no arguments produces a blank line.

We use parentheses `(` and `)`, not square brackets. Use straight code quotes such as `"`, not the curly quotes copied from formatted documents.

### Strings and quotes

A string is text. Quote marks tell Python that something is literal text rather than a variable name.

```python
planet = "Mars"
print(planet)       # Mars
print("planet")    # planet
```

Single and double quotes both work; match the opening and closing style. Spaces inside the quotes are part of the text. Spaces between arguments are added by `print()`.

```python
print("Let's launch!")
print('The robot says "Hello".')
```

For an apostrophe, the easiest explanation is to wrap the text in double quotes. If asked, a backslash can escape a quote, as in `"The robot says \"Hello\"."`. `\n` means a newline inside text. These are optional details, not prerequisites.

### Variables and assignment

A variable is a name referring to a value. For this lesson, “a labelled place to remember an answer” is a useful classroom explanation.

```python
pilot = "Ada"
print(pilot)
pilot = "Sam"
print(pilot)
```

The outputs are `Ada`, then `Sam`. Assignment with `=` evaluates the right side and gives that value to the name on the left. It does not mean “these must always be equal”. Reassigning changes what later uses of the name read; it does not rewrite earlier output.

```python
pilot = "Ada"
captain = pilot
pilot = "Sam"
print(captain)  # Ada
```

Here `captain` receives the earlier string value. It is not a permanent instruction to follow every future change to `pilot`.

Use descriptive English names: `pilot_name`, `destination`, `companion_name`. Names are case-sensitive: `Pilot` and `pilot` differ. For our naming convention, start with a letter and use letters, digits and underscores; avoid spaces, hyphens, keywords such as `class`, and names like `print` or `input` that already have a built-in purpose. Python allows broader identifiers, but we keep names simple and consistent in class.

### Input and storing answers

```python
pilot = input("Pilot name: ")
print("Welcome,", pilot)
```

`input()` displays the prompt and reads a line of text. In a terminal, the student types an answer and presses Enter. Some browser runners use a separate input panel; demonstrate the actual tested runner. Where input is supplied in advance, provide one answer per line in the same order as the calls.

The answer is returned as a string, even if it looks like a number. The Enter newline is removed; other typed spaces can remain. Pressing Enter without an answer gives an empty string. Week 1 does not require rejecting empty answers.

```python
input("Pilot name: ")
print("Welcome aboard")
```

This reads an answer but does not store it in a variable. Use assignment when the program needs the answer later. Asking three questions once is enough to reuse the three answers in many outputs.

### Joining text

For Week 1, prefer comma-separated arguments:

```python
print("Pilot", pilot, "is going to", destination)
```

If a student asks how to control punctuation precisely, show string concatenation or an f-string as an optional alternative:

```python
print("Welcome, " + pilot + "!")
print(f"Welcome, {pilot}!")
```

With `+`, spaces must be included inside the string fragments. In an f-string, the leading `f` enables `{variable}` substitution. Without `f`, the braces are printed literally. Students need only one working output style today.

### Comments and blank lines

```python
# Collect the player's answers
pilot = input("Pilot name: ")

# Create the briefing
print("Welcome,", pilot)
```

A comment begins with `#` outside a string and continues to the end of the line. It explains code to humans; Python does not execute it. A `#` inside quotes is ordinary text. Blank lines can separate input and output sections.

### Small vocabulary bridge

| English | Estonian classroom cue | Meaning today |
|---|---|---|
| variable | muutuja | Name used to remember a value |
| string | sõne | Text value |
| input | sisend | Answer provided to the program |
| output | väljund | Result the program displays |
| assignment | omistamine | Give a value to a variable |
| function | funktsioon | Named action such as `print()` |
| argument | argument | Value passed into a function call |
| bug | viga | Program behaves differently from the intention |

## Questions students may ask

| Question | Answer and tiny demonstration |
|---|---|
| Why do some words need quotes? | `"Mars"` is literal text; `destination` means look up a variable's value. |
| Can I choose my own variable names? | Yes. Keep them descriptive and use the exact same spelling everywhere. |
| Why does `Print` not work? | Python is case-sensitive. The built-in function is `print`. |
| Is `=` the same as an equals sign in maths? | Here it assigns a value. Comparing equality uses `==`, which we will use in Week 3. |
| Why is the program waiting? | It may be at `input()`. Check the input area and supply the next answer. |
| Why does changing my answer not change the code? | Answers are values during a run. Source code is the instructions. |
| Why does my name disappear next time? | Each fresh run asks again. Saving code does not save a previous run's answers automatically. |
| Can the user type a name with spaces or Estonian letters? | Yes, `input()` reads text. Try `Liis Mari` or `Jüri`; check that the environment displays it correctly. |
| Why is there a space before the exclamation mark? | `print("Hello", pilot, "!")` inserts spaces. Use `print("Hello, " + pilot + "!")` if precise punctuation matters. |
| Why does `"3" + "4"` give `"34"`? | They are strings, so `+` joins them. Number conversion is next week's focus. |
| What is a function? | Today it is a named action we call. `input()` gives us a value; `print()` displays values. We will write our own functions later. |
| Can it remember my answers forever? | Not with only today's code. Persistent data storage is separate from saving the program. |

## Related basics for teacher questions

This is a compact preview to answer curiosity, not additional required Week 1 material. Return students to a working text program before introducing new constructs.

| Topic | Minimal example | Explanation and course timing |
|---|---|---|
| Integer | `credits = 20` | Whole number; numeric work in Week 2 |
| Float | `price = 2.5` | Decimal number; use a dot in code |
| Conversion | `quantity = int("4")` | Convert suitable text to an integer; `int("four")` raises `ValueError` |
| Arithmetic | `total = 3 * 4` | `+`, `-`, `*`, `/`; `//` is floor division, `%` remainder, `**` power |
| Boolean | `ready = True` | A true/false value; capitals matter |
| Comparison | `credits >= 10` | Produces a Boolean; `==` equality, `!=` inequality |
| Conditions | `if ready:` with an indented body | Select a path; Week 3 |
| Repetition | `for turn in range(3):` with an indented body | Repeat; Week 5 |
| While loop | `while lives > 0:` with an indented body | Repeat while a condition holds; Week 6 |
| Own functions | `def greet(name):` with an indented body | Define reusable behaviour; Week 7 |
| List | `items = ["rope", "torch"]` | Collection; later module |
| Dictionary | `player = {"name": "Ada"}` | Values associated with keys; later module |

`/` produces a floating-point division result. `//` rounds the quotient down, which matters with negative numbers. We do not require these operators, branching, loops, lists, dictionaries, imports or exception handling in this first lesson. If students already know them, offer a harder design constraint from the task menu before expanding the lesson's scope.

## Preparation and lesson timing

Before students arrive, run the starter in the chosen environment, test how two answers are supplied, and test a cloud file upload and reopening. Put the four main briefs and extra task menu where students can read them independently. Keep a ready-made two-input recovery starter and the bug examples below.

Use Dodona's tested Python sandbox or the preinstalled PyCharm. These are original creative tasks, not automatically judged Dodona exercises. An unrelated exercise's judge may reject a perfectly good briefing because its required output is different. Keep that separate from running the project.

| Minutes | Teacher and student activity |
|---|---|
| 0–5 | Show a silly personalised briefing. Ask which parts are inputs, remembered values and outputs. |
| 5–12 | Everyone runs the two-line starter, changes the greeting, and runs again. Explain syntax while they use it. |
| 12–30 | Build the Mission in three milestones: first input, second input, three output lines. Check each milestone by running. |
| 30–40 | Students choose Upgrade, Challenge or an extra task; teacher checks individual explanations. |
| 40–50 | Partners predict and test output, then continue their chosen task. Swap driver/navigation roles if sharing a keyboard. |
| 50–57 | Repair a missing quote and compare a literal with a variable. Invite one short student demonstration. |
| 57–60 | Save to cloud storage, reopen the uploaded copy, record a change, and sign out. |

Ask each student: “Which variable remembers this answer?” and “What will change if the destination changes?” A polished story is not sufficient evidence if the student cannot trace a value. If access takes too long, shorten extensions and demonstrations; retain the saving check.

## Main exercises

### Guided starter Welcome aboard

**Time:** About 7 minutes. **Student brief:** Run this, enter a fictional pilot name, and make the greeting your own.

```python
name = input("Pilot name: ")
print("Welcome aboard,", name)
```

1. Run unchanged and see your answer in the output.
2. Change only `"Welcome aboard,"` to a new greeting; run again.
3. Predict what happens if you change `name` in the second line to `"name"`; try it and then restore the personalised greeting.

**Success:** The typed name appears and the student explains why the greeting has quotes but the variable does not. **Prompt if stuck:** “Where does the answer go after `input()` finishes?”

### Mission Three line briefing

**Time:** About 12–18 minutes, including testing. **Student brief:** Ask for a pilot name and a destination. Print a three-line mission briefing using both answers. Invent your own story.

**Build milestones:**

1. Store the pilot answer and print one personalised line.
2. Store the destination answer and use it in an output line.
3. Add a third briefing line. Keep the whole output coherent.

**Example behaviour:** With `Ada` and `Mars`, the program could print:

```text
Welcome aboard, Ada
Your destination is Mars
Ada must rescue the missing space hamster.
```

Exact wording is flexible. The input prompts may appear too; the requirement is three briefing output lines after the questions.

**Tests:** Run with `Ada` / `Mars`, then `Liis Mari` / `Moon`. Both answers must appear in their intended places. The second run should not leave `Ada` or `Mars` hard-coded in the briefing.

**Hint ladder:** “Which two things can change?” → “Create one variable for each answer.” → Provide the two input lines and ask the student to add the output lines. **Teacher check:** Student points from a prompt to a variable to a printed result.

### Upgrade Bring a companion

**Time:** About 4–6 minutes. **Student brief:** Ask for a companion's name and include it in an extra sentence. Keep the original pilot and destination working.

**Success:** Three answers are read once each; changing only the companion changes the companion detail. **Test:** `Ada` / `Mars` / `Bolt`, then the same pilot and destination with `Pip`. **Hint:** “Which new piece of information needs a new variable?”

### Challenge Two briefings from the same answers

**Time:** About 6–10 minutes. **Student brief:** From the same pilot, destination and companion answers, print two versions: one official mission notice and one silly news report. Do not ask the questions again. Give each version a title.

**Success:** Exactly three `input()` calls; both versions reuse all three values; no old answers are hard-coded. **Test:** A partner supplies three unexpected answers and checks both sections. **Hint:** “An answer can be used more than once; `print()` does not consume it.”

### Boss Four input story introduction

**Time:** About 10–15 minutes. **Student brief:** Design a story opening with four inputs. Decide what the fourth detail is: cargo, a lost object, a villain or a mission problem. Collect all four answers before printing a coherent opening. Reuse at least one answer in more than one sentence.

**Constraints:** Four questions, each asked once; each answer used meaningfully; no branches or loops required. Prefer clear code and a traceable story over extra length.

**Success:** A partner can identify the variable behind every personalised detail. Run two very different sets of answers and check that both stories still make sense. **Hint:** Draft four question labels and three or four sentence templates on paper before coding.

## Extra task menu

Choose one task at a time. Estimated times assume a working Mission. Students may pursue depth rather than climb every level. These tasks use the lesson's existing concepts; optional new syntax is identified explicitly.

### Quick modifications

**1. Reskin the briefing · 3–5 minutes.** Change the setting to a fantasy quest, sports team or underwater expedition. Rename relevant variables consistently; keep two inputs and three output lines. **Check:** No space-themed labels remain accidentally. **Hint:** Rename one variable and all its uses together.

**2. Mission identity card · 4–6 minutes.** From the existing answers, print a labelled card containing `Pilot`, `Destination` and `Companion`. Add a title and a blank line. Do not collect extra answers. **Check:** Each label matches the correct value. **Hint:** `print()` can output an empty line.

**3. Echo laboratory · 3–5 minutes.** Write one question, then print its answer three times: alone, after a label, and inside a sentence. Predict each output first. **Check:** Only one question is asked. **Hint:** Use the same variable in three calls.

**4. Prompt makeover · 3–5 minutes.** Make the questions specific enough that another student knows what kind of answer fits the story. Use a fictional example in each prompt. **Check:** A partner can answer without your verbal help. **Hint:** The question text affects usability, even when the syntax is unchanged.

### Reasoning and testing

**5. Trace the values · 5–7 minutes.** On paper, choose answers and write each variable's value immediately after its assignment. Predict the full briefing before running. **Check:** Compare prediction and actual output; explain one mismatch if there is one. **Hint:** Follow the lines from top to bottom.

**6. One change experiment · 4–6 minutes.** Run twice with all answers identical except destination. Mark which output lines should change. **Check:** Every change can be explained by a use of the destination variable. **Hint:** A line changes only if it depends on the changed value.

**7. Adversarial text tester · 5–7 minutes.** Try `Liis Mari`, `Jüri`, a destination such as `Planet 42`, and an empty companion answer. Record what the program actually does. **Check:** Distinguish awkward wording from a crash. Validation is not required. **Hint:** Input is text, even when it contains spaces, punctuation or digits.

**8. Refactor repeated names · 5–7 minutes.** Start with a briefing that writes `Ada` and `Mars` directly in several output strings. Replace the changing details with two variables and then two inputs. **Check:** A new run with `Sam` / `Venus` contains no stale name or planet. **Hint:** Keep fixed sentence text in quotes; put changing details outside them.

**9. Rename safely · 4–6 minutes.** Change `name` to `pilot_name` throughout a working program. Before running, count its assignment and all its uses. **Check:** No `NameError`, same behaviour. **Hint:** Similar spellings are different names.

**10. Snapshot mystery · 5–8 minutes.** Predict this output without running, explain it, then test it:

```python
pilot = "Ada"
original_pilot = pilot
pilot = "Sam"
print(original_pilot, pilot)
```

**Check:** Explain why the first value is still `Ada`. Extend the example with a third assignment and predict again. **Hint:** Ask what value each assignment receives at that moment.

### Longer creative challenges

**11. Two people one mission · 7–10 minutes.** Ask for two pilot names and one destination. Print a shared briefing and a separate responsibility for each pilot. **Check:** Change just one name and verify that only the relevant details change. **Hint:** Use distinct variable names for distinct answers.

**12. Briefing and reply · 7–10 minutes.** Collect the three briefing answers, display a briefing, ask the pilot for a reply, then acknowledge that exact reply. **Check:** The reply prompt happens after the briefing, and the reply appears in the acknowledgement. **Hint:** Input and output can be interleaved; the order is part of the design.

**13. Template designer · 8–12 minutes.** Design a four-input generator for a school announcement, monster introduction or game character. Write the templates first. Each input must be used at least twice, without asking again. **Check:** A partner traces all eight or more uses and tests a second set of answers. **Hint:** More reuse creates a reasoning challenge without needing more questions.

**14. Mission summary constraint · 7–10 minutes.** Produce a detailed briefing and a one-line summary from the same three answers. Use a maximum of three questions and five `print()` calls. **Check:** All three answers appear in both versions; the summary is a single output line. **Hint:** One `print()` call can accept several arguments.

**15. Role swap rehearsal · 8–10 minutes.** One partner writes a plain-language specification for a two-input, three-line program. The other implements it. Switch roles with a new theme. **Check:** The author supplies two test cases and the coder explains a variable. **Hint:** Agree on what must change and what stays fixed before typing.

**16. Minimal repair puzzle · 5–8 minutes.** Ask the teacher for a bug example below. Repair it with as few edits as you can, then explain why each edit is necessary. **Check:** It runs and matches the intended output, including a changed input. **Hint:** A program can run successfully and still be wrong.

### Optional syntax explorations

These introduce small additions. Show the example before assigning the task; they are not needed to complete any main level.

**17. Punctuation perfection · 5–8 minutes.** Convert two comma-based output lines to `+` concatenation or f-strings. Make the output read `Welcome, Ada!` with no space before `!`. **Check:** Try a different pilot; punctuation stays correct. **Hint:** With concatenation, include spaces inside strings.

**18. Clean up a name · 5–8 minutes.** Learn `pilot = pilot.strip()` and remove accidental leading/trailing spaces from a name before printing it. **Check:** Input `  Ada  ` becomes `Ada`; `Liis Mari` keeps its internal space. **Hint:** `.strip()` returns cleaned text; assign it if you want the variable to hold that result.

**19. Headline voice · 5–8 minutes.** Learn `destination.upper()` and print an uppercase destination headline plus an ordinary sentence with the original spelling. **Check:** `Mars` gives `MARS` in the headline and `Mars` elsewhere. **Hint:** Calling `.upper()` does not change the original string by itself.

**20. Decorative border · 5–8 minutes.** Learn `print("=" * 20)` and add a border around the briefing. **Check:** Explain the difference between repeating a string and doing numeric multiplication. **Hint:** `"3" * 4` gives `3333`, while `3 * 4` gives `12`. Numeric input conversion remains Week 2 material.

## Debugging reference and bug hunt

Teach the routine: **expected result → actual result → inspect → change one thing → run again**. Read the final error line, then inspect the indicated line and the line above it. Wording varies by Python version and environment.

| Symptom | Likely cause | First check |
|---|---|---|
| `SyntaxError` | Missing/mismatched quote, parenthesis or comma | Are delimiters paired? Is the previous line unfinished? |
| `NameError` | Misspelling, different capitals, or variable used before assignment | Compare the name with its assignment |
| `IndentationError` | Unexpected leading spaces in today's top-level code | Move the statement to the left edge |
| `TypeError` | Incompatible values or a built-in name overwritten | Inspect types or search for assignments to `print` / `input` |
| `EOFError` | Runner has no more supplied input | Provide one input line for every call |
| No personalised name, no error | Variable name printed as quoted text | Compare `print("pilot")` with `print(pilot)` |
| Old output after an edit | Program not rerun, or wrong file executed | Run the edited file and change a visible message |
| Waiting with no error | Program awaiting input | Find its prompt/input panel before rerunning |
| Name appears in destination line | Wrong variable used | Trace each output label to its source |

Give one bug at a time. Let students describe the fault before changing it.

### Bug A Missing quote

Deliberately broken code:

```python
pilot = input("Pilot name: )
print("Welcome,", pilot)
```

**Teacher answer:** The prompt string never closes. First line should be `pilot = input("Pilot name: ")`. Do not promise that any line runs: Python parses a script before executing it.

### Bug B Wrong capitals

Deliberately broken code:

```python
pilot = input("Pilot name: ")
print("Welcome,", Pilot)
```

**Teacher answer:** `Pilot` has not been defined. Change it to `pilot`.

### Bug C Literal instead of value

Deliberately incorrect behaviour:

```python
pilot = input("Pilot name: ")
print("Welcome,", "pilot")
```

**Teacher answer:** This runs but prints the word `pilot`. Remove the quotes around the second argument.

### Bug D Used too early

Deliberately broken code:

```python
print("Welcome,", pilot)
pilot = input("Pilot name: ")
```

**Teacher answer:** In a fresh run `pilot` does not exist when first used. Move the assignment before the output. If a persistent console masks the bug with an old variable, restart it to test a fresh run.

### Bug E Lost answer

Deliberately incorrect behaviour:

```python
pilot = input("Pilot name: ")
pilot = "Captain Nobody"
print("Welcome,", pilot)
```

**Teacher answer:** The second assignment replaces the answer. Remove it or store the fixed title under a different variable name. This is a logic bug, not a syntax error.

### Bug F Missing separator

Deliberately broken code:

```python
pilot = input("Pilot name: ")
print("Welcome," pilot)
```

**Teacher answer:** Add a comma: `print("Welcome,", pilot)`. Concatenation is another valid repair if spacing is handled.

## Teacher solution notes

These are possible solutions, not exact wording students must copy. Offer hints first.

### Mission reference solution

```python
pilot = input("Pilot name: ")
destination = input("Destination: ")

print("Welcome aboard,", pilot)
print("Your destination is", destination)
print(pilot, "must rescue the missing space hamster.")
```

### Upgrade and Challenge reference solution

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

### Boss reference solution

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

### Prediction answers

- Snapshot mystery: `Ada Sam`. The later assignment to `pilot` does not reassign `original_pilot`.
- `print("3" + "4")`: `34`; `print(3 + 4)`: `7`.
- `print("pilot")`: `pilot`; `print(pilot)`: whatever value `pilot` currently holds.
- An empty input is still a string; a briefing may contain a missing name without crashing.
- A changed destination should affect output lines using that variable, not independently stored pilot or companion values.

## Support and recovery

If a student is overwhelmed, provide the two input lines and ask for one output line at a time. Allow a paper template with blanks for the answers. When a student copies a full solution, ask them to change an input prompt, predict the next run and explain one value's journey before adding features.

For pair work, switch driver and navigator every 7–8 minutes. Check each student's explanation separately and have each save a copy. Do not require peer help before allowing a student to ask the teacher.

For an outage, one student acts as `input()`, another keeps labelled variable cards, and a third reads sentence templates using the current values. Replace one value and predict the revised output. If work cannot be saved, use the paper version rather than leave the only copy on a terminal that will be wiped.

## Saving and exit check

Dodona's sandbox code is not automatically saved. For these creative programs, the authoritative copy is the `.py` file in the student's school cloud folder. Exercise submissions are a separate route for tasks that actually match that exercise's specification.

1. Stop features at minute 57.
2. Save the latest plain-text code as `I_W01_MissionBriefing_ID.py`, replacing `ID` with the school-approved identifier.
3. Upload or sync it to the student's course folder.
4. Reopen the uploaded copy and locate a distinctive latest change. If time permits, run that reopened copy; the reopen check is the minimum.
5. Record one sentence: “I changed …” or “I fixed …”. Sign out of the shared terminal.

**Exit questions:** Where is one answer stored? Which line uses it? What changes when you choose a different destination? An unfinished extension is fine if the Mission works, the student can explain it, and the code is preserved.

## Teaching record

Date: ___ · Present: ___ / 12 · Mission completed: ___ / 12

- Students needing help with input or assignment: ___
- Students able to trace variables independently: ___
- Quote, spelling or runner problems: ___
- Saving problems and resolution: ___
- Extra tasks that worked well: ___
- Changes to make before Week 2: ___

If fewer than about 9 of 12 students finish the Mission and explain a variable, use the first 10 minutes of Week 2 for a briefing repair/remix and reduce that lesson's extensions. This is a planning signal, not a grade. No required homework; students may optionally design a different theme or write test inputs on paper.

## Official references

Reference links are for teacher lookup, not required reading for the children. Examples and task briefs above are original classroom material.

- [Python input](https://docs.python.org/3/library/functions.html#input) and [Python print](https://docs.python.org/3/library/functions.html#print) — behaviour of the two built-in functions.
- [Python text and numbers introduction](https://docs.python.org/3/tutorial/introduction.html) — strings, variables and basic operators.
- [Python string methods](https://docs.python.org/3/library/stdtypes.html#string-methods) — optional `.strip()` and `.upper()` lookup.
- [Python formatted string literals](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals) — optional f-string lookup.
- [Dodona Python sandbox](https://docs.dodona.be/en/guides/students/scratchpad/) — runner behaviour and saving limitation; rehearse the actual school workflow.

## Revision log

| Version | Date | Change |
|---|---|---|
| 1.0 | 4 October 2026 | Expanded existing Week 1 plan into a teacher reference with four main levels, 20 optional tasks, bug answers and saving checks |
| | | |
