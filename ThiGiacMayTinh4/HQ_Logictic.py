#Sigmoid activation:ham kich hoat
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv('data_classification.csv',header=None)
True_x=[]
True_y=[]
False_x=[]
False_y=[]
for item in data.values:
    if item[-1]==1.:
        True_x.append(item[0])
        True_y.append(item[1])
    else:
        False_x.append(item[0])
        False_y.append(item[1])
plt.scatter(True_x,True_y,marker='o',c='b')
plt.scatter(False_x,False_y,marker='s',c='r')
#plt.show()
def sigmoid(z):
    return 1.0/(1+np.exp(-z))
def phanchia(p):
    if p>=0.5:
        return 1
    else:
        return 0
def predict(features,weights):
    z=np.dot(features,weights)
    #z=W_0+W_1ST+W2Slept
    """
    3*1+4*6+6*8=75
    Cùng kích thước mới sử dụng dot trong numpy
    """
    return sigmoid(z)
def const_function(features,label,weight):
    """

    :param features:(100
    :param label:
    :param weight:
    :return:
    """




