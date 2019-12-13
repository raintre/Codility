# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math

def solution(X, Y, D):
    # write your code in Python 3.6
    difference = Y - X
    divide = D
    jump = math.ceil(difference/divide)
    
    return jump