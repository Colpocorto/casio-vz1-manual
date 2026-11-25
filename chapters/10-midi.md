# MIDI

The VZ-1 has IN, OUT and THRU. MIDI settings are in **3-03** (channels) and **3-04** (data). It can be a **master keyboard** (A), a **slave** (B) or part of a **chain** (C) driven by a sequencer or computer.

{{fig:midi_setups|Typical MIDI hook-ups.}}

## Multi-channel reception

The VZ-1 can receive MIDI in several ways: (1) 16-note polyphonic on one channel (mode 3, omni off/poly), or (2) **Multi Channel**: each MIDI "Multi Area" (1–8) is an independent timbre with its own polyphony, output level and channel. Total polyphony stays 16 notes; the sum for all 8 areas is 16.

## Messages sent and received

All of these are both sent and received in all four modes: **key pitch / note on-off / velocity, after touch, pitch bend, definable wheel 1 & 2, foot VR, main volume, sustain pedal, program change**. Portamento time/on-off, bend range, local control and mono/poly mode are handled in selected modes only (see *Open points*).

**System exclusive** (only when 3-04 EXCLUSIVE = ENA): patch data (specify the sound with A–H and 1–8 keys first; transmitted in Normal/Combination PLAY or to the Compare/Recall area of the receiver), operation data (specify the operation with A–H and 1–8, then press NORMAL for 1 patch or COMBINATION for combined sounds), multi-channel mode data (select with the MULTI CHANNEL key), save/load of 64 sounds and 64 operations, master tuning, transpose, mode change, card bank change, bend range, and System Exclusive END.
