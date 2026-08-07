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

## Images (first upload becomes the cover)

1. `gallery/hero_housings.jpg` — cover
2. `gallery/community/community_install_dusk.jpg` — lights on (permission granted, plate masked)
3. `gallery/community/community_fog_closeup.jpg` — Maks's foggy-forest shot (same permission basis)
4. `gallery/installed_front_both.jpg`
5. `gallery/installed_left.jpg`
6. `gallery/beam_pattern_1.jpg`
7. `gallery/beam_pattern_2.jpg`
8. `gallery/kit_product.png`
9. `gallery/cad_render_front.png`
10. `gallery/before_stock_bumper.jpg` — "before" comparison
11. `gallery/community/community_install_front.jpg` (permission granted)

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
