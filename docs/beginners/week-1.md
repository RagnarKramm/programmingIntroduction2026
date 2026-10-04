---
title: "Beginner Arcade · Week 1"
nav_order: 4
description: "Build a talking character with sprites, startup instructions and button events."
---

# Week 1: Talking character

Build a character that introduces itself and responds to the player. Use **MakeCode Arcade's Blocks editor** for this lesson.

**Your main goal:** one visible character, a startup greeting, and a different message when A is pressed. Explain what runs automatically and what waits for a button press. Extensions are optional choices.

## Jump to the help you need

- [Starter: a character appears](#starter-a-character-appears)
- [Theory: how the blocks work](#theory-how-the-blocks-work)
- [Mission: greeting and A message](#mission-greeting-and-a-message)
- [Upgrade: B and background](#upgrade-b-and-background)
- [Challenge: two sentences in order](#challenge-two-sentences-in-order)
- [Boss: a character anyone can use](#boss-a-character-anyone-can-use)
- [Debugging: find and fix a problem](#debugging-find-and-fix-a-problem)
- [Save your work](#save-your-work)

## How to read the examples

The examples below are **block recipes to recreate**, not text to paste into the editor. An indented line belongs **inside** the event above it. Create separate event containers for startup, A and B.

| What you need | Toolbox category | Block to look for |
|---|---|---|
| Startup container | Loops | `on start` — usually already in a new project |
| Create character | Sprites | `set mySprite to sprite [image] of kind Player` |
| Speech bubble | Sprites | `mySprite say [text] for [time] ms` |
| Background | Scene | `set background color to [colour]` |
| Button event | Controller | `on A button pressed` — change dropdown to B for B |
| Wait between messages | Loops | `pause [time] ms` |

Wording may vary slightly with editor language or version. Expand the speech block's options if needed to find its duration. Use ordinary sprite speech bubbles; keep animation off initially if that option is visible.

## Starter: a character appears

1. Open [MakeCode Arcade](https://arcade.makecode.com/) and create a new project.
2. Name it `B_W01_TalkingCharacter_ID`, replacing `ID` with your school-approved identifier.
3. Stay in **Blocks**. Add the sprite creation block inside `on start`.
4. Click its image square and choose a visible gallery character. Check the simulator: can you see it?
5. Add a contrasting background and a short greeting underneath creation.

### Complete block arrangement

```text
on start
    set mySprite to sprite [choose a gallery image] of kind Player
    set background color to [choose a contrasting colour]
    mySprite say "Hello!" for 1000 ms
```

**Expected:** restarting shows one character and a short `Hello!` bubble. After one second the bubble disappears, but the character stays.

**Try it:** change the greeting, restart, and check the new message. Personalise the art after the behaviour works.

## Theory: how the blocks work

### Editor, toolbox and simulator

The **toolbox** contains blocks you can choose. The **workspace** holds your program. The **simulator** shows the running game.

Drag an action into its event container and snap it into place. A loose action near an event is not inside that event. Edit text fields and dropdowns to change an instruction's settings.

Edits may restart the simulator. For a clear test, deliberately restart, watch the greeting, then test the buttons. Use the simulator's visible A and B controls first. Keyboard controls depend on the setup demonstrated by your teacher; do not assume the keyboard letters A and B are the game controls. Click the simulator if keyboard input is going into the editor.

### Sprite, image and variable

A **sprite** is a game object. Its **image** is what it looks like. The creation block makes the object; the image editor changes its appearance.

`mySprite` is a **variable** that lets later blocks find that character. Every speech block should select the same variable that the creation block uses.

- Create the sprite first, at the top of `on start`.
- Create it once; button events should use the existing sprite.
- The kind `Player` is a category. It does not automatically add movement, speech or score.
- Arrow movement needs a separate instruction in a later lesson.
- A second sprite can appear in the same place and hide the first. One character is enough today.

The character can introduce itself as Bolt while its code variable remains `mySprite`. These names serve different purposes. If you rename the variable, use the editor's rename operation and check every speech block.

### Startup and sequence

`on start` runs when the game starts or restarts. Its instructions run **from top to bottom**. It does not keep repeating.

```text
Create character → set background → show greeting
```

Creating first matters: speech needs an existing character. Separate event containers do not run according to their left-to-right position in the workspace.

### Events: responding to the player

An **event** is something that happens and triggers code. `on A button pressed` waits for an A press, then runs the actions inside it.

| Container | When its actions run |
|---|---|
| `on start` | At startup or restart |
| `on A button pressed` | When A changes from up to down |
| `on B button pressed` | When B changes from up to down |

Keep the button dropdown on **pressed** today. **Released** responds when you let go; **repeated** supports repeated actions while holding. To test `pressed` again, release the button and press again.

An event container can sit separately from startup. It does not connect beneath `on start`. An empty event does nothing. You do not need an `if` statement or a loop to detect today's button presses.

### Text, durations and parameters

Speech is text displayed in a bubble near the character. Keep messages short enough to read on the small screen.

Text, colour and time are **parameters**: settings supplied to a block. Changing a parameter changes what that action does.

| Duration | Reading time |
|---|---|
| 500 ms | Half a second |
| 1000 ms | One second |
| 2000 ms | Two seconds |
| 3000 ms | Three seconds |

Use 1000 ms for a very short greeting and 2000–3000 ms for longer messages. Shorten long text rather than filling the bubble with a paragraph.

### Speech time is different from a pause

**Speech duration controls visibility. A pause delays the next instruction.**

A sprite has one current speech bubble. Two speech actions immediately after each other can make the second replace the first before you read it. Giving the first message more display time alone does not make the sequence wait.

```text
say first message for 2000 ms
pause 2000 ms
say second message for 2000 ms
```

The pause waits before the next instruction in this sequence. It does not freeze every other event. Another button's speech can replace the same character's bubble, so test one event at a time and wait for it to finish.

### Vocabulary

| English | Estonian | Meaning today |
|---|---|---|
| Sprite | sprait / mängutegelane | A game object with an image |
| Image | pilt | The character's appearance |
| Block | plokk | An instruction or container |
| Sequence | käskude jada | Instructions followed in order |
| Event | sündmus | Something that triggers code |
| Variable | muutuja | A name used to find our character |
| Input | sisend | A player action, such as pressing A |
| Output | väljund | A visible response, such as speech |
| Pause | paus | Waiting before the next instruction |
| Bug | viga | Incorrect or unexpected behaviour |

## Mission: greeting and A message

**Task:** introduce the character at startup. Make A trigger a different message.

Build one milestone at a time: visible character → startup greeting → A response. Test each milestone before continuing.

### Complete block arrangement

```text
on start
    set mySprite to sprite [choose a gallery image] of kind Player
    set background color to [choose a contrasting colour]
    mySprite say "Hello! I am Bolt." for 2000 ms

on A button pressed
    mySprite say "I lost my space hamster!" for 2000 ms
```

**Why it works:** startup creates the sprite and introduces it. The separate A event uses that same sprite only when A is pressed. The greeting and response have different text.

**Test:**

1. Restart without pressing buttons: see the introduction.
2. Wait for the bubble to disappear, then press A: see the hamster message.
3. Release A, wait, and press again: see the message again.
4. Restart: the introduction returns.

**If stuck:** find the A event, check its dropdown says `A` and `pressed`, then snap the speech action inside it. Select `mySprite` in the speech block.

## Upgrade: B and background

**Task:** keep startup and A working. Choose a different starting background and give B its own message.

### Complete block arrangement

```text
on start
    set mySprite to sprite [your chosen image] of kind Player
    set background color to [your new contrasting colour]
    mySprite say "Hello! I am Bolt." for 2000 ms

on A button pressed
    mySprite say "I lost my space hamster!" for 2000 ms

on B button pressed
    mySprite say "Please bring snacks." for 2000 ms
```

**Why it works:** A and B have separate event containers. The starting background belongs in startup because it should be set without a button press.

**Test:** restart, wait, test A, wait, then test B. Each must show its intended message.

**Optional:** add a background-colour action before the speech inside B if B should also change the scene. Restart sets the original background again.

**If stuck:** if you duplicated A, change the duplicate's button dropdown to B. Two A events do not give you a B response.

## Challenge: two sentences in order

**Task:** make one A press tell a two-part joke. Both parts must remain readable.

### Complete block arrangement

```text
on start
    set mySprite to sprite [your chosen image] of kind Player
    set background color to [choose a contrasting colour]
    mySprite say "Hello! I am Bolt." for 2000 ms

on A button pressed
    mySprite say "Why did the robot stop?" for 2000 ms
    pause 2000 ms
    mySprite say "It needed a byte!" for 2000 ms

on B button pressed
    mySprite say "Please bring snacks." for 2000 ms
```

**Why it works:** the pause inside A delays the punchline until the question has been displayed for two seconds. The block is in the Loops category, but no loop is used here.

**Test:** press A once. Read the question, then the punchline. Wait for both to finish before testing again or pressing B.

**Try it:** predict what happens if you swap the two speech blocks while keeping the pause between them. Test, then restore the joke.

**If stuck:** seeing only the punchline usually means the pause is missing, too short, or outside the A event. Use one A container with speech → pause → speech.

## Boss: a character anyone can use

**Task:** make a startup introduction, clear controls, and different A and B actions. A partner should discover both actions without your spoken help.

### Complete block arrangement

```text
on start
    set mySprite to sprite [your chosen image] of kind Player
    set background color to [choose a contrasting colour]
    mySprite say "Hello! I am Bolt." for 2000 ms
    pause 2000 ms
    mySprite say "A: joke  B: advice" for 3000 ms

on A button pressed
    mySprite say "Why did the robot stop?" for 2000 ms
    pause 2000 ms
    mySprite say "It needed a byte!" for 2000 ms

on B button pressed
    mySprite say "Never feed a robot soup." for 3000 ms
```

**Why it works:** startup shows the introduction before the controls. A runs a two-step joke sequence; B gives advice. The controls tell a new player what each button does.

**Partner test:** ask someone to restart and use the character without coaching. Let them finish reading each sequence before pressing another button. Ask which actions they found and which instruction could be clearer.

**If stuck:** plan the greeting, control labels, joke and advice on paper first. Keep one character and short messages. Rapid or overlapping inputs do not need to be solved today.

## Debugging: find and fix a problem

**Predict → test → inspect → change one thing → retest.**

Use the help sentence: “I expected …; it did …; I tried …”.

| Problem | First check or repair |
|---|---|
| No character | Create the sprite inside startup; choose visible gallery art and a contrasting background |
| Greeting only appears after A | Move the greeting into startup after creation |
| A does nothing | Check A pressed, an attached speech action, the sprite variable, and simulator input focus |
| B does nothing but A triggers extra actions | Change the duplicated event's dropdown from A to B |
| Speech block is loose or faded | Snap it inside the intended event and check it is enabled |
| Wrong character speaks | Select the same variable used by the creation block |
| Only the last sentence appears | Put a pause between the speech actions inside the same event |
| Message disappears too quickly | Test without other presses; increase duration and shorten text |
| A and B messages are swapped | Compare each event's button dropdown and message |
| Background changes at the wrong time | Move the colour action into startup or the intended button event |
| More sprites appear after each press | Remove creation from the button event; create once in startup, then restart |
| Runtime error mentions a sprite | Create the sprite before using it and check the variable selection |
| Buttons interrupt a story | Test one press at a time and wait for the sequence to finish |
| Arrow keys do not move the Player | Movement needs its own instruction; it is not required today |

### Repair a missing wait

This arrangement is incorrect for a readable two-part story:

```text
on A button pressed
    mySprite say "I have a secret." for 2000 ms
    mySprite say "I am made of potatoes." for 2000 ms
```

Repair it by adding one block:

```text
on A button pressed
    mySprite say "I have a secret." for 2000 ms
    pause 2000 ms
    mySprite say "I am made of potatoes." for 2000 ms
```

**Explain:** why does changing only the first speech duration fail to make the second instruction wait?

Use the editor's Undo after an accidental edit. Preserve a working copy before deliberately breaking a project; the browser Back button is not the normal editing undo action.

## Save your work

Playing the game and saving its program are separate actions. Browser-local storage alone is not enough on a school computer that is wiped after logout.

1. Check the name `B_W01_TalkingCharacter_ID` with your school-approved identifier.
2. If using Cloud Sync, check the correct signed-in account and confirm the latest changes show as saved.
3. Reopen the project and find a distinctive latest change, such as your B message or character image.
4. If Cloud Sync is unavailable, use the teacher's tested full-project export/download workflow. Upload the file to your school cloud folder, retrieve/import the remote copy, and check it. A file left in Downloads is not a preserved copy.
5. If working with a partner, each person should retain and check their own copy using the classroom workflow. Avoid editing one project in several sessions at once.
6. Record “I changed … because …” and sign out of the shared computer.

If working in a skillmap, use **Save to My Projects** to bring the result into the full editor, then verify that project and its saved status. Ask your teacher immediately if saving or account access fails.

**Before you finish, explain:**

- What runs when the game starts?
- What runs when A is pressed?
- If you built the Challenge, why is the pause needed?

A working Mission that you can explain and have saved is enough. You do not need every extension.
