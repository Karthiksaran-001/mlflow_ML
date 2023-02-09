import os

a, b = range(0,5) , range(0,5)

for i in a:
    for j in b:
        print(f"logging experiment {i} : {j}")
        os.system(f"python demo.py -p1 {i} -p2 {j}")
