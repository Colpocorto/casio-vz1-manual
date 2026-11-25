# Menu 2 reference: effects

Modes: **00** Operation Memory; **01–06** Normal, Combination, Multi Channel; **07–17** Combination; **18** Multi Channel. Functions that use "per patch" values show 1–4 entries matching the patch numbers of the current key assign.

## 2-00 OPERATION NAME
<div class="spec">Domain: operation memory · Pages 1 · Graphic no</div>

Names an operation memory (12 characters, same entry as 1-18). Only accessible in Operation Memory mode. After naming, **re-write** the sound to the operation memory. To initialize the name: hold <kbd>WRITE</kbd> and answer <kbd>YES</kbd>.

## 2-01 PORTAMENTO / SOLO
<div class="spec">Domain: global · Pages 1 · Graphic no</div>

| Parameter | Values | Notes |
|---|---|---|
| PORTM TIME | 0–99 | Glide time (or rate, see mode) |
| PORTM MODE | 0 / 1 | 0 = constant **time** (same glide time whatever the interval); 1 = constant **rate** (time grows with distance) |
| SOLO | ON / OFF | Last-note priority, one note sounds at a time |

Portamento with SOLO gives a mono-synth feel; with SOLO ON and a PORTM TIME above 00, portamento happens only on legato playing. Toggle 2-01 ↔ 2-07 with the cursor on the function number.

## 2-02 PITCH BEND
<div class="spec">Domain: global · Pages 1 · Graphic no · Related 3-05</div>

BEND RANGE 00–48 half-steps (4 octaves); RELEASE ENA/DIS. DIS: bend only keys being held. ENA: bend sound still sounding after key release. If 3-05 TOTAL BEND = ON, this function shows "DATA NOT USED – SET MENU 3 05".

## 2-03 AFTER TOUCH, 2-04 DEF WHEEL 1, 2-05 DEF WHEEL 2, 2-06 FOOT VR
<div class="spec">Domain: global · Pages 2 · Graphic no · Related 1-14</div>

All four functions share the same parameters; they only differ in the physical controller. After touch = extra key pressure at the bottom of the stroke. Wheel 2 is spring-loaded; wheel 1 stays. FOOT VR uses an optional VP-10 pedal.

| Parameter | Values | Effect when ON |
|---|---|---|
| SENSITIVITY | 00–99 (Normal, Multi); −99…+99 (Combination; negative = inverted) | Controller sensitivity; 00 = off |
| VIB DEPTH / VIB RATE | ON / OFF | Increases vibrato depth/rate set in 1-07 |
| PITCH | +ON / −ON / OFF | Bends pitch up (+) or down (−), max 1 octave at 99; independent of 2-01's bend range |
| PORTM TIME | ON / OFF | Increases portamento time |
| TREM DEPTH / TREM RATE | ON / OFF | Increases tremolo depth/rate (1-13) |
| A ENV BIAS | ON / OFF | Raises DCA envelope bias up to its set maximum |

Effects can already be present at the normal setting; the controller then makes them deeper or stronger. TREM DEPTH, TREM RATE and A ENV BIAS strengths are scaled per module by 1-14.

## 2-07 LEVEL (combination)
<div class="spec">Domain: combined sounds · Pages 1</div>

LEVEL 00–99 per patch: relative volume of each patch in a combination (00 = silent, 99 = maximum). Toggle with 2-01.

## 2-08 PITCH (combination)
<div class="spec">Domain: combined sounds · Pages 1</div>

POLARITY ±, OCTAVE 0–5, NOTE 00–11 (100-cent steps, max 1100 cents), FINE 00–63 (≈1.6 cents). Shifts the pitch of each patch; small FINE offsets between layered patches make a thick ensemble sound.

## 2-09 SPLIT POINT
<div class="spec">Domain: combined sounds (split) · Pages 1</div>

Single split: SP POINT C0–C9. Three splits: LOWER SP C0–B♭8, MIDDLE SP C#0–B8, UPPER SP D0–C9. If the key assign has no split, a "layered" display appears; exit by pressing <kbd>COMBINATION</kbd> and choosing a key assign with a split.

## 2-10 SUS PEDAL
<div class="spec">Domain: combined sounds · Pages 1</div>

SUSTAIN ENA/DIS per patch; patches set to DIS ignore the sustain pedal (SP-2 optional).

## 2-11 VEL SPLIT
<div class="spec">Domain: combined sounds (layered) · Pages 1</div>

RANGE 001–127 (from–to) per layered patch. A patch sounds only within its velocity range. Works only with key assigns containing layers ("1+2", "1/3+4"…).

## 2-12 VELOCITY INVERSE
<div class="spec">Domain: combined sounds (layered) · Pages 1 · Related 1-12</div>

INVERSE ON/OFF per patch: reverses the velocity-level curves of 1-12, so modules triggered by a soft touch now sound with a hard one. Not inverted when INT LINE = PHASE or EXT PHASE is set for that line.

## 2-13 POSITIONAL CROSSFADE
<div class="spec">Domain: combined sounds (layered) · Pages 1 · Graphic yes</div>

EFFECT ON/OFF and POS (from–to) C0–C9. For layered configurations ("1+2", "3+4", "1+2+3+4"): the patches fade into each other along the keyboard within a range (the cross position). With four layered patches three ranges (LOWER/MIDDLE/UPPER POS) exist. With cross-fade each sound has 8-note (two layers) or 4-note polyphony. Zoom in graphic mode: ×1…×4.

{{fig:xfade|Positional cross-fade.}}

## 2-14 DELAY TRIGGER
<div class="spec">Domain: combined sounds (layered) · Pages 1</div>

DELAY 00–99 per layered patch: delays its NOTE ON (00 = immediately; 99 = long delay).

## 2-15 VIBRATO INVERSE · 2-16 TREMOLO INVERSE
<div class="spec">Domain: combined sounds (layered) · Pages 1 · Related 1-07 / 1-13</div>

INVERSE ON/OFF per layered patch: inverts the phase of vibrato (pitch rises where it would fall) or tremolo (volume).

## 2-17 COMBI COPY
<div class="spec">Domain: combined sounds · Pages 1</div>

COPY n→m with EXECUTE. Copies the source patch's timbre and the effect data (2-01 to 2-16, except 2-09 and 2-13) to another patch position; confirm with <kbd>YES</kbd> ("OK!").

## 2-18 PITCH (multi channel)
<div class="spec">Domain: area (MIDI) · Pages 1</div>

POLARITY, OCTAVE 0–5, NOTE 00–11, FINE 00–63 per AREA. In Multi-Channel PLAY choose the AREA with <kbd>MULTI AREA</kbd>, then return with <kbd>MENU 2</kbd>.
