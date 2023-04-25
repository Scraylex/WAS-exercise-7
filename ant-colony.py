import numpy as np
from environment import Environment
from ant import Ant
import random

# Class representing the ant colony
"""
    ant_population: the number of ants in the ant colony
    iterations: the number of iterations 
    alpha: a parameter controlling the influence of the amount of pheromone during ants' path selection process
    beta: a parameter controlling the influence of the distance to the next node during ants' path selection process
    rho: pheromone evaporation rate
"""


class AntColony:
    def __init__(self, ant_population: int, iterations: int, alpha: float, beta: float, rho: float):
        self.ant_population = ant_population
        self.iterations = iterations
        self.alpha = alpha
        self.beta = beta
        self.rho = rho

        # Initialize the environment of the ant colony
        self.environment = Environment(self.rho)

        # Initilize the list of ants of the ant colony
        self.ants = []

        starting_locations = self.environment.get_possible_locations()
        # Initialize the ants of the ant colony
        for _ in range(ant_population):
            # Initialize an ant on a random initial location
            random_index = random.randint(0, len(starting_locations) - 1)
            start_location = starting_locations.pop(random_index)
            ant = Ant(self.alpha, self.beta, start_location)

            # Position the ant in the environment of the ant colony so that it can move around
            ant.join(self.environment)

            # Add the ant to the ant colony
            self.ants.append(ant)

    # Solve the ant colony optimization problem
    def solve(self):
        # The solution will be a list of the visited cities
        solution = []

        # Initially, the shortest distance is set to infinite
        shortest_distance = np.inf

        # Execute the ant colony optimization algorithm for a number of iterations
        for it in range(self.iterations):

            # Move each ant of the ant colony
            for ant in self.ants:
                ant.run()

            for ant in self.ants:
                # Update the pheromone trails of the environment of the ant colony
                for i in range(len(ant.visited_locations) - 1):
                    j = i + 1
                    self.environment.update_pheromones(ant.visited_locations[i], ant.visited_locations[j],
                                                       1 / ant.travelled_distance)

        # Find the ant that found the shortest path
        for ant in self.ants:
            if ant.travelled_distance < shortest_distance:
                shortest_distance = ant.travelled_distance / self.iterations
                solution = ant.visited_locations

        return solution, shortest_distance


def main():
    # Intialize the ant colony
    ant_population = 48
    iterations = 10
    alpha = 1
    beta = 3
    rho = 0.5
    ant_colony = AntColony(ant_population, iterations, alpha, beta, rho)

    # Solve the ant colony optimization problem
    solution, distance = ant_colony.solve()
    print("Solution: ", solution)
    print("Distance: ", distance)


if __name__ == '__main__':
    main()
