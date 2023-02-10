import os
import numpy as np

alpha = np.linspace(0.1 , 1.0 ,5 )
l1_ratio = np.linspace(0.1 , 1.0 ,5)



for i in alpha:
    for j in l1_ratio:
        print(f"logging experiment alpha: {i} l1_ratio: {j}")
        os.system(f"python demo.py -a {i} -l1 {j}")


