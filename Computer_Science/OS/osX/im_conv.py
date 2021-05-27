import numpy as np
import cv2
import math
import pickle

def main(f_name):
	data = []
	with open(f_name, 'rb') as f:
		data = pickle.loads(f.read())
	m = math.floor(math.sqrt(len(data))) + 1
	_arr = np.zeros([m,m])
	k = 0
	for i in range(0, m):
		for j in range(0, m):
			if k < len(data):
				_arr[i][j] = data[k]
				k+=1
	_arr = _arr%255
	print(_arr)
	cv2.imshow("data", _arr)
	cv2.waitKey()

if __name__ == '__main__':

	f_ = "/Users/vinodpatil/Downloads/Learning/unknown_data.dat"
	main(f_)
