# Performance and memory operations

## Normal mode

**Select a sound:** <kbd>NORMAL</kbd> → <kbd>PLAY</kbd> → <kbd>INTERNAL</kbd> (or insert a card and press <kbd>CARD</kbd>) → bank key **A–H** + number **1–8**. With a ROM card, pressing <kbd>CARD</kbd> again toggles card bank 1/2. A new RAM card must be formatted first (3-06).

**Write a single patch:**

1. Select the patch to write (internal, card, or the Compare/Recall buffer).
2. Hold <kbd>WRITE</kbd>: the display shows *WRITE VOICE DATA – SELECT MEMORY!* and the INTERNAL/CARD indicators go out.
3. While still holding, press <kbd>INTERNAL</kbd> or <kbd>CARD</kbd>, then a bank key and number.
4. "OK!" appears when finished.

If memory protect (3-01) is ON, the display shows "PROTECT ON – SET MENU 3 01!": switch it OFF, re-enter PLAY and write again. If you used COMPARE/RECALL while editing, make sure its indicator is **ON** before writing.

**Edit:** press the **MENU** key of the function you want (chapter 4).

## Combination mode

{{fig:key_assign|The 8 key-assign configurations.}}

**Choose a key assign:** in Combination PLAY press the **value keys** (the slider does not work here); configurations cycle.

| Display | Mix out | Line out 1 | Line out 2 | Phones L | Phones R |
|---|---|---|---|---|---|
| 1+2 | 1+2 | 1 (8) | 2 (8) | 1 (8) | 2 (8) |
| 3+4 | 3+4 | 3 (8) | 4 (8) | 3 (8) | 4 (8) |
| 1+2+3+4 | 1+2+3+4 | 1+2 (4) | 3+4 (4) | 1+2 (4) | 3+4 (4) |
| 1/3 | 1/3 | 1 (8) | 3 (8) | 1 (8) | 3 (8) |
| 1/3+4 | 1/3+4 | 1 (8) | 3+4 (4) | 1 (8) | 3+4 (4) |
| 1+2/3 | 1+2/3 | 1+2 (4) | 3 (8) | 1+2 (4) | 3 (8) |
| 1+2/3+4 | 1+2/3+4 | 1+2 (4) | 3+4 (4) | 1+2 (4) | 3+4 (4) |
| 1/2/3/4 | 1/2/3/4 | 1/2 (4·4) | 3/4 (4·4) | 1/2 (4·4) | 3/4 (4·4) |

Numbers in parentheses = polyphony. With cross-fade, each sound has 8-note (2 patches) or 4-note (4 patches) polyphony.

**Choose patches:** in PLAY, move the cursor to a patch position, press <kbd>INTERNAL</kbd> or <kbd>CARD</kbd>, then bank + number. Positions that are not active in the current key assign show no name (selecting "1/3+4" hides position 2). If **two or more CARD patches** are chosen, the second and later ones do not sound until you press <kbd>COMBINATION</kbd> once more.

**Write one patch of a combination:** select its position, hold <kbd>WRITE</kbd>, then <kbd>INTERNAL</kbd>/<kbd>CARD</kbd> + bank + number.

**Write the combination to operation memory:** Combination → PLAY → hold <kbd>WRITE</kbd> → press <kbd>OPERATION MEMORY</kbd> → (still holding) <kbd>INTERNAL</kbd>/<kbd>CARD</kbd> + bank + number. This is impossible while COMPARE/RECALL is ON ("C/R ON CHECK VOICE NO.!"), or with memory protect ON. Name the operation with 2-00 and re-write it.

**Edit one patch of a combination:** PLAY → cursor on the patch → <kbd>MENU 1</kbd> (sound data) or use Menu 2 (effects).

## Operation memory mode

* **Copy from Normal/Combination:** write as above (Normal PLAY → hold <kbd>WRITE</kbd> → <kbd>OPERATION MEMORY</kbd> → destination).
* **Copy operation → operation:** select the source, hold <kbd>WRITE</kbd>, select destination bank + number (the operation write must be performed in PLAY).
* **Edit an existing operation or a card/preset sound:** in Operation Memory mode select it, hold <kbd>WRITE</kbd> and press <kbd>COMBINATION</kbd> or <kbd>NORMAL</kbd>. This writes it into the working buffer so all functions except 2-00 and 2-10 can be edited; then write it back normally.

## Multi Channel mode

Eight **areas**; areas 1–4 go to Line Out 1 / Phones L, areas 5–8 to Line Out 2 / Phones R; the mix output carries all.

| Task | How |
|---|---|
| Assign a patch | Press <kbd>MULTI CHANNEL</kbd>, choose the AREA with <kbd>MULTI AREA</kbd>, then <kbd>INTERNAL</kbd>/<kbd>CARD</kbd> + bank + number. Two or more CARD patches: press <kbd>MULTI CHANNEL</kbd> again to load |
| Polyphony | Cursor to POLY, set with value controls. Maximum total is 8 notes for areas 1–4 and 8 for areas 5–8 (lower another area if the value will not rise) |
| Volume | Cursor to LEV (99 = same as master volume) |
| MIDI channel | Cursor to CH, set channel with value controls |
| Pitch | 2-18 (per area) |

These settings are per area; switch areas at any time with <kbd>MULTI AREA</kbd>.
