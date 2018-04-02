from util import *


def questao5(originalImage, brightness):
	'''
	MUltiplica o brilho de uma imagem

	Parametros:
		originalImage: Imagem a ser modificada
		brightness : Variavel a ser multiplicada as cores RGB do pixel
	'''

	imageResult = None

	imageResult = applyToAllPixels(
	    originalImage, {'fun': mulBrightness, 'parameters': {'brightness': brightness}})

	return imageResult

	
def mulBrightness(b,g,r,parameters):
	'''
	Multiplica o brilho de uma imagem de acordo com o valor brightness dado

	Parametros:
		parameters : Dicionario {'brightness': int}
	'''
	brightness = parameters.get('brightness')
	b = b * brightness
	g = g * brightness
	r = r * brightness
	
	
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