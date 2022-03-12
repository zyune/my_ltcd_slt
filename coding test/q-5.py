import matplotlib
import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator


file_name = '/Users/mac/penguins.csv'


def read_file(filename):
    rows = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rows.append(row)
    return rows


def q2_plot(column1, column2, filename):

    rows = read_file(filename)
    y1 = []
    y2 = []
    for i in rows:
        y1.append(i.get(column1))
        y2.append(i.get(column2))

    my_y_ticks = np.arange(0, 50, 1)
    plt.yticks(my_y_ticks)
    size = len(rows)
    x = np.arange(size)
    l1 = plt.plot(x, y1, 'r--', label='bill_length')
#     l2 = plt.plot(x, y2, 'g--', label='bill_depth')
#     plt.plot(x, y1, 'ro-', x, y2, 'g+-')
    plt.plot(x, y1, 'ro-')
    my_y_ticks = np.arange(0, 50, 1)
    plt.yticks(my_y_ticks)
    plt.title('The Lasers in Three Conditions')
    plt.xlabel('row')
    plt.ylabel('column')
    plt.legend()

    plt.show()


# test case 1
q2_plot("bill_length_mm", "bill_depth_mm", file_name)
