import opensim as osim
import os

# ── Configuration ──────────────────────────────────────
BASE_MODEL = r"C:\SpineSimulation\Models\gait2392_simbody.osim"
OUTPUT_DIR = r"C:\SpineSimulation\Models"
DAYS       = [0, 30, 60, 90, 180]

# Bone mass loss: ~1% per month (30 days)
BONE_LOSS_PER_DAY   = 0.01 / 30

# Muscle atrophy: ~25% over 180 days
MUSCLE_LOSS_PER_DAY = 0.25 / 180

# Actual spine muscles from gait2392 model
SPINE_MUSCLES = [
    "ercspn_r",   # Erector Spinae Right
    "ercspn_l",   # Erector Spinae Left
    "intobl_r",   # Internal Oblique Right
    "intobl_l",   # Internal Oblique Left
    "extobl_r",   # External Oblique Right
    "extobl_l",   # External Oblique Left
    "psoas_r",    # Psoas Right
    "psoas_l",    # Psoas Left
    "iliacus_r",  # Iliacus Right
    "iliacus_l"   # Iliacus Left
]

# Spine bodies for bone mass reduction
SPINE_BODIES = [
    "torso",
    "pelvis"
]

# ── Main Loop ───────────────────────────────────────────
print("=" * 55)
print("  OpenSim Astronaut Spine - Microgravity Models")
print("=" * 55)

for day in DAYS:

    # Load fresh model each iteration
    model = osim.Model(BASE_MODEL)
    model.setName(f"astronaut_spine_day{day:03d}")

    # ── 1. Set Gravity ───────────────────────────────
    if day == 0:
        gravity = osim.Vec3(0, -9.80665, 0)
        grav_label = "Earth (-9.80665 m/s²)"
    else:
        gravity = osim.Vec3(0, -0.01, 0)
        grav_label = "Microgravity (-0.01 m/s²)"

    model.setGravity(gravity)
    print(f"\nDay {day:3d} → {grav_label}")
    print("-" * 55)

    # ── 2. Reduce Bone Mass ──────────────────────────
    bone_factor = 1.0 - (BONE_LOSS_PER_DAY * day)
    body_set    = model.getBodySet()

    print("  BONE MASS:")
    for body_name in SPINE_BODIES:
        body         = body_set.get(body_name)
        original     = body.getMass()
        new_mass     = original * bone_factor
        body.setMass(new_mass)
        print(f"    {body_name:10s}  {original:.4f} kg"
              f"  →  {new_mass:.4f} kg"
              f"  (loss {(1-bone_factor)*100:.2f}%)")

    # ── 3. Reduce Muscle Force (Atrophy) ────────────
    muscle_factor = 1.0 - (MUSCLE_LOSS_PER_DAY * day)
    muscle_set    = model.getMuscles()

    print("  MUSCLE FORCE:")
    for muscle_name in SPINE_MUSCLES:
        muscle    = muscle_set.get(muscle_name)
        original  = muscle.getMaxIsometricForce()
        new_force = original * muscle_factor
        muscle.setMaxIsometricForce(new_force)
        print(f"    {muscle_name:12s}  {original:.1f} N"
              f"  →  {new_force:.1f} N"
              f"  (atrophy {(1-muscle_factor)*100:.2f}%)")

    # ── 4. Save Model ────────────────────────────────
    out_path = os.path.join(
        OUTPUT_DIR, f"spine_day{day:03d}.osim"
    )
    model.printToXML(out_path)
    print(f"\n  ✅ Saved → {out_path}")

print("\n" + "=" * 55)
print("  All 5 models created successfully!")
print("  Ready for Phase 4 - Static Optimization")
print("=" * 55)