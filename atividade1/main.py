import cv2 #openCV
# Importante!!! open CV usa modelo BGR e nao RGB
import pdb
import config
import numpy as np
from questao1 import *
from questao2 import *
from questao3 import *
from questao4 import *
from questao5 import *

def main():
	# ler imagem.
	# A imagem lida eh um array[linha][coluna]
	img = cv2.imread(config.imageToRead)
	# img = cv2.cvtColor(cv2.imread(config.imageToRead),  cv2.COLOR_BGR2RGB)
	
	# imageResult = questao1(img)
	# imageResult = questao2(img, 'green')
	# imageResult = questao3(img)
	# imageResult = questao5(img, 2)
	# imageResult = questao4(img, 100)
	# imageResult = questao6(img,500)
	
	imageResult = questao7(img)

	# salvar arquivo transformado
	cv2.imwrite('newImage1.png',imageResult)

def questao1(originalImage):

	# Converter todos os pixels para YIQ
	# img2 = convertAllBGRtoYIQ(img)
	img2 = applyToAllPixels(originalImage, {'fun':BGRtoYIQ})
	
	# Converter todos os pixels para RGB
	# img3 =  convertAllYIQtoBGR(img2)
	img3 = applyToAllPixels(img2, {'fun':YIQtoBGR})


	# TODO: exibindo errado por algum motivo
	# # exibir imagem em uma janela separada
	# cv2.imshow('image',img3)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()

	return img3

def questao2(originalImage, color = 'gray'):
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

def questao3(originalImage):
	'''
	Coloca a imagem em modo negativo

	Parametros:
		originalImage: Imagem a ser modificada
	'''

	imageResult = None

	imageResult = applyToAllPixels(originalImage, {'fun': negative})

	return imageResult

def questao4(originalImage, brightness):
	'''
	Adiciona brilho a uma imagem

	Parametros:
		originalImage: Imagem a ser modificada
		brightness : Variavel a ser somada as cores RGB do pixel
	'''

	imageResult = None

	imageResult = applyToAllPixels(originalImage, {'fun': addBrightness, 'parameters': {'brightness': brightness}})

	return imageResult

def questao5(originalImage, brightness):
	'''
	MUltiplica o brilho de uma imagem

	Parametros:
		originalImage: Imagem a ser modificada
		brightness : Variavel a ser multiplicada as cores RGB do pixel
	'''

	imageResult = None

	imageResult = applyToAllPixels(originalImage, {'fun': mulBrightness, 'parameters': {'brightness': brightness}})

	return imageResult

def questao6(img, n):
	'''
	calcula o limiar com determina N
	Parametros:
		img: Imagem a ser modificada
		n :  e' o tamanho da mask	'''
	imageResult = None
	height = len(img)
 	width = len(img[0])
 
 	# Usar metodo pixel a pixel
 	newImage = []
 	for h in range(height):
 		newImage.append([])
 		for w in range(width):
 			newImage[-1].append(limiar(img[h][w][2], img[h][w][1], img[h][w][0],n))


	return convertArrayToNumpy(newImage)

def questao7(img):
	'''
	calcula o limiar pela media dos valores da imagem
	Parametros:
		img: Imagem a ser modificada
	'''
	imageResult = None
	height = len(img)
 	width = len(img[0])
	r = 0
	g = 0
	b = 0
	count = 0
 	# Usar metodo pixel a pixel
 	for h in range(height):
 		for w in range(width):
			r += img[h][w][2]
			g += img[h][w][1]
			b += img[h][w][0]
			count+=1


	limiarR = r / count
	limiarG = g / count
	limiarB = b / count
 	
	newImage = []
	for h in range(height):
 		newImage.append([])
 		for w in range(width):
 			newImage[-1].append(limiarMedia(img[h][w][2], img[h][w][1], img[h][w][0],limiarR,limiarG,limiarB))

	return convertArrayToNumpy(newImage)

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

def convertArrayToNumpy(array):
	'''	
	Coloca um array em forma de numpy_array pq eh o tipo de objeto que o openCV usa
	'''
	array_numPy = np.empty((len(array), len(array[0]), 3))

	for row in range(len(array)):
		for colunm in range(len(array[row])):
			array_numPy[row][colunm] = array[row][colunm]

	return array_numPy

def applyToAllPixels(img, action):
	'''
	Aplica uma uma funcao para todos os pixels
	parametros:
		img: array.numpy ou simplesmente um array 3-dimensional que contem os pixels
		action: dicionario que contem duas chaves:
			'fun': nome da funcao a ser aplicada
			'parameters': parametros que a funcao usa alem do R,G,B
			Ex.: Se a funcao a ser passada tiver seus proprios parametros, como 'programar(computador,cafe)', os parametros computador e cafe estarao em outro dicionario separado (o dicionario seria o valor da chave 'parameters'). A chamada da funcao do exemplo acima ficaria: applyToAllPixels(img,{'fun' : programar, 'parameters' : {'maquina' : computador, 'liquido' : cafe } })
	'''

	height = len(img)
	width = len(img[0])

	fun = action.get('fun')
	parameters = action.get('parameters')

	# Usar metodo pixel a pixel
	newImage = []
	for h in range(height):
		newImage.append([])
		for w in range(width):
			# Verifica se precisa de parametros fora o R,G,B
			if (parameters != None):
				newImage[-1].append(fun(img[h][w][0], img[h][w][1],  img[h][w][2],  parameters))
			else:
				newImage[-1].append(fun(img[h][w][0], img[h][w][1],  img[h][w][2]))

	return convertArrayToNumpy(newImage)

if __name__ == '__main__':
	main()