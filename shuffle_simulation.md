# Shuffle Simulation

## What the Shuffle Step Does

The map step processes each partition separately and produces key-value pairs such as (laptop, 1), (camera, 1), and (projector, 1).

The shuffle step groups together all values with the same item category, even when they come from different partition files.

## Grouped Results

- laptop: 1, 1, 1, 1, and other values from the partitions
- camera: 1, 1, 1, 1, and other values from the partitions
- projector: 1, 1, 1, 1, and other values from the partitions

Each 1 represents one loan record. The reduce step adds the values in each group to calculate the total number of loans for that category.

## Connection to Distributed Systems

In a real distributed system, map tasks can run on different computers. Their intermediate results are transferred and grouped by key so that matching keys can be processed together. This data movement is called a shuffle and can use significant network resources when datasets are large.

This project simulates the grouping locally without using a real distributed cluster.
