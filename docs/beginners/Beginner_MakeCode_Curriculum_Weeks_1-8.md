# Beginner MakeCode Arcade Curriculum Weeks 1 to 8

Editable teacher planning document · Version 1.1 · 13 October 2026

This document plans the first eight lessons of a 32-lesson after-school programming course for 27 beginners aged 10–13. Each lesson lasts 60 minutes. We teach in Estonian, use English coding terms and resources, and build small games in Microsoft MakeCode Arcade. The main aim is to help students break problems into steps, predict behaviour, experiment, and debug. Lessons 4 and 8 give us evidence for adjusting the next module.

The lesson plans are original classroom adaptations linked to official MakeCode materials. They are not instructions to complete entire online courses in one hour. Every student should reach the Mission; the other levels provide meaningful work for students who move faster. No homework is required.

## How to use and revise this document

- Before each lesson, test the named blocks and prepare the short demo and recovery starter. Put all four challenges where students can read them without asking.
- After each lesson, fill in its teaching record. Use observed explanations and changes to code as evidence of understanding.
- Keep completed weeks as a record. Edit future weeks when necessary and note the change in the revision log.
- Lesson numbers refer to meetings, not calendar dates. If a meeting is cancelled, continue with the next lesson rather than skipping its concept.
- A suggested adjustment rule: if fewer than roughly 20 of 27 students complete the Mission and explain its key idea, begin the following week with a 10-minute repair/remix. Remove an extension to make room. This is a planning signal, not a student pass mark.

## Course decisions and preparation

| Item | Current plan | Confirm or adjust |
|---|---|---|
| Group | 27 beginners aged 10–13 | Attendance and individual support needs |
| Platform | MakeCode Arcade in the browser | School access and browser compatibility |
| Persistence | Individual school-approved account with MakeCode Cloud Sync | Microsoft account availability is still unconfirmed |
| Backup | Export project and upload to school cloud storage | Exact storage service and folder permissions |
| Language | Estonian teaching and English blocks/materials | Translate task prose when useful |
| Collaboration | Individual ownership with occasional pairs | 13 pairs and one trio when everyone attends |
| Assessment | Observation, explanations and working projects | No formal grades or exams |

### Before the first meeting

1. Ask school IT to test the actual student login path, including access to MakeCode and school cloud storage. Use school-managed accounts where available; account setup is a school decision.
2. On a terminal, create a tiny signed-in project, wait for its cloud status to show it is saved, log out of the school session, then sign in again and reopen it. This is the essential persistence test.
3. Test exporting a MakeCode project file, uploading it to the school cloud, downloading it in a fresh session, and importing it. Keep an accessible teacher copy of every recovery starter.
4. Prepare a class resource page or school learning-platform post with this week's resource, four challenges and starter link/file. Do not depend on browser bookmarks surviving logout.
5. Test projector visibility. Use enlarged blocks and the simulator; avoid spending the first lesson on account administration if IT can resolve it beforehand.

MakeCode's official documentation says signed-in projects and tutorial progress can sync across computers. Existing local projects need to be opened after sign-in to transfer them. Students should check the cloud status indicator rather than assume sign-in alone has saved everything. See [Cloud Sync](https://arcade.makecode.com/identity/cloud-sync).

If sign-in fails, use the export-and-cloud-upload route for that lesson. If cloud storage is also unavailable, the teacher must capture each project's export into an approved persistent location before logout. A downloaded file left on the terminal is not a backup. During a full outage, use the week's unplugged activity and record the design for the next meeting.

### Project ownership and saving

Use names such as `B_W03_CherryCollector_A7`, where the last part is a school-approved student identifier. Avoid personal information in shared game content. For a pair or trio, one account owns the working project; at the end, each partner imports a copy into their own account and checks its save status. Do not edit one project from several sessions at once.

At minute 57, stop building:

