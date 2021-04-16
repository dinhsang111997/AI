import numpy as np
sofmax_outputs=np.array([[0.7,0.1,0.2],
                         [0.1,0.5,0.4],
                         [0.02,0.9,0.08]])
class_targets = np.array([[1, 0, 0],
                          [0, 1, 0],
                          [0, 1, 0]])
if len(class_targets.shape)==1:
    correct_confidences=sofmax_outputs[range(len(sofmax_outputs)),class_targets]
elif len(class_targets.shape)==2:
    correct_confidences=np.sum(sofmax_outputs*class_targets,axis=1)
neg_log=-np.log(correct_confidences)
average_loss=np.mean(neg_log)
print(average_loss)