import pandas as pd

df = pd.read_csv('tmpfile5.csv', header = None)

df[len(df.columns)] = float('nan')

df.to_csv('tmpfile6.csv', index=False, header = False)