1. Name the project and check that the latest edits are saved to the cloud.
2. For Weeks 4 and 8, export the project and upload it to the student's course folder as a second copy. Use this route every week if Cloud Sync is unavailable.
3. Reopen the saved project and confirm one distinctive change is present. At the next meeting, reopen it before starting new work.
4. Record the project name or approved class link and one sentence: “Today I changed … because …”. Sign out of shared terminals.

### Classroom routines

Use the same four labels all year: **Mission**, **Upgrade**, **Challenge**, **Boss**. Boss tasks combine taught ideas; they should not require a new API or programming concept. Give only the first helpful hint, then let the student try.

For help, students say what they expected, what happened, and what they tried. Encourage “Look → Try one change → Undo if needed → Ask a neighbour → Ask the teacher.” Students can ask directly when they are stuck or need access support.

In pairs, the driver uses the keyboard and mouse; the navigator reads the task and predicts what will happen. Switch every 7–8 minutes. In a trio, the tester runs the acceptance checks and proposes one change; rotate all roles. Ask every student to explain one block so that a working pair project does not hide gaps.

Keep drawing time to about two minutes during guided builds. Students can choose provided art, then personalise it once the behaviour works. Use quiet or muted sound in a large class.

## The eight lesson sequence

### Adjustment after Lesson 1

Teacher feedback: the lesson went well, but covered only a small part of the planned material. Most students created a character, made it move and say their chosen messages, and used A for speech with a pause between messages. This is the starting baseline for Lesson 2, not evidence that everyone completed every original Week 1 task or can explain it independently. Attendance, completion counts and saving results were not supplied and remain to be recorded.

Continue the same character project in Week 2; copy it where practical to preserve the first lesson. Spend time on reliable controls, readable sequences, testing and saving before coordinates in Week 3. The character becomes a treasure adventure across Weeks 3–5 and 7–8; Week 6 is a small separate loop experiment. These smaller steps retain the course's problem-solving goals while reducing setup and new concepts per meeting.

Week 4 remains a checkpoint, now covering events, movement, coordinates and the first overlap rule. Week 8 remains a showcase and checkpoint. Custom shield state, life, projectiles and interval spawning move to the next module or later, after checking readiness; they are not compulsory catch-up work. Conditions use familiar score in Week 7. Fixed-count loops remain a small Week 6 experiment and can be revisited later if needed.

| Week | Project | Main idea | Evidence of progress |
|---|---|---|---|
| 1 | Talking character — completed | Actual baseline: sprite, movement, chosen speech, A sequence with pause | Verify each student's events and timing in Week 2 |
| 2 | Character controls and testing | Consolidate events, movement and sequence; B help | Tests controls separately and explains one event |
| 3 | Treasure locations | Coordinates and two sprite references | Predicts a position change |
| 4 | Find the treasure | First overlap rule; debug/checkpoint | Collection removes Food; repairs and explains a bug |
| 5 | Cherry collector | Score, then bounded randomness | One collection changes score once; explains limits |
| 6 | Robot patrol | Repeat loops and pauses | Predicts the number and direction of steps |
| 7 | Treasure goal | Conditions using familiar score | Predicts both outcomes of a B status check |
| 8 | Character adventure showcase | Plan, remix, test and revise | Demonstrates a playable project and one tested change |

Weeks 1–8 form the first module. Later modules can develop functions, game state, lists, larger projects and teamwork, then independent projects and a final showcase. Do not accelerate into these just because students finish a tutorial quickly.

## Week 1 Talking character

**Historical plan:** The original Week 1 plan below is retained as the teaching record. It describes intended activities, not completed coverage. Use the feedback above and revised Week 2 plan for the next meeting. The [Week 1 teacher reference](Beginner_Week_1_Teacher_Reference.md) also remains the original preparation document.

**Learning objective:** Create a sprite, run a short sequence at startup, and make a button trigger a different action. Explain the difference between startup code and an event. No prior coding knowledge is assumed.

