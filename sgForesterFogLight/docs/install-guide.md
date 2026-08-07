# Install Guide — SG Forester Amber Auxiliary Light Kit

Step-by-step instructions to install your printed auxiliary lights. Merged from the
original SMITHTRONIC assembled-kit and DIY-kit guides, with an added section on
preparing self-printed parts.

- **Estimated install time:** 2–3 hours
- **Skill level:** moderate
- **Fitment:** 2006–2008 Subaru Forester Sports (SG with facelift) bumper

> **Disclaimer:** no one involved in this project is liable for any damages to your
> vehicle, property, or person resulting from the installation or use of these parts.
> Proceed at your own risk, and consult a professional installer if necessary.
> The lights you choose may or may not be SAE approved — ensure your application
> complies with local regulations.

## What you'll need

See the [bill of materials](bom.md) for the complete list with part numbers and the
[print settings](print-settings.md) for producing the four printed parts. In short:
the four printed parts, 12 brass M3 heat-set inserts, 12 M3 stainless button-head
bolts, the OEM Subaru fog light relay and switch, a pair of lights meeting the size
limits in step 2, and a 9005 male connector.

**Factory relay — Subaru 82501AE03A (not printed, required):**

![Fog light relay](images/parts_relay.jpg)

**Factory fog light switch — Subaru 83001SA000 (not printed, required):**

![Fog light switch](images/parts_fog_switch.webp)

**The printed kit (housings + retainers + hardware):**

![The kit](images/parts_diy_kit.png)

**Tools:** wire cutters/strippers · soldering iron and solder · heat shrink ·
2.5 mm Allen key · 4 mm drill bit and drill · bumper clip removal tool or flathead
screwdriver · skinny marking tool (pen or scribe) · plus whatever your light kit
needs for bracket assembly.

## 0. Prepare your printed parts *(new for self-printers — sold kits came assembled)*

- Print the four parts per the [print settings](print-settings.md).
- **Finish the housings** (sand → high-build primer → UV-resistant satin black)
  per the [finishing guide](finishing.md) — this is how production kits got their
  smooth factory look. Do it **before** installing inserts and hardware.
- **Install the heat-set inserts:** each retainer takes 6 brass M3 inserts. Seat
  them into the hole bosses on the face that will point **toward the engine** — the
  retainers are embossed with orientation text ("Towards Engine") to keep this
  unambiguous. Press each insert flush with a soldering iron (~250 °C works well
  for ASA); keep the iron square to the hole so the insert goes in straight.

## 1. Safety first

- Ensure the car is **off** and parked on a **level surface**.
- Depending on ride height, you may need to raise the vehicle to get under the
  front bumper.
- **Read the entire guide before starting.**

## 2. Prepare your light assembly

**Light size limits** — the housing accepts lights that mount with a **single
through-bolt bracket**. For full vertical articulation without the bracket corners
hitting the cutout: bracket **height ≤ 64.5 mm, width ≤ 23 mm**. A narrower bracket
at maximum height can still interfere at the extremes of rotation — check yours.

![Bracket dimension limits](images/bracket_dimensions.png)

(Production kits used 3-inch dual-LED amber spot pods — spot style keeps the light
vertical, tight to the body, and lets articulation put the beam where a flood
pattern would.)

- **Attach the light to its bracket** per the light manufacturer's instructions —
  tight, but still allowing articulation.
- **Trim and strip wires:** cut the connector off your light and strip ~10 mm on
  both wires.
- **Mount the bracket to the housing:** slip the wire through the rear hole in the
  housing, guide the bracket bolt through the center hole, and secure with the
  bracket's nut (and lock washer) — light pointed forward, large-radius curve
  toward the front. Optional: blue Loctite on the threads, but **keep Loctite off
  the printed plastic — it attacks it over time**.
> **Order matters:** the 9005 connector will not fit through the housing's wire
> hole. Feed the light's bare cable **through the housing first** (it happens as
> part of mounting the bracket, above) — and only then solder the connector on.
> If you solder first, you'll be cutting it back off.

- **Solder the 9005 connector** (with the cable already through the housing):
  1. Slide one larger heat-shrink sleeve over the cable pair, and a small sleeve
     over each individual wire.
  2. Twist and tin the stripped ends of both the light's wires and the 9005
     pigtail's wires.
  3. Polarity on the car's harness: **white = positive (+), black = ground (−)**.
     Solder light-positive to white, light-negative to black.
  4. Shrink the small sleeves over each joint, then the larger sleeve over both —
     the joints live behind the bumper in road spray, so seal them well.

![Soldered connector](images/step02_solder_connector.jpg)

## 3. Install the relay

- Inside the vehicle, remove the small door leading to the fuse panel.
- The relay slot is the **third position from the bottom** in the relay column to
  the right of the fuse panel.
- Insert the relay until it **clicks** — the tabs only line up one way.

