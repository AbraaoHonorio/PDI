from util import *
import numpy as np
import cv2


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
	kernel = np.array(([0, 0, 0], [0, 1, 0], [0, 0, -1]))
	return applyFilter3x3(img, kernel)

def questao9ATest(img):
	'''
	Usa a funcao da propria biblioteca prar observar o resultado
	'''
	kernel = np.array(([0,-1,0],[-1, 5, -1],[ 0, -1, 0]))
	resultImage = img # pegar o mesmo tamanho da imaem original
	cv2.filter2D(src=img, ddepth=-1, kernel=kernel, dst=resultImage)

	return resultImage

def questao9BTest(img):
	kernel = np.array(([0, 0, 0], [0, 1, 0], [0, 0, -1]))	
	resultImage = img # pegar o mesmo tamanho da imaem original
	cv2.filter2D(src=img, ddepth=-1, kernel=kernel, dst=resultImage)

	return resultImage