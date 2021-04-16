import math

sofmax_output=[0.7,0.1,0.2]
target_output=[1,0,0]

loss=-(math.log(sofmax_output[0]*target_output[0]))
print(loss)