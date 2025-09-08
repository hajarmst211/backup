import numpy as np
from gradient_decent import gradient_descent

training_data=[[1,1,1], [1,0,1], [0,1,1], [0,0,0]]
itterations= 10_000

def _or(x,y):
	return x or y

def sigmoid_function(x, parameters):
	z= parameters[1]*x[0] + parameters[2]*x[1] + parameters[0]
	predicted_output= 1/(1+np.exp(-z))
	return predicted_output

def loss_function(x,y, parameters):
	y_predicted= sigmoid_function(x,parameters)
	dimension=len(x)
	loss= np.zeros(dimension)
	for i in range(dimension):
		loss[i]=-(y[i]*log(y_predicted[i]) + (1-y[i])*log(1-y_predicted[i]))
	return loss

def average_loss(loss):
	return np.mean(loss)

def main():
	parameters= np.zeros(3)
	predicted_y= np.zeros(2)
	for i in range(itterations):
		parameters = gradient_descent(training_data, parameters)
	for x1,x2,y in training_data:
		y_predicted = sigmoid_function([x1,x2], parameters)
		print(f"Input=({x1},{x2}), True={y}, Predicted={y_predicted:.4f}")