![Fuse panel door](images/step03_fuse_panel_door.jpg)
![Fuse panel](images/step03_fuse_panel.jpg)
![Relay position](images/step03_relay_position.png)
![Relay panel](images/step03_relay_panel.jpg)

## 4. Install the factory fog light switch

- Just above the fuse panel, find the switch panel with blank covers.
- Reach through the fuse panel hole and **pop out the blank cover** (clips top and
  bottom).
- Find the **fog light connector** behind the panel (of the two connectors there,
  the correct one fits the switch), route it through, plug it into the switch, and
  seat the switch (**indicator light up**).

![Switch connection](images/step04_switch_connector.jpg)
![Switch panel](images/step04_switch_panel.jpg)

## 5. Prepare the bumper

- Remove the bumper clips under the front edge and pry the dust guard open —
  gently, the clips break easily.
- Press the clips on the factory fog light hole cover and remove it.

![Splash guard clips](images/step05_splash_guard_1.jpg)
![Splash guard open](images/step05_splash_guard_2.jpg)
![Fog panel and connector](images/step05_fog_panel_connector.jpg)

## 6. Test before you drill

- Plug the light into the factory fog light harness connector (one correct
  orientation only).

![Plug in the light](images/step06_plug_light_1.jpg)
![Connector detail](images/step06_plug_light_2.jpg)

- Rest the light somewhere safe, turn on the ignition with headlights on, and
  press the fog switch.
- If it doesn't light: re-check the relay, the switch seating, the harness
  connector, and your soldered polarity.

## 7. Mount the housings

- Press the housing into the fog light hole until snug.
- Use the housing as a template to **mark the 6 bolt holes**, then **remove it**
  before drilling.

![Fit and mark](images/step07_fit_mark_1.jpg)
![Marking the holes](images/step07_fit_mark_2.jpg)

- Unplug the light connector from the factory harness and set the housing
  assembly safely aside.

![Disconnect](images/step07_disconnect.jpg)

- Drill **4 mm** holes — keep the drill **parallel to the housing's mounting
  direction**, not perpendicular to the bumper's curved skin, or the retainer
  holes won't line up.
- Some holes pass clean through; others sit over an edge. That's by design: the
  retainer clamps the housing against the back of the bumper — the bolt threads
  never grip the bumper itself.

![Drill the holes](images/step07_drill.jpg)

## 8. Prepare the retainer

- Slip the wire through the hole in the bumper, then through the matching-side
  retainer — **heat-set inserts (and the "Towards Engine" embossing) facing the
  engine** — before plugging the connector back in.

![Wire through the retainer](images/step08_wire_retainer.jpg)

## 9. Replace the housing

- Press the housing fully back into its hole and slip the retainer over its rear,
  inside the bumper.
- Check hole alignment — a flashlight behind the retainer makes this easy.

![Retainer in place](images/step09_retainer_place.jpg)
![Check alignment](images/step09_alignment_check.jpg)

## 10. Secure the housing

- Insert the **6 M3 bolts** through the housing into the retainer, one hand inside
  the bumper guiding the retainer, the other driving the 2.5 mm Allen key.
- Get **all bolts threaded before fully tightening.**

![Bolts into the retainer](images/step10_bolts.jpg)

- Tighten in a **cross pattern**, snug only — overtightening strips the inserts or
  cracks the housing.

## 11. Reconnect and close up

- Plug the light connector back into the factory harness.
- Reattach the splash panel with the bumper clips.

![Reconnected](images/step11_reconnect.jpg)

## 12. Repeat for the other side

Back to step 5 for the second light.

![Right side installed](images/step12_right_installed.jpg)
![Both lights, front view](../gallery/installed_front_both.jpg)
![Left side installed](images/step12_left_installed.jpg)

## 13. Aim the beam

- Park on a flat surface ~**25 feet** from a wall, lights on.
- **Vertical:** top edge of the amber beam aligned with the **bottom edge of your
  headlight beam**. **Horizontal:** slightly toward center, or to taste.

![Beam pattern](images/step13_beam_pattern.jpg)

## Known quirks

- One owner reported having to slightly trim a tab on the washer-fluid reservoir
  for clearance (possibly an isolated case on his car). If something behind the
  bumper interferes on your side, look there first before modifying the printed
  parts.

## Adjustment tips

- **Vertical aim too loose:** tighten the bracket nut on the back of the housing
  until the light holds position but still adjusts smoothly. Don't crack the
  housing.
- **Horizontal aim too loose:** remove the bracket (loosen the rear nut), tighten
  the light-to-bracket bolts, reinstall.
- **Reattaching the bracket:** seat the bolt in the bracket's retaining grooves,
  guide it through the housing, add lock washer then nut, thread by hand first,
  tighten snug.

Cheers — enjoy the lights, and share your install photos on the Thingiverse page!

Questions or problems: ron@smithtronic.com
