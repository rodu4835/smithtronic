# Checkpoint Map — SG Forester Fog Light open-source release

This file is the living map of the release work. Each checkpoint records what was
decided, what was produced, and what stayed open — so any area can be revisited by
name ("let's look at CP3 again") with full context, in this session or a future one.

Source material lives in the private archive `e:\Projects\SMITHTRONIC\` (never
published, never committed here). Everything in this repo is a hand-picked,
sanitized copy.

---

## CP0 — Decisions (2026-08-06) ✅

- **License: CC BY-NC-SA 4.0.** Attribution name: SMITHTRONIC *(open: confirm Ron
  wants brand-only attribution, or brand + personal name)*.
- **Thingiverse account: `SMITHtRONiC`**. Contact stays ron@smithtronic.com.
- **Scope: the SG fog light kit only.** Excluded: `fogLightHousing_0305` (third-party
  design, listing "6141020" — not Ron's, never publish), kit QR cards (packaging,
  dead store URLs), vented headlight cap (separate future project), all business/
  client/personal files.
- **Naming: LEFT/RIGHT** (not Driver/Passenger) — works for RHD markets too. Docs
  define left = left side seated in the car; US driver side = left.
- **Customer review photos**: use chrisshim dusk shot + one Joe Sosa shot only —
  plates masked, real names out of filenames, credited as "community photo, used
  with permission — not covered by the project license." Ashton Grogg photo skipped
  (baked-in AI watermark).
- **Repo**: GitHub `rodu4835/smithtronic` (private during prep → public at release).
  Local clone `e:\Projects\smithtronic-oss` (can't be `smithtronic` — Windows
  case-insensitive collision with the private archive folder).

## CP1 — Preserve ✅ (2026-08-06)

The only copies of the install instructions were live pages on smithtronic.com
(site no longer paid for). Archived to
`e:\Projects\SMITHTRONIC\Products\fogLight\siteArchive\`:
both install guides (assembled + DIY), both shop pages, homepage, 111 images.
CP3 sources its content from this archive.

## CP2 — Geometry (in progress)

Goal: canonical, sanitized model files in `models/`.

- Canonical geometry = the meshes embedded in the **production print projects**
  (`printing\MAIN HOUSINGs…3mf`, `MAIN RETAINERs…3mf`) — these are what shipped.
  The FINAL_2 STLs they were sliced from are lost (another machine's Downloads).
- Extract the four meshes → `models/stl/` as `housing_left/right.stl`,
  `retainer_left/right.stl`; establish Driver/Passenger ↔ LEFT/RIGHT mapping by
  geometric comparison against the v8-named exports (`All_ASA.3mf`, plain exports).
- Sanitize published 3MFs: strip Bambu account DesignerUserId + local Windows
  paths; fill Title/Designer/License metadata.
- Copy Fusion source `SGForesterFogLight v9.f3z` → `models/cad/`.
- *Needs Ron (optional, any time)*: open v9.f3z in Fusion — confirm v9 didn't
  change geometry after the v8 exports; export STEP for remixers.

## CP3 — Documentation (planned)

`docs/` + README: unified install guide (assembled + DIY merged), BOM with OEM part
numbers (relay 82501AE03A, switch 83001SA000, M3 hardware, 9005 connector, light
size limits), print settings per part. Source: CP1 archive + print-project configs.

## CP4 — Images (planned)

`gallery/` + `docs/images/`: curate, fix EXIF rotations, mask plates, strip
identifying info; hero = ditMAIN; community photos per CP0 policy.

## CP5 — Package & license (planned)

LICENSE.md, thingiverse/description.md (paste-ready listing), upload-checklist.md,
final privacy pass over every shipped byte, repo → public.

## CP6 — Publish (planned)

Thingiverse API with Ron's app token (verified portal live 2026-08-06; API-first,
manual upload as fallback). Optional: GitHub repo linked from the listing.

## CP7 — Optional extras (parked)

Kit cards re-QR'd to the new home; companion SG parts as future listings; vented
headlight cap project.
