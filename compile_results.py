# ── All Simulation Results Compiled ────────────────────

days         = [0,       30,      60,      90,      180    ]

# Parameter 1 — Bone Mass
torso_mass   = [34.2366, 33.8942, 33.5519, 33.2095, 32.1824]
pelvis_mass  = [11.7770, 11.6592, 11.5415, 11.4237, 11.0704]

# Parameter 2 — Muscle Forces
ercspn_force = [2500.0,  2395.8,  2291.7,  2187.5,  1875.0 ]
intobl_force = [900.0,    862.5,   825.0,   787.5,   675.0  ]
extobl_force = [900.0,    862.5,   825.0,   787.5,   675.0  ]
psoas_force  = [1113.0,  1066.6,  1020.2,   973.9,   834.8  ]
iliac_force  = [1073.0,  1028.3,   983.6,   938.9,   804.8  ]
total_muscle = [12972.0,12431.5, 11891.0, 11350.5,  9729.0  ]

# Parameter 3 — L4/L5 Load
l4l5_load    = [2318.70,   2.27,    2.17,    2.07,    1.77  ]

# Parameter 4 — Load Deficit
load_deficit = [0.00,    99.90,   99.91,   99.91,   99.92  ]

# Parameter 5 — Muscle Loss
muscle_loss  = [0.00,     4.17,    8.33,   12.50,   25.00  ]

# Parameter 6 — Bone Density Loss
bone_loss    = [0.00,     1.00,    2.00,    3.00,    6.00   ]

# Parameter 7 — Gravity
gravity      = [-9.80665, -0.01,  -0.01,   -0.01,   -0.01  ]

# Parameter 8 — Health Score
health_score = [100,      30,      25,      20,      10     ]

# Parameter 9 — Risk
risk         = ["None", "Critical","Critical","Critical","Critical"]

# Parameter 10 — Rehab needed
rehab        = ["None", "1 week", "2 weeks","3 weeks","6 weeks"]

# ── Color codes for terminal ────────────────────────────
RESET  = "\033[0m"
BOLD   = "\033[1m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
RED    = "\033[91m"
CYAN   = "\033[96m"
WHITE  = "\033[97m"
BLUE   = "\033[94m"

def color_val(val, good, warn, bad, reverse=False):
    """Color a value green/yellow/red based on thresholds."""
    if reverse:
        if   val <= good: return f"{GREEN}{val}{RESET}"
        elif val <= warn: return f"{YELLOW}{val}{RESET}"
        else:             return f"{RED}{val}{RESET}"
    else:
        if   val >= good: return f"{GREEN}{val}{RESET}"
        elif val >= warn: return f"{YELLOW}{val}{RESET}"
        else:             return f"{RED}{val}{RESET}"

def risk_color(r):
    if r == "None":     return f"{GREEN}{r}{RESET}"
    if r == "Critical": return f"{RED}{r}{RESET}"
    return f"{YELLOW}{r}{RESET}"

# ════════════════════════════════════════════════════════
# TABLE 1 — Mission Overview
# ════════════════════════════════════════════════════════
print(f"\n{BOLD}{'='*75}{RESET}")
print(f"{BOLD}{CYAN}  TABLE 1 — MISSION OVERVIEW{RESET}")
print(f"{BOLD}{'='*75}{RESET}")

print(f"\n  {BOLD}{'Parameter':<28} {'Day 0':>8} {'Day 30':>8} "
      f"{'Day 60':>8} {'Day 90':>8} {'Day 180':>8}{RESET}")
print(f"  {'-'*68}")

rows_t1 = [
    ("Gravity (m/s2)",
     [f"{g:.5f}" for g in gravity]),
    ("Health Score (0-100)",
     [str(h) for h in health_score]),
    ("Risk Level",
     risk),
    ("Rehab Needed",
     rehab),
]

for param, vals in rows_t1:
    row = f"  {param:<28}"
    for i, v in enumerate(vals):
        if param == "Health Score (0-100)":
            colored = color_val(
                int(v), 70, 40, 0)
            row += f" {colored:>8}"
        elif param == "Risk Level":
            colored = risk_color(v)
            row += f" {colored:>8}"
        else:
            row += f" {v:>8}"
    print(row)

# ════════════════════════════════════════════════════════
# TABLE 2 — Bone Parameters
# ════════════════════════════════════════════════════════
print(f"\n{BOLD}{'='*75}{RESET}")
print(f"{BOLD}{CYAN}  TABLE 2 — BONE PARAMETERS{RESET}")
print(f"{BOLD}{'='*75}{RESET}")

