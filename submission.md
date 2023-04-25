# Submission
Github Fork: https://github.com/Scraylex/WAS-exercise-7

## Task 3

### 1)

How do the parameters α and β impact the performance of your algorithm (comparing the
produced solution to the optimal solution)? Describe and interpret the behavior of your ant
colony for different parameter values, while considering that the ant population, the number
of iterations, and the evaporation rate remain fixed.

### 2)

How does the evaporation rate ρ affect the performance of your algorithm (comparing the
produced solution to the optimal solution)? Describe and interpret the behavior of your ant
colony for different evaporation rates, while considering that the ant population, the number
of iterations, and the parameters α and β remain fixed.

### 3)

This would require the following steps:

1. Update distance matrix size as well as nodes and edges
2. Update pheromone matrix dimensions and either insert default value for new edges and nodes or repeat the nearest neighbor calculation
3. Possibly play around further with the hyper parameters of the ACO algorithm. Maybe even introducing something like a higher decay rates for pheromones on certain edges encouraging either exploration or exploitation
4. Monitor the solution and adjust accordingly

This algorithm is definitely a good approach calculating the optimum path but will definitly get out performed in any type of practical scenario by a more deterministic algorithm using a variety of distance metrics in a more greedy fashion.
