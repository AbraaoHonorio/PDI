from numpy import mean
from util import *

def questao2(originalImage, color='gray'):
	'''
	Coloca a imagem em modo monocromatico

	Parametros:
		originalImage: ----
		color: string que siginfica a banda escolhida:
			gray: --- (default)
			red: ---
			green:---
			blue: ---
	'''

	imageResult = None

	if (color == 'gray'):
		# media dos  valores de cada pixel
		imageResult = applyToAllPixels(originalImage, {'fun': calculateMeanAndAplly})

	# para cores primarias basta remover os outros valores
	elif (color == 'red'):
		imageResult = applyToAllPixels(originalImage, {'fun': toRed})
	elif (color == 'blue'):
		imageResult = applyToAllPixels(originalImage, {'fun': toBlue})
	elif (color == 'green'):
		imageResult = applyToAllPixels(originalImage, {'fun': toGreen})
	else:
		print("cor invalida")

	return imageResult

def calculateMeanAndAplly(b,g,r):
    '''
    Calcula a media de tres pixels e retorna um pixel com essa media
    '''
    
    average = mean([b,g,r])

    return [average,average,average]

def toGreen(b,g,r):
    '''
    converte todo o pixel para a banda verde
    '''
    return [0,g,0]

def toRed (b,g,r):
    '''
    converte todo o pixel para a banda vermelha
    '''
    return [0,0,r]

def toBlue (b,g,r):
    '''
    converte todo o pixel para a banda azul
    '''
    return [b,0,0]
    