print(f"\n  {BOLD}{'Parameter':<28} {'Day 0':>8} {'Day 30':>8} "
      f"{'Day 60':>8} {'Day 90':>8} {'Day 180':>8}{RESET}")
print(f"  {'-'*68}")

rows_t2 = [
    ("Torso Bone Mass (kg)",    torso_mass),
    ("Pelvis Bone Mass (kg)",   pelvis_mass),
    ("Bone Density Loss (%)",   bone_loss),
    ("L4/L5 Load (N)",          l4l5_load),
    ("Load Deficit (%)",        load_deficit),
]

for param, vals in rows_t2:
    row = f"  {param:<28}"
    for v in vals:
        row += f" {v:>8.2f}"
    print(row)

# Bone mass change row
print(f"\n  {BOLD}{'Torso Mass Change':<28}{RESET}", end="")
for m in torso_mass:
    chg = ((m - torso_mass[0]) / torso_mass[0]) * 100
    val = f"{chg:+.2f}%"
    if   chg >= -1: c = GREEN
    elif chg >= -4: c = YELLOW
    else:           c = RED
    print(f" {c}{val:>8}{RESET}", end="")
print()

# Pelvis mass change row
print(f"  {BOLD}{'Pelvis Mass Change':<28}{RESET}", end="")
for m in pelvis_mass:
    chg = ((m - pelvis_mass[0]) / pelvis_mass[0]) * 100
    val = f"{chg:+.2f}%"
    if   chg >= -1: c = GREEN
    elif chg >= -4: c = YELLOW
    else:           c = RED
    print(f" {c}{val:>8}{RESET}", end="")
print()

# ════════════════════════════════════════════════════════
# TABLE 3 — Muscle Parameters
# ════════════════════════════════════════════════════════
print(f"\n{BOLD}{'='*75}{RESET}")
print(f"{BOLD}{CYAN}  TABLE 3 — MUSCLE FORCE PARAMETERS (N){RESET}")
print(f"{BOLD}{'='*75}{RESET}")

print(f"\n  {BOLD}{'Muscle':<28} {'Day 0':>8} {'Day 30':>8} "
      f"{'Day 60':>8} {'Day 90':>8} {'Day 180':>8}{RESET}")
print(f"  {'-'*68}")

muscle_data = [
    ("Erector Spinae R",   ercspn_force),
    ("Erector Spinae L",   ercspn_force),
    ("Internal Oblique R", intobl_force),
    ("Internal Oblique L", intobl_force),
    ("External Oblique R", extobl_force),
    ("External Oblique L", extobl_force),
    ("Psoas R",            psoas_force),
    ("Psoas L",            psoas_force),
    ("Iliacus R",          iliac_force),
    ("Iliacus L",          iliac_force),
]

for muscle, vals in muscle_data:
    row = f"  {muscle:<28}"
    for v in vals:
        row += f" {v:>8.1f}"
    print(row)

print(f"  {'-'*68}")
# Total row
row = f"  {'TOTAL SPINE FORCE':<28}"
for v in total_muscle:
    row += f" {v:>8.1f}"
print(f"{BOLD}{row}{RESET}")

# ════════════════════════════════════════════════════════
# TABLE 4 — Muscle Loss % per Muscle
# ════════════════════════════════════════════════════════
print(f"\n{BOLD}{'='*75}{RESET}")
print(f"{BOLD}{CYAN}  TABLE 4 — MUSCLE ATROPHY (% Loss from Baseline){RESET}")
print(f"{BOLD}{'='*75}{RESET}")

print(f"\n  {BOLD}{'Muscle':<28} {'Day 0':>8} {'Day 30':>8} "
      f"{'Day 60':>8} {'Day 90':>8} {'Day 180':>8}{RESET}")
print(f"  {'-'*68}")

for muscle, vals in muscle_data:
    row = f"  {muscle:<28}"
    for v in vals:
        loss = ((vals[0] - v) / vals[0]) * 100
        val  = f"{loss:.2f}%"
        if   loss <= 5:  c = GREEN
        elif loss <= 15: c = YELLOW
        else:            c = RED
        row += f" {c}{val:>8}{RESET}"
    print(row)

print(f"  {'-'*68}")
# Total muscle loss row
row_label = f"  {'TOTAL MUSCLE LOSS':<28}"
print(BOLD + row_label + RESET, end="")
for v in total_muscle:
    loss = ((total_muscle[0] - v) / total_muscle[0]) * 100
    val  = f"{loss:.2f}%"
    if   loss <= 5:  c = GREEN
    elif loss <= 15: c = YELLOW
    else:            c = RED
    print(f" {c}{val:>8}{RESET}", end="")
print()

