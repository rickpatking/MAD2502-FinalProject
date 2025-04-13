import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt

# Example
sites = np.array([[1,0], [4,2.5], [1,5], [7.5,4]])
start = np.array([5,6])
stop = np.array([6,0])

def voronoi_plotter(start: np.ndarray, stop: np.ndarray, sites: np.ndarray) -> None:
    """
    Takes the input of a starting point, ending point, and a list of sites then computes a voronoi diagram using the list of sites.
    The voronoi diagram along with the start and end points are displayed using matplotlib.
    :param start: A 1d numpy array containing a starting point
    :param stop: A 1d numpy array containing an ending point
    :param sites: A 2d numpy array containing various sites in the form of a point
    :return: Nothing is returned
    """
    vor = Voronoi(sites)
    fig, ax = plt.subplots()
    plt.plot(start[0], start[1], 'bo')
    plt.plot(stop[0], stop[1], 'ro')
    voronoi_plot_2d(vor, ax=ax)
    plot_max = max(start[1], stop[1])
    plot_min = min(start[1], stop[1])
    for site in sites:
        if site[1] > plot_max:
            plot_max = site[1]
        if site[1] < plot_min:
            plot_min = site[1]
    plt.ylim([plot_min-3, plot_max+3])
    plt.show()

def point_in_region(point: np.ndarray, sites: np.ndarray) -> tuple:
    """
    Takes the input of a 1d numpy array in the form of [1,0] as a point and a 2d numpy array in the form of [point, point]
    that can hold any number of points. The function will return a 1d tuple that holds the site closest to the entered point
    and the region number that the entered point is in. This is in the form of (site, region #).
    :param point: A point in the form of 1d numpy array
    :param sites: A list of points in the form of a 2d numpy array
    :return: Returns a tuple containing the site and region number that the entered point is in
    """
    def helper_distance(point1, point2):
        distance = ((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)**0.5
        return distance
    distance = []
    count = 0
    for site in sites:
        current_distance = helper_distance(point, [site[0], site[1]])
        distance.append([current_distance, [site[0], site[1]], count])
        count += 1
    min_distance = distance[0][0]
    for sub_list in distance:
        if sub_list[0] < min_distance:
            min_distance = sub_list[0]
    for array in distance:
        if array[0] == min_distance:
            cell_point = array[1]
            cell_point_number = array[2]
    vor = Voronoi(sites)
    return (cell_point, vor.point_region[cell_point_number])