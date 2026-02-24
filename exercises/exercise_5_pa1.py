import numpy as np
import math
import matplotlib.pyplot as plt


def silly_walk(steps: int):
    """creats a 'random walk' and returns list with the outcomes"""

    position = 0
    distance_list = []
    for i in range(steps):
        if np.random.random() >= 0.5:
            position = position + 1
            distance_list.append(position)
        else:
            position = position - 1
            distance_list.append(-1)

    return distance_list


def stats(walk_list: list):
    """prints the stats to a randomly generated walk"""

    return (
        print("max. distance from starting position:", max(walk_list)),
        print("final position:", walk_list[len(walk_list) - 1]),
        print("mean total distance:", sum(walk_list) / len(walk_list)),
    )


def plot_walk(walk_list: list):
    """plots a silly walk"""

    plt.plot(walk_list)
    plt.show()


def plot_walk_n(multi_walk: int):
    """creates and plots 'n' silly walks"""

    walks = []
    for i in range(multi_walk):
        walks.append(silly_walk(100))
        plt.plot(walks[len(walks) - 1])

    print(sum(walks) / len(walks))

    plt.legend()
    plt.show()


print(plot_walk_n(5))
