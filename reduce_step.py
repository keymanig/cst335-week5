import csv
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MAP_DIR = ROOT / "map_outputs"
RESULTS_DIR = ROOT / "results"

RESULTS_DIR.mkdir(exist_ok=True)

# Shuffle: group values by item category
grouped = defaultdict(list)

for map_file in sorted(MAP_DIR.glob("*_map.csv")):
    with open(map_file, "r", newline="") as source:
        reader = csv.DictReader(source)

        for row in reader:
            category = row["item_category"]
            count = int(row["count"])
            grouped[category].append(count)

# Reduce: add the values for each category
output_file = RESULTS_DIR / "final_counts.csv"

with open(output_file, "w", newline="") as destination:
    writer = csv.writer(destination)
    writer.writerow(["item_category", "total_loans"])

    for category in sorted(grouped):
        total = sum(grouped[category])
        writer.writerow([category, total])
        print(f"{category}: {total}")

print("Reduce step complete!")
print("Results saved to results/final_counts.csv")
