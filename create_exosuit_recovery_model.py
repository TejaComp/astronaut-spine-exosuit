import opensim as osim
import os

# ── Our Phase 9 result ───────────────────────────────────
# With exosuit after 6 months:
# Bone loss: 2.63% (vs 6.00% without)
# Muscle loss: 22.80% (vs 25.00% without)

BASE_MODEL   = r"C:\SpineSimulation\Models\gait2392_simbody.osim"
NO_EXOSUIT   = r"C:\SpineSimulation\Models\spine_day180.osim"
WITH_EXOSUIT = r"C:\SpineSimulation\Models\spine_day180_exosuit.osim"

SPINE_MUSCLES = [
    "ercspn_r", "ercspn_l",
    "intobl_r", "intobl_l",
    "extobl_r", "extobl_l",
    "psoas_r",  "psoas_l",
    "iliacus_r","iliacus_l"
]

print("=" * 60)
print("  Creating Exosuit Recovery Model")
print("  Phase 9 Results Applied to Spine Model")
print("=" * 60)

# ── Load Day 180 no-exosuit model ────────────────────────
print(f"\n  Loading Day 180 model (no exosuit)...")
model     = osim.Model(NO_EXOSUIT)
state     = model.initSystem()
orig_mass = model.getTotalMass(state)
print(f"  Current total mass : {orig_mass:.4f} kg")

# ── Apply exosuit bone recovery ──────────────────────────
# Without exosuit: bone loss = 6.00%
# With exosuit:    bone loss = 2.63%
# Recovery factor = (100-2.63)/(100-6.00) = 1.0358

BONE_RECOVERY = (100 - 2.63) / (100 - 6.00)
print(f"\n  Bone recovery factor : {BONE_RECOVERY:.4f}")
print(f"  (bone loss 6.00% → 2.63%)")

body_set = model.getBodySet()
print(f"\n  Recovering bone mass:")
print(f"  {'Body':<14} {'Day180(kg)':>12} "
      f"{'+Exosuit(kg)':>13} {'Recovery':>10}")
print(f"  {'-'*52}")

for i in range(body_set.getSize()):
    body = body_set.get(i)
    if body.getName() == "ground":
        continue
    old_mass = body.getMass()
    new_mass = old_mass * BONE_RECOVERY
    body.setMass(new_mass)
    diff = new_mass - old_mass
    print(f"  {body.getName():<14} "
          f"{old_mass:>12.4f} "
          f"{new_mass:>13.4f} "
          f"{diff:>+10.4f}")

# ── Apply exosuit muscle recovery ────────────────────────
# Without exosuit: muscle loss = 25.00%
# With exosuit:    muscle loss = 22.80%
# Recovery: muscles are 2.20% stronger

MUSCLE_RECOVERY = (100 - 22.80) / (100 - 25.00)
print(f"\n  Muscle recovery factor : {MUSCLE_RECOVERY:.4f}")
print(f"  (muscle loss 25.00% → 22.80%)")

muscle_set = model.getMuscles()
print(f"\n  Recovering muscle forces:")
print(f"  {'Muscle':<14} {'Day180(N)':>10} "
      f"{'+Exosuit(N)':>12} {'Recovery':>10}")
print(f"  {'-'*50}")

for name in SPINE_MUSCLES:
    try:
        muscle   = muscle_set.get(name)
        old_f    = muscle.getMaxIsometricForce()
        new_f    = old_f * MUSCLE_RECOVERY
        muscle.setMaxIsometricForce(new_f)
        diff     = new_f - old_f
        print(f"  {name:<14} {old_f:>10.1f} "
              f"{new_f:>12.1f} {diff:>+10.1f}")
    except:
        pass

# ── Set microgravity (still in space) ───────────────────
gravity = osim.Vec3(0, -0.01, 0)
model.setGravity(gravity)

# ── Save recovery model ──────────────────────────────────
model.setName("astronaut_spine_day180_WITH_exosuit")
model.printToXML(WITH_EXOSUIT)

# ── Final comparison ─────────────────────────────────────
state2     = model.initSystem()
new_mass   = model.getTotalMass(state2)

print(f"\n{'='*60}")
print(f"  COMPARISON SUMMARY")
print(f"{'='*60}")
print(f"\n  {'Metric':<30} {'No Exosuit':>12} "
      f"{'With Exosuit':>13}")
print(f"  {'-'*57}")
print(f"  {'Total body mass':<30} "
      f"{orig_mass:>12.4f} "
      f"{new_mass:>13.4f}")
print(f"  {'Bone loss':<30} "
      f"{'6.00%':>12} "
      f"{'2.63%':>13}")
print(f"  {'Muscle loss':<30} "
      f"{'25.00%':>12} "
      f"{'22.80%':>13}")
print(f"  {'Erector Spinae force':<30} "
      f"{'1875.0 N':>12} ")

# Get new ercspn force
try:
    new_erc = model.getMuscles().get(
        "ercspn_r").getMaxIsometricForce()
    print(f"  {'':30} {'':12} {new_erc:>13.1f} N")
except:
    pass

print(f"  {'Health Score':<30} "
      f"{'10/100':>12} "
      f"{'51.6/100':>13}")
print(f"  {'Rehab needed':<30} "
      f"{'6 weeks':>12} "
      f"{'2.6 weeks':>13}")

print(f"\n  Saved → {WITH_EXOSUIT}")
print(f"\n{'='*60}")
print(f"  Now load in OpenSim GUI:")
print(f"  1. spine_day000.osim      ← Earth healthy")
print(f"  2. spine_day180.osim      ← Space no exosuit")
print(f"  3. spine_day180_exosuit.osim ← Space WITH exosuit")
print(f"  Compare Properties of each to show improvement!")
print(f"{'='*60}\n")