import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
OUTPUT_DIR = ROOT / "map_outputs"

OUTPUT_DIR.mkdir(exist_ok=True)

partitions = sorted(DATA_DIR.glob("partition*.csv"))

if not partitions:
    print("Error: No partition files found in data/")
else:
    for partition in partitions:
        output_file = OUTPUT_DIR / f"{partition.stem}_map.csv"

        with open(partition, "r", newline="") as source:
            reader = csv.DictReader(source)

            with open(output_file, "w", newline="") as destination:
                writer = csv.writer(destination)
                writer.writerow(["item_category", "count"])

                for row in reader:
                    writer.writerow([row["item_category"], 1])

        print(f"Processed {partition.name}")

    print("Map step complete!")
