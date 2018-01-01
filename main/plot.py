import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("processed.csv")

k = df['value']
l=[]

k = np.power(np.log10(k),2)
max= k.max()
k = k/max

df['value'] = k
#df.loc[df.value == 0.00000, 'value'] = np.inf

df.to_csv('norm.csv', index=False)
l = list(df.itertuples(index=False))


data = np.genfromtxt('norm.csv', dtype = float, delimiter=',', names=True)

print(data)

l=list(df.itertuples(index=False, name = None))

m = np.zeros((1000, 1000))

for x, y, value in l:
    m[int(x), int(y)] = value

m = m.transpose()

print("This matrix has normalized values of all 1000000 pixels\n\n")
print(m)

plt.imshow(m, cmap='hot')

for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.savefig('myimage.png', format='png', dpi=1000)
plt.show()