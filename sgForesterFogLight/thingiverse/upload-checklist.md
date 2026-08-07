# Thingiverse upload checklist

Account: **SMITHtRONiC** · License selector: **CC BY-NC-SA** · Category: **Automotive**

## Files (upload in this order)

1. `models/stl/housing_left.stl`
2. `models/stl/housing_right.stl`
3. `models/stl/retainer_left.stl`
4. `models/stl/retainer_right.stl`
5. `models/3mf/all_parts_ASA.3mf` — recommended all-in-one project
6. `models/3mf/plate_housings_ASA.3mf` — production plate, 45° + supports
7. `models/3mf/plate_retainers_ASA.3mf` — production plate
8. `models/3mf/all_parts_PLA.3mf` — test-fit only
9. `models/cad/SGForesterFogLight_FINAL.step` — CAD source for remixing (opens in any
   CAD package; 4.8 MB)
10. `thingiverse/install-guide.pdf` — offline copy of the full illustrated guide
11. (skip the 56 MB Fusion `.f3z` — proprietary and large; linked via GitHub instead)

## Images (first upload becomes the cover; curated set, 2026-08-07)

1. `gallery/community/community_install_dusk.jpg` — COVER: lights blazing at dusk (Chris S., plate masked)
2. `gallery/closeup_installed.jpg` — pod seated in the bezel, the best product close-up
3. `gallery/installed_front_both.jpg` — both pods installed, straight-on
4. `gallery/community/community_daylight_lit.jpg` — full car, both pods lit in daylight (Chris S.)
5. `gallery/hero_housings.jpg` — the bare printed housings (what you print)
6. `gallery/community/community_install_lit_closeup.jpg` — pod glowing mid-install (Chris S.)
7. `gallery/installed_quarter.jpg` — front 3/4 with pod, high resolution
8. `gallery/community/community_pod_lit.jpg` — pod lit on the blue car (Joe S.)
9. `gallery/beam_pattern_2.jpg` — real-world beam on the road
10. `gallery/beam_pattern_1.jpg` — wall aiming test (matches guide step 13)
11. `gallery/community/community_forest_symmetric.jpg` — foggy forest, straight-on (Maks)
12. `gallery/cad_render_front.png` — CAD, the remix teaser

## Listing text

Copy from [`description.md`](description.md) (title, tags, and the description
body below its divider).

## Publish paths

- **API path** (Thingiverse uses OAuth2; there is no non-browser flow):
  1. Register an app at <https://www.thingiverse.com/apps/create> — type **Desktop**,
     callback URL `https://www.smithtronic.com/`. Copy its **Client ID**.
  2. `py -3 get_token.py url <CLIENT_ID>` → open the printed URL, click Authorize.
  3. You land on the callback with `#access_token=...` in the address bar. Run
     `py -3 get_token.py token "<pasted address>"` to extract and verify it.
  4. `py -3 publish_thing.py --token <TOKEN> --dry-run`, then without `--dry-run`
     to create the draft, then `--publish` to go live.

  The token is password-equivalent — never commit it, and delete the app at
  thingiverse.com/apps when publishing is done. Rate limit is 300 requests per
  5 minutes; this upload uses about 20.
- **Manual path:** thingiverse.com → Create → Upload a Thing → drag the files and
  images above in order → paste title/description/tags → set license + category →
  Publish.

## After publishing

- Flip the GitHub repo `rodu4835/smithtronic` to public (the description links it).
- Verify the thing page renders all files and the cover image.
- Optionally post it to r/subaruforester / SG owners groups.
