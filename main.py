import random
from collections import deque

import matplotlib
from matplotlib import animation
from matplotlib import pyplot as plt

import insertionsort


def randomize_list(n):
    data = list(range(1, n + 1))
    random.shuffle(data)
    return deque(data)


def animate(step):
    xes = range(n)
    bars = sequence[step]
    # print (bars)

    colors = [cm(norm(float(i))) for i in bars]

    return plt.bar(xes, bars, color=colors)


if __name__ == "__main__":
    n = 50
    global sequence
    # sequence = bubblesort.bubblesort(randomize_list(n))
    # sequence = cocktailsort.cocktailsort(randomize_list(n))

    sequence = insertionsort.insertionsort(randomize_list(n))
    #for line in sequence:
    #    print(len(line))
    # print(len(sequence))

    cm = matplotlib.cm.get_cmap('viridis')
    norm = matplotlib.colors.Normalize(vmin=0, vmax=n)
    fig = plt.figure()
    anim = animation.FuncAnimation(fig, animate, frames=len(sequence), interval=1, blit=True)
    plt.show()

# todo make it quit nicer
# todo add a marker to show where the algorithm is looking??
