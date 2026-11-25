# Appendix A: initialized (factory) data {.nonum}

## Voice (per patch)

| Item | Initial value |
|---|---|
| INT LINE / EXT PHASE | MIX / OFF (all lines) |
| OCTAVE / TOTAL LEV | 0 / 99 |
| VIBRATO & TREMOLO | WAVE = 1 (triangle), DEPTH 00, RATE 75, DELAY 00, MULTI OFF |
| Wave form (all modules) | SINE |
| DETUNE | PITCH FIX OFF, HARMONIC 1, POL +, OCT 0, NOTE 00, FINE 00 |
| DCA envelope | RATE 99, 50, 50, 50, 50, 50, 50, 50 · LEV 99, 00 × 7 · SS/ED = SS on step 1, ED on step 8 |
| DCA ENV DEPTH | 99 |
| DCA KF LEVEL | KEY C2 F4 C7 A7 E8 C9 · LEV 99 × 6 |
| DCA VEL LEVEL | SENS 00, CURVE 1 |
| AMP SENS | 00 |
| DCO envelope | RATE 50 × 8 · LEV 00 × 8 · ENV DEPTH: NARROW, 63 |
| DCO KF LEVEL | KEY C2 F4 C7 A7 E8 C9 · LEV 63 × 6 |
| DCO VEL LEVEL | SENS 00, CURVE 1 |
| KF RATE | KEY C2 F4 C7 A7 E8 C9 · RATE 00 × 6 |
| VEL RATE | SENS 00, CURVE 1, all steps enabled as stored ("E/*" = "*") |

## System

| Item | Initial value |
|---|---|
| Operation memory / internal | 64 preset tones, 64 preset operation memories |
| Compare/Recall | preset voice A-1 |
| 3-00 | 442 Hz, transpose C |
| 3-01 | INTERNAL = ON, CARD = ON |
| 3-02 | SAVE, CARD, VC+OP |
| 3-03 | RECEIVE = 01, SEND = 01 |
| 3-04 | PROG No. = 0–127, EXCLUSIVE = DIS, CONT No. = OFF, VOLUME IN = ENA |
| 3-05 | TOTAL BEND = OFF, RANGE = 12, RELEASE = ENA |

## Menu 2

| Function | Initial value |
|---|---|
| 2-01 | PORTM TIME 00, MODE 0, SOLO OFF |
| 2-02 | BEND RANGE 02, RELEASE ENA |
| 2-03…06 | SENSITIVITY 50 (after touch: 20); all switches OFF |
| 2-07 / 2-08 | LEVEL 99 / POLARITY +, OCT 0, NOTE 00, FINE 00 |
| 2-09 | SP point B3; LOWER E3 / MIDDLE A♭4 / UPPER C6 |
| 2-10 | SUSTAIN ENA |
| 2-11 | RANGE 001–127 |
| 2-12 | INVERSE OFF |
| 2-13 | EFFECT OFF; POS C3–F5; L POS B♭2–F=3 (?); M POS D♭4–A4; U POS F5–D♭6 (see open points) |
| 2-14 | DELAY 00 |
| 2-15, 2-16 | OFF |
| 2-18 | POLARITY +, OCT 0, NOTE 00, FINE 00 |

!!! note
    Preset sound data is also on the ROM card: bank 2, **H-8 "INIT VOICE"** is the initialized voice.