# ════════════════════════════════════════════════════════
# TABLE 5 — Full Compiled Summary
# ════════════════════════════════════════════════════════
print(f"\n{BOLD}{'='*75}{RESET}")
print(f"{BOLD}{CYAN}  TABLE 5 — COMPLETE HEALTH MONITORING SUMMARY{RESET}")
print(f"{BOLD}  NASA HRP Study Simulation | Dr. Ashley Weaver, Wake Forest{RESET}")
print(f"{BOLD}{'='*75}{RESET}")

headers = [
    "Mission Day",
    "Gravity(m/s2)",
    "Torso(kg)",
    "Pelvis(kg)",
    "BoneLoss%",
    "TotalMuscle(N)",
    "MuscLoss%",
    "L4L5(N)",
    "Deficit%",
    "HealthScore",
    "Risk",
    "Rehab"
]

print(f"\n  {BOLD}", end="")
for h in headers:
    print(f"{h:>14}", end="")
print(f"{RESET}")
print(f"  {'-'*168}")

for i in range(len(days)):
    print(f"  ", end="")

    # Day
    print(f"{days[i]:>14}", end="")

    # Gravity
    print(f"{gravity[i]:>14.5f}", end="")

    # Torso mass
    tm = torso_mass[i]
    c  = GREEN if tm > 33.5 else (YELLOW if tm > 32.5 else RED)
    print(f"{c}{tm:>14.4f}{RESET}", end="")

    # Pelvis mass
    pm = pelvis_mass[i]
    c  = GREEN if pm > 11.5 else (YELLOW if pm > 11.2 else RED)
    print(f"{c}{pm:>14.4f}{RESET}", end="")

    # Bone loss
    bl = bone_loss[i]
    c  = GREEN if bl < 1 else (YELLOW if bl < 3 else RED)
    print(f"{c}{bl:>14.2f}{RESET}", end="")

    # Total muscle
    tm2 = total_muscle[i]
    c   = GREEN if tm2 > 12000 else (YELLOW if tm2 > 11000 else RED)
    print(f"{c}{tm2:>14.1f}{RESET}", end="")

    # Muscle loss
    ml = muscle_loss[i]
    c  = GREEN if ml < 5 else (YELLOW if ml < 15 else RED)
    print(f"{c}{ml:>14.2f}{RESET}", end="")

    # L4/L5 load
    ll = l4l5_load[i]
    c  = GREEN if ll > 1000 else RED
    print(f"{c}{ll:>14.2f}{RESET}", end="")

    # Load deficit
    ld = load_deficit[i]
    c  = GREEN if ld < 10 else RED
    print(f"{c}{ld:>14.2f}{RESET}", end="")

    # Health score
    hs = health_score[i]
    c  = GREEN if hs >= 70 else (YELLOW if hs >= 40 else RED)
    print(f"{c}{hs:>14}{RESET}", end="")

    # Risk
    rk = risk[i]
    c  = GREEN if rk == "None" else RED
    print(f"{c}{rk:>14}{RESET}", end="")

    # Rehab
    print(f"{rehab[i]:>14}", end="")
    print()

# ── Legend ──────────────────────────────────────────────
print(f"\n  {BOLD}Color Legend:{RESET}")
print(f"  {GREEN}GREEN{RESET}  = Healthy / Safe")
print(f"  {YELLOW}YELLOW{RESET} = Caution / Monitor")
print(f"  {RED}RED{RESET}    = Critical / Danger")

# ── Key Findings ─────────────────────────────────────────
print(f"\n{BOLD}{'='*75}{RESET}")
print(f"{BOLD}{CYAN}  KEY FINDINGS — NASA Confirmed{RESET}")
print(f"{BOLD}{'='*75}{RESET}")
print(f"""
  1. BONE LOSS
     Torso loses 6% mass over 6 months (1%/month)
     Matches NASA finding of ~1%/month in microgravity

  2. MUSCLE ATROPHY
     All 10 spine muscles lose exactly 25% force capacity
     by Day 180 without any countermeasures

  3. SPINAL LOAD
     L4/L5 drops from 2318 N to 1.77 N (99.9% deficit)
     Bones receive virtually zero stimulus to stay dense

  4. HEALTH DEGRADATION
     Health score: 100 (Earth) → 10 (Day 180)
     Risk status: Normal → Critical from Day 1 in space

  5. REHAB REQUIREMENT
     6 months in space = 6 weeks rehabilitation needed
     (NASA estimate: ~1 week rehab per month in space)
""")

print(f"{BOLD}{'='*75}{RESET}")
print(f"  Results compiled successfully!")
print(f"{'='*75}\n")