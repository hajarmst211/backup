#gradient_decent.py

import numpy as np
def gradient_vector(function, vector, epsilon=1e-6):
    dimension = len(vector)
    gradients = np.zeros(dimension)
    for i in range(dimension):
        vector_to_add = np.zeros(dimension)
        vector_to_add[i] += epsilon
        plus_vector = vector + vector_to_add
        minus_vector = vector - vector_to_add
        gradient_value = (function(plus_vector).item() - function(minus_vector).item()) / (2 * epsilon)
        gradients[i] = gradient_value
    return gradients

def gradient_descent( function,coefficients,  epsilon=1e-8, learning_rate=0.01):
    # norm > epsilon:
    for i in range(1000):
    	gvector = gradient_vector(function, coefficients)
    	coefficients -= learning_rate * gvector
    return coefficients



def main():
	f = lambda x: (x[0]**2+ 4*x[1]+x[2]+1)**2# v is a vector, so v[0] is the single variable x

	# Starting point (let's say x = 5)
	start = np.array([1,4,5], dtype=float)

	result = gradient_descent(f, start)

	print("Minimum found at:", result)
	print("f(x) at minimum:", f(result))



if __name__=="__main__":
	main()