import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_demo = pd.read_csv('./output/Demography/Top2Feature.csv')
N = 36
x = list(df_demo[df_demo.columns[1]])[:24] + list(df_demo[df_demo.columns[1]])[25:]
y = list(df_demo[df_demo.columns[2]])[:24] + list(df_demo[df_demo.columns[2]])[25:]
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

plt.scatter(x, y, s=area, c=colors, alpha=0.5)

plt.show()