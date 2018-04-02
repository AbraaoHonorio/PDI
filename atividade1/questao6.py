from util import *
from math import trunc

def questao6(img):
	'''
	calcula o limiar pela media dos valores da imagem
	Parametros:
		img: Imagem a ser modificada
	'''

	height=len(img)
	width=len(img[0])
	r=0
	g=0
	b=0
	count=0
	# Usar metodo pixel a pixel
	for h in range(height):
		for w in range(width):
			r += img[h][w][2]
			g += img[h][w][1]
			b += img[h][w][0]
			count += 1


	limiarR=r / count
	limiarG=g / count
	limiarB=b / count

	newImage=[]
	for h in range(height):
		newImage.append([])
		for w in range(width):
			newImage[-1].append(limiarMedia(img[h][w][2], img[h][w]
			                    [1], img[h][w][0], limiarR, limiarG, limiarB))

	return convertArrayToNumpy(newImage)

def questao6B(img, n):
	'''
	calcula o limiar com determina N
	Parametros:
		img: Imagem a ser modificada
		n :  e' o tamanho da mask	
	'''
	imageResult = None
	height = len(img)
	width = len(img[0])
 
	# Usar metodo pixel a pixel
	newImage=[]
	for h in range(height):
		newImage.append([])
		for w in range(width):
			newImage[-1].append(limiar(img[h][w][2], img[h][w][1], img[h][w][0], n))


	return convertArrayToNumpy(newImage)

def limiar(b,g,r,n):
	'''
	Multiplica o brilho de uma imagem de acordo com o valor brightness dado

	Parametros:
		parameters : Dicionario {'brightness': int}
	'''
	
	if r < n:
		r = 0
	else:
		r = 255
	if g < n:
		g = 0
	else:
		g = 255
	if b < n:
		b = 0
	else:
		b = 255
		
	return [trunc(b),trunc(g),trunc(r)]

def limiarMedia(b,g,r,limiarR,limiarG,limiarB):

	'''
	limiar e' igual media de valores da banda
	
	Parametros:
		b: valor do azul
		g: valor do verde
		r: valor do vergmelho
		limiarR: media dos valores vermelhos
		limiarG: media dos valores verdes
		limiarB: media dos valores azul
	'''
    
	if r < limiarR:
		r = 0
	else:
		r = 255
	if g < limiarG:
		g = 0
	else:
		g = 255
	if b < limiarR:
		b = 0
	else:
		b = 255
            
	return [trunc(b),trunc(g),trunc(r)]
