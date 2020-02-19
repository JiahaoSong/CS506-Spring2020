from collections import defaultdict
from math import inf
import random
import csv


def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """
    dim = len(points[0])
    avgs = []

    for x in range(dim):
        avg = 0
        for point in points:
            avg += point[x]
        
        avg /= len(points)
        avgs.append(avg)

    return avgs


def update_centers(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    clustering = defaultdict(list)
    centers = []
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    
    for c in clustering:
        center = point_avg(clustering[c])
        centers.append(center)
    
    return centers


def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """
    dim = len(a)
    dist = 0
    for x in range(dim):
        dist += (a[x] - b[x]) ** 2
    
    return dist ** (1 / 2)


def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    return random.sample(dataset, k = k)


def cost_function(clustering):
    cost = 0
    for c in clustering:
        center = point_avg(clustering[c])
        for point in clustering[c]:
            cost += distance(point, point)
    
    return cost



def generate_k_pp(dataset, k):
    pass


def _do_lloyds_algo(dataset, k_points):
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering


def k_means(dataset, k):
    k_points = generate_k(dataset, k)
    return _do_lloyds_algo(dataset, k_points)


def k_means_pp(dataset, k):
    k_points = generate_k_pp(dataset, k)
    return _do_lloyds_algo(dataset, k_points)
