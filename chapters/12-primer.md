# Sound primer: elements of synthesis

## What is sound?

Sound is vibration of air detected by the ear. When a bell is struck, its surface oscillates; air alternately **condenses** and **rarefies**, producing *compression waves*. A microphone turns these into positive (condensed) and negative (rarefied) voltage, whose shape over time is the **waveform**, visible on an oscilloscope.

## Pitch, amplitude, timbre

* **Pitch** – how fast the cycle repeats. Frequency in hertz; doubling the frequency raises the pitch one octave (220 → 440 → 880 Hz). Higher frequency = shorter wavelength = higher pitch.
* **Amplitude** – the height of the wave, heard as loudness. The way it evolves over time is the **amplitude envelope** (a piano: instant attack, long decay; release when the damper falls).
* **Timbre** – what distinguishes a flute from a clarinet at the same pitch and loudness: the *shape* of the wave.

{{fig:waveforms|Sine (soft), triangle, saw-tooth (bright), square (simple/hollow). Instrument examples: flute/whistle ≈ sine; violin/trumpet ≈ saw; clarinet/oboe ≈ square.}}

## Harmonics

Any waveform can be built by adding sine waves. Frequencies that are integer multiples of the fundamental are **harmonics**; the set of harmonic amplitudes is the **harmonic spectrum**, and it decides the timbre.

{{fig:additive|Adding harmonics of amplitude 1/n to a sine builds a saw-tooth.}}

## Envelopes

An **envelope** is a value that changes over time. On the VZ-1, envelopes shape **pitch** (DCO, 1-03) and **amplitude/timbre** (DCA, 1-09) with up to 8 steps, each defined by:

* **RATE** – the slope of the step (99 ≈ nearly vertical, 00 ≈ nearly flat). It's an absolute value, whether the level rises or falls.
* **LEVEL** – the height to reach. For DCO, pitch (±63 around 0); for DCA, volume (00–99).

A **sustain point** keeps the level until key-off; the next step is the release. An **end point** terminates the envelope.

## Musical sound vs. noise

Sounds with regular cyclic vibration (few components other than harmonics) are *musical*; sounds with many irregular components whose pitch cannot be measured are *noise* (VZ-1 waveforms NOISE1 and NOISE2).
