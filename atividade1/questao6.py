from util import *
from math import trunc
from questao1 import *

def questao6A(img, n):
	'''
	calcula o limiar aplicado a banda y de uma imagem com m setado pelo usuario
	Parametros:
		img: Imagem a ser modificada
		n: parametro setado pelo usuario	
	'''

	# Converte a imagem em YIQ
	img2 = applyToAllPixels(img, {'fun': BGRtoYIQ})

	imageResult = None
	height = len(img2)
	width = len(img2[0])
 
	# Usar metodo pixel a pixel
	newImage=[]
	for h in range(height):
		newImage.append([])
		for w in range(width):
			newImage[-1].append([limiar(img2[h][w][0],n), # muda apenas Y
									img2[h][w][1],
									img2[h][w][2]])

	# Converte YIQ para RGB
	img3 = applyToAllPixels(newImage, {'fun': YIQtoBGR})


	return img3

def limiar(y,n):
	'''
	retorna a banda y maxima se o valor original eh maior que o parametro
	ou retorn y minimo se a banda y e menor que o parametro
	'''
	if y > n:
		return 255
	else:
		return 0

def questao6B(img):
	'''
	calcula o limiar pela media dos valores da imagem
	Parametros:
		img: Imagem a ser modificada
	'''
	# Converte a imagem em YIQ
	img2 = applyToAllPixels(img, {'fun': BGRtoYIQ})

	height=len(img2)
	width=len(img2[0])
	y=0
	i=0
	q=0
	count=0
	# Usar metodo pixel a pixel
	for h in range(height):
		for w in range(width):
			y += img2[h][w][0]
			i += img2[h][w][1]
			q += img2[h][w][2]
			count += 1


	limiarY= y / count

	newImage=[]
	for h in range(height):
		newImage.append([])
		for w in range(width):
			newImage[-1].append([limiar(img2[h][w][0],limiarY), # muda apenas Y
									img2[h][w][1],
									img2[h][w][2]])

	# Converte YIQ para RGB
	img3 = applyToAllPixels(newImage, {'fun': YIQtoBGR})

	return img3

def questao6BemRGB(img, n):
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
			newImage[-1].append(limiarRGB(img[h][w][2], img[h][w][1], img[h][w][0], n))


	return convertArrayToNumpy(newImage)

def limiarRGB(b,g,r,n):
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

def limiarMediaRGB(b,g,r,limiarR,limiarG,limiarB):

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
