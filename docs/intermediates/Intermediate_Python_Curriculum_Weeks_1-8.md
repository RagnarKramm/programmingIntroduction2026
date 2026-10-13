# Intermediate Python Curriculum Weeks 1 to 8

Editable teacher planning document · Version 1.1 · 13 October 2026

This document plans the first eight lessons of a 32-lesson after-school programming course for 12 students aged 10–13. Lessons last 60 minutes and happen weekly. Students previously learned block programming with another teacher; their individual confidence with variables, conditions and loops is not yet known. We teach in Estonian, write code in English, and use short interactive programs to connect familiar ideas to Python.

By the end of this module, students should be able to build and test a small interactive program using input, output, variables, arithmetic, conditions and simple functions, with fixed-count repetition if ready. Condition-controlled loops and returned values move to the next module unless readiness allows an optional introduction. Lists, dictionaries, broader string processing and larger projects follow in later modules. No required homework or formal exams are planned. Weeks 4 and 8 provide evidence for adjusting the course.

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

## Revision based on completed Lesson 1

**Teacher feedback:** Students reached opening their first script file and editing the initial Hello World function to say their name. This introduced creating a function, calling it, passing function inputs and setting a variable. The planned multi-input mission briefing was not reached. The number of students independently confident with each idea and the saving workflow are not yet recorded.

Treat these ideas as introduced, then check each student's understanding in Lesson 2. A value passed to a function is an argument; the name in its definition is a parameter. This does not establish that students have used keyboard `input()`. Lesson 2 explicitly bridges the two. The Week 1 teacher reference remains the original intended plan; this record describes what actually happened.

Keep the environment used successfully in Lesson 1. The platform section above records earlier options, not confirmation that a particular service or cloud workflow was used. Before Lesson 2, test reopening students' files and keyboard input in that environment. Update the platform decision with the actual route once confirmed.

## The eight lesson sequence

| Week | Project | Main idea | Evidence of progress |
|---|---|---|---|
| 1 — completed | Personalised Hello World | Open/edit a script; variable; function definition, argument and call introduced | Teacher reports a greeting changed to the student's name; individual independence still to check |
| 2 | Interactive greeting | Consolidate functions and variables; introduce keyboard input | Traces an answer into a variable, argument, parameter and printed greeting |
| 3 | Space shop | Integer conversion, multiplication and subtraction | Checks totals for quantities 0, 2 and 4 |
| 4 | Airlock security | Two-way decisions; checkpoint on weeks 1–3 | Tests correct and incorrect passwords and explains the branch |
| 5 | Mini quiz and repair workshop | Consolidate conditions and changing score | Tests all-correct and all-wrong answers; explains a score update |
| 6 | Countdown and repeated greetings | Fixed-count repetition with for/range | Predicts number of calls and tests a different count |
| 7 | Three-round quiz | Combine a known loop, input and conditions | Explains what happens once and what repeats; checks final score |
| 8 | Small interactive showcase | Finish, test and explain a familiar project | Demonstrates a working program and a tested change |

Functions that print remain familiar tools throughout. `return`, `while`, randomness, `and`/`or`, and division/remainder are deferred rather than compressed into later lessons. Introduce optional syntax only after a short demonstration and secure core work. No required homework.

## Week 1 Personalised Hello World — completed record

**Original intention:** Mission briefing using keyboard input and output; see the unchanged [Week 1 teacher reference](Intermediate_Week_1_Teacher_Reference.md).

**Actual reach:** Opening the first script and personalising the initial Hello World function. Function creation, function calls, function inputs and variable assignment were introduced. Do not retrospectively count the planned briefing as completed or assume independent mastery.

**Follow-up evidence to collect:** Can each student reopen and run their file, change a value, identify the definition and call, and predict the greeting? Was the latest version saved and recoverable? Date ___ · Present ___/12 · Independent explanations ___/12 · Actual filename/platform ___ · Saving issues ___

## Week 2 Interactive greeting

**Objective:** Reopen and run a script; explain definition versus call and variable versus quoted text; read one keyboard answer and pass it to a greeting function. Use the detailed [Week 2 teacher reference](Intermediate_Week_2_Teacher_Reference.md).

**Prepare:** The actual Lesson 1 starter, a recovery copy, a tested input route and save route. The example below is a planning model, not a claim about the exact starter used.

