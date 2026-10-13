---
title: "Beginner Arcade · Week 2"
nav_order: 6
description: "Improve character controls, readable speech and help through prediction and testing."
---

# Week 2: Character controls and testing

Continue your Week 1 character in **MakeCode Arcade's Blocks editor**. Make it easy for another player to move it, hear its story and find help.

**Your main goal:** one character that moves in four directions, stays on screen, shows two readable messages on A and explains its controls on B. Predict a result, test it, and explain where one action belongs. Extensions are optional.

## Jump to the help you need

- [Starter: reopen and test](#starter-reopen-and-test)
- [Theory: controls, events and timing](#theory-controls-events-and-timing)
- [Mission: reliable character controls](#mission-reliable-character-controls)
- [Upgrade: discoverable controls](#upgrade-discoverable-controls)
- [Challenge: a matching B response](#challenge-a-matching-b-response)
- [Boss: a character another person can use](#boss-a-character-another-person-can-use)
- [Extra practice](#extra-practice)
- [Debugging](#debugging)
- [Save your work](#save-your-work)

## Starter: reopen and test

1. Open your saved Week 1 project using the classroom workflow. Check that it is your latest version.
2. Make a Week 2 copy using the teacher's demonstrated copy or export/import route. Name it `B_W02_CharacterControls_ID`, replacing `ID` with your school-approved identifier. Verify the copy before editing. If copying is unavailable, ask for help preserving your original and record the actual project name.
3. Restart. Try all four directions. Press A once and wait for its speech to finish.
4. Identify one missing or unclear behaviour. Keep working movement, artwork and messages.

If your old project is unavailable, ask for the teacher's recovery copy. You can also build the complete Mission arrangement below with gallery art. You only need one project today.

## Theory: controls, events and timing

The following examples are **block recipes to recreate**, not code to paste. Indented actions belong inside the event above them. Select your actual character variable wherever an example says `mySprite`.

| Toolbox | Block to look for | Purpose |
|---|---|---|
| Loops | `on start` | Set up the character when the game starts |
| Sprites | `set mySprite to sprite [image] of kind Player` | Create the character once |
| Controller | `move mySprite with buttons` | Add directional movement |
| Sprites | `set mySprite stay in screen ON` | Keep the character visible at the edges |
| Controller | `on A button pressed` / `on B button pressed` | Respond to that button |
| Sprites | `mySprite say [text] for [time] ms` | Show a speech bubble |
| Loops | `pause [time] ms` | Wait before the next instruction in that sequence |
| Scene | `set background color to [colour]` | Change the background |

Block wording may vary. Stay-in-screen may appear as a sprite flag dropdown; select **stay in screen** and turn it on. Expand movement options to see vx and vy.

### Movement and boundaries

Create the sprite first, then configure movement and stay-in-screen in `on start`. `Player` is a kind; it does not automatically enable movement. The movement block must refer to the sprite you created.

Use vx 80 and vy 80 as a starting point if movement is missing. These are horizontal and vertical **speeds**, not positions. A vertical speed of 0 prevents up/down movement. Keep existing speeds if they already work well. Stay-in-screen keeps the character at the screen boundary; it does not create walls.

Use the simulator's visible controls first. Follow the keyboard mapping demonstrated by your teacher; the keyboard letter A is not necessarily the game's A control. Click the simulator if the editor has keyboard focus.

### Which event owns the action?

`on start` runs at startup or restart. A pressed and B pressed run when their buttons are pressed. Actions inside one event run in order; moving separate event containers around the workspace does not change their triggers.

Create one character in startup and reuse it in the button events. If B already exists, improve it. Check event dropdowns before adding another handler: two A events do not give you a B action.

### Speech time and pause

1000 ms is one second. **Speech duration keeps the bubble visible; a pause delays the next instruction.** Without a pause, a second speech action can replace the first immediately.

```text
say first message for 2000 ms
pause 2000 ms
say second message for 2000 ms
```

The pause waits in this sequence. Movement and other events can still run. Another speech action on the same character can replace the bubble, so press A once, wait for both messages to finish, then test B separately. Keep messages short; test speech near the centre first.

| English | Estonian | Meaning today |
|---|---|---|
| Event | sündmus | Something that triggers actions |
| Sequence | käskude järjekord | Instructions in order |
| Movement | liikumine | Moving the character |
| Pause | paus / ooteaeg | Waiting before the next action |
| Testing | testimine | Comparing expected and actual behaviour |
| Debugging | vigade leidmine ja parandamine | Finding and repairing a problem |

## Mission: reliable character controls

**Task:** keep one movable character visible, make A show two readable messages, and make B give useful help. Complete only the missing parts of your existing project. A startup greeting is optional for this Mission.

Build and test in small steps: movement → screen boundary → A timing → B help.

### Complete block arrangement

```text
on start
    set mySprite to sprite [choose a visible gallery image] of kind Player
    move mySprite with buttons vx 80 vy 80
    set mySprite stay in screen ON

on A button pressed
    mySprite say "Why did the robot stop?" for 2000 ms
    pause 2000 ms
    mySprite say "It needed a byte!" for 2000 ms

on B button pressed
    mySprite say "Arrows: move. A: joke." for 3000 ms
```

Keep your own A messages if you already have them. B's wording must describe what your project actually does. You may write messages in Estonian.

**Why it works:** startup creates and configures one sprite. A reuses it for an ordered sequence with a wait. B reuses it for a separate help action.

**Test:**

1. Restart: one character appears.
2. Move in all four directions; hold each direction at its edge. The character remains visible.
3. Predict A's messages and order. Press A once and wait at least four seconds: both messages are readable.
4. After A finishes, press B once: help matches your controls.
5. Point to one changed action and explain why it belongs in that event.

**If stuck:** compare the sprite dropdowns with the creation block. Check that movement and stay-in-screen are after creation, and the pause is between both speech blocks inside one A event.

## Upgrade: discoverable controls

**Task:** add or improve startup instructions so a new player can find movement, A and B without spoken help.

Keep the Mission. Add this after startup setup:

```text
    mySprite say "Arrows: move. A: joke. B: help." for 3000 ms
```

If you keep a greeting before the instructions, use greeting for 2000 ms → pause 2000 ms → instructions for 3000 ms. Shorten or split long messages with a pause between them.

**Test:** a partner restarts, reads the instructions and finds all three controls. Change any unclear wording and repeat the test.

## Challenge: a matching B response

**Task:** B changes the background and gives a matching help or personality message. Keep the Mission working.

Replace your existing B contents with a colour action followed by speech:

```text
on B button pressed
    set background color to [choose a contrasting colour]
    mySprite say "Blue mood! Arrows: move. A: joke." for 3000 ms
```

Choose wording that matches your colour and controls. To restore a starting colour on restart, put a background-colour action in startup.

**Test:** press B, wait, then A once. Restart and repeat. The colour remains until another colour action changes it; restart restores a colour only if startup sets it. Explain why both new actions belong inside B.

## Boss: a character another person can use

**Task:** turn your character into a guide, comedian or helper with clear instructions and distinct A/B purposes. Use the blocks you already know.

Ask a partner to restart and operate it without coaching. Record three tests, improve one confusing behaviour or instruction, and retest.

| Test | Expected | Actual | Change and retest |
|---|---|---|---|
| Restart and read controls | ___ | ___ | ___ |
| Move to an edge | ___ | ___ | ___ |
| A once, wait, then B | ___ | ___ | ___ |

**Explain:** what did your tester find confusing, which action did you change, and how do you know the change helped?

## Extra practice

Choose one after your Mission works:

- **Readability editor:** shorten a message or adjust its display time. Have a partner read it and explain your choice.
- **Speed experiment:** try vx/vy 50, then 100, using the same route. Predict, compare, and choose the speed you prefer.
- **Two moods:** put one background action before A's speech and another before B's help. Test A, wait, B, wait, A.
- **New joke or tip:** change only A's text. Keep the pause and test the message order.
- **Wait experiment:** in a copy, shorten the pause while keeping speech duration. Observe what happens, then restore readable timing.

## Debugging

**Predict → test → inspect → change one thing → retest.** Ask for help with “I expected …; it did …; I tried …”.

| Problem | First check or repair |
|---|---|
| Missing character after reopening | Check the project/account, then creation in startup; ask for a recovery copy if needed |
| Character does not move | Check movement block, selected sprite, nonzero speeds and simulator focus |
| Only left/right works | Check that vy is positive, such as 80 |
| Character leaves screen | Turn stay-in-screen on for the correct sprite after creation |
| Only A's last sentence appears | Put a pause matching the first display duration between the speeches |
| B does nothing; A gives extra messages | Check duplicate A handlers; change the intended help handler to B pressed |
| Wrong character speaks | Use the same sprite variable as creation |
| B speech is interrupted by A | Wait for A's full sequence to finish before testing B |
| More characters appear after a press | Remove creation from button events; create once in startup |
| Instructions disappear too fast | Shorten them, increase duration and pause between consecutive speeches |

**Bug hunt:** a movement block has vx 80, vy 0. Predict which directions fail, repair one value, then test all four directions. Preserve your working project before deliberately introducing a bug.

## Save your work

Stop adding features for the final six minutes.

1. Check the name `B_W02_CharacterControls_ID` with your approved identifier, or record the actual name if you continued the original.
2. Use the teacher's tested save workflow. With Cloud Sync, check the correct account and latest saved status.
3. Reopen the saved project and find your latest B message or other distinctive change.
4. If Cloud Sync is unavailable, export/download the full project using the demonstrated route, upload it to your school cloud folder, retrieve/import that remote copy, and check it. A file left in Downloads or browser-local storage is not enough on a wiped school computer.
5. Each partner keeps and verifies their own copy. Record “I changed … because …” and sign out of the shared computer.

**Before you finish, explain:** which event sets up movement, which event gives help, why A needs a pause, and one expected result you tested.

A working Mission that you can explain and have saved is enough. Next lesson introduces coordinates; today is about reliable controls and testing.
