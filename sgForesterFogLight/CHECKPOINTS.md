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
- **Customer review photos**: use the chrisshim dusk shot + one Joe S. shot only —
  plates masked, real names out of filenames, credited as "community photo, used
  with permission — not covered by the project license." The third customer's photo
  skipped (baked-in AI-content watermark).
- **Repo**: GitHub `rodu4835/smithtronic` (private during prep → public at release).
  Local clone `e:\Projects\smithtronic-oss` (can't be `smithtronic` — Windows
  case-insensitive collision with the private archive folder).

## CP1 — Preserve ✅ (2026-08-06)

The only copies of the install instructions were live pages on smithtronic.com
(site no longer paid for). Archived to
`e:\Projects\SMITHTRONIC\Products\fogLight\siteArchive\`:
both install guides (assembled + DIY), both shop pages, homepage, 111 images.
CP3 sources its content from this archive.

## CP2 — Geometry ✅ (2026-08-06)

Canonical geometry = the meshes embedded in the **production print projects**
(what customers actually received); the FINAL_2 STLs they were sliced from are
lost (another machine's Downloads folder).

**Produced**
- `models/stl/`: `housing_left/right.stl`, `retainer_left/right.stl` — extracted
  losslessly from `printing\MAIN HOUSINGs…3mf` / `MAIN RETAINERs…3mf` (binary STL,
  byte-count-verified against triangle counts).
- `models/3mf/`: `all_parts_ASA/PLA.3mf` (4-part projects with full print
  profiles), `plate_housings_ASA.3mf` + `plate_retainers_ASA.3mf` (production
  plates: 45° housing orientation, manual supports, proven settings). All four
  sanitized: Bambu account DesignerUserId removed, local Windows paths stripped
  to basenames, Title/Designer/Description/License metadata filled, objects
  renamed to left/right. Verified: geometry bit-identical, zero personal strings,
  zero dangling internal references (entry renames were required — first sanitize
  pass broke `p:path`/`.rels` references; caught by integrity check, fixed).
- `models/cad/SGForesterFogLight_v9.f3z` — Fusion 360 source (57 MB).

**Findings (evidence, not assumption)**
- **Driver = LEFT, Passenger = RIGHT.** The retainers are not mirror-identical
  (13,352 vs 16,114 triangles — per-side embossed text), and the production
  "Driver" retainer matches `RETAINER_LEFT` exactly (triangles, area, volume).
  Housing surface areas (51,167 vs 51,185 mm²) pair the same way.
- **v8 vs FINAL_2**: retainers unchanged from the v8 exports; production housings
  are a finer retessellation (~68.6k vs ~64.9k triangles) with geometry equal to
  within 0.003% — consistent with a re-export (plausibly v9), not a redesign.

**Open (Ron, optional, any time)**
- Open v9.f3z in Fusion: confirm v9 housing = shipped geometry; export STEP to
  `models/cad/` for remixers.

## CP3 — Documentation ✅ (2026-08-06)

- Full verbatim text of both install guides recovered from the CP1 archive
  (3-agent extraction; the site is a Framer export with content triplicated per
  responsive breakpoint and double-encoded UTF-8 — both handled).
- `docs/install-guide.md`: unified 13-step guide (DIY structure with assembled-kit
  hardware notes folded in) + a **new step 0** covering what sold kits never
  needed: printing and heat-set insert installation. 28 step photos recovered from
  the archive into `docs/images/`.
- `docs/bom.md`: printed parts, hardware (M3×25 bolts per production receipts),
  OEM part numbers (relay 82501AE03A, switch 83001SA000), light size limits
  (bracket ≤ 64.5 × 23 mm), 9005 wiring polarity (white +, black −).
- `docs/print-settings.md`: per-part production settings verified directly from
  the sanitized 3MF configs (not from memory or summaries).
- **Correction found during CP3**: fitment is 2006–2008 Forester **Sports (SG
  facelift)** only — earlier drafts said 2003–2008; README, BOM, and 3MF metadata
  all corrected. (The 2003–05 opening is different; that variant was the excluded
  third-party design.)
- Historical context recovered: kits sold at $250 assembled / $150 DIY; SAE
  non-certification disclaimer carried into the docs and listing.

## CP4 — Images ✅ (2026-08-06)

- `gallery/` + `docs/images/` populated; EXIF orientation baked in; **all metadata
  stripped** from published copies (no GPS was present in any source — verified).
- Community photos: plates blurred (chrisshim's front plate; reinforced Joe S.'s
  pre-blurred plate), filenames anonymized, `gallery/community/CREDITS.md` states
  permission + license exclusion. AI-watermarked customer photo excluded.
- Site carousel/beam shots and step photos re-checked visually for plates before
  inclusion (own car's plate was already blurred in the site-era images).

## CP5 — Package & license ✅ (2026-08-06)

- `LICENSE.md` = CC BY-NC-SA 4.0 full legal code (fetched verbatim).
- `thingiverse/description.md` = paste-ready title/tags/description;
  `thingiverse/upload-checklist.md` = file + image order, both publish paths.
- Final privacy scan over every shipped file: no usernames, account IDs, local
  paths, customer surnames, or credentials (the one hit — customer names in this
  file's own decision log — was scrubbed).
- Remaining before public: Ron's Fusion v9 check (optional), CP6 publish, then
  flip the GitHub repo public.

## CP6 — Publish (planned)

Thingiverse API with Ron's app token (verified portal live 2026-08-06; API-first,
manual upload as fallback). Optional: GitHub repo linked from the listing.

## CP7 — Optional extras (parked)

Kit cards re-QR'd to the new home; companion SG parts as future listings; vented
headlight cap project.
