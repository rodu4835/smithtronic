# Release provenance — Glove Box Shelf

Where every published artifact came from and how it was verified. Release
prepared 2026-08-07/08.

## Source of truth

- **Geometry:** Ron staged the release inputs at
  `E:\Projects\3D Printing\Created\subieParts\gloveBoxShelf\v5\gloveBoxShelf_v5\`:
  `ASA_GloveBoxShelf.3mf` (production Bambu project, re-saved 2026-08-08 with
  Bambu Studio 2.7) and `gloveBoxShelf_v5.stp` (fresh SolidWorks 2026 export).
  The native source `gloveBoxShelf_v5.SLDPRT` (2024-03-03, the v5 design) sits
  one level up. Versions v1–v4 (Jan 2024, multi-piece iterations) exist alongside
  and were deliberately not shipped — v5 is the one-piece final.
- **Copy:** the smithtronic.com "Custom 3D Printed Glove Box Shelf" project post.
- **Photo:** original from `E:\Projects\SMITHTRONIC\Blog\Subaru\Images\shelf.jpg`.

## Verification performed

- 3MF mesh: single object, **848 triangles, watertight manifold** (0 boundary
  edges, 0 duplicated directed edges, 0 degenerate; Bambu's own mesh_stat also
  records 0 repairs). Bounding box **271.0 × 45.0 × 132.9 mm**.
- The 3MF's `source_file` metadata records the mesh was tessellated **from the
  same `gloveBoxShelf_v5.stp` being shipped**, and the v4 STL's envelope
  (272 × 45 × 133.8) matches — three independent artifacts agree on the part.
- STEP: single solid, product `gloveBoxShelf_v5`. Its raw point extent reads
  larger (350 × 66.8 × 138.7) because B-spline **control points overshoot the
  actual surfaces** — expected for SolidWorks spline exports, not a geometry
  discrepancy (the caps STEP showed the inverse effect: arc extremes reading
  under).
- Release STL was extracted from the 3MF mesh verbatim (identical triangle
  count) and written as binary STL.
- 3MF sanitized with the same pipeline as prior releases: metadata filled
  (title/designer/license), object names normalized, source paths reduced to
  basenames. Post-checks: geometry unchanged, zero personal strings, zero
  dangling internal references.
- Photo verified EXIF-free after strip-on-copy.

## Corrected during review

- An automated mesh scan flagged ~Ø7.5 mm circular vertex rings, initially read
  as "mounting recesses." **Ron corrected this: the model is deliberately solid
  with no mounting holes at all** — builders drill to suit their own bolts (M5
  is plenty). The rings were a misread of other curved features. Lesson noted:
  a geometry detector proves a shape exists, not what it's for.

## Known gaps

- **No print-time/filament figures** — the project was saved unsliced.
- The design is intentionally simple and may see future revisions (e.g.,
  modeled mounting holes).
- Thing 7393048 created as an **unpublished draft** (files + image verified
  uploaded); category must be set to Automotive in the web UI after publishing.
