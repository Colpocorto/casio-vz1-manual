# The iPD sound engine

The VZ-1's core is **iPD (Interactive Phase Distortion)**: **8 independent modules**, each a DCO + DCA, so each can produce a complete waveform with its own pitch and amplitude contour. A module's wave can be **heard** or used to **modify** another module's wave.

{{fig:modules_lines|8 modules form 4 internal lines whose outputs are summed.}}

## Three line formats

Within a line the two modules combine in one of three ways:

{{fig:combine_modes|MIX, RING and PHASE for line A (M1, M2).}}

* **MIX** – both waves are heard together: `A = M1 + M2`. Think of two oscillators.
* **RING** – ring modulation: `A = M2 + M1×M2`. Gong-like, metallic, clangorous sounds.
* **PHASE** – only M2 is heard; M1 acts as the phase "reader" of M2: `A = M2(M1)`. The depth of the effect follows the amplifier (DCA) envelope of the modulating module, so DCA envelope, amp envelope, key follow and velocity all shape the timbre.

!!! tip "Rule of thumb"
    In PHASE/RING mode the DCA envelope of the *modulator* is your timbre control; the DCA of the *carrier* is your volume control.

## External phase

When **EXT PHASE = ON** for line B, C or D, the preceding line's output becomes the phase of the **second module** of that line. A line used as external phase **does not sound**.

{{fig:ext_phase|External phase from line A into line B.}}

Chaining lets you stack up to 8 modules: only module 8 is heard while modules 1–7 modulate it, like chained guitar preamp stages that overdrive each other. Modulators "overdrive" the output modules.

## Complete line table

| Module pair | EXT PHASE | INT LINE | Result |
|---|---|---|---|
| M1 M2 | – | MIX / RING / PHASE | A = M1+M2 / M2+M1×M2 / M2(M1) |
| M3 M4 | OFF | MIX / RING / PHASE | B = M3+M4 / M4+M3×M4 / M4(M3) |
| M3 M4 | ON | MIX / RING / PHASE | B = M3+M4(A) / M4(A)+M3×M4(A) / M4(M3+A) |
| M5 M6 | OFF | MIX / RING / PHASE | C = M5+M6 / M6+M5×M6 / M6(M5) |
| M5 M6 | ON | MIX / RING / PHASE | C = M5+M6(B) / M6(B)+M5×M6(B) / M6(M5+B) |
| M7 M8 | OFF | MIX / RING / PHASE | D = M7+M8 / M8+M7×M8 / M8(M7) |
| M7 M8 | ON | MIX / RING / PHASE | D = M7+M8(C) / M8(C)+M7×M8(C) / M8(M7+C) |

`X(Y)` means "X with Y as phase". Configure with **1-00 LINE**; hold <kbd>LINE</kbd> to see the whole configuration on screen.
