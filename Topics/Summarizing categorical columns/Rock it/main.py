import pandas as pd
import numpy as np

df=pd.read_csv(r'./data/dataset/input.txt')
print(df.labels.value_counts().loc[['R']][0])

