# -*- coding: utf-8 -*-
import cv2
import numpy as np
from util import *

'''
Teste o sistema desenvolvido no item 1 com as seguintes máscaras convolucionais, sobre
cada banda de imagens RGB e sobre a imagem convertida para níveis de cinza (banda Y), e
explique os resultados. Cuidado com valores negativos ou superiores a 255 na imagem
resultante. Compare com os resultados obtidos com a função conv2 do MATLAB.
'''

def questao2_a1(img, c=1, d=1):
	'''
	Aplica um filtro especifico:
	
	Parametros:
		c e d sao inteiros positivos quaisquer


	'''
	mask = [[0, -c, 0],
			[-c, 4*c+d, -c],
			[0, -c, 0]]

	return correlacao_comum(img, mask)

def questao2_a2(img, c, d):
	'''
	Aplica um filtro especifico:
	Parametros:
		c e d sao inteiros positivos quaisquer
	'''


	mask = [[-c, -c, -c],
			[-c, 8*c+d, -c],
			[-c, -c, -c]]

	return correlacao_comum(img, mask)

def questao2_b1(img):
	'''
	Aplica um filtro especifico:
	
	'''
	mask = [[-1/8, -1/8, -1/8],
		[-1/8, 1, -1/8],
		[-1/8, -1/8, -1/8]]

	return correlacao_comum(img, mask)

def questao2_b2(img):
	'''
	Aplica um filtro especifico:
	
	'''


	mask = [[-1, -1, -1],
			[0, 0, 0],
			[1, 1, 1]]

	return correlacao_comum(img, mask)

def questao2_b3(img):
	'''
	Aplica um filtro especifico:
	
	'''
	mask = [[-1, 0, 1],
			[-1, 0, 1],
			[-1, 0, 1]]

	return correlacao_comum(img, mask)

def questao2_b4(img):
	'''
	Aplica um filtro especifico:
	
	'''


	mask = [[-1, -1, 0],
			[-1, 0, 1],
			[0, 1, 1]]

	return correlacao_comum(img, mask)

def questao2_c1(img):
	'''
	Aplica um filtro especifico:
	
	'''
	mask = [[0, 0, 0],
			[0, 1, 0],
			[0, 0, -1]]

	return correlacao_comum(img, mask)

def questao2_c2(img):
	'''
	Aplica um filtro especifico:
	
	'''
	mask = [[0, 0, -1],
			[0, 1, 0],
			[0, 0, 0]]

	return correlacao_comum(img, mask)

def questao2_c3(img):
	'''
	Aplica um filtro especifico:
	
	'''

	mask = [[0, 0, 2],
        	[0, 1, 0],
        	[-1, 0, 0]]

	return correlacao_comum(img, mask)

def correlacao_comum(image, kernel):
	'''
	Cria uma função para fazer a correlação simples, movendo a máscara sobre a imagem
	Fonte: https://www.pyimagesearch.com/2016/07/25/convolutions-with-opencv-and-python/
	Parametros:
		- img: imagem original
		- mascara: mascara a ser correlacionada. Deve ser uma matriz 3x3

	'''
	
	# grab the spatial dimensions of the image, along with
	# the spatial dimensions of the kernel
	(iH, iW) = image.shape[:2]
	(kH, kW) = (len(kernel), len(kernel[0]))

	# allocate memory for the output image, taking care to
	# "pad" the borders of the input image so the spatial
	# size (i.e., width and height) are not reduced
	pad = (kW - 1) / 2
	image = cv2.copyMakeBorder(image, pad, pad, pad, pad,
		cv2.BORDER_REPLICATE)
	output = np.zeros((iH, iW,3), dtype="float32")
	
	

	# loop over the input image, "sliding" the kernel across
	# each (x, y)-coordinate from left-to-right and top to
	# bottom
	for y in np.arange(pad, iH + pad):
		for x in np.arange(pad, iW + pad):
			# extract the ROI of the image by extracting the
			# *center* region of the current (x, y)-coordinates
			# dimensions
			roi = image[y - pad:y + pad + 1, x - pad:x + pad + 1]

			# perform the actual convolution by taking the
			# element-wise multiplicate between the ROI and
			# the kernel, then summing the matrix
			k = (roi * kernel).sum()

			# store the convolved value in the output (x,y)-
			# coordinate of the output image
			output[y - pad, x - pad] = k

	
	# # rescale the output image to be in the range [0, 255]
	for i in range(len(output)):
		for j in range(len(output[i])):
			grayLevel = truncar(output[i][j][0])
			output[i][j] = np.array([grayLevel, grayLevel, grayLevel], dtype='uint8')
	


	# output = rescale_intensity(output, in_range=(0, 255))
	# output = (output * 255).astype("uint8")
	# return the output image
	return output

def correlacao_comum_old(img, mask):
	'''
	@deprecated
	Cria uma função para fazer a correlação simples, movendo a máscara sobre a imagem
	Fonte: http://www.rafaelzottesso.com.br/tag/python/
	Parametros:
		- img: imagem original
		- mascara: mascara a ser correlacionada. Deve ser uma matriz 3x3
	'''

	# imagem modificada
	# Recebe a imagem original apenas para ter as mesmas proporcoes
	img_corr = img

	# Percorre cada pixel da imagem
	for x in range(img.shape[0]):
		for y in range(img.shape[1]):

			# Usa o try porque algumas coordenadas não existem, assim não apresenta o erro. As bordas não estão sendo consideradas.
			try:

				# Cálculo da máscara coluna a coluna: multiplica o peso que está na máscara pela intensidade do pixel

				### Máscara simples, primeira coluna ##
				m = img[x-1][y+1] * mask[0][0]
				m += img[x-1][y] * mask[1][0]
				m += img[x-1][y-1] * mask[2][0]

				# Segunda coluna
				m += img[x][y+1] * mask[0][1]
				m += img[x][y] * mask[1][1]
				m += img[x][y-1] * mask[2][1]

				# Terceira coluna
				m += img[x+1][y+1] * mask[0][2]
				m += img[x+1][y] * mask[1][2]
				m += img[x+1][y-1] * mask[2][2]

				# Faz a média dos valores e guarda como intensidade do pixel
				img_corr[x][y] = m/9

			# Quando a coordenada não existir, passe para o próximo pixel
			except:
				continue


	return img_corr

def rebater_mascara_old(mascara):
	'''
	Recebe uma mascara (h) 3x3 e retorna ela rebatida
	@deprecated
	'''

	# Copiar as mesmas dimensoes da mascara original
	mascaraRebatida = mascara.copy()


	# TODO: hard coded!!
	mascaraRebatida[0][0] = mascara[2][2]
	mascaraRebatida[0][1] = mascara[2][1]
	mascaraRebatida[0][2] = mascara[2][0]
	
	mascaraRebatida[1][0] = mascara[1][2]
	mascaraRebatida[1][1] = mascara[1][1]
	mascaraRebatida[1][2] = mascara[1][0]
	
	mascaraRebatida[2][0] = mascara[0][2]
	mascaraRebatida[2][1] = mascara[0][1]
	mascaraRebatida[2][2] = mascara[0][0]

	return mascaraRebatida
