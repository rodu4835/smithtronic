# Release provenance — Vented Headlight Bulb Caps

A short log of where every published artifact came from and how it was verified,
in the same spirit as the fog light kit's CHECKPOINTS.md. Release prepared
2026-08-07.

## Source of truth

- **Geometry:** `E:\Projects\3D Printing\Created\subieParts\headlightCap_Vented\`
  — `cap.stl` and `cap.3mf`, both last modified 2025-07-30 (the end of the
  production run; newest cap files anywhere on the machine).
- **Copy:** the smithtronic.com product page (shop/headlightcaps) and the
  "Custom 3D-Printed Headlight Rear Caps for LED Bulbs" project post — both
  carried over from the original site.
- **Photos:** originals from `E:\Projects\SMITHTRONIC\Blog\Subaru\cap*.jpg`
  (4000 px) plus the background-removed product shot from the design folder.

## Verification performed

- `cap.stl`: binary STL, 43,944 triangles, bbox **84.40 × 84.40 × 27.80 mm**.
  Edge audit: 0 boundary edges, 0 degenerate triangles, 2 duplicated directed
  edges (a cosmetic non-manifold pinch; the mesh is the exact geometry that
  production caps were sliced from, so it ships unmodified rather than
  "repaired" into something unproven).
- `cap.3mf`: Bambu Studio 2.3.0 project, two build items of one mesh —
  triangle-for-triangle identical to `cap.stl` (43,944). Confirms the plate
  prints a pair of the same part (no left/right variants).
- Sanitization (same pipeline as the fog light 3MFs): Bambu account ID removed,
  `source_file` paths reduced to basenames, license/designer metadata filled,
  object name `cap.stl` → `headlight_cap` with zip entries and internal
  references renamed consistently. Post-checks: geometry unchanged, zero
  personal-string hits, zero dangling internal references.
- Photos: EXIF verified GPS-free, then stripped entirely on copy (matching the
  fog light gallery).

## Known gaps

- **No print-time/filament figures.** The production 3MF was saved unsliced, so
  no G-code estimate is recorded anywhere; the docs deliberately don't claim
  one.

## Follow-ups resolved

- **CAD source added 2026-08-07:** `subieHeadlightCap_Vented.step` exported
  fresh from Fusion 360 (AP214, single solid). Verified against the production
  mesh: Z height matches exactly (27.80 mm); X/Y point extents read ~82.9 mm
  against the mesh's Ø84.4 mm because STEP arc extremes fall between vertex
  points — consistent, not a discrepancy.
- The Thingiverse listing (thing 7392999) was reviewed and published; category
  set in the web UI (the API ignores category on create/patch).
