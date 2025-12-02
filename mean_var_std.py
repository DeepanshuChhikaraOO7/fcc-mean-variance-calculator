import numpy as np

def calculate(list):
    # 1. Error Handling: Check if list has exactly 9 elements
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    # 2. Convert list to 3x3 Numpy Array
    a = np.array(list).reshape(3, 3)

    # 3. Calculate metrics
    # Format: [axis=0 (cols), axis=1 (rows), flattened]
    
    calculations = {
        'mean': [
            a.mean(axis=0).tolist(), 
            a.mean(axis=1).tolist(), 
            a.mean()
        ],
        'variance': [
            a.var(axis=0).tolist(), 
            a.var(axis=1).tolist(), 
            a.var()
        ],
        'standard deviation': [
            a.std(axis=0).tolist(), 
            a.std(axis=1).tolist(), 
            a.std()
        ],
        'max': [
            a.max(axis=0).tolist(), 
            a.max(axis=1).tolist(), 
            a.max()
        ],
        'min': [
            a.min(axis=0).tolist(), 
            a.min(axis=1).tolist(), 
            a.min()
        ],
        'sum': [
            a.sum(axis=0).tolist(), 
            a.sum(axis=1).tolist(), 
            a.sum()
        ]
    }

    return calculations
