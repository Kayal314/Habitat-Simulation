import matplotlib.pyplot as plt


def write_population(rabbit: list, fox: list, grassland: list, forest: list, pond: list, lake: list):
    f = open('population_graph', 'w')
    size = len(rabbit)
    for i in range(0, size):
        f.write(rabbit[i] + " " + fox[i] + " " + grassland[i] + " " + forest[i] + " " + pond[i] + " " + lake)


def plot_animal_population(rabbit: list, fox: list):
    x_coordinates = range(1, len(rabbit) + 1)
    plt.plot(x_coordinates, rabbit, color='#3daeff', label='rabbit population')
    plt.plot(x_coordinates, fox, color='#ff3679', label='fox population')
    plt.legend(['rabbit', 'fox'])
    plt.show()


def plot_resource_changes(grassland: list, forest: list, pond: list, lake: list):
    x_coordinates = range(1, len(grassland) + 1)
    plt.plot(x_coordinates, grassland, color='#21d9c3', label='grassland')
    plt.plot(x_coordinates, forest, color='#460991', label='forest')
    plt.plot(x_coordinates, pond, color='#088538', label='pond')
    plt.plot(x_coordinates, lake, color='#d6d30b', label='lake')
    plt.legend(['grassland', 'forest', 'pond', 'lake'])
    plt.show()


def plot_all(grassland: list, forest: list, pond: list, lake: list, rabbit: list, fox: list):
    x_coordinates = range(1, len(rabbit) + 1)
    plt.plot(x_coordinates, rabbit, linestyle='dashed', color='#3daeff', label='rabbit population')
    plt.plot(x_coordinates, fox, linestyle='dashed', color='#ff3679', label='fox population')
    plt.plot(x_coordinates, grassland, color='#21d9c3', label='grassland')
    plt.plot(x_coordinates, forest, color='#460991', label='forest')
    plt.plot(x_coordinates, pond, color='#088538', label='pond')
    plt.plot(x_coordinates, lake, color='#d6d30b', label='lake')
    plt.legend(['rabbit', 'fox', 'grassland', 'forest', 'pond', 'lake'])
    plt.show()


def write(grassland: list, forest: list, pond: list, lake: list, rabbit: list, fox: list):
    f = open('population_graph', 'w')
    size = len(rabbit)
    for i in range(0, size):
        f.write(str(rabbit[i]) + "," + str(fox[i]) + "," + str(grassland[i]) + "," + str(forest[i]) +
                "," + str(lake[i]) + "," + str(pond[i]) + "\n")
    f.close()
