import numpy as np

inputs = [0, 2, -1, 5, -6, 0.6, 9, 2.5, -120]
output = []
for i in inputs:
    if i > 0:
        output.append(i)
    else:
        output.append(0)
print(output)

# Cach 2:
output2 = []
for i in inputs:
    output2.append(max(0, i))
print(f"Ket qua cach 2 {output2}")

# Cach 3 su dung thu vien cua numpy
output3 = np.maximum(0, inputs)
print(f"ket qua su dung Numpy {output3}")
