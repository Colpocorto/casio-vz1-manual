# Tutorials

Three short exercises that teach the operating system by doing. Do them in order.

## A. Edit vibrato with graphic editing (1-07)

1. <kbd>NORMAL</kbd>, then select internal patch **C-3 "VZ-MONICA"**.
2. <kbd>MENU 1</kbd>; select **07 VIBRATO** with the value controls; press <kbd>MENU 1</kbd> again to access parameters.
3. DEPTH starts at **00** (no vibrato). Move the cursor to DEPTH and set about **60**.
4. Press <kbd>DISPLAY</kbd>: the triangle vibrato waveform is drawn. Move the cursor to **WAVE**, pick SQUARE, play: a trill. Hold a key; the vibrato starts after the DELAY (63).
5. Try DEPTH 99; the shape stays the same, only the size changes.
6. Compare with the original at any time using <kbd>COMPARE/RECALL</kbd>.
7. Press <kbd>DISPLAY</kbd> to leave graphic mode, then a mode/menu key to exit.

{{fig:waveforms|Vibrato/tremolo wave shapes (triangle, saw up, saw down, square) plus sine and noise.}}

## B. Shape a DCA envelope (1-09)

1. <kbd>NORMAL</kbd>, internal patch **C-7 "COOL ORGAN"**; <kbd>MENU 1</kbd>; function **09**.
2. Press <kbd>DISPLAY</kbd> for the graphic editor (you edit M1's envelope; switch off other modules to focus: module ON/OFF keys).
3. Change **RATE1** (try 99 → 87): the lower the rate, the gentler the slope. Change **LEVEL1** to 50: the first step now rises only to half volume.
4. Press <kbd>INTERNAL/SUSTAIN</kbd> on step 1 to make it a sustain point (SS); remove it to hear the difference.
5. Set RATE2 ≈ 36, LEVEL2 = 99; RATE3 = 70, LEVEL3 = 50; RATE4 = 40, LEVEL4 = 99 and press <kbd>INTERNAL/SUSTAIN</kbd> (SS). Press <kbd>CARD/END</kbd> to cancel the old end point; set step 5: RATE 20, LEVEL 00 and press <kbd>CARD/END</kbd> (ED).
6. Use the zoom (<kbd>MULTI AREA</kbd>) to see the whole envelope. Hold a key: it rises, drops, rises again and sustains; release and it falls.
7. Turn on M3 and compare envelopes with the ON/OFF keys.

{{fig:envelopes|The envelope built in this tutorial.}}

## C. Velocity rate (1-17) in brief

Select patch **G-5 "VZ TOUCH"** and go to **1-17**. *SENSITIVITY* (00–31) sets how much key velocity speeds the envelope; *CURVE* (1–8) chooses the response (see 1-17). On display page 2/3, enable the effect per envelope step with <kbd>YES</kbd> ("E") / <kbd>NO</kbd> ("*"). Enable all steps of the amp envelope on all modules to hear the global effect.

!!! note
    The last-used function of each menu is remembered: pressing <kbd>NORMAL</kbd> then <kbd>MENU 1</kbd> returns to where you stopped.
