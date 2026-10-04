# Beginner MakeCode Arcade Week 1 Teacher Reference

Editable lesson companion · Version 1.0 · 4 October 2026

For the teacher of 27 beginners aged 10–13, teaching in Estonian with English blocks and materials. This expands Week 1 of **Beginner MakeCode Arcade Curriculum Weeks 1 to 8** and follows the structure of the intermediate reference: quick lookup first, then detailed exercises, extra tasks, debugging answers and teaching records.

**Today’s project:** Talking character. **Essential learning:** create a sprite, run a short startup sequence and attach actions to button events. A student succeeds when they can make a character greet the player, make A trigger a different message, and explain which code runs automatically and which waits for a button press. Extensions are choices, not a checklist or a ranking of children.

## At a glance

| Need | Quick answer or action |
|---|---|
| First visible win | A Player sprite appears in the simulator |
| Minimum finished project | One sprite; startup greeting; different message on A |
| Four lesson levels | Mission: greeting and A; Upgrade: B and background; Challenge: two messages in order; Boss: character another student can use independently |
| Required categories | Sprites, Scene, Controller; Loops for the Challenge's pause |
| Main concept | `on start` runs at startup; `on A button pressed` runs in response to an event |
| Main debugging checks | Correct event, attached blocks, correct sprite variable, readable speech duration |
| Important timing detail | Speech duration is not a pause; insert `pause` between consecutive speech messages |
| Evidence of understanding | Predict startup and A behaviour before testing |
| Saving | `B_W01_TalkingCharacter_ID`; verify Cloud Sync or export to school cloud storage |
| Time limit | Stop features at minute 57 and protect saving time |

## MakeCode essentials for this lesson

### The editor and simulator

