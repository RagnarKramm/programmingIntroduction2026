# Beginner MakeCode Arcade Curriculum Weeks 1 to 8

Editable teacher planning document · Version 1.0 · 4 October 2026

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

| Week | Project | Main idea | Evidence of progress |
|---|---|---|---|
| 1 | Talking character | Sequence, sprites, button events | Predicts startup and button behaviour |
| 2 | Treasure explorer | Movement, coordinates, events | Explains a position change |
| 3 | Cherry collector | Overlap, score, randomness | Collection changes state once |
| 4 | Collection game remix | Combine and debug Weeks 1–3 | Repairs one bug and explains a rule |
| 5 | Shield station | Variables, conditions, if and else | Predicts shield-on and shield-off results |
| 6 | Robot patrol | Repeat loops and pauses | Predicts the number and direction of steps |
| 7 | Meteor dodge | Repeated interval events | Explains how the interval affects difficulty |
| 8 | Arcade showcase | Plan, build, test and revise | Demonstrates a working game and one tested change |

Weeks 1–8 form the first module. Later modules can develop functions, game state, lists, larger projects and teamwork, then independent projects and a final showcase. Do not accelerate into these just because students finish a tutorial quickly.

## Week 1 Talking character

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

## Week 2 Treasure explorer

**Learning objective:** Move a character with the controller and describe its position using x and y coordinates. Use an event to change its position. Prerequisite: creating a sprite and attaching code to events.

**Hook:** Show a character that walks around and teleports to a treasure when A is pressed. Ask, “What two numbers tell the game where the treasure is?”

**Prepare:** A plain background with one Player and one stationary Food sprite as treasure. No tilemap is needed. Have a recovery starter with the Player already created. Show a screen coordinate sketch: Arcade's screen is 160 by 120 pixels; x grows rightward and y downward.

### The 60 minute plan

- **0–5:** Reopen Week 1 as a save check, then show today's demo. Students point to the top-left and centre.
- **5–12:** Create Player, use `move mySprite with buttons`, and turn on `stay in screen`. Run immediately. Set a Food sprite's position to x 120, y 30. Demonstrate A setting the Player position to the same coordinates.
- **12–30:** Mission wins: movement works, treasure is visible, teleport reaches it. Students test two other coordinates before choosing their final location.
- **30–50:** Ladder work. Use pairs for five minutes: navigator names a target coordinate, driver predicts and tests it; switch roles.
- **50–57:** Compare walking and teleporting. Ask what changes when y increases. Explain that touching treasure does nothing until we add a rule next week.
- **57–60:** Name and save the new project.

### Student challenge ladder

- **Mission:** Make a Player move with arrow buttons, remain on screen, and teleport to the treasure when A is pressed. Success: movement works in all directions and A reaches the treasure.
- **Upgrade:** Make B return the Player to a starting position. Test A then B three times.
- **Challenge:** Choose two clearly different locations. Make A and B move the Player to them. Write down both coordinate pairs and predict which is higher on screen.
- **Boss:** Design a two-location treasure trail using the known position and speech blocks. A sends the Player to the first clue; B sends it to the second. A partner must find both clues and explain your coordinates.

**Likely mistakes and hints:** x and y may be swapped; change one number at a time. Moving the Food instead of Player is a variable-selection error. A sprite can sit partly off screen even when its centre is in range; use comfortable positions such as x 20–140 and y 20–100. `stay in screen` applies to the selected sprite.

**Support and backup:** Keep the supplied art and one target location. During an outage, use a paper grid and coordinate cards; students instruct a token to move, then debug swapped coordinates.

**Exit evidence:** Student explains which direction changes when y increases. Save `B_W02_TreasureExplorer_ID`. Optional mission: sketch a three-location map without adding new code concepts.

