import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("processed.csv")

#Un-comment the next line to hide points with 0 placements
#df['value'].fillna(1, inplace = True)

k = df['value']

k = np.power(np.log10(k),2)
max= k.max()

df['value'] = k

l = list(df.itertuples(index = False, name = None))

m = np.zeros((1000, 1000))

for x, y, value in l:
    m[int(x), int(y)] = value

m = m.transpose()

plt.imshow(m, cmap='hot')

for spine in plt.gca().spines.values():
    spine.set_linewidth(0.05)

plt.savefig('heatmap.png', format='png', dpi=1200)
plt.show()