Use [MakeCode Arcade](https://arcade.makecode.com/), with the **Blocks** editor. The simulator shows the running game; the toolbox contains available blocks; the workspace contains the program. A tutorial may show a smaller toolbox than an ordinary project. Do not switch students to JavaScript or Python in this lesson.

Start a new project, name it and keep the code workspace simple. Students drag a block from a toolbox category and connect it inside an event container. Clicking text fields edits messages; dropdowns select a button, event type or sprite. The image square opens the sprite art editor.

Code edits may cause the simulator to restart. When comparing behaviour, make a deliberate restart and wait for the greeting to finish before testing buttons. Use the visible on-screen A and B controls first. Demonstrate keyboard equivalents on the actual school setup rather than assuming students should press the literal keyboard letters A and B. If keyboard input goes into the editor, click the simulator to give it focus.

### Sprites and images

A sprite is an object in the game, such as a character. Its image is what it looks like. Creating a sprite and drawing its image are related but different actions: the creation block makes the game object; the art editor changes its appearance.

Find the **Sprites** block resembling `set mySprite to sprite [image] of kind Player` and put it in `on start`. Choose a visible gallery image for the first build. Cap guided drawing at about two minutes; personalise after the character's behaviour works.

The new sprite starts near the centre of the screen. If a second sprite is created, it may occupy the same place and hide the first. Multiple characters and coordinates are optional future work, not needed today.

**Player** is a sprite kind: a category used by game rules. It does not automatically give movement, speech or a score. Arrow-button movement requires its own instruction in Week 2.

### The sprite variable

`mySprite` is a variable holding a reference to the created sprite. In today's language: “This name lets later blocks find our character.” Select the same name in all speech blocks. There is no need to teach general variable arithmetic yet.

Creating the sprite should happen before code tries to make it speak. Keep its creation at the top of `on start`, before any pause or speech. Do not put creation inside the A event: that would create more sprites when the player presses A.

If a student renames `mySprite` to `robot`, use the variable rename operation and check that later blocks refer to `robot`. The name used in code is separate from the character's fictional name in its greeting.

### Startup and sequence

`on start` holds setup instructions. Inside that stack, instructions run from top to bottom. For this lesson, create the sprite, set a background, then show the greeting.

`on start` runs again when the game restarts. It does not continuously repeat while the game is running. A startup message can disappear after its display duration while the character remains.

Do not teach that every stack in the workspace executes left to right. Separate event containers run when their respective events occur; their position on the workspace does not determine when a button is pressed.

### Button events

An event is something happening that can trigger code. Find **Controller** → the block resembling `on A button pressed`. Place the A-message block **inside** it. The event container can sit separately from `on start`; it does not need to connect underneath startup code.

An empty event container has no action. A loose action block does not become button behaviour merely by sitting near the event; snap it into the container. Disabled or grey action blocks should be inspected.

For the main lesson, use **pressed**: an action when the button changes from up to down. **Released** triggers on letting go. **Repeated** is intended for repeated actions while a button is held. Ask students to press, release and press again during tests.

An event is not an `if` statement students have to check manually. The game responds to the button event. Conditions and loops come later.

### Speech and text

Find the **Sprites** speech block resembling `mySprite say "Hello!" for 1000 ms`. Current editors may expose extra fields with a small expand control. Use the normal sprite speech bubble, not a full-screen dialog. Keep text short enough to read on the small screen and use animation off initially if that option is visible.

A message is text; students edit its text field. It appears near the sprite rather than in a Python-style console. Start with 1000 ms for a very short greeting; use 2000–3000 ms for instructions or a longer sentence. Prefer rewriting a long message into short sentences over fitting a paragraph into a bubble.

Each sprite has a current speech bubble. A later speech action for that sprite can replace its earlier bubble. Messages from A, B and startup can therefore interrupt one another. First test one event at a time; wait for each sequence to finish.

### Milliseconds and pauses

| Value | Time |
|---|---|
| 500 ms | Half a second |
| 1000 ms | One second |
| 2000 ms | Two seconds |
| 3000 ms | Three seconds |

**Display duration and waiting are different.** The speech duration controls how long the bubble remains visible; it does not delay the next instruction in the stack. Two speech blocks next to each other can replace the first message before the player reads it.

For the two-message Challenge, demonstrate **Loops** → `pause (ms)` before students need it. Use this order inside the same A event:

1. Say the first message for 2000 ms.
2. Pause for 2000 ms.
3. Say the second message for 2000 ms.

The pause makes that sequence wait before its next instruction. It does not freeze every other event in the game. Keep this explanation concrete; scheduling and protection against overlapping button actions are beyond today's core objectives.

### Background and parameters

Find **Scene** → `set background color to [colour]`. A parameter is a setting supplied to an action: colour, speech text or duration. Changing a parameter changes what an instruction does without requiring a new type of block.

Put a background setting in `on start` for the initial colour. Put one in a button event if that button should change it. Avoid using the same colour for the character and background if it makes the character hard to see.

### Debugging

A bug is a difference between the intended and actual behaviour, even when the project runs. Teach: **predict → test → inspect → change one thing → retest**.

Ask: “What did you expect? What happened? Which event should contain this action?” A child who can give those answers is practising programming thinking, even if the project still needs help.

Undo is useful after a mistaken change. Keep the working project before making deliberately broken copies. Do not use the browser Back button as the normal editing undo action.

### Small vocabulary bridge

| English | Estonian classroom cue | Meaning today |
|---|---|---|
| sprite | sprait or mängutegelane | Game object represented by an image |
| image | pilt | Appearance of the sprite |
| block | plokk | One instruction or container |
| sequence | käskude jada | Instructions followed in order |
| event | sündmus | Something that triggers code |
| variable | muutuja | Name we use to find our character |
| input | sisend | Player action such as pressing A |
| output | väljund | Visible response such as speech |
| pause | paus | Wait before the next instruction |
| bug | viga | Unexpected or incorrect behaviour |

## Questions students may ask

| Question | Teacher answer or demonstration |
|---|---|
| Is the sprite the same as its picture? | The sprite is the game object; its picture is its appearance. Change the art and its button behaviour can stay the same. |
| Why do arrow keys not move it? | Creating a Player does not add movement. We will add the movement instruction next week. |
| Why does the greeting happen again? | The simulator restarted, so startup code ran again. |
| Why does A do nothing? | Check that the message is inside the A pressed event, uses the right sprite, and that input reaches the simulator. |
| Why does the speech disappear? | Its display time ended. Increase the duration if it is too short to read. |
| Why do I only see the second sentence? | The second speech block replaces the first immediately. Put a pause between them. |
| Why does B interrupt A? | Both events are telling the same sprite to speak. Test them separately for now. |
| Why does holding A not repeat my action? | `pressed` responds to a new press. Release and press again; `repeated` is a different event option. |
| Why is the block grey or faded? | Check that it is enabled and connected inside an executable event stack. A nearby loose action is not enough. |
| Can I call it anything? | Yes. Choose a fictional character name and a short code variable name. They do not have to match. |
| Can I make a score or enemies? | Yes, later. Today make the character respond reliably first. |
| Is pressing A saving my project? | No. Playing the game and saving its code are separate actions. |
| Is Download enough to keep my work? | Only if the downloaded project is then stored somewhere persistent. Files left on this terminal disappear at logout. |
| Why are my projects missing after sign-out? | Cloud projects are shown when signed into their owning account. Sign into the correct account and check again. |

## Preparation and lesson timing

Before class, test the school account sign-in, Cloud Sync status and a fresh-session reopening. Prepare a teacher demo and a recovery project containing only a visible Player sprite in `on start`. Keep these in approved persistent storage. Put the challenge menu and saving steps where students can see them without asking.

Rehearse the A and B controls, background setting, speech expansion and pause block in the current editor. For the demo, use short fictional text, a gallery sprite and a plain background. The first win should be the character appearing by about minute 8.

| Minutes | Teacher and student activity |
|---|---|
| 0–5 | Show startup greeting and A action. Students predict what happens without a button press. |
| 5–12 | Sign in and name the project. Create the sprite, then add background and greeting, running after each addition. Show the A event. |
| 12–30 | Mission milestones: character visible, greeting visible on restart, different message on A. Visit students without a visible sprite first. |
| 30–40 | Students choose extensions. Demonstrate speech → pause → speech before assigning the Challenge. |
| 40–50 | Partners predict and test each other's button actions. Continue a chosen task while the teacher checks individual explanations. |
| 50–57 | Show two projects and repair one event-placement bug. Keep demonstrations short. |
| 57–60 | Stop features, check cloud status or upload export, reopen and confirm a distinctive change, sign out. |

If logins consume more time than expected, shorten extensions and sharing. Use the verified export-and-cloud-upload fallback rather than relying on browser storage. If every student needs a manual upload, begin saving earlier than minute 57; three minutes is a target for a rehearsed workflow, not a reason to leave unsaved work.

## Main exercises

The block arrangements below are descriptions to recreate in **Blocks**, not code to paste. Block wording can vary slightly with editor language or version.

### Guided starter A character appears

**Time:** About 5–7 minutes after access is working. **Student brief:** Make a character appear. Give it a short greeting.

1. Open a new Arcade project and name it `B_W01_TalkingCharacter_ID`.
2. In `on start`, add `set mySprite to sprite [image] of kind Player`.
3. Choose a ready-made visible image and run. First win: a character on screen.
4. Add `set background color to [colour]` underneath creation.
5. Add `mySprite say "Hello!" for 1000 ms`. Restart and look for the greeting.

**Success:** Character and greeting are visible. **Hint:** “Which block actually creates your character?” If needed, supply the one-sprite recovery project and let the student add the greeting.

### Mission Greeting and A message

**Time:** About 12–18 minutes, including testing. **Student brief:** Your character introduces itself when the game starts. Pressing A makes it say something different.

**Build milestones:**

1. Keep the creation and startup greeting working.
2. Drag `on A button pressed` from Controller into the workspace as its own event container.
3. Add a speech block inside A, selecting the same `mySprite`.
4. Choose a message different from the greeting and give it enough reading time.

**Example:** Startup says `Hello! I am Bolt.` A says `I lost my space hamster!`.

**Tests:** Restart without pressing buttons: greeting appears. Wait for it to finish, press A: the second message appears. Release A, wait, and press A again: it works again. Restart: the introduction returns.

**Hint ladder:** “Which action happens immediately?” → “Which container should wait for A?” → Show an empty A event and ask the student to place the speech inside it.

**Teacher check:** Student points to the startup stack and the A event, then predicts each one's behaviour. A working button response is the core outcome; decorative art is optional.

### Upgrade Add B and change the background

**Time:** About 4–7 minutes. **Student brief:** Give B its own message and choose a different starting background. Keep A and the greeting working.

Add `on B button pressed` with a different speech message. Change the startup background colour to suit the character. If ready, also add a background change inside B, but this is optional.

**Tests:** Restart, then test A, then B, waiting between actions. Both buttons must produce their intended message. **Hint:** “Duplicate the idea of A, then change the button dropdown and the message.” Check that duplication has not left two A handlers instead of A and B.

### Challenge Two sentences in order

**Time:** About 6–10 minutes. **Student brief:** A should tell a tiny joke or two-part story. The player must be able to read the first sentence before the second appears.

Inside **one** A event, place:

1. `mySprite say "Why did the robot stop?" for 2000 ms`
2. `pause 2000 ms`
3. `mySprite say "It needed a byte!" for 2000 ms`

Explain and demonstrate pause first. It is the small timing addition that makes this challenge possible; no loop is needed despite the toolbox category being called Loops.

**Tests:** Predict the order, press A once, and watch both sentences. Wait for the sequence to finish before trying again. Reverse the two speech blocks and predict how the joke changes, then restore the intended version.

**Hint:** “What makes the instructions wait before the next speech?” **Success:** Both messages are readable in the intended order. Increasing only the speech durations does not solve immediate replacement.

### Boss An independently usable character

**Time:** About 10–15 minutes. **Student brief:** Build a small character experience with a startup introduction and useful A and B actions. Give another student enough instructions to discover both actions without your spoken help.

Use only the demonstrated creation, background, speech, events and pause blocks. Example roles: A tells a joke; B gives advice. Provide a readable startup instruction such as `A: joke  B: advice`, after the introduction if necessary with a pause.

**Constraints:** One character, a clear startup introduction, distinct A and B responses, and understandable instructions. More blocks are not automatically better.

**Tests:** A partner restarts and uses the character without coaching. Ask which actions they found, which message was unclear, and one change that would help. Test buttons separately; handling rapid or overlapping inputs is beyond the core brief.

**Success:** Partner finds both actions, and the creator explains an event and a sequence. **Hint:** Design the messages and button meanings on paper before adding blocks.

## Extra task menu

Choose one task at a time. Times assume a working Mission. Tasks 1–16 use the core blocks and the demonstrated pause; tasks 17–20 add small optional features and need a teacher demonstration first. They are alternatives for students who finish quickly, not required work.

### Quick modifications

**1. New personality · 3–5 minutes.** Turn the character into a pirate, detective or friendly monster by changing art and messages. **Check:** Both startup and A still work and the messages fit the same personality. **Hint:** Change appearance and behaviour separately, testing after each.

**2. Readable greeting · 3–5 minutes.** Ask a partner to read the greeting. Adjust wording and duration until they can read it comfortably. **Check:** Explain why you changed text or time. **Hint:** A shorter message can be clearer than a much longer duration.

**3. Colour detective · 3–5 minutes.** Try three background colours with the same sprite. Choose the clearest contrast. **Check:** Explain the choice without saying only “I like it.” **Hint:** Can you still see the outline and face?

**4. Button labels · 4–6 minutes.** Make the startup message tell the player what A and B do. **Check:** A partner can predict both actions from the instructions. **Hint:** Keep the labels short enough for the bubble.

### Reasoning and testing

**5. Predict before pressing · 4–6 minutes.** Write or say the expected result of restart, A, B, then restart again. Run those tests in order. **Check:** Explain any mismatch. **Hint:** Identify the event before looking at the message.

**6. Move the message · 4–6 minutes.** Move one speech action from A to startup. Predict what changes, test, then move it back. Use a pause if startup now contains two messages. **Check:** The student explains why placement changes timing. **Hint:** Near an event is not inside it.

**7. One thing experiment · 4–6 minutes.** Change only speech time, only text, then only background. Test after each change. **Check:** Identify what changed and what stayed the same. **Hint:** One change makes cause and effect easier to see.

**8. Reorder a story · 5–7 minutes.** With two speech blocks separated by a pause, swap the sentences. Predict the result. **Check:** Explain which order makes sense and restore it. **Hint:** Instructions inside one stack follow their order.

**9. Press versus hold · 4–6 minutes.** Test one A press, holding A, then release and press again, keeping the event on `pressed`. **Check:** Explain the difference between a new press and continued holding. **Hint:** Watch the event dropdown; do not change it yet.

**10. Rename the character reference · 4–6 minutes.** With the teacher's variable rename demonstration, change `mySprite` to a descriptive name such as `robot`. Check every speech block. **Check:** Behaviour stays the same. **Hint:** The variable identifies the sprite; its spelling is not spoken automatically.

### Longer creative tasks

**11. Two-part joke · 6–10 minutes.** Invent another joke for B using speech → pause → speech. **Check:** Both parts can be read and A still works. **Hint:** Draw two message cards and place a wait card between them.

**12. Tiny tour guide · 7–10 minutes.** Startup introduces a guide; A gives one tip; B gives another. **Check:** A new user finds both tips from the introduction. **Hint:** Clear button meanings matter more than a long story.

**13. Robot instructions · 7–10 minutes.** A gives a two-step instruction such as “Look up” then “Wave”; B explains how to start again. Use only on-screen messages, with no requirement for the game to detect a real-world action. **Check:** A partner follows the order. **Hint:** Messages describe actions; they do not sense whether the human performed them.

**14. Two moods · 7–10 minutes.** A changes background and says a cheerful message; B changes background and says a sleepy message. **Check:** A, B, A consistently select the intended background/message pair. **Hint:** Put both actions inside the corresponding button event.

**15. Three-beat introduction · 8–12 minutes.** Startup shows three short messages in order, separated by pauses; the last explains A and B. **Check:** Restart and read all three without pressing buttons. **Hint:** You need a wait between adjacent messages, not just a duration on each.

**16. Designer and tester · 8–10 minutes.** One partner specifies a greeting and two button responses; the other builds them. Swap roles with a new theme. **Check:** Each partner predicts one event and proposes a test. **Hint:** Agree on expected behaviour before touching the blocks.

### Optional new blocks

Demonstrate the new block and its location first. Keep a working copy before experimenting. These do not turn the main lesson into a movement, collision or scoring lesson.

**17. Costume change · 6–10 minutes.** Learn the Sprites `set mySprite image to [image]` action. A gives the character one appearance, B another, with matching messages. **Check:** The same character changes appearance rather than new sprites accumulating. **Hint:** Set its image instead of creating it again.

**18. Press and release face · 6–10 minutes.** After learning `released`, make A pressed show one image and A released restore the original. **Check:** Hold A, then release it slowly; both events work. **Hint:** Separate event containers respond to different moments of the same button action.

**19. Brief celebration · 5–8 minutes.** Learn a sprite `start effect` action with a short duration such as 500 ms. Add it to a button response. **Check:** Speech stays readable and the effect stops. **Hint:** Start with one short effect; more effects can obscure the character.

**20. Silent comic · 7–10 minutes.** Using the demonstrated image-change block, make a two-image reaction sequence separated by a pause, then display a final short message. **Check:** A partner describes the image order and its meaning. **Hint:** Keep all steps inside one event; this is a hand-built sequence, not an animation extension.

## Debugging reference and bug hunts

| Symptom | Likely cause | First check |
|---|---|---|
| No visible character | Creation missing, disconnected or image hard to see | Check creation in startup and choose gallery art |
| Greeting works but A does nothing | Wrong event/button or action outside event | Inspect A pressed container and simulator input |
| Speech on the wrong character | Wrong sprite variable selected | Compare creation name and speech dropdown |
| Only final message visible | Consecutive speech actions replace each other | Insert a pause between messages |
| Speech too brief | Duration too small or another event replaced it | Test once without other input, then adjust time |
| A and B appear swapped | Incorrect button dropdowns or messages | Compare each event with its intended label |
| Background changes at startup rather than on B | Setting in wrong container | Move it into B if that is the intended rule |
| New character appears after each press | Creation placed inside button event | Create once in startup; reuse the sprite |
| Unexpected behaviour while pressing rapidly | Event sequences interrupt or overlap | Test one press and wait; simplify the sequence |
| Run-time error mentioning a sprite | Sprite used before creation or wrong reference | Create first and inspect selected variable |
| Project missing next session | Wrong account or work only saved locally | Check owning account and remote backup |

Give one deliberately broken example at a time. Ask students to predict, observe and explain a repair rather than guess random blocks.

### Bug A The greeting waits for A

**Setup:** Creation is in startup, but both the introduction and button message are inside A, separated by a pause. Nothing speaks on restart.

**Expected:** A greeting without a button press. **Teacher answer:** Move the greeting to startup, after creation. Keep the different A response in A. Test a restart before touching the controls.

### Bug B B behaves like A

**Setup:** Duplicate the A event to create B behaviour, but leave its dropdown on A.

**Expected:** A and B have separate actions. **Teacher answer:** Change the second event to B pressed. Two A handlers can both react; ordering their separate stacks on the workspace does not fix the incorrect event choice.

### Bug C The missing first sentence

**Setup:** A contains two timed speech blocks with no pause.

**Expected:** Both sentences readable in order. **Teacher answer:** Insert a pause matching the first message's display duration. Extending that duration alone does not make the next instruction wait.

### Bug D A loose action

**Setup:** A speech block sits outside the A event and is disabled or disconnected.

**Expected:** A causes speech. **Teacher answer:** Snap the action into the event. Move the event itself separately if needed; event containers do not connect underneath one another.

### Bug E The disappearing instruction

**Setup:** Startup instructions use 100 ms instead of 2000 ms.

**Expected:** User can read the controls. **Teacher answer:** Increase the duration and shorten the text if necessary. Ask the student to explain the unit: 1000 ms is one second.

### Bug F Creating instead of changing

**Setup:** A creates a new Player sprite each time, then makes it speak.

**Expected:** One persistent character responds. **Teacher answer:** Keep one creation in startup and make A use that sprite. Restart to remove the extra sprites from the previous run, then test A again.

## Teacher reference arrangements

These are block recipes, not executable text. Use them to prepare a demo or a recovery copy. Students can choose their own messages, art and colours.

### Mission arrangement

**On start**, in this order:

1. Set `mySprite` to a visible sprite image of kind Player.
2. Set background colour to a contrasting colour.
3. Make `mySprite` say `Hello! I am Bolt.` for 2000 ms.

**On A button pressed:**

1. Make `mySprite` say `I lost my space hamster!` for 2000 ms.

### Upgrade arrangement

Keep the Mission. Change its startup background as desired. Add:

**On B button pressed:**

1. Make `mySprite` say `Please bring snacks.` for 2000 ms.

An optional background-setting action can precede the B message.

### Challenge arrangement

Keep startup and B. Replace the single A message with:

1. Say `Why did the robot stop?` for 2000 ms.
2. Pause 2000 ms.
3. Say `It needed a byte!` for 2000 ms.

### Boss arrangement

**On start:** Create sprite → set background → say `Hello! I am Bolt.` for 2000 ms → pause 2000 ms → say `A: joke  B: advice` for 3000 ms.

**On A pressed:** First joke line for 2000 ms → pause 2000 ms → punchline for 2000 ms.

**On B pressed:** Say `Never feed a robot soup.` for 3000 ms.

Acceptance test: restart and wait through the introduction; test A once and wait; test B once. A peer should discover both actions from the instructions. There is no requirement for the program to count jokes, pick random answers or remember conversation history.

## Classroom support for 27 beginners

Pair work fits as 13 pairs and one trio when everyone attends. Driver controls the mouse and keyboard; navigator reads and predicts; in the trio, the tester checks behaviour. Rotate roles every 7–8 minutes. For individual work, use a short partner testing session around minute 40.

Circulate first to children without a visible sprite, then those whose button event does not work. A working Mission can go straight to the menu instead of waiting for you. Ask each child one brief prediction question, including navigators; a successful shared project alone does not show that both understand it.

For students needing support, supply the one-sprite starter and ask them to add only a greeting and one A response. Use event containers like labelled baskets: “At the start” and “When A is pressed.” Keep messages short and allow a gallery image.

The help sentence is: “I expected …; it did …; I tried …”. Encourage looking, one change and a neighbour's test, while allowing direct teacher help when needed. Account problems should come straight to the teacher.

**Unplugged fallback:** Give students a character card and instruction cards. One event card says “At the start”; another says “When I clap”. A student robot performs the corresponding instructions; a pause card adds a short wait. Move an instruction into the wrong event, predict the result, and repair it. A trio can act as programmer, robot and tester. Keep instructions simple and accessible.

## Saving and exit check

MakeCode Cloud Sync requires sign-in. Browser-local saving is not sufficient for school terminals that are wiped after logout. Sign-in alone is not the verification: check the project's cloud status and saved changes.

1. Stop adding features at minute 57, or earlier if the fallback upload takes longer.
2. Check the name `B_W01_TalkingCharacter_ID`, using a school-approved identifier.
3. For the primary route, confirm the correct account and that the cloud status shows the latest changes saved.
4. Reopen the project and locate a distinctive latest edit, such as its B message or chosen image.
5. If Cloud Sync is unavailable, export/download the full project using the tested school workflow, upload it to the school cloud folder, then retrieve/import the remote copy and check it. A file left in Downloads is not preserved.
6. Each partner should retain their own project copy using the rehearsed import/copy workflow and check that it saves under their account. Do not have several sessions edit the same project simultaneously.
7. Record “I changed … because …” and sign out of the shared terminal.

If students worked in a skillmap, use its **Save to My Projects** route to bring the result into the full editor before relying on it as the class project. Verify the resulting project and cloud status. Tutorial progress and the final editable project are related but should each be checked in the workflow you use.

If both cloud routes fail, the teacher must capture exports into an approved persistent location before terminal logout. If preservation is impossible, use the unplugged design activity. Do not promise that anonymous browser storage will survive.

**Exit questions:** What runs at startup? What runs after A? Why is the pause needed between two messages? Students completing only the Mission need answer only the first two. An unfinished extension is fine when the core behaviour works and is preserved.

## Teaching record

Date: ___ · Present: ___ / 27 · Mission completed: ___ / 27

- Students who can distinguish startup and button events: ___
- Students needing help with block attachment or sprite selection: ___
- Speech timing misunderstandings: ___
- Access and saving problems and resolutions: ___
- Extra tasks that worked well: ___
- Partner rotation or participation issues: ___
- Changes to make before Week 2: ___

If fewer than roughly 20 of 27 students complete the Mission and explain the event distinction, start Week 2 with a 10-minute repair/remix and reduce extensions. This is a planning signal, not a grade. No required homework; optional activities are inventing another message or drawing a character on paper.

## Official references

These links support teacher preparation; they are not a requirement to finish whole tutorials during this lesson. The task briefs above are original classroom adaptations.

- [Beginner's Guide educator notes](https://arcade.makecode.com/skillmap/educator-info/basic-map-info) — use the initial orientation and storytelling activities selectively; the guide links to its tutorial paths.
- [MakeCode orientation](https://arcade.makecode.com/courses/csintro1/intro/makecode-orientation) — interface and project workflow.
- [Create a sprite](https://arcade.makecode.com/reference/sprites/create) — sprite creation and kind.
- [Button events](https://arcade.makecode.com/reference/controller/button/on-event) — pressed, released and repeated.
- [Sprite speech](https://arcade.makecode.com/reference/sprites/sprite/say) — speech text and duration.
- [Pause](https://arcade.makecode.com/reference/loops/pause) — waiting between instructions.
- [Microsoft sprite implementation](https://github.com/microsoft/pxt-common-packages/blob/master/libs/game/sprite.ts) — teacher technical reference confirming speech updates a bubble rather than pausing execution; not student reading.
- [Cloud Sync](https://arcade.makecode.com/identity/cloud-sync) — sign-in, status and cross-computer persistence.

## Revision log

| Version | Date | Change |
|---|---|---|
| 1.0 | 4 October 2026 | Expanded Week 1 into a teacher reference with four main levels, 20 extra tasks, block recipes, bug answers and saving checks; made the pause between consecutive speech messages explicit |
| | | |
