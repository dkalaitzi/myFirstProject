import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv("final.csv")
#Figure 1: most popular item per zipcode
q=data.groupby('zip_code').bottles_sold.max()

f1 = plt.figure(1)
plt.scatter(q.index,q,c=np.random.rand(len(q),3), s=400)
plt.xlabel('Zip Code')
plt.ylabel('Bottles Sold')
plt.title('Bottles Sold')

#Figure 2: percentage of sales per store
q2=data.groupby('store_number').bottles_sold.sum().sort_values()
q2 = pd.DataFrame(q2, columns=['store_number','bottles_sold'])
# Computing Percentage
q2['Percent of Sales %'] = (q2['bottles_sold'] /
                  q2['bottles_sold'].sum()) * 100
s = pd.DataFrame(q2, columns=['Percent of Sales %'])
#plot
s.plot(kind='barh')
f2 = plt.figure(2)
plt.xlabel('Sales per Store')
plt.ylabel('Store Number')
plt.title('Sales per Store %')
plt.show()


