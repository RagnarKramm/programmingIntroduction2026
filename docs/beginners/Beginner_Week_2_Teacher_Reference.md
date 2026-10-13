# Beginner MakeCode Arcade Week 2 Teacher Reference

Editable lesson companion · Version 1.0 · 13 October 2026

For 27 beginners aged 10–13, with Estonian teaching and English MakeCode Arcade blocks. Companion to [the revised Weeks 1–8 curriculum](Beginner_MakeCode_Curriculum_Weeks_1-8.md). Lesson numbers refer to meetings, not calendar weeks.

**Today's project:** Character controls and testing. Continue the character from Lesson 1. The teacher reported that most students created a character, made it move and say chosen messages, and used A for a speech sequence with a pause. Treat this as the likely starting point, then verify each student's project and explanation. Do not assume startup greetings, B actions, independent debugging or successful saving were completed.

**Essential learning:** Place actions in the intended events, make a sequence readable, and use a prediction and test to improve behaviour. The next step is a reliable character another student can operate. Coordinates arrive in Week 3; treasure overlap in Week 4; score and randomness in Week 5. Today does not need a new game system.

## At a glance

| Need | Quick answer or action |
|---|---|
| Default project route | Reopen and copy/remix the Week 1 character using the tested school workflow |
| Fresh project route | Recovery when the old project cannot be retrieved; use starter art and the same lesson goal |
| First visible win | Existing character moves and A responds after reopening |
| Mission | Movement, stay-in-screen, A speech → pause → speech, B controls/help |
| New additions | Stay-in-screen if missing; B event if missing; deliberate testing |
| Categories | Sprites, Controller, Loops for pause; Scene only for background work |
| Main distinction | Startup sets up; button events respond; instructions inside one event follow their sequence |
| Timing reminder | Speech duration displays the bubble; pause delays the next instruction in that sequence |
| Evidence | Student predicts a button result, tests it, and explains one block's placement |
| Save name | `B_W02_CharacterControls_ID`, using an approved student identifier |
| Protected ending | Stop features at minute 54; use the final six minutes to save and verify |

Extensions are choices, not a required checklist. A student already meeting the Mission should test and improve it, not rebuild it.

## Preparation and project choice

Prepare three teacher projects before class:

1. **Finished demo:** One Player, directional movement, stay-in-screen on, short startup controls, A with two messages and a pause, B with help.
2. **Working recovery copy:** Movement and a readable A sequence already present. Student adds B, makes one personal change and explains it. This is for access problems or students substantially behind the reported baseline.
3. **Minimal starter:** One visible Player created in startup. Use for students who can add the missing movement and A quickly; do not make a struggling student rebuild everything before receiving help.

Test the blocks, simulator inputs and school's copy/save path on the actual classroom setup. Keep recovery files in an approved location students can reach. This document supplies recipes; it does not claim a prepared MakeCode file or share link exists.

**Continue by default.** Keeping the character preserves ownership and avoids spending another lesson drawing and setting up. Give it a small role: guide, comedian, helpful robot or explorer. The behaviour goal is the same for every theme.

If the editor offers a suitable project-copy route, rehearse it and make a Week 2 copy. Otherwise export the full Week 1 project to approved storage, import a separate copy and name it for Week 2. Verify the copy before editing. If copying takes too long, continue the original after preserving a backup where possible; do not let copying consume the building period. Record the actual name used.

**A fresh project is a recovery route.** Use gallery art and a starter to reach the same goal. Students should not complete both a fresh build and a continuation. If the old project is missing, solve access privately and keep the student working from the recovery copy.

## The 60 minute lesson

| Minutes | Teacher action | Student action / evidence |
|---|---|---|
| 0–10 | Help reopen projects; show the short baseline test; organise copies where practical | Restart, try four directions, press A once and wait; identify one missing behaviour |
| 10–17 | Demonstrate stay-in-screen if needed, then B help; predict before each test | Identify the selected sprite and the event that owns the action |
| 17–35 | Circulate to missing movement/A first; use recovery copies as needed | Complete and test the Mission in small steps |
| 35–47 | Offer optional ladder tasks; organise a partner test | Partner uses the project without coaching; creator records an observation |
| 47–54 | Model one repair and retest; ask individual exit questions | Fix one unclear behaviour or instruction and retest it |
| 54–60 | Stop features; support saving and verification | Save, reopen, locate latest change and record project name |

Keep whole-class demonstrations short: show one change, test it, then release students to try. Limit guided art work to about two minutes; existing images are already good enough for the behaviour task.

**If reopening takes more than ten minutes:** distribute recovery copies and continue the Mission. Cut Challenge/Boss work and shorten the demo; protect partner testing and saving. Do not introduce coordinates to fill time for quick finishers.

