# -*- coding: utf-8 -*-
'''
Implemente e teste as operações de expansão e equalização de histograma. Aplique as
operações seguidas nas ordens:
a) Expansão → Equalização;
b) Equalização → Expansão.
E, compare os resultados obtidos entre a) e b)
'''

import config
import cv2
import numpy as np
from util import *

def questao3_a1(img):
	'''
	Equalizacao
	Parametros:
		img: imagem a ser tratada.
	'''
	# Conversao BGR para YIQ
	YIQ = img.copy()
	YIQ = np.double(YIQ) # Cast para double
	YIQ[:,:,2] = 0.299*img[:,:,2] + 0.587*img[:,:,1] + 0.114*img[:,:,0]
	YIQ[:,:,1] = 0.596*img[:,:,2] - 0.274*img[:,:,1] - 0.322*img[:,:,0]
	YIQ[:,:,0] = 0.211*img[:,:,2] - 0.523*img[:,:,1] + 0.312*img[:,:,0]

	
	for banda in range(0, 3):
		for linha in range(0, img[:,:,0].__len__()) :       	# Linhas
			for coluna in range(0, img[:,:,0][0].__len__()) :   # Colunas
				n = YIQ[linha,coluna,banda]
				n = truncar(n)
				YIQ[linha,coluna,banda] = n
	YIQ = np.uint8(YIQ) # Cast para unsigned integer 8 bits
	# Conversao finalizada

	histograma = []
	for i in range(0, 256):
		histograma.append(0)

	# Preenchendo o histograma
	for linha in range(0, img[:,:,0].__len__()) :       		# Linhas
			for coluna in range(0, img[:,:,0][0].__len__()) :  	# Colunas
				histograma[YIQ[linha,coluna,2]] += 1

	totalDePiexls = img[:,:,0].__len__() * img[:,:,0][0].__len__()

	# Com o histograma calculado, aplica as funcoes pmf, cdf e normalize
	pmf(histograma, totalDePiexls)
	cdf(histograma)
	normalize(histograma)

	for linha in range(0, img[:,:,0].__len__()) :       		# Linhas
		for coluna in range(0, img[:,:,0][0].__len__()) :    	# Colunas
			YIQ[linha,coluna,2] = histograma[YIQ[linha,coluna,2]]  

	# Conversao YIQ para BGR
	BGR = img.copy()
	BGR = np.double(BGR)
	BGR[:,:,0] = 1.000*YIQ[:,:,2] - 1.106*YIQ[:,:,1] + 1.703*YIQ[:,:,0]
	BGR[:,:,1] = 1.000*YIQ[:,:,2] - 0.272*YIQ[:,:,1] - 0.647*YIQ[:,:,0]
	BGR[:,:,2] = 1.000*YIQ[:,:,2] + 0.956*YIQ[:,:,1] + 0.621*YIQ[:,:,0]

	for banda in range(0, 3):
		for linha in range(0, img[:,:,0].__len__()) :         	# Linhas
			for coluna in range(0, img[:,:,0][0].__len__()) :   	# Colunas
				n = BGR[linha,coluna,banda]
				n = truncar(n)
				BGR[linha,coluna,banda] = n
	BGR = np.uint8(BGR)
	# Conversao finalizada 


	return BGR


# Funcao massa de probabilidade
def pmf(histograma, totalDePixels):
	for i in range(0, 256):
		histograma[i] = histograma[i] / float(totalDePixels)

# Funcao distribuicao acumulada
def cdf(histograma):
	for i in range (1, 256):
		histograma[i] = histograma[i] + histograma[i-1]

def normalize(histograma):
	for i in range(0, 256):
		histograma[i] = histograma[i] * 255

def questao3_b1(img):
	'''
	Expansao
	Parametros:
		img: imagem a ser tratada
	'''
	# Conversao BGR para YIQ
	YIQ = img.copy()
	YIQ = np.double(YIQ)
	YIQ[:,:,2] = 0.299*img[:,:,2] + 0.587*img[:,:,1] + 0.114*img[:,:,0]
	YIQ[:,:,1] = 0.596*img[:,:,2] - 0.274*img[:,:,1] - 0.322*img[:,:,0]
	YIQ[:,:,0] = 0.211*img[:,:,2] - 0.523*img[:,:,1] + 0.312*img[:,:,0]

	for banda in range(0, 3):
		for linha in range(0, img[:,:,0].__len__()) :       	# Linhas
			for coluna in range(0, img[:,:,0][0].__len__()) :   # Colunas
				n = YIQ[linha,coluna,banda]
				n = truncar(n)
				YIQ[linha,coluna,banda] = n
	YIQ = np.uint8(YIQ) # Cast para unsigned integer 8 bits
	# Conversao finalizada

	histograma = []
	for i in range(0, 256):
		histograma.append(0)
		
	# Preenchendo o histograma
	for linha in range(0, img[:,:,0].__len__()) :       		# Linhas
			for coluna in range(0, img[:,:,0][0].__len__()) :   # Colunas
				histograma[YIQ[linha,coluna,2]] += 1

	rmin = 255
	irmin = 0
	rmax = 0
	irmax = 0
	L = 256

	for i in range(0,histograma.__len__()):
		if histograma[i] <= rmin and histograma[i] > 0:
			rmin = histograma[i]
			irmin = i
				
	for i in range(0,histograma.__len__()):
		if histograma[i] >= rmax:
			rmax = histograma[i]
			irmax = i

	bandaY = YIQ.copy()

	for linha in range(0, img[:,:,0].__len__()) :       		# Linhas
		for coluna in range(0, img[:,:,0][0].__len__()) :   # Colunas
			aux = (float(YIQ[linha,coluna,2] - irmin) / (irmax - irmin)) * (L - 1)
			aux = truncar(aux)
			aux = round(aux)
			YIQ[linha,coluna,2] = aux

	# Conversao YIQ para BGR
	BGR = img.copy()
	BGR = np.double(BGR) # Cast para double
	BGR[:,:,0] = 1.000*YIQ[:,:,2] - 1.106*YIQ[:,:,1] + 1.703*YIQ[:,:,0]
	BGR[:,:,1] = 1.000*YIQ[:,:,2] - 0.272*YIQ[:,:,1] - 0.647*YIQ[:,:,0]
	BGR[:,:,2] = 1.000*YIQ[:,:,2] + 0.956*YIQ[:,:,1] + 0.621*YIQ[:,:,0]

	for banda in range(0, 3):
		for linha in range(0, img[:,:,0].__len__()) :       	# Linhas
			for coluna in range(0, img[:,:,0][0].__len__()) :   # Colunas
				n = BGR[linha,coluna,banda]
				n = truncar(n)
				BGR[linha,coluna,banda] = n
	BGR = np.uint8(BGR)
	# Conversao finalizada

	return BGR