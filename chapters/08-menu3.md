# Menu 3 reference: total control

Available in all modes except **3-07**, which is **Normal** only.

| Fn | Name | Parameters |
|---|---|---|
| 3-00 | TUNE/TRANSPOSE | TUNE A4 = 417.2 … 442 … 468.3 Hz (≈1.6-cent steps; both cursor keys at once reset to 442). TRANSPOSE G … C … F# (shifts the key; TUNE display follows) |
| 3-01 | MEMORY PROTECT | INTERNAL ON/OFF; CARD ON/OFF. ON protects internal (voices+operations) / card contents from writing; LOAD is also blocked |
| 3-02 | SAVE/LOAD | SAVE / LOAD; CARD / MIDI; DATA = VOICE / OP MEM / VC+OP; then EXECUTE with <kbd>YES</kbd>. Abort transmission with <kbd>MENU 3</kbd> |
| 3-03 | MIDI CH | RECEIVE 01–16; SEND 01–16 (separate per sound in a split). In Multi-Channel each area has its own (set in PLAY); this is the common basic channel |
| 3-04 | MIDI DATA | PROG NO. DIS / 0–63 / 0–127; EXCLUSIVE ENA/DIS; CONT NO. OFF / 12–31 (control number sent by Def. Wheel 2); VOLUME IN ENA/DIS |
| 3-05 | PITCH BEND | TOTAL BEND ON/OFF; BEND RANGE 00–48; RELEASE ENA/DIS. ON = global range for all voices (useful as a uniform-bend MIDI controller); 2-02 is then disabled |
| 3-06 | CARD FORMAT | EXECUTE = YES? Formats a RAM card (erases it, writes 64 preset patches + 64 preset operations). Not for ROM cards |
| 3-07 | PRESET CALL | PRESET = A–H, 1–8: loads internal patches into the Compare/Recall buffer; up to 64 can be loaded in sequence, each replacing the previous |

## 3-02 SAVE/LOAD notes

* When using a **new RAM card**, format it first (3-06).
* Saving an operation memory with INTERNAL sounds to a card changes its sound reference to "CARD".
* One MIDI cable only: abort transmission on the transmitting unit with <kbd>MENU 3</kbd>.
* With two VZ-1s over MIDI the DATA setting must match.
* **LOAD to MIDI fails** if memory protect is ON, MIDI exclusive is disabled (3-04), basic channels do not match (3-03) or the rear MIDI ON/OFF switch is OFF.

## 3-04 MIDI program numbers

Transmit:

| PROG NO. setting | Internal A1–H8 | Card A1–H8 |
|---|---|---|
| 0–127 | 0–63 | 64–127 |
| 0–63 | 0–63 | 0–63 |
| DIS | × | × |

(Receive table: see *Open points*.)

## 3-06 Card format messages

"NOT READY – INSERT CARD!" (no card); "PROTECT ON – SET MENU 3 01!" (memory protect on); "NOT READY – CHECK CARD!" (ROM card inserted; no formatting needed).
