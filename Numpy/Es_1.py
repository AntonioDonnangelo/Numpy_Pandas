'''Excercise 1: the max item of each row of a matrix.'''
import numpy as np 
x = [[1,2,3],[3,4,5],[6,7,8]] 
y = np.asarray(x)
y_max = y.max()
print(y_max)