**Resources:** [Coordinate Walker](https://arcade.makecode.com/courses/csintro1/sprites/coordinate-walker) for the coordinate idea; [Sprite Motion and Events](https://arcade.makecode.com/courses/csintro1/motion/sprite-motion-event) for movement. Select relevant sections rather than requiring both complete activities.

**Teaching record:** Date ___ · Mission completed ___/27 · Coordinate confusion ___ · Save issues ___ · Next adjustment ___

## Week 3 Cherry collector

**Learning objective:** Use an overlap event to change score and move a collectible. Explain a variable as a value that can change and randomness as choosing a value within limits. Prerequisite: movement and position blocks.

**Hook:** Collect one cherry and watch another appear elsewhere. Ask, “Which rule should run when the two sprites touch?”

**Prepare:** Duplicate the Week 2 style of project with Player and Food sprites. Use one collectible only. Keep the Cherry Pickr resource open, but omit its tilemap for this first version.

### The 60 minute plan

- **0–5:** Demo three collections and ask students to predict the next cherry's position.
- **5–12:** Set score to 0 on startup. Add `on Player overlaps Food`; inside, change score by 1 and reposition the event's `otherSprite` with random x 10–150 and y 10–110. Pause 200 ms after moving it. Explain that overlapping for several frames can trigger a rule repeatedly, so moving the item and a short pause help.
- **12–30:** Build movement, then collection, then random relocation. Run after each win. Explain score as a built-in changing value; avoid adding a second custom variable today.
- **30–50:** Ladder and testing. Partners collect ten cherries and watch for unexpected score jumps.
- **50–57:** Compare two random ranges. Use a test run to discuss why unpredictable does not mean unrestricted.
- **57–60:** Save and check the latest version.

### Student challenge ladder

- **Mission:** A movable Player collects one Food sprite, adds 1 to score, and sends it to a random position. Success: three separate collections give score 3.
- **Upgrade:** Start a 30-second countdown on startup. Show the player how many points they can collect before time runs out.
- **Challenge:** Make a small-target version and a large-target version by changing the Food image. Ask a partner to play both and identify which is harder.
- **Boss:** Balance a collector game so your partner can usually collect 5–10 items in 30 seconds. Change movement speed, collectible size or placement range, and explain the effect of two changes. No new blocks are required.

**Likely mistakes and hints:** Score resets inside the overlap event; move its initialisation to startup. Both sprites have the same kind; select Player and Food correctly. Updating the global Food variable becomes confusing with many collectibles; today keep one, and demonstrate the overlap event's `otherSprite`. If score jumps, check relocation and the short pause; the new random position can occasionally overlap the Player again.

**Support and backup:** Supply movement and Food creation, leaving the overlap rule for the student. In an outage, throw two paper dice to choose a grid location and update a score counter by hand after each collection.

**Exit evidence:** Ask what changes and what stays the same after collection. Save `B_W03_CherryCollector_ID`. Optional mission: invent a theme with the same mechanics.

**Resources:** [Cherry Pickr](https://arcade.makecode.com/lessons/cherry-pickr), adapted to a plain background; [Overlap and Events Part 1](https://arcade.makecode.com/courses/csintro1/motion/overlap1); [Random Sprite Location](https://arcade.makecode.com/courses/csintro1/motion/random).

**Teaching record:** Date ___ · Mission completed ___/27 · Can explain score ___ · Repeated-overlap problems ___ · Next adjustment ___

## Week 4 Collection game remix

**Learning objective:** Combine sprites, events, movement, position and score; find a bug using a prediction and a small test. This is a checkpoint with no required new programming concept.

**Hook:** Demonstrate a collector that stubbornly stays at score 1. Ask whether it is broken even though it runs without an error.

**Prepare:** Three separate bug examples: score set to 1 rather than increased; an overlap event using the wrong sprite kind; a random position range that puts Food off screen. Give each pair one bug first. Keep a working Week 3 recovery starter.

### The 60 minute plan

- **0–5:** Predict and run the score bug. Explain that incorrect behaviour is also a bug.
- **5–12:** Model “expected → actual → suspect one block → change → retest.” Fix the score bug together. Review an event and a variable using students' explanations.
- **12–30:** Pairs complete a bug hunt, switching roles after seven minutes, then each student begins their own remix from Week 3.
- **30–50:** Work through the ladder. Circulate with the four checkpoint questions below; ask quieter students individually.
- **50–57:** Partners play and report one useful change. Share one repair, including the evidence that it worked.
- **57–60:** Cloud save and export backup. Have students reopen the uploaded copy at the start of Week 5 if time is tight today.

### Student challenge ladder

- **Mission:** Fix one supplied bug, then make a playable themed collector with movement, one collectible and increasing score. Success: three collections add exactly three points in the test run.
- **Upgrade:** Add button instructions and a countdown, using known speech and countdown blocks.
- **Challenge:** Give a partner a deliberately broken copy with one changed block. They must explain and repair the rule. Keep the working original.
- **Boss:** Create two difficulty versions using only known blocks. Run the same 30-second test with a partner and explain which parameter caused the biggest difference.

**Checkpoint questions:** What triggers collection? Where does the starting score belong? Why do we move the Food afterwards? How did you prove your repair worked? Mark each student's understanding as seen, with help, or independent. Working art or a high score is not evidence of conceptual understanding by itself.

**Likely mistakes and hints:** Students may change several blocks at once; restore the last working state and isolate one change. They may delete the original while remixing; duplicate first. In pair work, ask the navigator to explain the repaired block before switching.

**Support and backup:** Supply a working starter and ask for one deliberate behaviour change before personalisation. For an outage, give block printouts with one misplaced rule and ask students to trace three collections.

**Exit evidence:** Save `B_W04_CollectionRemix_ID`, export a backup, and record one bug and its fix. Optional mission: design new art for the existing game.

**Resources:** [Touch the Button review](https://arcade.makecode.com/courses/csintro1/review/touch-the-button) as a related remix activity; [Cherry Pickr](https://arcade.makecode.com/lessons/cherry-pickr) for the familiar game rules.

**Teaching record:** Date ___ · Mission completed ___/27 · Students needing events/score review ___ · Best evidence ___ · Week 5 changes ___

## Week 5 Shield station

**Learning objective:** Store a shield state in a custom variable and use an `if/else` rule to choose an outcome. Prerequisite: events, score and simple state changes.

**Hook:** A shield protects a spaceship from a meteor. Press A to turn it on, B to turn it off, and touch the meteor. Ask, “The same collision happens, so why are there two outcomes?”

**Prepare:** A movable Player and one stationary Enemy meteor. Use a numeric variable `shield` with values 0 and 1 for this first lesson. Display the state through speech. A recovery starter contains sprites and movement only.

### The 60 minute plan

- **0–5:** Demo shield-on and shield-off collisions. Students predict both outcomes.
- **5–12:** Create `shield = 0` on startup and set life to 3. A sets shield to 1 and says “Shield on”; B sets it to 0 and says “Shield off”. In Player–Enemy overlap, add `if shield = 1`: add 1 to score; `else`: change life by -1. Move `otherSprite` to a random safe-screen position and pause 200 ms after either outcome.
- **12–30:** Mission wins: buttons change state, each branch works, collision finishes by relocating the meteor. Trace the variable aloud before running.
- **30–50:** Ladder; partners run a two-row test table with shield 0 and shield 1. Before the recharge extension, show that `score ≥ 2` checks whether score is at least 2 and test scores 1, 2 and 3.
- **50–57:** Show an `else` accidentally outside the intended logic and compare the results. Ask why a condition needs to be checked when the collision happens.
- **57–60:** Save and note one successful test.

### Student challenge ladder

- **Mission:** Shield-off collision costs one life; shield-on collision gains one point. Success: both outcomes match the test table and the meteor relocates.
- **Upgrade:** Make the shield single-use: after a protected collision, set shield to 0 and say “Shield used”. The next collision must cost a life until A is pressed again.
- **Challenge:** Only allow A to activate the shield when score is at least 2. Activation spends 2 score; otherwise say “Collect 2 points first”. To earn starting points, add one Food collectible using Week 3's rule.
- **Boss:** Balance the recharge system using known events, score and conditions. Explain the score cost and show a test where the player cannot recharge, then one where they can.

**Likely mistakes and hints:** The shield is checked only on startup; move the condition into the collision event. Life decreases after both branches; inspect the indentation of blocks visually. Startup never sets shield; initialise it. Repeated overlap can drain life rapidly; relocate the meteor after either branch and use the pause.

**Support and backup:** Keep A and B as direct on/off controls and omit the score-recharge extension. For an outage, use a shield token and collision cards; students act out `if` and `else` and update life.

**Exit evidence:** Student predicts two collisions after a single-use shield is activated. Save `B_W05_ShieldStation_ID`. Optional mission: draw the two states of a shield.

**Resources:** [MakeCode if blocks](https://arcade.makecode.com/blocks/logic/if) for conditional logic; [Overlap reference](https://arcade.makecode.com/reference/sprites/on-overlap) for the collision event. These references support the original shield task.

**Teaching record:** Date ___ · Mission completed ___/27 · Independent branch predictions ___ · Extra support needed ___ · Next adjustment ___

## Week 6 Robot patrol

**Learning objective:** Replace repeated movement instructions with a repeat loop and predict its total effect. Use a pause to make changes visible. Prerequisite: sprite positions, events and conditions.

**Hook:** Show a robot taking ten steps out and ten back. Ask whether we should drag the same block ten times.

**Prepare:** One Player robot at x 30, y 60. A teacher example has three repeated “change x by 5; pause 100 ms” sequences. Use no controller movement in the Mission so that manual input cannot obscure the patrol.

### The 60 minute plan

- **0–5:** Predict where three 5-pixel steps will end. Run the long version.
- **5–12:** Replace it with `repeat 3 times`, containing change x by 5 and pause 100 ms. Show A pressed: set position to 30,60; repeat 10 rightward steps; repeat 10 steps of -5. First win is the visible outward patrol.
- **12–30:** Complete the return trip. Students calculate the endpoint, run, and compare. Keep pauses inside each loop.
- **30–50:** Ladder. Partners change one of step count, step size or pause and predict before testing.
- **50–57:** Remove a pause in the demo and ask why movement now looks instant. Discuss “repeat a fixed number” versus “keep running”.
- **57–60:** Save with the final count and step size in the reflection.

### Student challenge ladder

- **Mission:** A makes the robot take ten 5-pixel steps right and ten 5-pixel steps left, returning to its starting point. Success: starts and ends at x 30 after one patrol.
- **Upgrade:** Make a different out-and-back patrol with another step count or size. Predict its furthest x coordinate before running.
- **Challenge:** Make B perform a square using four consecutive repeat loops: five steps of +5 x, five of +5 y, five of -5 x, five of -5 y. Start at a position that keeps it on screen.
- **Boss:** Design a patrol that draws an imaginary rectangle and ends exactly where it started. Use different horizontal and vertical lengths, and explain why each direction cancels its opposite. Do not require nested loops.

**Likely mistakes and hints:** Both directions use +5; inspect signs. A pause after the loop cannot show intermediate steps. The loop count is mistaken for a destination coordinate; trace a three-step example. Repeated button presses can cause overlapping patrol runs; test with one press and wait for completion. A press-in-progress lock can be an optional condition-based repair using Week 5's state idea.

**Support and backup:** Provide the outward loop and ask for the inverse return. During an outage, students act as robots on a paper grid while a partner reads loop cards.

**Exit evidence:** Predict the result of six steps of +4 from x 30. Save `B_W06_RobotPatrol_ID`. Optional mission: design a path on graph paper.

**Resource:** [Loops Intro](https://arcade.makecode.com/courses/csintro1/loops/intro), using its movement-and-repeat idea. The rectangle task is our extension of this idea.

**Teaching record:** Date ___ · Mission completed ___/27 · Accurate loop predictions ___ · Timing confusion ___ · Next adjustment ___

## Week 7 Meteor dodge

**Learning objective:** Use a repeated interval event to create hazards and explain how timing changes difficulty. Distinguish a fixed-count loop from an event that runs repeatedly while the game continues. Prerequisite: movement, collisions, life, randomness and repeat loops.

**Hook:** Show a dodge game first with one meteor every two seconds, then every half-second. Ask which single setting might explain the difference.

**Prepare:** A Player spaceship with button movement and stay-in-screen; life 3. Introduce two API blocks as the new tools: `on game update every 1000 ms` and a projectile created from the side with vx 0 and vy 40. Explain that the projectile already moves and is automatically removed off screen. Keep the core to these two new tools.

### The 60 minute plan

- **0–5:** Run the two versions and ask for a difficulty prediction.
- **5–12:** Inside the interval event create a projectile with vx 0, vy 40, then set its position to random x 10–150 and y 0. Run to see falling hazards. Show Player–Projectile overlap: destroy `otherSprite`, then subtract one life.
- **12–30:** Build falling meteors, then movement, then life loss. Set a 30-second countdown on startup. The Mission is surviving until the countdown ends; the default countdown ending is enough, without requiring a new win handler.
- **30–50:** Ladder and paired playtests. Compare one setting at a time.
- **50–57:** Students explain why a repeat-10 loop creates a finite batch and an interval event keeps creating hazards throughout play.
- **57–60:** Save with one chosen difficulty setting.

### Student challenge ladder

- **Mission:** Move to avoid meteors that appear every second; a hit removes one meteor and one life. Success: two separate hits reduce life from 3 to 1, without one meteor draining all lives.
- **Upgrade:** Tune interval and speed so a partner can survive about 20–30 seconds. State which change made survival easier.
- **Challenge:** Inside each interval, use `repeat 2 times` to create two meteors with separate random x positions. Increase the interval if needed to keep the game playable.
- **Boss:** Combine the shield rule from Week 5 with the dodge game. A protected hit consumes the shield instead of life; an unprotected hit removes life. Demonstrate both cases and ensure the colliding projectile is destroyed in either case.

**Likely mistakes and hints:** Meteor creation is outside the interval, producing only one. The overlap event checks Enemy instead of Projectile. One projectile remains touching the Player; destroy the event's `otherSprite` first. Very fast spawning creates an unfair game; restore 1000 ms and 40 pixels per second before tuning.

**Support and backup:** Supply the interval and projectile creation so the student adds collision logic and tests it. During an outage, a student dealer introduces paper hazards every few seconds; compare fixed batches with a continuing timer.

**Exit evidence:** Explain what changing 1000 ms to 2000 ms does. Save `B_W07_MeteorDodge_ID`. Optional mission: write a fair-game rule and an unfair-game rule.

**Resources:** [Update Interval reference](https://arcade.makecode.com/reference/game/on-update-interval) and [Overlap reference](https://arcade.makecode.com/reference/sprites/on-overlap). These support our original dodge activity; the [Intro CS course](https://arcade.makecode.com/courses/csintro1) provides related projectile lessons for later exploration.

**Teaching record:** Date ___ · Mission completed ___/27 · Can distinguish repeat and interval ___ · Difficulty issues ___ · Week 8 changes ___

## Week 8 Arcade showcase

**Learning objective:** Plan a small game, combine known ideas, test it against stated rules and make one evidence-based improvement. This is a project checkpoint, with no required new concept.

**Hook:** Offer two briefs: “Collect treasure before time runs out” or “Survive falling meteors”. Students choose a game and one personal twist.

**Prepare:** Working minimal starters from Weeks 3 and 7, a short planning template and an acceptance checklist. Students may remix an existing project or build from a starter; a blank project is optional for confident students. Avoid tilemaps or new features that would use the whole lesson.

### The 60 minute plan

- **0–5:** Show the two briefs and explain the minimum playable version.
- **5–12:** Students write three game rules and choose their starter. Teacher models one small plan and one test, without giving a new full build. First win is the starter running and one personalised change.
- **12–30:** Build the Mission and run after every rule change. Ask students to explain where their state changes.
- **30–45:** Ladder work and paired testing. Reserve the final five minutes of this block for fixing one reported issue.
- **45–54:** Show three 60–90-second demos. Other students test in pairs rather than waiting for every project to be presented.
- **54–57:** Students answer the checkpoint questions and write one next-module wish.
- **57–60:** Save, export and cloud-upload the backup. Do not let showcase time consume the save ritual.

### Student challenge ladder

- **Mission:** Make either a collector with score and a countdown, or a dodge game with life and repeated hazards. Include working controls and a short instruction message. Success: a partner can start, play and describe how the game ends.
- **Upgrade:** Add one taught feature: a second button action, a shield, or a change to spawn timing. Test it before adding more art.
- **Challenge:** Write three acceptance tests, ask a partner to run them, then fix one problem. Include a test that intentionally checks an edge case such as an unprotected hit or repeated collection.
- **Boss:** Create two balanced difficulty versions and justify the differences using playtest results. All features must use concepts from Weeks 1–7.

**Acceptance checks:** Controls respond; score or life changes according to the stated rules; the ending works; each tested collision affects the correct sprite; the latest project can be reopened after saving. Students record expected and actual results rather than just “works”.

**Checkpoint questions:** Which event starts your main rule? Which value changes? Where do you use repetition or a condition, if your game has one? What failed in testing, and how did you improve it? For a collector without conditions, assess that student's condition knowledge using the Week 5 shield example separately.

**Support and backup:** Cut the personal twist and complete a working starter with one student-made rule change. For an outage, storyboard the game and act out three turns using score/life counters; carry the build into the next meeting.

**Exit evidence:** Save `B_W08_Showcase_ID`, its backup and three tests. Optional mission: plan a feature for the next module without introducing it into today's build.

**Resources:** [Cherry Pickr](https://arcade.makecode.com/lessons/cherry-pickr), [Touch the Button review](https://arcade.makecode.com/courses/csintro1/review/touch-the-button), and the [Intro CS course index](https://arcade.makecode.com/courses/csintro1). Use them as references for chosen mechanics.

**Teaching record:** Date ___ · Playable projects ___/27 · Independent explanations ___ · Main gaps ___ · Student interests ___ · Week 9 priority ___

## Progress tracking and next module decisions

Use one record per student. Mark **S** for seen, **H** for can use with help, **I** for independent, and a dash for not yet observed. Add a date and a concrete example when a skill becomes independent. Observations during pair work must include the student's own explanation or action.

| Student ID | Sequence and events | Coordinates | Changing state | Conditions | Repetition | Debugging | Saving | Evidence and next step |
|---|---|---|---|---|---|---|---|---|
| ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ |
| ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ |
| ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ |

Duplicate rows for the class. At Weeks 4 and 8, review patterns:

- If events or score remain unclear, use another collection remix before adding more systems.
- If conditions need practice, start Week 9 with shield predictions and two-outcome rules.
- If students can explain repetition and debug independently, proceed toward functions and decomposing larger games.
- If saving fails, repair that workflow before starting projects that span several meetings.
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
| ___ | ___ | ___ | ___ |
| ___ | ___ | ___ | ___ |

## Resource notes

Official MakeCode pages were checked during preparation on 4 October 2026 in the teacher's timezone. Online lessons and interfaces can change; rehearse the relevant section before class. Our timings, challenge ladders and adjustment rules are teaching recommendations, not claims made by Microsoft. The linked materials supplement this document; the core instructions above remain usable if a tutorial changes.