**If many students still lack movement or a working A:** focus the class demonstration on those repairs. B can be supplied in a recovery copy or become next lesson's opening repair. Record this as partial Mission completion and adjust Week 3; do not count supplied code as independent understanding.

## Blocks and concepts to explain

### Movement and screen boundaries

After creating Player in `on start`, use **Controller** → `move mySprite with buttons`. Select the actual character variable. Expand its speed fields if needed; use vx 80 and vy 80 for the demo. These are movement speeds, not coordinates. Positive speed values allow the directional buttons to choose left/right and up/down.

Use **Sprites** → the sprite flag block resembling `set mySprite stay in screen ON`, after creation. The wording may appear as a flag dropdown. Select **stay in screen** and switch it on. This keeps the character visible at the boundary. It is not a wall or tilemap rule. See [movement](https://arcade.makecode.com/reference/controller/move-sprite) and [stay-in-screen](https://arcade.makecode.com/reference/sprites/sprite/set-stay-in-screen).

Try all four directions, then hold each direction at its edge. Choose small art and a plain background. Speech bubbles near edges may be harder to read; test A near the centre first. If a student already has suitable movement, preserve it rather than require the teacher's exact speed.

### Events and existing handlers

`on start` creates and configures the character. `on A button pressed` responds to A. `on B button pressed` responds to B. Event containers sit separately; their visual order in the workspace does not decide which runs first.

Before adding B, inspect the existing code. If B already exists, improve that handler instead of adding a second one. If duplication produces two A handlers, change the intended help handler to B. Do not create a new sprite inside either button event; reuse the character created at startup.

Use the simulator's visible buttons first. Demonstrate the keyboard mapping on the actual setup; pressing the literal keyboard letter A is not necessarily the simulator's A input. Click the simulator if the editor has keyboard focus.

### Speech and waiting

Keep A's existing text where possible. If it has only one message, add a second short message with a pause between. Use this block recipe inside **one** A pressed event:

1. Make Player say `Why did the robot stop?` for 2000 ms.
2. Pause 2000 ms.
3. Make Player say `It needed a byte!` for 2000 ms.

1000 ms is one second; 2000 ms is two seconds. The speech duration keeps a bubble visible but does not make the following block wait. The pause delays the next instruction in this event. It does not stop all other events or directional movement. See the [Week 1 timing explanation](Beginner_Week_1_Teacher_Reference.md) and [Pause reference](https://arcade.makecode.com/reference/loops/pause).

Another speech action on the same sprite can replace the current bubble. During acceptance tests, press A once and wait until both messages finish, then test B separately. Rapid input and protection against simultaneous sequences are beyond today's core goal; no custom lock variable is required.

### B as a useful help action

Add a B pressed event with one short message, for example `Arrows: move. A: joke.` for 3000 ms. Adapt wording to the student's actual A action; a guide might use `Arrows: move. A: tip.` Students may write in Estonian.

B is today's small new win. It practises choosing an event and reusing a sprite reference, rather than introducing another game mechanic. Startup instructions can mention B in the Upgrade.

## Student challenge ladder

### Mission — reliable character controls

**Brief:** Your existing character should move, remain visible, give two readable messages on A and explain its controls on B.

**Steps:** Verify movement → add boundary protection if missing → repair A timing if needed → add or improve B help → test separately. Keep the student's own art and messages.

**Success checks:**

- Restart creates one visible character.
- All four directions work; holding at an edge keeps the character visible.
- One A press shows first message, a readable wait, then second message.
- After A has finished, one B press gives a controls/help message matching the project.
- Student identifies one event and explains why its action belongs there.

**Hint:** “Which container should own this action?” A startup greeting is optional for the Mission if it was not reached in Lesson 1. Repeated tests and explanations matter more than adding blocks.

### Upgrade — discoverable controls

**Brief:** Make a startup introduction that tells a new player how to move and use A and B. Keep it short. If there are two startup messages, put a pause between them.

**Test:** A partner restarts and reads instructions before touching controls, then finds movement and both actions without spoken coaching.

**Hint:** “What does your player need to know first?” Test one restart; keep instructions readable rather than adding a long story.

### Challenge — a matching B response

**Brief:** B changes the background and gives a matching help or personality message. Keep the help understandable and A's sequence working.

**Test:** Run B, wait, then A once. Restart and repeat. Explain which setting persists until another background action or restart changes it.

**Hint:** “Put the colour action and B speech inside the same B event.” This uses known event placement and the Scene background block; demonstrate the background block if the student has not used it before.

### Boss — a character another person can use

**Brief:** Design a small guide, comedian or helper using only today's blocks. Give it clear instructions and distinct A/B purposes. Record three tests with expected and actual results, then improve one confusing behaviour.

**Test:** A peer restarts, discovers controls and tests A and B separately. Creator explains the repair and repeats the failed test successfully.

**Hint:** “Ask what your tester could not understand, then change one thing.” More characters, random answers, scores and animations are not needed.

## Extra task menu

Choose one task at a time after the Mission works. These practise the same concepts; no student needs to finish them all.

| Task | Suggested time | Test / reasoning |
|---|---|---|
| Readability editor | 3–5 min | Shorten one message or adjust time; partner reads it comfortably and creator explains the change |
| One-change speed experiment | 5–7 min | Try movement speeds 50 and 100 in both fields; compare control using the same route, then choose one |
| Two moods | 5–8 min | A sets one background before its sequence; B sets another before help; test A, wait, B, wait, A |
| New two-part joke or tip | 5–8 min | Change only A's text; predict and test the order without removing its pause |
| Wait experiment | 4–6 min | In a copy, shorten the pause while keeping speech duration; observe replacement, then restore readable timing |
| Startup versus button | 5–7 min | Move a short extra message between startup and B; predict and test, then keep the intended version |
| Navigator's specification | 6–8 min | Partner specifies one message and its event; creator implements and both compare expected/actual result |
| Instructions in Estonian | 4–6 min | Rewrite controls accurately in Estonian; another student can operate the project from those instructions |

For the speed experiment, demonstrate the Controller speed fields first. Keep coordinate changes, tilemaps, overlap, score and conditions for their later lessons. Do not require students to finish Lesson 1's long extra menu before moving on.

## Debugging quick reference

| Symptom | Likely cause | First check / repair |
|---|---|---|
| Character missing after reopening | Wrong project/account or missing creation | Check project identity, then creation in startup; use recovery copy if retrieval fails |
| Character visible but does not move | Movement block absent, wrong variable or speed 0 | Select the created sprite; inspect vx/vy; focus simulator |
| Only horizontal movement works | Vertical speed is 0 | Set a suitable positive vy and retest up/down |
| Character leaves the screen | Stay-in-screen off or applies to another sprite | Select Player and turn the flag on after creation |
| A shows only the last message | No pause or pause too short | Match the wait to the first message's display duration |
| A does unexpected extra speech | Duplicate A handlers | Inspect each event dropdown; consolidate intended A sequence |
| B does nothing | Wrong input, wrong event or loose speech block | Use visible B, check B pressed and block attachment |
| Another character speaks | Wrong sprite reference | Compare creation and speech dropdowns |
| B help appears then disappears during A | A's waiting sequence continues and replaces it | Test separately; wait for A to finish before B |
| More characters appear on each button press | Creation inside event | Create once in startup; restart and retest |
| Startup instructions cannot be read | Too short, too long or replaced | Shorten text, increase display time and pause between messages |

### Three prepared bug hunts

**Bug A — the horizontal-only character.** In a copied demo, set movement to vx 80, vy 0. Expected: all four directions work. Students predict which directions fail, change only vy to 80 and test again. Teacher answer: horizontal and vertical speeds are separate settings.

**Bug B — help is attached to A.** Put joke and help in separate A pressed handlers; leave no B handler. Expected: B gives help. Teacher answer: change the intended help event to B pressed. Moving that stack around the workspace will not change its trigger.

**Bug C — missing first sentence.** Remove the pause between A messages. Expected: both messages readable in order. Teacher answer: insert pause 2000 ms after the first 2000 ms speech. Changing speech duration alone does not delay the second action.

Give one bug at a time, preferably after a student's Mission works. Use expected → actual → suspect one block → change → retest. Preserve working originals; do not ask students to break their only saved project.

## Teacher block recipes

These are arrangements to build in Blocks, not executable code. Replace `mySprite` with the actual character reference. Message text and image choices are examples.

### Mission recovery arrangement

**On start:**

1. Set `mySprite` to a visible small gallery image of kind Player.
2. Move `mySprite` with buttons, vx 80 and vy 80.
3. Set `mySprite` stay in screen ON.

**On A button pressed:** Say first line for 2000 ms → pause 2000 ms → say second line for 2000 ms.

**On B button pressed:** Say `Arrows: move. A: joke.` for 3000 ms.

Create the sprite before configuring it. Existing startup greetings and backgrounds may remain if they are readable and do not obstruct separate tests.

### Upgrade arrangement

Keep Mission; append startup speech `Arrows: move. A: joke. B: help.` for 3000 ms. If preserving a greeting, use greeting for 2000 ms → pause 2000 ms → controls for 3000 ms. Shorten or split controls if necessary for the bubble.

### Challenge arrangement

Keep Mission/Upgrade. Inside B, set background colour, then say a matching short help message for 3000 ms. Optional A background setting belongs before its first speech. No new sprite is created.

### Acceptance test record

| Test | Expected | Actual / repair |
|---|---|---|
| Restart; wait for startup to finish | One character; optional instructions readable | ___ |
| Move in four directions; hold at edges | Movement works; character remains visible | ___ |
| A once; wait at least four seconds | First sentence, readable wait, second sentence | ___ |
| B after A finishes | Help matches actual controls | ___ |
| Restart and repeat a repaired test | Initial state restored; repair still works | ___ |

The Mission uses the control tests and one explanation. Boss students record three selected tests; everyone need not fill in the whole table on paper.

## Supporting a class of 27

Use individual projects with a short partner test, or 13 pairs and one trio. In pairs, driver handles input and navigator predicts; switch every 7–8 minutes. The trio's tester records expected/actual behaviour; rotate roles. Ask each student to explain one event or perform one repair, including students who did not drive.

Prioritise access problems, no visible character, no movement, then broken A timing, then B. A working Mission can move to the menu independently. Do not turn quick finishers into permanent assistants.

Use the help sentence: “I expected …; it did …; I tried …”. Encourage one change and a retest. Permit direct teacher help for access or prolonged confusion.

**Estonian language support:** event — sündmus; sequence — käskude järjekord; pause — paus / ooteaeg; movement — liikumine; testing — testimine; debugging — vigade leidmine ja parandamine. Keep English block names visible; accept explanations in Estonian.

**Unplugged fallback:** Use a paper screen and a character token. Startup cards place the character; arrow cards move it; a boundary card keeps it visible. A triggers two message cards with a wait card between; B triggers controls. Programmer predicts, robot performs, tester compares. Move a card into the wrong event and repair it. This rehearses today's concepts without introducing coordinates early.

## Saving and exit evidence

Begin at minute 54, earlier if the backup route needs longer. Follow the school's already-tested account and storage workflow; do not assume browser-local storage survives terminal logout.

1. Check the Week 2 project name and owning account.
2. With Cloud Sync, check the latest edits have saved; reopen and locate a distinctive change such as the B message.
3. If Cloud Sync is unavailable, export the full project, upload to approved school storage, then retrieve/import the remote copy and check the latest change. A file remaining in Downloads is not sufficient.
4. Each partner retains their own copy using the tested copy/import route and verifies it under their account. Do not edit one project from simultaneous sessions.
5. Record the actual project name/location and “I changed … because …”; sign out of shared terminals.

If both routes fail, the teacher captures exports in an approved persistent location before logout. Record unresolved access problems. See [Cloud Sync](https://arcade.makecode.com/identity/cloud-sync) and the curriculum's persistence routine.

**Exit prompts:** What creates the character? What runs only after B? Why is a pause between A's messages useful? What did your test make you change? Ask one or two per student while circulating; do not hold a long whole-class interrogation at saving time.

## Teaching record and Week 3 decision

Date ___ · Present ___ / 27 · Existing project retrieved ___ · Recovery starter used ___

- Movement and A baseline verified: ___
- Mission completed: ___; completed independently / with help: ___ / ___
- Can distinguish startup, A and B events: ___
- Can explain speech duration versus pause: ___
- Partner test led to a specific improvement: ___
- Saving verified / unresolved: ___ / ___
- Successful extra tasks: ___
- Specific students needing a short repair: ___
- Week 3 adjustment: ___

Use the curriculum's approximate 20-of-27 completion-and-explanation signal, adjusted for attendance; it is not a pass mark. If many students still need event or timing support, start Week 3 with a ten-minute repair and cut teleport/clue extensions. With a larger gap, make the next meeting another controls/remix lesson and shift coordinates later. Students ready for more can refine the same character with the extra menu while others receive support. No required homework.

## Official references and revision log

Movement and stay-in-screen documentation was checked for this reference on 13 October 2026. Rehearse the other blocks and saving workflow before class. Task designs, timings and progression decisions are classroom adaptations.

- [Controller movement](https://arcade.makecode.com/reference/controller/move-sprite)
- [Stay in screen](https://arcade.makecode.com/reference/sprites/sprite/set-stay-in-screen)
- [Button events](https://arcade.makecode.com/reference/controller/button/on-event)
- [Sprite speech](https://arcade.makecode.com/reference/sprites/sprite/say)
- [Pause](https://arcade.makecode.com/reference/loops/pause)
- [Cloud Sync](https://arcade.makecode.com/identity/cloud-sync)

| Version | Date | Change |
|---|---|---|
| 1.0 | 13 October 2026 | Created from Lesson 1 feedback: continue existing characters, consolidate movement/events/timing, add B help, protect testing and saving, and provide recovery and optional tasks |
