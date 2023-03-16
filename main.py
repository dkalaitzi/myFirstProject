import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv("final.csv")
q=data.groupby('zip_code').bottles_sold.max()
#n = df.groupby('zip_code')
#n=cn.agg({'bottles_sold':max})
f1 = plt.figure(1)
plt.scatter(q.index,q,c=np.random.rand(len(q),3), s=400)
plt.xlabel('Zip Code')
plt.ylabel('Bottles Sold')
plt.title('Bottles Sold')
#plt.show()
q2=data.groupby('store_number').bottles_sold.sum().sort_values()
f2 = plt.figure(2)
q2.plot(kind='barh')
plt.xlabel('Sales per Store')
plt.ylabel('Store Number')
plt.title('Sales per Store')
plt.show()

