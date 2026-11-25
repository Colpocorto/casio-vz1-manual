# Open points & unreliable transcriptions {.nonum}

Machine-readable copy in `OPEN_POINTS.md`. IDs are stable for issue tracking.

## Source contradictions or ambiguities

| ID | Where | Issue |
|---|---|---|
| OP-01 | Concepts / original p.9 | Text says the RAM card holds "128 sounds"; specs and features say a RAM card holds 64 voices + 64 operations; ROM card holds 128. This edition follows the specs. |
| OP-02 | 3 / original p.12 | Ring-mod formula printed in text is garbled ("M2 + M1 × M1"); the p.15 table (`M2 + M1×M2`) was used. |
| OP-03 | 1-02 | Parameter table lists OCT = 0–5; the text for PITCH FIX mentions OCT "10" and a NOTE limit 00–07; the pitch range text (F#−1…C#6) is partly illegible. |
| OP-04 | 3-00 | TRANSPOSE range text reads "E♭4 to D5"; the parameter list says G … F#. |
| OP-05 | 1-16 | Spec says RATE 0–99, but the display example shows signed values (+22…+99); negative range unconfirmed. |
| OP-06 | 3-01 vs App. A | Initial table says INT = ON, CARD = ON; display examples in 3-01 show OFF. |
| OP-07 | Operation-memory editing | "except for menu 2-00 and 10" – function numbers as printed; unclear whether 2-10 is meant. |
| OP-08 | Front panel | Value slider labelled 22 in key list, 27 in drawing; selector rows 25/26 swapped between drawing and text. |
| OP-09 | Names (1-18, 2-00) | Key table maps "3" → 9 and "4" → 0 on ×2; verify on hardware. |

## Doubtful transcriptions

| ID | Item |
|---|---|
| OP-10 | KF example keys: P5 shown as "A♭6" for DCO/DCA/rate and key P6 of KF RATE "F7" are blurred in the scan. |
| OP-11 | Key-assign table (original p.81): cell values and the footnote marks (\*, \*\*) for cross-fade polyphony; row "1/2/3/4" shown as "(4·4)". |
| OP-12 | MIDI standard-data matrix (original p.89): only the all-mode rows are transcribed; portamento, bend range, local control, mono, poly and the SysEx send/receive matrix are not (circle positions unclear). |
| OP-13 | 3-04 MIDI program-number **receive** table (original p.75): second row ("0–63") is garbled. |
| OP-14 | Appendix A: initial-data tables were read from a dense chart; the 2-13 position data (L/M/U POS) is partly illegible ("F=3", "D♭4"). Menu-2 SENSITIVITY: after touch is 20, others 50. |
| OP-15 | Preset names (Appendix B) are OCR-grade; ROM-card name lists (pp. 103–104) not transcribed. |
| OP-16 | Mode availability for Menu 3 functions is read from the page tabs (all modes for 00–06; Normal only for 07). |
| OP-17 | Page 12 introduces "DCO/DCA" for pairs; the text of "1-17 domain" says pitch = global, amp = modular; consistent here but unverified on hardware. |

## Figures that are redrawn, not copied

| ID | Figure | Note |
|---|---|---|
| FG-01 | Velocity curves | Eight shapes approximated from small diagrams; SENS variations not drawn. |
| FG-02 | Envelopes | Time axis schematic (the manual gives no rate → time law). |
| FG-03 | Front/rear panel | Schematic layout; positions approximate. |
| FG-04 | Photos/illustrations | The original's drawings (guitar amp chain, bell and air particles, oscilloscope, instrument envelopes) are described in text, not redrawn. |
| FG-05 | LCD screenshots | Not reproduced; consider generating them with a 64×96 pixel font renderer. |

## Not covered

* Original p.5–6 "Important terms" is merged into the glossary.
* Original Quick-start diagrams of amplifier connections.
* ROM cards RC-100 contents, VP-10/SP-2 pedals, RA-500 specs beyond what the manual states.
* Hardware verification: **nothing here has been tested on an actual VZ-1**.
