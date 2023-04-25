import tsplib95
import numpy as np
import random


class Ant():
    def __init__(self, alpha: float, beta: float, initial_location):
        self.environment = None
        self.alpha = alpha
        self.beta = beta
        self.initial_location = initial_location
        self.current_location = initial_location
        self.travelled_distance = 0
        self.visited_locations = [initial_location]

    # The ant runs to visit all the possible locations of the environment
    def run(self):
        possible_locations = self.environment.get_possible_locations()
        possible_locations.remove(self.initial_location)

        # Visit all possible locations
        while possible_locations:
            # Select the next path based on the Ant System algorithm
            next_location = self.select_path(possible_locations)
            # Move to the next location
            self.move(next_location)
            # Remove the next location from the list of possible locations to visit
            possible_locations.remove(next_location)

        # Move back to the initial location
        self.move(self.visited_locations[0])

    def select_path(self, possible_locations):
        # Compute the probabilities for each possible location
        total_prob = 0
        prob_list = []
        for possible_location in possible_locations:
            pheromone_level = self.environment.get_pheromone_map()[self.current_location][possible_location]
            distance = self.environment.dist_matrix[self.current_location][possible_location]
            current_to_j = (pheromone_level * self.alpha) * (distance * self.beta)

            sum_current_to_l = 0
            for l in possible_locations:
                sum_current_to_l += (self.environment.get_pheromone_map()[self.current_location][l] ** self.alpha) * (
                        self.environment.dist_matrix[self.current_location][l] ** self.beta)

            sum_current_to_l = np.nansum(np.nan_to_num(sum_current_to_l)) + 1e-8
            prob = current_to_j / sum_current_to_l
            total_prob += prob
            prob_list.append(prob)

        prob_list = np.nan_to_num(prob_list)  # replace NaN values with zeros
        prob_list /= prob_list.sum()  # normalize the probability distribution
        valid_mask = ~np.isnan(prob_list)  # create a mask of non-NaN values
        if valid_mask.sum() == 0:  # handle case where all probabilities are NaN
            return np.random.choice(possible_locations)  # choose randomly
        else:
            prob_list[~valid_mask] = 0  # set NaN probabilities to zero
            prob_list /= prob_list.sum()  # renormalize the probability distribution
            return np.random.choice(possible_locations, p=prob_list)  # sample from the distribution

    # Position an ant in an environment
    def join(self, environment):
        self.environment = environment

    # Move an ant to a new location and update its attributes
    def move(self, location):
        distance = self.get_distance(self.current_location, location)
        self.travelled_distance += distance
        if location != self.initial_location:
            self.visited_locations.append(location)
        self.current_location = location

    # Compute the pseudo-euclidean distance between two cities in the environment
    def get_distance(self, city1, city2):
        x1, y1 = self.environment.get_current_location(city1)
        x2, y2 = self.environment.get_current_location(city2)
        # tsplib95.distances.euclidean((x1, y1), (x2, y2))
        xd = x1 - x2
        yd = y1 - y2
        rij = np.sqrt((xd ** 2 + yd ** 2) / 10.0)
        tij = np.round(rij)
        if tij < rij:
            return tij + 1
        else:
            return tij
