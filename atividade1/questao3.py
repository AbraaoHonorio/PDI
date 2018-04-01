from util import *

def questao3(originalImage):
	'''
	Coloca a imagem em modo negativo

	Parametros:
		originalImage: Imagem a ser modificada
	'''

	imageResult = None

	imageResult = applyToAllPixels(originalImage, {'fun': negative})

	return imageResult

def negative(b,g,r):
    return [255-b,255-g,255-r]