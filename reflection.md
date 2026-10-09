# Reflection on Distributed Processing

This project demonstrates the three main stages of MapReduce: map, shuffle, and reduce. During the map stage, each partition is processed separately, and every loan record becomes a key-value pair such as (laptop, 1). During shuffle, values with the same item category are grouped together. During reduce, the values in each group are added to calculate the final loan totals. The results are saved in a CSV file.

At a larger scale, distributed systems can process partitions on different computers. However, transferring intermediate data between computers can create network bottlenecks. Data skew can also occur when one category contains far more records than others, causing some tasks to take longer. Efficient partitioning and data movement are important for good performance.

Apache Spark improves on traditional MapReduce by organizing operations into a directed acyclic graph, or DAG, and optimizing how work is executed. Spark can keep useful data in memory to reduce repeated disk reads and can optimize shuffle operations. This project does not run Spark directly, but it demonstrates the basic ideas behind distributed data processing.