**Hook:** Show a character that introduces itself and tells a joke when A is pressed. Ask, “How does it know when we press the button?” The first win is a character appearing on screen, ideally by minute 8.

**Prepare:** A finished demo and a starter containing only a simple Player sprite. Open the Beginner's Guide before class. Use its initial sprite and event activities selectively; the four classroom challenges below are our own adaptations.

### The 60 minute plan

- **0–5:** Demo the character. Ask students to predict which action happens immediately and which waits.
- **5–12:** Sign in, create and name a project. In `on start`, create `mySprite` as Player, set a background colour, and make it say “Hello!” for 1000 ms. Run after each addition. Show an A-button-pressed event that makes it say another message.
- **12–30:** Build the Mission in three wins: sprite appears, startup speech works, A changes speech. Circulate first to students without a visible sprite.
- **30–50:** Students work through the ladder. At minute 40, partners predict each other's B-button action before running it.
- **50–57:** Show two different characters. Move a speech block outside the intended event in the teacher example and ask when it will run.
- **57–60:** Save using the routine. Account problems take priority over extensions.

### Student challenge ladder

- **Mission:** Make a character greet the player at startup and say a different sentence when A is pressed. Success: restart produces the greeting; pressing A produces the second sentence.
- **Upgrade:** Add a B-button message and change the background. Both buttons must still work.
- **Challenge:** On A, make the character say two short sentences in order using timed speech blocks. Predict the order before running.
- **Boss:** Create a tiny interactive character with A and B actions and a startup introduction. Give a partner instructions and check that they can discover both actions without your help.

**Likely mistakes and hints:** A disconnected block does not run; inspect where it is attached. A button event waits for a press; startup runs on restart. If a sprite variable is missing, use the creation block inside `on start`. If speech disappears too quickly, increase its duration.

**Support and backup:** Provide the one-sprite starter and ask the student to add only one event. For an outage, one child plays a robot and another reads three instruction cards; compare “do now” and “when I clap” instructions.

**Exit evidence:** Ask, “What runs when the game starts? What runs only after A?” Save `B_W01_TalkingCharacter_ID`. Optional home mission: invent a new message or draw a character on paper.

