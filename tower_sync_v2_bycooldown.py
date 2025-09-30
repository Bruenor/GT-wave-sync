
from math import gcd, floor

WAVE_CD = 35
TOTAL_TIME = 36000  # 10 hours in seconds

def compute_exact_overlaps(golden_tower_cd, golden_tower_duration):
    # Step 1: LCM of A and B. Returns an integer
    lcm = (golden_tower_cd * WAVE_CD) // gcd(golden_tower_cd, WAVE_CD)

    # Step 2: A and B event times within one LCM cycle. Result is array of times when event A or B occurs
    gt_activation_times = [golden_tower_cd * i for i in range(lcm // golden_tower_cd)]
    new_wave_start_times = [WAVE_CD * i for i in range(lcm // WAVE_CD)]

    # Step 3: Count exact overlaps
    overlaps = 0
    for gt_start in gt_activation_times:
        gt_end = gt_start + golden_tower_duration
        for wave_start in new_wave_start_times:
            if gt_start <= wave_start < gt_end:
                overlaps += 1

    # Step 4: Number of full LCM cycles in 10 hours
    full_cycles = floor(TOTAL_TIME / lcm)

    # Step 5: Total overlaps
    total_overlaps = overlaps * full_cycles

    return [
        golden_tower_duration,
        lcm,
        len(gt_activation_times),
        len(new_wave_start_times),
        overlaps,
        full_cycles,
        total_overlaps
    ]

# Cooldowns and durations to test
cooldowns = [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]
durations = list(range(28, 38))  # 26 to 31 inclusive

# Headers for the inner tables
headers = [
    "Duration(GT)", "Cycle[s]",
    "GT/cycle", "Waves/cycle",
    "Overlaps/cycle", "Full cycles", "Total overlaps"
]
header_fmt = "{:>12} {:>10} {:>10} {:>12} {:>15} {:>12} {:>15}"
row_fmt    = "{:12d} {:10d} {:10d} {:12d} {:15d} {:12d} {:15d}"

print("New wave every 35 seconds (Tier 1).")
print("Assume 10 hour run time. 36000 seconds.")

for cd in cooldowns:
    print("=" * 100)
    print(f"Cooldown (GT) = {cd} sec")
    print(header_fmt.format(*headers))
    print("-" * 100)
    for d in durations:
        row = compute_exact_overlaps(cd, d)
        print(row_fmt.format(*row))
    print()  # blank line between tables