```python
def greet(name):
    print("Hello,", name)

player_name = input("Your name: ")
greet(player_name)
```

**60 minutes:** 0–10 reopen/run and change a fixed name; 10–20 trace variable → argument → parameter → output, then make a second call; 20–30 demonstrate one `input()` and let students run it; 30–45 Mission and optional extensions; 45–52 partner tests and one bug repair; 52–57 individual explanation; 57–60 save and reopen. If file access takes longer, drop extensions and protect saving.

**Ladder:** Mission — one keyboard name passed to `greet`, tested with two names. Upgrade — call the same function twice with two separately collected names. Challenge — demonstrate a second parameter, then create `briefing(name, destination)` and print two lines. Boss — reuse that function for two travellers and predict which output changes when one destination changes.

**Tests:** `Ada`, then `Liis Mari`, must appear in the greeting; no old name remains. **Hints:** Definition alone does not print; call after the definition. Body is indented, call is at the left edge. `greet("player_name")` passes literal text. **Recovery:** Start with a fixed-name call and provide the input line when ready. Paper backup: pass named value cards to a greeting station.

**Exit:** Point to definition, call, variable and parameter; explain where the typed answer goes. Save `I_W02_InteractiveGreeting_ID.py`. **Record:** Mission ___/12 · Independent trace ___/12 · Input/access issues ___ · Week 3 repair needed ___

## Week 3 Space shop

**Objective:** Convert text to an integer and calculate a total with `*` and balance with `-`. Prerequisite: one working input/output program. Start with fixed quantity if input still needs repair. Teach only the operators needed today.

```python
credits = 20
price = 3
quantity_text = input("How many batteries? Enter a whole number: ")
quantity = int(quantity_text)
total = price * quantity
remaining = credits - total
print("Total:", total)
print("Credits left:", remaining)
```

**60 minutes:** 0–10 greeting retrieval/repair; 10–20 predict fixed quantity 4, then show separate input and conversion lines; 20–35 Mission in two stages (total, balance); 35–48 ladder and paired calculations; 48–57 compare text `"4"` with number `4`, collect explanations; 57–60 save/reopen.

**Ladder:** Mission — total and balance for one product. Upgrade — change price and predict the result. Challenge — add a second product and combine totals with `+` after modelling it. Boss — let the user choose the starting budget and test an overspend. No purchase rejection yet.

**Tests:** Quantities 0, 2, 4 give total/balance 0/20, 6/14, 12/8; 7 gives 21/-1. A negative balance is useful output. **Hints:** `"4" * 3` repeats text; `4 * 3` calculates. Require valid nonnegative whole-number quantities; exceptions/validation are deferred. **Recovery:** Supply input/conversion and prices; student writes the total line. Paper backup: value cards and bills.

**Exit:** Explain why `int` is needed and predict quantity 3. Save `I_W03_SpaceShop_ID.py`. **Record:** Mission ___/12 · Conversion understood ___ · Arithmetic support ___ · Week 4 repair ___

## Week 4 Airlock security — first checkpoint

**Objective:** Choose one of two outcomes with `if`, `else` and `==`. Strings suffice; numeric clearance and compound conditions are not required.

```python
password = input("Password: ")
if password == "moon":
    print("Door opens")
else:
    print("Access denied")
```

**60 minutes:** 0–12 reopen and check one input trace and one Week 3 calculation; 12–22 model correct/incorrect password and indentation; 22–37 Mission; 37–48 ladder and two-branch tests; 48–57 individual checkpoint and repair; 57–60 save/reopen.

**Ladder:** Mission — password door with one result per run. Upgrade — change password and messages, test both outcomes. Challenge — after modelling `>=`, add a separate numeric clearance checker. Boss — put the password decision in `check_password(password)` and call it with two values; no return needed.

**Tests:** `moon` opens; `sun` and `Moon` deny. **Hints:** `=` assigns; `==` compares. Colon and indentation form a branch. **Recovery:** Supply the full branch skeleton, ask for a changed password and predictions. Paper backup: sort password cards.

**Checkpoint:** Independently trace input and a greeting call, explain one calculation and both branches. If fewer than about 9 of 12 can explain the Mission, make Week 5 a repair workshop with one question and postpone loops if necessary. Record observations rather than a grade.

**Exit:** Explain why only one message prints. Save `I_W04_AirlockSecurity_ID.py`. **Record:** Mission ___/12 · Input/functions ___ · Arithmetic ___ · Branches ___ · Week 5 priorities ___

