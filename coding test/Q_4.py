import Q_1
import Q_2
import numpy as np
import matplotlib.pyplot as plt
file_name2 = "/Users/mac/iris-data.csv"
print(Q_1.read_file(file_name2))
# Q_2.q2_plot("sepal length", "sepal width")


# def q4_plot(column1, column2, filename):
#     rows = Q_1.read_file(filename)
#     bill_lengths = []
#     bill_depths = []
#     for i in rows:
#         bill_lengths.append(i.get(column1))
#         bill_depths.append(i.get(column2))
#     # print(bill_depths)
#     # print(rows[1].get("bill_length_mm"))
#     size = len(rows)
#     x = np.arange(size)
#     total_width, n = 0.8, 2
#     width = total_width / n
#     ax = plt.gca()
#     ax.set_ylabel("y_label")
#     ax.set_xlabel("x_label")
#     plt.bar(x, bill_lengths,  width=width, label='column1')
#     plt.bar(x + width, bill_depths, width=width, label='column2')
#     plt.legend()
#     plt.show()


Q_2.q2_plot("sepal length", "sepal width", file_name2)
