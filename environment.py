import tsplib95
import numpy as np

# Class representing the environment of the ant colony
"""
    rho: pheromone evaporation rate
"""


def initialize_topology():
    return np.loadtxt("./att48-specs/att48_distance_matrix.txt")


class Environment:
    def __init__(self, rho):
        self.rho = rho
        problem = tsplib95.load_problem("./att48-specs/att48.tsp")
        # Initialize the environment topology
        self.dist_matrix = initialize_topology()
        #self.nodes = list(problem.get_nodes())
        self.node_coords = problem.node_coords
        self.node_count = self.dist_matrix.shape[0]
        # Intialize the pheromone map in the environment
        self.pheromone_matrix = self.initialize_pheromone_map()

    # Intialize the pheromone trails in the environment
    def initialize_pheromone_map(self):
        pheromone_matrix = np.copy(self.dist_matrix)
        pheromone_matrix[pheromone_matrix != 0] = self.node_count / self.greedy_traversal()
        return pheromone_matrix

    # Update the pheromone trails in the environment
    def update_pheromones(self, i, j, pheromone):
        self.pheromone_matrix *= self.rho
        self.pheromone_matrix[i, j] += pheromone
        self.pheromone_matrix[j, i] += pheromone

    # Get the pheromone trails in the environment
    def get_pheromone_map(self):
        return self.pheromone_matrix

    # Get the environment topology
    def get_possible_locations(self):
        return [x - 1 for x in self.node_coords.keys()]

    def get_current_location(self, location):
        return self.node_coords[location + 1]

    def greedy_traversal(self):
        # Get number of nodes
        num_of_nodes = len(self.dist_matrix)

        # Start at node 0
        current_node = 0
        visited_nodes = [current_node]

        # While there are still unvisited nodes
        while len(visited_nodes) < num_of_nodes:
            # Find the nearest unvisited neighbor
            unvisited_nodes = np.setdiff1d(range(num_of_nodes), visited_nodes)
            nearest_neighbor = np.argmin(self.dist_matrix[current_node][unvisited_nodes])
            nearest_node = unvisited_nodes[nearest_neighbor]
            # Add nearest neighbor to visited nodes and update current node
            visited_nodes.append(nearest_node)
            current_node = nearest_node

        # Add the distance from the last node back to the starting node
        total_distance = self.dist_matrix[visited_nodes[-1], 0]

        # Sum up the distances between each visited node
        for i in range(num_of_nodes - 1):
            total_distance += self.dist_matrix[visited_nodes[i], visited_nodes[i + 1]]

        print("Total tour distance greedy:", total_distance)
        return total_distance
