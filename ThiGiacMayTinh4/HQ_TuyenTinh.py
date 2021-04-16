import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('Advertising.csv')
X=data.values[:,2]
Y=data.values[:,-1]
plt.scatter(X,Y,marker='o')
print(X)
plt.show()
def predict(new_radio,weight,bias):
    return weight*new_radio+bias
def cost_function(X,Y,weight,bias):
    n = len(X)
    sum_error = 0
    for i in range(n):
        sum_error+=(Y[i]-(weight*X[i]+bias))**2
    return sum_error/n
def update_weight(X,Y,weight,bias,learning_rate):
    n=len(X)
    weight_temp = 0.0
    bias_temp = 0.0
    for i in range(n):
        weight_temp+=-2*X[i]*(Y[i]-(weight*X[i]+bias))
        bias_temp+=-2*(Y[i]-(weight*X[i]+bias))
    weight-=(weight_temp/n)*learning_rate
    bias-=(bias_temp/n)*learning_rate
    return weight,bias
def train(X,Y,weight,bias,learning_rate,inter):
    cost_his=[]
    for i in range(inter):
       weight,bias=update_weight(X,Y,weight,bias,learning_rate)
       cost=cost_function(X,Y,weight,bias)
       cost_his.append(cost)
    return weight,bias
weight,bias= train(X,Y,0.03,0.0014,0.001,30)
print('Ket qua:')
print(weight)
print(bias)
print('Gia tri du doan')
print(predict(19,weight,bias))




