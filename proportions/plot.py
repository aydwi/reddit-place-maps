import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("file.csv")

colors = ["#FFFFFF", "#E4E4E4", "#888888", "#222222", "#FFA7D1", "#E50000", "#E59500", "#A06A42",
          "#E5D900", "#94E044", "#02BE01", "#00E5F0", "#0083C7", "#0000EA", "#E04AFF", "#820080"]

t=len(df)
l=[]

for i in range (16):
    k = len ( df [ ( df['value'] == i ) ] )
    p = k*100/t
    l.append(p)

"""
np.random.seed(19680801)

N = 16
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii = l
#width = (2*np.pi) / N
width = np.pi / 4 * np.random.rand(N)

ax = plt.subplot(111, projection='polar')
bars = ax.bar(theta, radii, width=width, bottom=0)

val = 0

for bar in bars:
    bar.set_facecolor(colors[val])
    bar.set_alpha(0.85)
    val += 1

plt.show()
"""

sns.set_style("whitegrid")
sns.barplot(colors,l,saturation = 0.85, palette = colors, linewidth=0.8, edgecolor=".8")

plt.show()