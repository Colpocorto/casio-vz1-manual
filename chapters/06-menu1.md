# Menu 1 reference: sound editing

Available in **Normal** and **Combination** modes. Spec bars: *Domain · Pages · Graphic · Related*.

## 1-00 LINE
<div class="spec">Domain: per line · Pages 1 · Graphic no</div>

| Parameter | Values |
|---|---|
| INT LINE | MIX / RING / PHASE |
| EXT PHASE | ON / OFF (lines B–D, i.e. modules M3–M8) |

Sets the configuration of the four lines (chapter 3). A diagram shows the line; press a module selector to view another line. Hold <kbd>LINE</kbd> to see all lines (letters in parentheses mean "A is used as external phase of B", etc.). Initializing this function resets all 8 modules to MIX, EXT PHASE OFF.

## 1-01 WAVE FORM
<div class="spec">Domain: modular · Pages 1 · Graphic no</div>

FORM = SINE / SAW1 / SAW2 / SAW3 / SAW4 / SAW5 / NOISE1 / NOISE2. Waveform sets the basic timbre of each module. **Sine** is purest (fundamental only). **Saw 1** is the "buzzy" wave with harmonics in decreasing amplitude (Saw 1 has the least upper harmonics, Saw 5 the most). **Noise 1** contains all harmonics (non-pitched static); **Noise 2** is static with the fundamental pitch present.

*Copy*: select 1-01 and the source module, hold <kbd>WRITE</kbd>, press the destination module selector. *Initialize*: select the module, hold <kbd>WRITE</kbd>, press <kbd>YES</kbd> (back to SINE).

## 1-02 DETUNE
<div class="spec">Domain: modular · Pages 1 · Graphic no</div>

| Parameter | Values | Notes |
|---|---|---|
| PITCH FIX | ON / OFF | ON = fixed pitch, same note for every key |
| HARMONIC | 1–63 | Harmonic ratio relative to the standard frequency (1 = no detune) |
| POLARITY (POL) | + / − | Tune above/below standard |
| OCTAVE (OCT) | 0–5 | 1-octave steps |
| NOTE | 00–11 | Semitone steps (100 cents) |
| FINE | 00–63 | ≈1.6-cent steps |
| RANGE (PITCH FIX ON) | ×1 / ×1/16 | Keyboard-pitch range of the fixed-pitch sound |

Detune some modules to make a "thick" sound or emphasise harmonics. With NOTE/FINE the harmonic is no longer exact (arrows ↑/↓ by HARMONIC show slightly higher/lower). PITCH FIX is good for the "attack" of instruments. Copy/initialize works as in 1-01 (initialized = PITCH FIX OFF).

## 1-03 ENVELOPE (DCO)
<div class="spec">Domain: global · Pages 3 · Graphic yes · Related 1-04, 1-05</div>

| Parameter | Values |
|---|---|
| STEP | S1–S8 |
| RATE | 0–99 |
| LEV | −63…+63 |
| SS / ED | sustain step (<kbd>INTERNAL/SUSTAIN</kbd>) / end step (<kbd>CARD/END</kbd>) |

The **pitch envelope** of all modules, up to 8 steps. Level 00 = no pitch change; positive rises, negative falls. Real depth is scaled by 1-04 (at maximum, ±63 ≈ more than 5 octaves). A **sustain point** holds pitch until the key is released; the next step becomes the release. The end point starts at step 8 and can be moved; steps after it are removed. To delete an SS/ED, move the cursor to the step and press the same key. Initialize: select 1-03 + module, hold <kbd>WRITE</kbd>, <kbd>YES</kbd>; this also initializes PITCH ENV in 1-17.

## 1-04 ENV DEPTH (DCO)
<div class="spec">Domain: global · Pages 1 · Graphic no · Related 1-03, 1-05</div>

RANGE = WIDE / NARROW; ENV DEPTH = 00–63. WIDE: level units are 100 cents (±5 octaves). NARROW: 25-cent units (≈ ±1 octave max). Depth 63 = envelope as set in 1-03; 00 = no pitch change.

## 1-05 KF LEVEL (DCO)
<div class="spec">Domain: global · Pages 2 · Graphic yes · Related 1-16, 1-03, 1-04</div>

POINT P1–P6, KEY C0–C9, LEV 00–63. Six-point **key follow curve** that scales the pitch-envelope depth with the key played (A4 is the centre; keys move in semitones). Higher LEV raises the contour, lower flattens it.

{{fig:kf_curves|Key-follow curves with the factory example values for DCO, DCA and rate.}}

## 1-06 VELOCITY LEVEL (DCO)
<div class="spec">Domain: global · Pages 1 · Graphic yes · Related 1-03, 1-04, 1-05</div>

SENSITIVITY 00–31 and CURVE 1–8: how key velocity scales the DCO envelope level for all modules. 00 = no velocity response; 31 = maximum. CURVE chooses the response shape (below, same curves as 1-12 and 1-17); the graphic display shows the curve and does not change with SENSITIVITY.

{{fig:velocity_curves|The 8 velocity curves (schematic).}}

