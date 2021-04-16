import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

data=pd.read_csv('data.csv',header=None)
print(data)
X=data.values
im=SimpleImputer(missing_values=np.nan,strategy='most_frequent')
im.fit(X)
result=im.transform(X)
print('Ket qua la:')
print(result)