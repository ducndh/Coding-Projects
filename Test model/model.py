import numpy as np
import json
import random
from sklearn.linear_model import LinearRegression
class Model: 

    def __init__(self, file: str, ground_truth: str):
        self.file = file
        self.ground_truth = ground_truth
    def run(self) -> None:
        X = []
        Y = []
        f = open(self.file, "r")
        next(iter(f))
        i = 0
        for line in f:
            row_ele = line.split()
            # x = float(row_ele[8])*random.uniform(0.85, 1.1) + float(row_ele[8])*2*float(row_ele[7])*random.uniform(0.9, 1.2) + float(row_ele[6])*random.uniform(0.5, 1.7)
            # x = float(row_ele[8])*random.uniform(0.7, 1.15) + float(row_ele[7])*3*random.uniform(0.6, 1.1)
            x = float(row_ele[9])*random.uniform(0.86, 1.17)
            X.append(x)
            i += 1
            if i > 200:
            	break        
        with open(self.ground_truth, 'r') as f:
            Y = json.load(f)['ground_truth']
        X_np = np.array(X)
        Y_np = np.array(Y)
        score = (X_np-Y_np).T@(X_np-Y_np)/X_np.shape[0]
        return({'result': X}, {'score': score})
