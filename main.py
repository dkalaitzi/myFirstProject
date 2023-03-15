import pandas as pd
import numpy as np

df=pd.read_csv("final.csv")

cn = df.groupby('zip_code')
print(cn.agg({'bottles_sold':max}))
