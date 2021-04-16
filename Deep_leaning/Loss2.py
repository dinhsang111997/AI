softmax_outputs=[[0.7,0.1,0.2],
                 [0.1,0.5,0.4],
                 [0.02,0.9,0.08]]
#[0.7,0.1,0.2] 0.7 lon nhat nen du doan la 0
class_targets=[0,1,1]
for targ_idx,distribution in zip(class_targets,softmax_outputs):
    print(distribution[targ_idx])
