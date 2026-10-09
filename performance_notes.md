# Sequential vs. Partitioned Processing

## Sequential Workflow

A sequential workflow reads the entire loans_full.csv file and counts the item categories in one pass. This approach is simple and works well for small datasets that fit on one computer.

## Partitioned Workflow

The partitioned workflow divides the loan records into four smaller CSV files. The map script processes each partition separately, and the reduce script combines the intermediate results to calculate final totals.

## Comparison

- Workflow: Sequential processing reads one complete file. Partitioned processing handles separate files before combining results.
- Parallelism: Partitions can be processed simultaneously on different computers in a distributed system. Our Python script processes them one after another, so it demonstrates the concept rather than actual parallel execution.
- Error isolation: Separate partitions can make it easier to identify which file contains a problem.
- Scalability: Partitioning allows large workloads to be spread across multiple machines. However, partitioning alone does not guarantee faster performance because combining data adds overhead.
- Timing: This assignment does not require actual timing measurements, so this comparison focuses on workflow and scalability.

For this small dataset, sequential processing would likely be sufficient. Partitioning becomes more useful when datasets grow and work can be distributed across multiple machines.