## Week 5 Mini quiz and repair workshop

**Objective:** Practise input, conditions and score updates without a new control construct. Begin with one question; a two-question quiz is the target when ready.

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

**60 minutes:** 0–12 checkpoint-led repair; 12–22 model score before/after; 22–37 Mission; 37–48 ladder; 48–57 test and debug; 57–60 save/reopen.

**Ladder:** Mission — one question, score 1 for correct and 0 otherwise. Upgrade — add a second question; initialise score only once. Challenge — add a third and test mixed answers. Boss — add a familiar printing function for a personalised final message; pass name and score as two parameters after a demonstration.

**Tests:** Two-question version: both correct → 2; both wrong → 0; one correct → 1. **Hints:** `score = 1` replaces rather than accumulates; compare text answer with `"7"`. Keep the final print outside branches. **Recovery:** One question is a complete Mission. Paper backup: trace score cards after each answer.

**Exit:** Explain `score = score + 1`. Save `I_W05_MiniQuiz_ID.py`. **Record:** Mission ___/12 · Score explanations ___ · Ready for fixed-count loops ___ · Repair next week ___

## Week 6 Countdown and repeated greetings

**Objective:** Repeat a familiar action a fixed number of times with `for` and `range`. No randomness or new game rules. Proceed only after basic branches and variables are secure; otherwise repeat Week 5 with changed questions.

```python
def greet(name):
    print("Hello,", name)

player_name = input("Your name: ")
for round_number in range(3):
    greet(player_name)
print("Finished")
```

**60 minutes:** 0–10 retrieve/repair; 10–20 compare three calls with one loop; 20–35 Mission; 35–48 extensions and predictions; 48–57 trace indentation and count; 57–60 save/reopen.

**Ladder:** Mission — greet three times and print Finished once. Upgrade — change count to 5 and explain the change. Challenge — print round labels using `round_number + 1`, model zero-based values first. Boss — demonstrate `range(3, 0, -1)` for a 3, 2, 1 launch countdown and explain why 0 is excluded.

**Tests:** Counts 3, 1, 0 give that many greetings and one Finished each. **Hints:** `range(3)` supplies 0, 1, 2; indented statements repeat, later top-level statements do not. **Recovery:** Teacher supplies loop header; student predicts and changes count. Paper backup: repeat a greeting station three times.

**Exit:** Identify what repeats and what happens once. Save `I_W06_RepeatedGreetings_ID.py`. **Record:** Mission ___/12 · Loop count explained ___ · Indentation issues ___ · Week 7 readiness ___

## Week 7 Three-round quiz

**Objective:** Combine fixed-count repetition, a question, a condition and changing score. Use one repeated question first to isolate repetition; different question data and lists are deferred.

```python
score = 0
for round_number in range(3):
    answer = input("What is 3 + 4? ")
    if answer == "7":
        score = score + 1
        print("Correct")
    else:
        print("Try again next round")
print("Final score:", score)
```

**60 minutes:** 0–10 count/indentation recap; 10–22 trace one round and model nesting; 22–37 Mission; 37–48 ladder and partner tests; 48–57 explain score placement and repair; 57–60 save/reopen.

**Ladder:** Mission — three questions asked, final score correct. Upgrade — show round numbers and feedback. Challenge — move familiar feedback into `show_feedback(answer)`; keep score update in the caller, without requiring return. Boss — after modelling `elif`, use the round number to choose three different questions and expected answers; this is optional, not a class prerequisite.

**Tests:** Answers 7/7/7 → 3, 0/0/0 → 0, 7/0/7 → 2. **Hints:** Initialise score before loop; input inside loop; final score after loop. Function that prints feedback does not automatically update the caller's score. **Recovery:** Continue Week 6 count practice or Week 5 two-question quiz; do not require nesting before readiness. Paper backup: trace round, answer and score.

**Exit:** Explain why score starts outside the loop. Save `I_W07_RoundQuiz_ID.py`. **Record:** Mission ___/12 · State trace ___ · Nesting support ___ · Showcase starter ___

## Week 8 Small interactive showcase

**Objective:** Finish a familiar program, test two cases and explain one change. No new syntax. Choose greeting/briefing, shop, password checker or quiz according to demonstrated readiness; loops are required only for the round-based option.

