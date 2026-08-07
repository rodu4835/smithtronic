# Print settings

These are the settings SMITHTRONIC used for production caps, taken directly from the
slicer project in [`models/3mf/`](../models/3mf/). If you have a Bambu printer, open
[`cap_pair_ASA.3mf`](../models/3mf/cap_pair_ASA.3mf) and everything below is already
configured — including orientation and the manually painted supports. On any other
printer/slicer, reproduce the settings from the table and read the notes.

## Material

Production caps were printed in **ASA** (Polymaker PolyLite, black). This is the
recommended material: the caps sit on the back of a headlight housing in the engine
bay, over LED bulbs with cooling fans — sustained heat, plus under-hood temperature
swings. PLA is not suitable here; PETG survives but softens sooner than ASA.

## Caps (one plate prints the pair)

Production project: [`cap_pair_ASA.3mf`](../models/3mf/cap_pair_ASA.3mf) — two
instances of the same cap (the design fits both sides of the car).

| Setting | Value |
|---|---|
| Printer / nozzle | Bambu Lab P1 series, 0.4 mm |
| Layer height | **0.08 mm** (first layer 0.2 mm) |
| Walls | 4 |
| Top / bottom shells | 9 / 7 |
| Infill | 40 %, **Rectilinear** |
| Nozzle temp | 260 °C (ASA) |
| Bed | 100 °C, High Temp Plate |
| Supports | manual, snug style, 15° threshold |
| Brim | outer only, 5 mm |
| Orientation | open side down, dome and louvers up (as placed in the project) |

## A note on setting names

These values are transcribed from the project file. Where Bambu Studio's saved
config uses a different word than its own interface, the table gives the
**interface** name — the infill pattern is stored as `zig-zag` in the file but
appears as **Rectilinear** in the slicer, which is what you'll be looking for.

## Notes for non-Bambu slicers

- Import [`models/stl/headlight_cap.stl`](../models/stl/headlight_cap.stl) and print
  it **open side down** — the threaded skirt and locking tabs print cleanly in that
  orientation, and the sealing surfaces stay unscarred.
- Supports in the project are **manually painted** under the louver overhangs only
  ("normal" type, snug style). If you can't paint supports, support the louver
  region and leave the rest alone — a blanket threshold will scar the dome.
- The louvers are the fine-detail part of the print; the 0.08 mm layer height is
  what keeps their edges crisp. They also shed water downward — don't thicken or
  "optimize" them away.
- The project was saved with Bambu Studio **2.3.0** — use 2.3 or newer to open it.
  It targets a P1P profile; on a P1S/X1C just accept the printer prompt — the
  settings carry over.