## 1-07 VIBRATO (DCO)
<div class="spec">Domain: global · Pages 1 · Graphic yes · Related 2-15</div>

| Parameter | Values | Meaning |
|---|---|---|
| WAVE | TRIANGLE / SAW UP / SAW DOWN / SQUARE | Triangle: smooth up/down. Saw up: repeating rise from the fundamental. Saw down: repeating "swoop" down. Square: trill between original and higher pitch |
| DEPTH | 00–99 | 00 = no vibrato; raise it before altering other settings |
| RATE | 00–99 | Speed |
| DELAY | 00–99 | Time before vibrato starts |
| MULTI | ON / OFF | ON: each note's vibrato is independent (ensemble sound). OFF: synchronized across keys |

## 1-08 OCTAVE
<div class="spec">Domain: global · Pages 1 · Graphic no</div>

OCTAVE = −2 / −1 / 0 / +1 / +2: shifts all 8 modules. At 0, with Detune HARMONIC = 1, pitch is standard (A4 = 442 Hz).

## 1-09 ENVELOPE (DCA)
<div class="spec">Domain: modular · Pages 2 · Graphic yes · Related 1-10, 1-11</div>

STEP S1–S8, RATE 00–99, LEV 00–99, SS, ED. The **amplitude envelope** of each module. Behaviour as 1-03 (sustain/end points, delete by pressing the key again). If the module line is PHASE or EXT PHASE, the DCA envelope shapes **timbre** of the following module instead of loudness. Copy copies DCA data (1-10, 11, 12, 14, 17) to the destination module. Initializing resets 1-09 and 1-17 (AMP ENV steps).

## 1-10 ENV DEPTH (DCA)
<div class="spec">Domain: modular · Pages 1 · Graphic no</div>

ENV DEPTH 00–99. Raises/lowers the whole DCA envelope contour (overall level of the module), without changing its shape.

## 1-11 KF LEVEL (DCA)
<div class="spec">Domain: modular · Pages 2 · Graphic yes · Related 1-09, 1-10</div>

As 1-05 but for loudness: POINT 1–6, KEY C0–C9, LEV 00–99, per module.

## 1-12 VELOCITY LEVEL (DCA)
<div class="spec">Domain: modular · Pages 1 · Graphic yes · Related 1-09, 1-10, 1-11, 2-12</div>

SENSITIVITY 00–31, CURVE 1–8. Velocity control of the amplifier level per module (curves as 1-06). With **2-12 VEL INVERSE = ON** the displayed curve is inverted too.

## 1-13 TREMOLO
<div class="spec">Domain: global · Pages 1 · Graphic yes · Related 1-14</div>

Same parameters as vibrato (WAVE, DEPTH, RATE, DELAY, MULTI) but modulates **volume**. Triangle: pulsating; saw up: repeated rise then cut; saw down: repeated swoop down; square: on/off. Per-module depth is set in 1-14.

## 1-14 AMP SENSITIVITY
<div class="spec">Domain: modular · Pages 1 · Graphic no · Related 1-13, 2-03…2-06</div>

SENSITIVITY 0–7 per module: how much each module is affected by TREMOLO DEPTH, and by the **after touch / wheel / pedal** controls for tremolo depth and DCA envelope bias. 0 = no effect; 7 = strongest.

## 1-15 TOTAL LEVEL
<div class="spec">Domain: global · Pages 1 · Graphic no · Related 2-07</div>

TOTAL LEV 00–99: the maximum volume of the whole patch (all modules). At 00 nothing sounds even with VOLUME at MAX.

## 1-16 KF RATE (DCO/DCA)
<div class="spec">Domain: global · Pages 1 · Graphic yes · Related 1-05, 1-03, 1-11, 1-09</div>

POINT P1–P6, KEY C0–C9, RATE (displayed signed, e.g. +22 … +99). Key-dependent modification of envelope **rates** for both DCO and DCA envelopes. Where the value is high, "attack"/"decay" is quicker; where low, the envelope rate equals what is set in 1-03/1-09.

## 1-17 VELOCITY RATE (DCO/DCA)
<div class="spec">Domain: pitch = global, amp = modular · Pages 3 · Graphic yes · Related 1-03, 1-09</div>

| Page | Parameters |
|---|---|
| 1 | SENSITIVITY 00–31 (global, all modules); CURVE 1–8 |
| 2 | PITCH ENV: STEP 1–8, ENA = E / * (global) |
| 3 | AMP ENV: STEP 1–8, ENA = E / * (per module) |

Velocity speeds up envelope rates. At SENSITIVITY 00 the effect is off. The curve's horizontal axis adds to the rate: the higher the velocity, the faster the rate. Enable a step with <kbd>YES</kbd> ("E"), disable with <kbd>NO</kbd> ("*"). Steps after the END point are not displayed. Pages can be initialized independently.

## 1-18 VOICE NAME
<div class="spec">Domain: global · Pages 1 · Graphic no</div>

Names a patch (up to 12 characters of A–Z, 0–9 and the marks ". – /"). See *Entering names*.