**Resources:** [Beginner's Guide educator notes](https://arcade.makecode.com/skillmap/educator-info/basic-map-info) and [MakeCode orientation](https://arcade.makecode.com/courses/csintro1/intro/makecode-orientation). Use the guide's save-to-project workflow if students work inside a skillmap.

**Teaching record:** Date ___ · Mission completed ___/27 · Students needing event review ___ · Login/save issues ___ · Change for next week ___

## Week 2 Character controls and testing

**Learning objective:** Consolidate movement, startup and button events; build a readable sequence and test separate controls. Prerequisite: the actual Week 1 baseline, with recovery support for students who need it.

**Project decision:** Continue the existing character, preferably in a copied Week 2 project. A fresh project is a recovery option, not a second task. See [Week 2 teacher reference](Beginner_Week_2_Teacher_Reference.md) for block recipes, pacing, extra tasks and bug answers.

**Hook:** The character can already move and talk. Can a new player discover its controls without the creator explaining them?

**Prepare:** A demo with movement, stay-in-screen, A speech → pause → speech and B help. Prepare both a working recovery copy and a minimal one-sprite starter. Check the school's copy/export/import workflow before class.

### The 60 minute plan

- **0–10:** Reopen and test each student's existing project. Check movement and A separately; repair access or missing essentials. Preserve the Week 1 copy where practical.
- **10–17:** Demonstrate one improvement at a time: stay-in-screen if missing, then B help. Reuse an existing B handler if present. Predict before running.
- **17–35:** Complete the Mission. Give individual help first to students without movement or a working A event. Students already at the baseline add B and test rather than rebuild.
- **35–47:** Optional ladder work. A partner tries the controls without coaching and gives one specific observation.
- **47–54:** Repair one issue and retest. Ask individual students which event contains their change and why a pause is needed.
- **54–60:** Name, save and verify the latest change. Keep this longer saving window while the routine is still becoming familiar.

### Student challenge ladder

- **Mission:** Keep one movable character visible on screen; A shows two readable messages with a pause between; B gives a short controls/help message. Success: restart, movement, A once and B once all pass separate tests. Startup greeting is welcome if already present, but does not block this Mission.
- **Upgrade:** Add or improve startup instructions so a partner can discover movement, A and B. Pause between consecutive startup messages if needed.
- **Challenge:** Make B change the background and give a matching message; A's sequence must still work. Explain why both B actions belong in that event.
- **Boss:** Make a tiny character experience another student can use independently. Record three expected/actual tests and improve one confusing behaviour using taught blocks.

**Likely mistakes and hints:** Wrong sprite selected; compare variable dropdowns. Two A handlers after duplication; change the intended help event to B. Speech duration does not delay the next instruction; retain the explicit pause. Test one event at a time before investigating rapid input.

**Support and backup:** Give the working recovery project and require one student-made change and explanation. With no computers, act out startup, A and B instruction cards with a wait card between messages.

**Exit evidence:** Explain startup versus a button event and one test. Save `B_W02_CharacterControls_ID`. No required homework.

**Resources:** [Controller movement](https://arcade.makecode.com/reference/controller/move-sprite), [Stay in screen](https://arcade.makecode.com/reference/sprites/sprite/set-stay-in-screen), [Pause](https://arcade.makecode.com/reference/loops/pause).

**Teaching record:** Date ___ · Present ___ · Baseline independently verified ___ · Mission completed ___ · Event/timing support ___ · Save issues ___ · Week 3 changes ___

## Week 3 Treasure locations

**Learning objective:** Use x and y to place sprites and predict a position change. This week's new idea is coordinates; movement and button events are review.

**Hook:** Show the familiar character walking to a treasure. Ask which two numbers tell the game where the treasure sits.

**Prepare:** A copy of the character project with one Player; a recovery copy with movement already working. Use small gallery images, a plain background and no tilemap. Draw a 160 × 120 screen: x grows rightward, y downward; coordinates locate a sprite's centre.

### The 60 minute plan

- **0–10:** Reopen and check movement. Keep A's existing speech; explain that today's B will replace the help action in this copied project.
- **10–18:** Set Player to x 30, y 60. Create one separate variable `treasure` of kind Food and set it to x 120, y 30. Predict and test one coordinate change.
- **18–35:** Complete the Mission, running after each position change. Check variable selection before adding more blocks.
- **35–47:** Demonstrate B setting Player to x 30, y 60; students add the return action, then choose optional ladder tasks.
- **47–54:** Partner predicts which of two locations is higher. Compare walking with setting a position directly.
- **54–60:** Save and verify.

### Student challenge ladder

- **Mission:** Place a movable Player and stationary treasure at two chosen visible positions. Record both coordinate pairs and explain what increasing y does. Touching treasure has no rule yet.
- **Upgrade:** B returns Player to its starting coordinates. Walk away and test B three times.
- **Challenge:** Keep A's speech and append a position action after its final message to send Player to treasure. Predict the speech/wait/move order before testing; pause after the final message too if it should finish before the move.
- **Boss:** Design a two-location clue trail using existing speech, button and position blocks. A partner explains the two locations after testing.

**Likely mistakes and hints:** Setting `treasure` overwrites Player's variable; keep separate references. Swapped x/y; change one value. Use comfortable positions such as x 20–140 and y 20–100 for small sprites, rather than screen edges.

**Support and backup:** Supply the two sprites; ask the student to change and explain one coordinate. Unplugged: move a token on a paper screen using coordinate cards.

**Exit evidence:** Predict the direction of a y change. Save `B_W03_TreasureLocations_ID`.

**Resources:** [Set position](https://arcade.makecode.com/reference/sprites/sprite/set-position), [Coordinate Walker](https://arcade.makecode.com/courses/csintro1/sprites/coordinate-walker).

**Teaching record:** Date ___ · Mission completed ___ · Can explain x/y ___ · Sprite-reference confusion ___ · Week 4 changes ___

## Week 4 Find the treasure — first checkpoint

**Learning objective:** Add one overlap rule to a familiar project, then test and repair it. New idea: an event can be triggered by two sprite kinds touching. This checkpoint measures events, movement, coordinates and debugging; score is not yet expected.

**Hook:** Last week touching treasure did nothing. Today reaching it makes it disappear and the character says “Found it!”.

**Prepare:** Week 3 copy and working recovery starter. Remove optional A teleportation so collection requires walking. Keep B return if useful. Prepare a wrong-kind overlap bug and a wrong-sprite destroy bug.

### The 60 minute plan

- **0–10:** Reopen, check two different sprite kinds and predict the result of touching treasure.
- **10–18:** Demonstrate `on Player overlaps Food`: destroy the event's `otherSprite`, then make Player say “Found it!” for 2000 ms. Restart to bring treasure back.
- **18–35:** Build and test one collection. Then repair one supplied event/kind bug using expected → actual → one change → retest.
- **35–47:** Optional ladder and individual checkpoint conversations.
- **47–54:** Partner tests from restart, then creator fixes one issue.
- **54–60:** Save and export/upload a backup; verify the latest copy.

### Student challenge ladder

- **Mission:** Walk to one treasure; it disappears and Player announces success. Restart restores it. Explain the overlap event and repair one supplied bug, with help if needed.
- **Upgrade:** Add clear startup instructions using known speech/pause blocks.
- **Challenge:** Choose new starting and treasure locations. Predict the walking route and ask a partner to test it.
- **Boss:** Give a partner a copied project with one deliberate bug. They explain and repair it; preserve the working original.

**Checkpoint questions:** What triggers A compared with the overlap? Which sprite does `otherSprite` refer to here? What changes when y increases? What test proves the repair worked?

**Likely mistakes and hints:** Both sprites are Player; check creation kinds. Destroying the event's `sprite` removes Player; use `otherSprite` for Food in this event. Creating Food inside the overlap continually adds objects; create once at startup.

**Support and backup:** Supply the overlap container and ask for its actions. If coordinates/events remain unclear, use the next meeting for repair and cut Week 5 extensions. Unplugged: move paper sprites, trigger the matching kind rule and remove the Food card.

**Exit evidence:** Save `B_W04_FindTreasure_ID`, backup and one bug/fix note.

**Resource:** [Overlap reference](https://arcade.makecode.com/reference/sprites/on-overlap).

**Teaching record:** Date ___ · Mission completed ___ · Events independent ___ · Coordinates independent ___ · Debugging evidence ___ · Week 5 decision ___

## Week 5 Cherry collector — score and randomness

**Learning objective:** Track collections using score and choose bounded random locations. Prerequisite: the Week 4 overlap rule. Introduce score first; random placement follows only after one collection works.

**Hook:** Collect treasure, see the score rise, then restart to find it in a different place.

**Prepare:** Copy Week 4; retain one Player and one Food. Use small sprites. The reliable minimum destroys the Food after one collection; repeated random relocation is an extension rather than a requirement.

### The 60 minute plan

- **0–10:** Reopen and test the Week 4 rule; repair if needed.
- **10–18:** Set score to 0 in startup. In the overlap, destroy `otherSprite` first, then change score by 1. Predict restart versus collection.
- **18–32:** Complete the scoring win. Students test that one collection gives exactly 1 and restart resets to 0.
- **32–40:** Demonstrate random x 20–140 and y 20–100 for Food's startup position; restart several times to test the bounds.
- **40–54:** Finish the Mission and optional ladder; compare expected and actual score.
- **54–60:** Save and verify.

### Student challenge ladder

- **Mission:** Food starts at a bounded random location. One collection removes it and increases score from 0 to 1; restart resets score and places Food again.
- **Upgrade:** Add a 30-second countdown in startup after a brief teacher demonstration. Try to find Food before time runs out.
- **Challenge:** Replace destruction with moving `otherSprite` to a random location, then pause 200 ms. Test ten collections for score jumps; explain that a new location can overlap Player again and a pause does not guarantee separation. If unreliable, restore the one-collection version.
- **Boss:** Compare two placement ranges or movement speeds with the same timed playtest. Explain one setting's effect using results; use the reliable Mission if the repeated version is unstable.

**Likely mistakes and hints:** Score reset in overlap prevents accumulation; initialise in startup. Setting score to 1 differs from adding 1. Random means within chosen limits; margins must accommodate the image size. A random spawn can start on Player; an immediate collection is possible, so use fixed separated positions when diagnosing the score rule.

**Support and backup:** Keep a fixed Food position until scoring is understood, then add randomness with help. Unplugged: choose coordinates using dice and update a score card on collection.

**Exit evidence:** Explain where score begins and when it changes. Save `B_W05_CherryCollector_ID`.

**Resources:** [Score](https://arcade.makecode.com/reference/info/change-score-by), [Random Sprite Location](https://arcade.makecode.com/courses/csintro1/motion/random), [Countdown](https://arcade.makecode.com/reference/info/start-countdown).

**Teaching record:** Date ___ · Score rule understood ___ · Random bounds understood ___ · Relocation issues ___ · Week 6 changes ___

## Week 6 Robot patrol — repeat loops

**Learning objective:** Replace repeated position changes with a fixed-count loop and predict its result. Prerequisite: coordinates, sequence and pause. This is a short separate experiment; preserve the collector for Weeks 7–8.

**Hook:** A robot takes three equal steps. Must we copy the same instructions three times?

**Prepare:** One robot at x 30, y 60, without controller movement or stay-in-screen clamping that would obscure endpoint arithmetic. Show three copies of change x by 5 → pause 200 ms. Keep every route inside the screen.

### The 60 minute plan

- **0–10:** Predict the three-step endpoint and run the long version.
- **10–18:** Replace the three copies with `repeat 3 times` containing change x by 5 and pause 200 ms, inside A pressed.
- **18–35:** Mission: A resets to x 30, y 60, then repeats six steps of +5 x. Predict x 60 before testing.
- **35–47:** Optional ladder; change one of count, step size or pause at a time.
- **47–54:** Partner predicts a new endpoint. Remove the pause in a teacher copy to compare visible and near-instant movement.
- **54–60:** Save and verify.

### Student challenge ladder

- **Mission:** One A press resets the robot and runs six 5-pixel rightward steps with pauses. Explain count × step size and the endpoint x 60.
- **Upgrade:** Add six steps of -5 x to return to x 30.
- **Challenge:** Change step count or size, predict the furthest position, then test an out-and-back route.
- **Boss:** Use consecutive loops to make a rectangle returning to its start; explain why opposite changes cancel. No nested loop is needed.

**Likely mistakes and hints:** Pause outside the loop hides intermediate steps. Both directions positive prevents return. Rapid A presses can start overlapping sequences; press once and wait for the patrol to finish. A lock variable is deferred.

**Support and backup:** Provide the loop container and ask students to adjust its count and predict. Unplugged: a student robot follows repeat cards on a grid.

**Exit evidence:** Predict six +4 steps from x 30. Save `B_W06_RobotPatrol_ID`.

**Resource:** [Loops Intro](https://arcade.makecode.com/courses/csintro1/loops/intro).

**Teaching record:** Date ___ · Mission completed ___ · Endpoint predictions ___ · Pause placement support ___ · Week 7 readiness ___

## Week 7 Treasure goal — conditions

**Learning objective:** Use `if/else` to select a response based on score. Prerequisite: score and button events. Use familiar game state before introducing a custom shield variable.

**Hook:** B says “Find the treasure” before collection and “Mission complete” afterwards. The same button gives two outcomes: what value decides?

**Prepare:** Reopen the reliable Week 5 collector: one Food, destroyed on collection, score +1. Retain movement and A speech. Replace B's old return/help action deliberately with the status check. No repeat loop is required in this game.

### The 60 minute plan

- **0–10:** Test score 0 on restart and score 1 after collection. Repair the collector before adding logic.
- **10–18:** In B pressed add `if score >= 1`: Player says “Mission complete”; `else`: Player says “Find the treasure”. Predict both branches.
- **18–35:** Complete the Mission; test B before and after collection, then restart and test again.
- **35–47:** Optional ladder and partner tests. Explain that B checks the current score at the moment it is pressed.
- **47–54:** Debug a status check accidentally placed only in startup. Ask individuals to explain which branch runs and why.
- **54–60:** Save and verify.

### Student challenge ladder

- **Mission:** B gives the correct status at score 0 and score 1; restart restores the incomplete status. Explain the condition and both outcomes.
- **Upgrade:** Each branch sets a matching background colour as well as its message.
- **Challenge:** Use a teacher-prepared three-treasure starter: three Food sprites at fixed, separated positions; overlap destroys the touched `otherSprite` and adds 1. Change the goal to score >= 3; test scores 0, 2 and 3. Demonstrate extra sprite creation/references before this extension.
- **Boss:** Write and run a test table for below, at and above the goal. Use a teacher test copy with adjustable startup score if the one-treasure game cannot reach those values; restore normal score 0 afterwards.

**Likely mistakes and hints:** A condition checked only at startup cannot give current status later; move it into B. Swapped branches; trace score 0. A response outside the condition can overwrite the chosen message; put the intended speech inside its branch.

**Support and backup:** Supply the condition container and let students build two short responses. If score remains unclear, repair that first and use paper score cards for branch predictions; unfinished conditions become the next module's starting point.

**Exit evidence:** Predict B at score 0 and 1. Save `B_W07_TreasureGoal_ID`.

**Resources:** [If blocks](https://arcade.makecode.com/blocks/logic/if), [Score value](https://arcade.makecode.com/reference/info/score).

**Teaching record:** Date ___ · Both branches tested ___ · Independent predictions ___ · Score gaps ___ · Week 8 adjustments ___

## Week 8 Character adventure showcase — second checkpoint

**Learning objective:** Combine familiar ideas into a small playable project, test stated rules and make one evidenced improvement. No required new concept.

**Hook:** Turn the familiar character and treasure into a tiny adventure another student can understand and finish.

**Prepare:** Working Week 4 and Week 7 starters. Students remix their own project or use a recovery starter; a blank build is optional. Offer two achievable briefs: find one treasure with a success message, or collect treasure with score and a B status check. No tilemap, projectile or interval event is required.

### The 60 minute plan

- **0–10:** Choose a brief and write three rules: controls, what happens on collection, how the player knows they finished.
- **10–18:** Reopen the chosen project and make one personal change; agree expected tests before building.
- **18–35:** Complete the Mission and run after every behaviour change.
- **35–47:** Partner tests three rules; creator repairs one issue or improves one unclear instruction and retests.
- **47–54:** Three short demos while others test in pairs. Ask individual checkpoint questions.
- **54–60:** Save, export/upload backup and record next-module needs.

### Student challenge ladder

- **Mission:** A character adventure with movement, one collectible, a visible completion response and clear instructions. A partner can start, play and describe completion. Keep the smaller Week 4 brief valid for students needing consolidation.
- **Upgrade:** Add or refine the taught score and B condition from Week 7.
- **Challenge:** Record three expected/actual tests including restart and collection, then make and retest one improvement.
- **Boss:** Compare two versions differing in one taught setting; use partner results to justify the final choice. A repeat-loop celebration is optional only if it works and remains understandable.

**Acceptance checks:** Movement responds; the intended Food disappears on contact; completion is readable; score/status follows the selected brief; restart restores the initial state; the latest saved change can be reopened.

**Checkpoint questions:** Which event causes collection? What changes after it? How did you prove your fix worked? Predict a coordinate change. Check conditions with Week 7's score example and loops with Week 6's robot example separately when the chosen project omits them. Do not mistake absent optional features for missing understanding.

**Support and backup:** Keep the smaller brief and supply working movement. In an outage, storyboard and act out three tests; resume the build next meeting.

**Exit evidence:** Save `B_W08_CharacterAdventure_ID`, backup and three tests.

**Resources:** [Overlap reference](https://arcade.makecode.com/reference/sprites/on-overlap), [Intro CS course index](https://arcade.makecode.com/courses/csintro1) for later teacher preparation.

**Teaching record:** Date ___ · Playable projects ___ · Independent explanations ___ · Main gaps ___ · Student interests ___ · Week 9 priority ___


## Progress tracking and next module decisions

Use one record per student. Mark **S** for seen, **H** for can use with help, **I** for independent, and a dash for not yet observed. Add a date and a concrete example when a skill becomes independent. Observations during pair work must include the student's own explanation or action.

| Student ID | Sequence and events | Coordinates | Changing state | Conditions | Repetition | Debugging | Saving | Evidence and next step |
|---|---|---|---|---|---|---|---|---|
| ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ |
| ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ |
| ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ |

Duplicate rows for the class. At Weeks 4 and 8, review patterns:

- If events or score remain unclear, use another collection remix before adding more systems.
- If conditions need practice, start Week 9 with the familiar score/status predictions before introducing a custom shield variable.
- If students can explain repetition and debug independently, proceed toward functions and decomposing larger games.
- If saving fails, repair that workflow before starting projects that span several meetings.
- Introduce custom state, life, projectiles and repeated interval events in later lessons only when students can explain the relevant prerequisites. Keep the deferred shield and meteor ideas as future options, not a fixed Week 9 checklist.
- If only a few students need reinforcement, provide a small starter clinic while others extend a familiar game. Do not use fast finishers as permanent substitute teachers.

## Estonian vocabulary support

| English term | Estonian teaching term |
|---|---|
| sequence | käskude järjekord |
| event | sündmus |
| sprite | sprait ehk mängutegelane |
| variable | muutuja |
| condition | tingimus |
| loop | tsükkel |
| random | juhuslik |
| debugging | vigade leidmine ja parandamine |

Translate task explanations when necessary, while keeping block names recognisable in the English interface. Ask students to explain ideas in Estonian if that makes their reasoning clearer.

## Revision log

| Version and date | Lesson or decision | What changed | Evidence or reason |
|---|---|---|---|
| 1.0 · 4 October 2026 | First eight lessons | Initial classroom plan | Agreed group size, timing and persistence constraints |
| 1.1 · 13 October 2026 | Weeks 2–8 after Lesson 1 | Continue the character; consolidate in Week 2; separate coordinates, overlap and score; simplify conditions; defer shields and meteors; add Week 2 teacher reference | Most students reached sprite/movement/speech and A with a pause; actual coverage was smaller than planned |
| ___ | ___ | ___ | ___ |
| ___ | ___ | ___ | ___ |

## Resource notes

Initial resources were checked during preparation on 4 October 2026. Movement, stay-in-screen, position and overlap references were checked again for this revision on 13 October 2026 in the teacher's timezone. Rehearse all lesson-specific blocks and recovery starters before class; no classroom demo or browser save workflow is claimed to have been tested by this document revision. Our timings, challenge ladders and adjustment rules are teaching recommendations, not claims made by Microsoft. The linked materials supplement this document; the core instructions remain usable if a tutorial changes.
