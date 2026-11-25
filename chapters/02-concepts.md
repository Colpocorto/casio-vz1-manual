# Concepts

## The four modes

{{fig:modes_flow|The four modes and how data moves between them.}}

| Mode | Purpose | Key facts |
|---|---|---|
| **NORMAL** | Single-patch performance and editing | One patch at a time. Write to internal memory (64) or a card. |
| **COMBINATION** | Build multi-timbral setups | A *work area* ("buffer") for up to **4 patches** with key assign (split/layer), velocity split, per-patch effects and levels. |
| **OPERATION MEMORY** | Store/recall complete setups | 64 memories holding patches, effects, splits and control-panel settings. Used together with Normal/Combination. |
| **MULTI CHANNEL** | MIDI multitimbral | Up to **8 areas**, each with its own patch, polyphony, level and MIDI channel. Total polyphony stays 16 notes. |

Each mode has a **PLAY** sub-mode (perform, select sounds) and **MENU 1/2/3** sub-modes (edit). Press a mode key, then a menu key (or PLAY).

!!! note "Typical workflow"
    1. Write/edit single patches in **Normal**. 2. Combine up to 4 in **Combination**. 3. Store setups in **Operation Memory**. 4. Optionally use **Multi Channel** from a sequencer.

## Memory map

| Memory | Contents |
|---|---|
| Internal | 64 voices (patches) — Normal mode |
| Operation memory | 64 setups |
| RAM card (RA-500) | 64 voices + 64 operations |
| ROM card (RC-100) | 128 voices + 128 operations (two banks of 64; press <kbd>CARD</kbd> again to switch) |
| Compare/Recall | Edit buffer holding the original sound; also up to 64 loaded presets via 3-07 |

## Glossary

| Term | Meaning |
|---|---|
| **Menu / Function / Parameter / Value** | Menu → function (two-digit number) → parameter (a variable setting) → value |
| **Module (M1–M8)** | One independent oscillator (DCO) with its own amplifier (DCA) |
| **Internal line** | A pair of modules: A = M1+M2, B = M3+M4, C = M5+M6, D = M7+M8 |
| **External phase** | Output of a line used as the phase input of the next line |
| **Patch (voice)** | Complete sound data produced by modules 1–8 |
| **Operation memory** | A full keyboard setup (up to 4 patches, splits, MIDI, controllers) |
| **Envelope** | A control value that changes over time, shaping pitch (DCO) or volume (DCA) |
| **DCO / DCA** | Digitally controlled oscillator / amplifier |
