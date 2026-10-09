# CST 335 Week 5: MapReduce Simulation

## Project Overview

For this assignment, I created a small MapReduce simulation using Python and sample equipment loan data. The goal was to learn how data can be split into smaller files, processed separately, and combined to get final results. I used four partitions with loan records for laptops, cameras, and projectors.

## Project Files

* `data/` contains the full loan dataset and the four partition CSV files.
* `map_step.py` reads each partition and creates the map output files.
* `map_outputs/` stores the results from the map step.
* `reduce_step.py` groups the data by item category and counts the loans.
* `results/final_counts.csv` contains the final totals.
* `shuffle_simulation.md` explains how the shuffle step groups the data.
* `performance_notes.md` compares processing one file with processing multiple partitions.
* `reflection.md` explains what I learned about MapReduce and Spark.

## How to Run the Project

I used Python to run the scripts. From the project folder, run:

```bash
python3 map_step.py
python3 reduce_step.py
```

The first script processes the partition files, and the second script combines the results and saves the final counts.

## What I Learned

This assignment helped me understand how MapReduce works through the map, shuffle, and reduce steps. Instead of processing all the data as one large file, the data can be split into partitions and processed separately before the results are combined.

I also learned that partitioning can help with larger datasets because different parts of the work can run on different computers. My project runs locally on my computer, so it simulates the process rather than using an actual distributed system.

## AI Assistance

I used AI to help me work through the Python code and organize some of the project documentation. I tested the scripts and used the results to check that the workflow was working as expected.

