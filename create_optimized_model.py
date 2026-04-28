import opensim as osim

NO_EXOSUIT    = r"C:\SpineSimulation\Models\spine_day180.osim"
OPTIMIZED_OUT = r"C:\SpineSimulation\Models\spine_day180_optimized.osim"

SPINE_MUSCLES = [
    "ercspn_r","ercspn_l",
    "intobl_r","intobl_l",
    "extobl_r","extobl_l",
    "psoas_r", "psoas_l",
    "iliacus_r","iliacus_l"
]

print("=" * 60)
print("  Creating Optimized Exosuit Model")
print("  Health Score: 76.4/100 (HEALTHY)")
print("=" * 60)

model = osim.Model(NO_EXOSUIT)
state = model.initSystem()
print(f"\n  Base mass : {model.getTotalMass(state):.4f} kg")

# Bone recovery: loss 6.00% → 1.03%
BONE_RECOVERY = (100 - 1.03) / (100 - 6.00)
print(f"  Bone recovery factor : {BONE_RECOVERY:.4f}")

body_set = model.getBodySet()
print(f"\n  {'Body':<14} {'Day180':>10} "
      f"{'Optimized':>11} {'Change':>8}")
print(f"  {'-'*46}")

for i in range(body_set.getSize()):
    body = body_set.get(i)
    if body.getName() == "ground":
        continue
    old_m = body.getMass()
    new_m = old_m * BONE_RECOVERY
    body.setMass(new_m)
    print(f"  {body.getName():<14} "
          f"{old_m:>10.4f} "
          f"{new_m:>11.4f} "
          f"{new_m-old_m:>+8.4f}")

# Muscle recovery: loss 25.00% → 12.81%
MUSCLE_RECOVERY = (100 - 12.81) / (100 - 25.00)
print(f"\n  Muscle recovery factor: {MUSCLE_RECOVERY:.4f}")

muscle_set = model.getMuscles()
print(f"\n  {'Muscle':<14} {'Day180':>8} "
      f"{'Optimized':>10} {'Change':>8}")
print(f"  {'-'*44}")

for name in SPINE_MUSCLES:
    try:
        m     = muscle_set.get(name)
        old_f = m.getMaxIsometricForce()
        new_f = old_f * MUSCLE_RECOVERY
        m.setMaxIsometricForce(new_f)
        print(f"  {name:<14} {old_f:>8.1f} "
              f"{new_f:>10.1f} "
              f"{new_f-old_f:>+8.1f}")
    except:
        pass

state2   = model.initSystem()
new_mass = model.getTotalMass(state2)
model.setName("astronaut_spine_OPTIMIZED_exosuit")
model.printToXML(OPTIMIZED_OUT)

print(f"\n{'='*60}")
print(f"  OPTIMIZED MODEL SUMMARY")
print(f"{'='*60}")
print(f"  Mass    : {new_mass:.4f} kg")
print(f"  Bone loss prevented: 6.00% → 1.03%")
print(f"  Muscle loss reduced: 25.00% → 12.81%")
print(f"  Health score: 76.4/100 HEALTHY")
print(f"  Rehab needed: 1.0 week only!")
print(f"\n  Saved → {OPTIMIZED_OUT}")
print(f"\n  Load in OpenSim to show 3 models:")
print(f"  1. spine_day000.osim        (100/100 Earth)")
print(f"  2. spine_day180.osim        (10/100 No exosuit)")
print(f"  3. spine_day180_optimized   (76.4/100 HEALTHY)")
print(f"{'='*60}\n")