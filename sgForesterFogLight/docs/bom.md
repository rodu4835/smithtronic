# Bill of Materials

## Printed parts (this repo)

| Part | Qty | File | Material |
|---|---|---|---|
| Housing, left | 1 | [`housing_left.stl`](../models/stl/housing_left.stl) | ASA |
| Housing, right | 1 | [`housing_right.stl`](../models/stl/housing_right.stl) | ASA |
| Retainer, left | 1 | [`retainer_left.stl`](../models/stl/retainer_left.stl) | ASA |
| Retainer, right | 1 | [`retainer_right.stl`](../models/stl/retainer_right.stl) | ASA |

Left/right = side of the car as seated in it (US driver side = left). The parts are
not mirror-copies — each retainer is embossed with its side and a "Towards Engine"
orientation mark, so print all four. See [print settings](print-settings.md).

## Hardware

| Item | Qty | Notes |
|---|---|---|
| Brass M3 heat-set inserts | 12 | 6 per retainer |
| M3 × 25 mm button-head bolts | 12 | 6 per side, 2.5 mm Allen — stainless or black-oxide alloy (see below) |
| Blue threadlocker (optional) | — | bracket threads only — **keep it off the printed plastic** |
| Heat shrink assortment + rosin-core solder | — | for the 9005 connector splice (one larger sleeve for the cable pair, small sleeves per wire) |

## The exact parts used in the original kits (2025 production)

These are the products SMITHTRONIC actually bought for production kits — listed
by full product title so you can find them (or an equivalent) yourself:

| Role | Product | ~Price |
|---|---|---|
| Lights | **AKD Part Amber LED Pods, 3 Inch CREE LED Fog Lights 40W Spot** — [Amazon listing](https://www.amazon.com/dp/B09MVVQMC2) (sold as a 2-pack) | ~$33 / pair |
| Connectors | **TOMALL 9005 9006 Male Socket Connector** retrofit wiring pigtail — [Amazon listing](https://www.amazon.com/dp/B07CVH3R75) | ~$7 |
| Bolts | **iexcell M3 × 25 mm alloy steel 10.9 button head, black oxide finish** (100-pc kit) — [Amazon listing](https://www.amazon.com/dp/B08R375CSJ) | ~$8 |
| Heat-set inserts | **Yaocom M3 threaded inserts, M3 × D5 × L4, brass knurled** — [Amazon listing](https://www.amazon.com/dp/B0F43D2TTH) | ~$10 |

Insert compatibility, measured from the actual part geometry: the retainer's
insert pockets are **Ø4.2 mm** (opening from a Ø3.2 mm bolt-clearance bore on the
engine-side face) — any short-series M3 heat-set insert around **5 mm OD × 4 mm
long** fits; longer inserts will bottom out.

A note on the bolts: the published spec said stainless; production batches used
the black-oxide alloy kit above (black hardware disappears nicely against the
black parts). Black oxide is not as corrosion-proof as stainless in road spray —
either works. The stainless equivalent is
[M3 × 25 mm 304 stainless button head](https://www.amazon.com/dp/B08H2GZYKQ).

## Finishing supplies (production process — see [finishing guide](finishing.md))

- Sandpaper: ~220 and 400 grit (400 used wet)
- **SEM 42003 Black High Build Primer** (16 oz aerosol) — [Amazon listing](https://www.amazon.com/dp/B000PL07B6)
- **SEM 49143 Trim Black Ultra**, satin finish (UV-resistant, made for plastic/trim) — [Amazon listing](https://www.amazon.com/dp/B07NDM9SPB)

## OEM Subaru parts (not printed, required)

| Item | Part number | Notes |
|---|---|---|
| Fog light relay | **[82501AE03A](https://www.amazon.com/dp/B00IW33M5W)** | plugs into the cabin fuse/relay panel |
| Fog light switch | **[83001SA000](https://www.subaruparts.com/oem-parts/subaru-fog-lamp-switch-83001sa000)** | factory dash switch, plugs into existing harness connector |

Both are plug-in parts — the car's harness already has the wiring. Available from
Subaru parts counters, subaruparts.com, Amazon, or a junkyard SG.

## Lights + connector (your choice)

| Item | Spec | Notes |
|---|---|---|
| Auxiliary lights, pair | single through-bolt bracket, bracket ≤ **64.5 mm high × 23 mm wide** | production kits used 3-inch dual-row amber LED **spot** pods (~40 W); see the [dimension diagram](images/bracket_dimensions.png) |
| 9005 male connectors | 2 | two-wire pigtail ([the one production used](https://www.amazon.com/dp/B07CVH3R75)); splices to your light's leads — harness polarity: **white = +, black = −** |

## Vehicle fitment

2006–2008 Subaru Forester **Sports** bumper (SG facelift) — the kit fills the
factory fog light openings. Pre-facelift (2003–2005) bumpers use a different
opening and are **not** covered by these parts.
