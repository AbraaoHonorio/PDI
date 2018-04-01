from util import *

def questao4(originalImage, brightness):
	'''
	Adiciona brilho a uma imagem

	Parametros:
		originalImage: Imagem a ser modificada
		brightness : Variavel a ser somada as cores RGB do pixel
	'''

	imageResult = None

	imageResult = applyToAllPixels(
	    originalImage, {'fun': addBrightness, 'parameters': {'brightness': brightness}})

	return imageResult


def addBrightness(b,g,r,parameters):
	'''
	Adiciona brilho a uma imagem de acordo com o valor brightness dado

	Parametros:
		parameters : Dicionario {'brightness': int}
	'''
	brightness = parameters.get('brightness')
	b = b + brightness
	g = (g + brightness)
	r = (r + brightness)

	if r > 255:
		r = 255
	elif r < 0:
		r = 0
	if g > 255:
		g = 255
	elif g < 0:
		g = 0
	if b > 255:
		b = 255
	elif b < 0:
		b = 0
	
	return [b,g,r]
