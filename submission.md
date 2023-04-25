# Submission
Github Fork: https://github.com/Scraylex/WAS-exercise-7

## Task 3

Total tour distance greedy: 40551.0

### 1)

α generally manipulates the weight that the pheromone has in the probability calculation
β gives more weight to the distance heuristic

In my solution probably due to problems in the implementation it fluctuates weirdly and usually performs best when either alpha or beta are set to 0 or disproportionally strong.


Example (always 10 iterations):

| alpha | beta | distance |
| ----- | ---- | -------- |
| 1     | 2    | 53470    |
| 0     | 3    | 38805    |
| 0     | 1    | 46897    |
| 2     | 0    | 49736    |
| 1     | 1.5  | 57694    |
| 0.4   | 4    | 59251    |

as we can see from the data beta is a better in this example

### 2)

rho generally manipulates the weight of the pheromone evaporation indirectly influencing the probabilities picked

Experiment design:

- alpha = 1
- beta = 3
- iteration = 10

| rho | distance |
| --- | -------- |
| 0.1 | 62028    |
| 0.2 | 58212    |
| 0.3 | 57211    |
| 0.4 | 58656    |
| 0.5 | 58699    |
| 0.7 | 57166    |
| 0.9 | 58975    |

As can be seen the evaporation rate seems to be rather arbitrary for my implementation. =(

### 3)

This would require the following steps:

1. Update distance matrix size as well as nodes and edges
2. Update pheromone matrix dimensions and either insert default value for new edges and nodes or repeat the nearest neighbor calculation
3. Possibly play around further with the hyper parameters of the ACO algorithm. Maybe even introducing something like a higher decay rates for pheromones on certain edges encouraging either exploration or exploitation
4. Monitor the solution and adjust accordingly

This algorithm is definitely a good approach calculating the optimum path but will definitly get out performed in any type of practical scenario by a more deterministic algorithm using a variety of distance metrics in a more greedy fashion.
