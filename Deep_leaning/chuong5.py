import numpy as np
import  nnfs
from  nnfs.datasets import spiral_data
nnfs.init()

class Layer_Dense:
    def __init__(self,n_inputs,n_neurons):
        self.weights=0.01*np.random.randn(n_inputs,n_neurons)
        self.biases=np.zeros((1,n_neurons))
    def foward(self,inputs):
        self.output=np.dot(inputs,self.weights)+self.biases
class Activation_ReLU:

    def forward(self,inputs):
        self.output=np.maximum(0,inputs)
class Activation_Softmax:
    def forward(self,inputs):
        exp_values=np.exp(inputs-np.max(inputs,axis=1,keepdims=True))
        probabilities=exp_values/np.sum(exp_values)
        self.output=probabilities
class Loss:
    def calculate(self,output,y):
        sample_losses=self.forward(output,y)
        data_loss=np.mean(sample_losses)
        return data_loss
class Loss_CategoricalCrossentropy(Loss):
    def forward(self,y_pred,y_true):
        samples=len(y_pred)
        y_pred_c

