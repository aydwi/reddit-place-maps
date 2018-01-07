import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

username = sys.argv[1]
filename = username + ".csv"

df = pd.read_csv(filename)

#colors = np.where(df.color == 6, 'r', 'b')
#print(colors)

plt.scatter(df.x, df.y, s=10)

plt.gca().set_aspect('equal', 'box')
plt.xlim(1,1000)
plt.ylim(1,1000)

plt.show()