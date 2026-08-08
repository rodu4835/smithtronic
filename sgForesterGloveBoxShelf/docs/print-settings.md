# Print settings

These are the settings from the production Bambu Studio project in
[`models/3mf/`](../models/3mf/). If you have a Bambu printer, open
[`shelf_ASA.3mf`](../models/3mf/shelf_ASA.3mf) and everything below is already
configured — including the on-edge orientation and manually painted supports. On any
other printer/slicer, reproduce the settings from the table and read the notes.

## Material

The shelf was printed in **ASA** (Polymaker PolyLite, black). A dashboard interior
bakes in the sun, so the material needs the heat tolerance — PLA will sag here.
PETG or ABS also survive; ASA is what the production part used and what matches
the interior's low-gloss black.

## The shelf (one piece)

| Setting | Value |
|---|---|
| Printer / nozzle | Bambu Lab P1S, 0.4 mm |
| Layer height | **0.08 mm** (first layer 0.2 mm) |
| Walls | 4 |
| Top / bottom shells | 9 / 7 |
| Infill | 60 %, **Rectilinear** |
| Nozzle temp | 260 °C (ASA) |
| Bed | 100 °C, High Temp Plate |
| Supports | manual, snug style, 15° threshold |
| Brim | outer only, 10 mm |
| Orientation | standing on edge (as placed in the project) |

## Why on edge

The shelf is **271 mm long** — longer than a P1-series bed is deep — so it prints
standing on its edge, which fits the plate and puts the layer lines along the
shelf's length where they're strongest and least visible. The brim plus ASA's
warp tendency is exactly why the project uses a 10 mm outer brim on a 100 °C
plate: a tall, narrow ASA print wants to peel.

## A note on setting names

Values are transcribed from the project file. Where Bambu Studio's saved config
uses a different word than its interface, the table gives the **interface** name —
the infill pattern is stored as `zig-zag` in the file but appears as
**Rectilinear** in the slicer.

## Notes for non-Bambu slicers

- Import [`models/stl/glove_box_shelf.stl`](../models/stl/glove_box_shelf.stl)
  and stand it on edge as described above.
- Supports in the project are **manually painted** (normal type, snug). Support
  the overhung mounting wings only; a blanket 15° threshold without painting will
  bury the part.
- The project was saved with **Bambu Studio 2.7** — open it with a current
  version.
