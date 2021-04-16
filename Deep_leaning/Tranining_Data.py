from nnfs.datasets import spiral_data
import numpy as np
import matplotlib.pyplot as plt
import nnfs
nnfs.init()
class Layer_Dense:
    #Khởi tạo ngẫu nhiên trọng số với độ lệch
    def __init__(self,n_inputs,n_neurons):
        self.weight=0.01*np.random.randn(n_inputs,n_neurons)
        self.biases=np.zeros((1,n_neurons))
    def forward(self,inputs):
        self.output=np.dot(inputs,self.weight)+self.biases
#Tao ra dataset
X,y=spiral_data(samples=100,classes=3)
#Tao ra Dense layer voi 2 vecto dac trung dau vao va 3 gia tri dau ra
dense1=Layer_Dense(2,3)

#Thuc hien chuyen tiep lop thong qua huan luyen du lieu

dense1.forward(X)

print(dense1.output[:5])