**Prepare:** Students' saved projects plus working recovery starters from Weeks 2–7. A plan names the user, input, output and one small change. Keep project scope to one existing program.

**60 minutes:** 0–10 retrieve starter and choose change; 10–20 plan and run first change; 20–38 build; 38–48 paired tests/repair; 48–55 short demonstrations and individual explanations; 55–57 reflection; 57–60 save/reopen.

**Ladder:** Mission — working interactive project, one independently explained modification and two tests with expected/actual results. Upgrade — reuse a printing function with a parameter. Challenge — add a third boundary test and fix/retest an issue if found. Boss — combine two already secure ideas, such as numeric shop total and affordability decision, after teacher checks scope. Do not add `while` or `return` as showcase requirements.

**Tests:** Greeting: two names including one with a space. Shop: zero items and quantity 4. Password: accepted and rejected. Quiz: all correct and all wrong; third test mixed answers. **Recovery:** A small working greeting with a clear explanation is valid evidence; separately record concepts still needing practice. Paper backup: trace planned inputs and outputs.

**Exit:** Demonstrate, trace one value and name the tested change. Save `I_W08_Showcase_ID.py` and test notes. **Record:** Working projects ___/12 · Independent explanations ___ · Concepts secure ___ · Week 9 priorities ___

## Progress tracking and future decisions

Use **S** for seen, **H** for can use with help, **I** for independent, and a dash for not yet observed. Add a date and one concrete action or explanation. Duplicate the rows for all 12 students. Pair success alone does not establish independent understanding.

| Student ID | Input and output | Types and arithmetic | Conditions | for loops | while loops | Functions | Debugging and tests | Cloud saving | Evidence and next step |
|---|---|---|---|---|---|---|---|---|---|
| ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ |
| ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ |
| ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ |

At Week 4, check input, function calls, arithmetic and two-way conditions; use Week 5 for the observed gaps. After Week 8:

- If fixed-count loops remain uncertain, repeat a short round-based activity and trace its state before introducing another loop type or lists.
- Check parameters separately from return: parameters were introduced in Lesson 1, while return is deferred. Consolidate calls, then introduce returned values with tiny calculation functions and separate tests.
- Start Weeks 9–16 with deferred while loops and return when ready, using a fixed-secret guessing game and small calculation functions. Randomness and compound conditions can follow. Introduce lists, string methods and dictionaries only after these foundations are secure; the original dates are flexible.
- Later modules can develop modules, file/data concepts in the tested environment, larger teamwork projects and an independent showcase. Basic object-oriented ideas remain optional and depend on readiness.
- A saving failure is a workflow issue to repair before multiweek projects, not a reason to blame the student.

## Online exercise selection guide

The original projects above are deliberately creative and use manual acceptance tests. Existing online tasks supplement them; automatic judging is useful for short precise problems, while a teacher or partner evaluates open-ended game choices.

When adding a Dodona exercise, record the exact URL here only after reviewing it. Choose a task of roughly 5–10 minutes, with a clear English or translated statement, matching prerequisites and a quick visible success. Prefer deterministic inputs and outputs while students are learning syntax. Read [Solving Exercises](https://docs.dodona.be/en/guides/students/exercises/) to rehearse the student submission route.

| Week | Desired supplement | Selected exercise URL | Access and test checked |
|---|---|---|---|
| 2 | Keyboard input, output and greeting calls | ___ | ___ |
| 3 | Integer calculation | ___ | ___ |
| 4–5 | Two-way decisions and score updates | ___ | ___ |
| 6–7 | Fixed-count repetition | ___ | ___ |
| 8 or later | Consolidation; return only once taught | ___ | ___ |

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
| 1.1 · 13 October 2026 | Feedback after Lesson 1 | Lesson 2 greeting consolidation and input; re-paced weeks 3–8; deferred while/return | Class reached opening and personalising first function-based script |

## Resource notes

Official Python, Dodona and Raspberry Pi links were checked during preparation on 4 October 2026 in the teacher's timezone. Raspberry Pi project pages require JavaScript and should be rehearsed before assigning them; their full step-by-step contents were not inspected in this preparation. Core tasks here are self-contained original lesson plans. Timings, challenge levels and adjustment thresholds are teaching recommendations. Lesson 1 has taken place; confirm the actual platform and file recovery route before Lesson 2. Existing reference links are retained from the original preparation and were not rechecked for this pacing revision.
