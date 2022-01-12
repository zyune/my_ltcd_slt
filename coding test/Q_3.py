import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# source : https://stackoverflow.com/questions/42372617/how-to-plot-csv-data-using-matplotlib-and-pandas-in-python
# https://zhuanlan.zhihu.com/p/25128216


def plot_with_pandas():
    file_name = '/Users/mac/penguins.csv'
    df = pd.read_csv(file_name)
    # print(type(df))
    bl = df['bill_length_mm']
    bd = df['bill_depth_mm']

    size = len(df)
    # print(size)
    x = np.arange(size)
    total_width, n = 0.8, 2
    width = total_width / n
    plt.bar(x, bl,  width=width, label='bill_lengths')
    plt.bar(x + width, bd, width=width, label='bill_depths')
    plt.legend()
    plt.show()
# since I didn't receive an email telling me which github address to push to, I wrote my git commend here
# pull request: git add /Users/mac/my_ltcd_slt/coding test/Q_3.py
# git commit -m "my solution to Q3"
# git push <remote> <branch>
