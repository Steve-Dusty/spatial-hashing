import math
import timeit
from shg import SpatialHashing

bounds = ((-100, -100), (100, 100))
dimensions = (10, 10)
sh = SpatialHashing(bounds, dimensions)

for i in range(100):
    position = (i, i)
    dimensions = (1, 1)
    sh.new_entity(position, dimensions)

query_position = (50, 50)
query_bounds = (10, 10)

def benchmark():
    entities = sh.query(query_position, query_bounds)

execution_time = timeit.timeit(benchmark, number=1) * 1000  
print("Execution time:", execution_time, "ms")