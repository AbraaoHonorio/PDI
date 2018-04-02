from util import *
import numpy as np


def questao9A(img):
	'''
	aplicar o filtro
	  0  -1	   0
		+	+
	 -1	  5   -1
		+	+
	  0	  -1   0

	'''
	kernel = np.array(([0,-1,0],[-1, 5, -1],[ 0, -1, 0]))
	return applyFilter3x3(img, kernel)


	

def questao9B(img):
	'''
	aplicar o filtro
	  0   0	   0
		+	+
	  0	  1    0
		+	+
	  0	   0   -1
	'''

	applyFilter(img, [[],[],[]])
	pass