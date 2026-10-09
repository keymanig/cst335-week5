# CST 335 Week 5: MapReduce Simulation

## Project Overview

This project simulates a MapReduce-style workflow using Python and sample university equipment loan records. It demonstrates partitions, mapping, shuffling, reducing, and the differences between sequential and partitioned processing.

## Project Structure

- data/loans_full.csv: Full dataset containing 40 loan records.
- data/partition1.csv through partition4.csv: Four smaller CSV partitions.
- map_step.py: Reads each partition and generates key-value pairs.
- map_outputs/: Stores the intermediate map output CSV files.
- reduce_step.py: Groups map outputs and calculates category totals.
- results/final_counts.csv: Stores the final aggregated results.
- shuffle_simulation.md: Explains the shuffle stage.
- performance_notes.md: Compares sequential and partitioned workflows.
- reflection.md: Discusses MapReduce and Spark concepts.

## How to Run

Run these commands from the project folder:

    python3 map_step.py
    python3 reduce_step.py

The map script creates intermediate files in map_outputs/. The reduce script groups the values and saves final totals in results/final_counts.csv.

## Distributed Processing Concepts

The four CSV partitions represent separate portions of a larger dataset. The map stage processes records independently, the shuffle stage groups records by item category, and the reduce stage sums the values.

This project runs locally and does not use a real distributed cluster or actual parallel processing.

## AI Assistance Note

AI assistance was used to help draft and review the Python scripts and project documentation. The code and explanations should be reviewed and tested by the student to ensure understanding.
