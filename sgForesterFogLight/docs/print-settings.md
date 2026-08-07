# Print settings

These are the settings SMITHTRONIC used for production kits, taken directly from the
slicer projects in [`models/3mf/`](../models/3mf/). If you have a Bambu printer, open
those projects and everything below is already configured — including part orientation
and manual supports. On any other printer/slicer, reproduce the settings from the
tables and read the notes.

## Material

Production parts were printed in **ASA** (Polymaker PolyLite). This is the recommended
material: the parts live in a car bumper — sun, heat, and road spray. A PLA profile is
included (`all_parts_PLA.3mf`) for test fits and mock-ups, but PLA is not recommended
for the final installed parts, especially in hot climates.

## Housings (left + right)

Production project: [`plate_housings_ASA.3mf`](../models/3mf/plate_housings_ASA.3mf)

| Setting | Value |
|---|---|
| Printer / nozzle | Bambu Lab P1S, 0.4 mm |
| Layer height | **0.08 mm** (first layer 0.2 mm) |
| Walls | 4 |
| Top / bottom shells | 9 / 7 |
| Infill | 60 % zig-zag |
| Nozzle temp | 260 °C (ASA) |
| Bed | 100 °C, Engineering Plate |
| Supports | manual, snug style, 15° threshold |
| Brim | outer only, 10 mm |
| Orientation | tilted **45°** (as placed in the project) |

Both housings together: roughly 1 d 8 h and ~350 g of filament (from the production
project's file label; not re-verified by a fresh slice).

## Retainers (left + right)

Production project: [`plate_retainers_ASA.3mf`](../models/3mf/plate_retainers_ASA.3mf)

| Setting | Value |
|---|---|
| Printer / nozzle | Bambu Lab P1S, 0.4 mm |
| Layer height | **0.16 mm** (first layer 0.2 mm) |
| Walls | 4 |
| Top / bottom shells | 6 / 4 |
| Infill | **100 %** zig-zag |
| Nozzle temp | 260 °C (ASA) |
| Bed | 90 °C, High Temp Plate |
| Supports | manual, snug style, 25° threshold |
| Brim | outer only, 5 mm |

Both retainers together: roughly 2 h 28 m and ~61 g (same caveat as above).
Retainers are printed solid (100 %) because they clamp the housing against the bumper
and carry the M3 heat-set inserts.

## All-in-one projects

[`all_parts_ASA.3mf`](../models/3mf/all_parts_ASA.3mf) /
[`all_parts_PLA.3mf`](../models/3mf/all_parts_PLA.3mf) hold all four parts on two
plates (plate 1 housings, plate 2 retainers) with the same profile as above on a
textured PEI plate at 90 °C (ASA) / 65 °C (PLA, 220 °C nozzle). The retainers carry
per-object overrides (0.16 mm layer, 100 % infill) — keep those if you rearrange.

## Notes for non-Bambu slicers

- Import the STLs from [`models/stl/`](../models/stl/) and orient housings at ~45°
  (opening up-and-forward as in the production project) — printed flat, the deep
  bucket needs far more support and finishes worse.
- Supports in the projects are **manually painted** (snug/tree-free "normal" type).
  If you can't reproduce that, support the flange lip and the overhung rim only;
  a blanket 15° threshold without painting will bury the part.
- The projects were saved with Bambu Studio 2.2 — older versions may not open them.
