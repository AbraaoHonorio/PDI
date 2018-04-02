from math import trunc
import numpy as np
import pdb

def ArrayToimage(r, g, b):

	return [trunc(b), trunc(g), trunc(r)]

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

	height=len(img)
	width=len(img[0])

	fun=action.get('fun')
	parameters=action.get('parameters')

	# Usar metodo pixel a pixel
	newImage=[]
	for h in range(height):
		newImage.append([])
		for w in range(width):
			# Verifica se precisa de parametros fora o R,G,B
			if (parameters != None):
				newImage[-1].append(fun(img[h][w][0], img[h][w][1],
				                    img[h][w][2],  parameters))
			else:
				newImage[-1].append(fun(img[h][w][0], img[h][w][1],  img[h][w][2]))

	return convertArrayToNumpy(newImage)

def convertArrayToNumpy(array):
	'''
	Coloca um array em forma de numpy_array pq eh o tipo de objeto que o openCV usa
	'''
	array_numPy=np.empty((len(array), len(array[0]), 3))

	for row in range(len(array)):
		for colunm in range(len(array[row])):
			array_numPy[row][colunm]=array[row][colunm]

	return array_numPy

def applyFilter(img, filter):
	'''
	Aplica um filtro a toda uma imagem
	Parametros:
		filter: deve ser uma matrix nXn

	@Deprecated
	'''

	# identifica o n do filtro (ex: 3x3)
	n = len(filter)
	k = n/2
	nn = n*n
	
	
	height=len(img)
	width=len(img[0])

	# Gerar borda:
	# pegar as k linhas superiores e replicar como borda
	topBorder = []
	for i in range(k):
		topBorder+=(img[0])



	# Usar metodo pixel a pixel
	newImage=[]
	for i in range(height):
		newImage.append([])
		for j in range(width):
			mediaR = 0
			mediaG = 0
			mediaB = 0
			for h in range(i-k, i+k):
				for w in range(j-k, j+k):
					#TODO: esse filtro nao leva em cosideracao as bordas
					if (h >= 0 and h < height and w >= 0 and w < width):
						mediaR += img[h][w][0]
						mediaG += img[h][w][1]
						mediaB += img[h][w][2]
			newImage[-1].append(ArrayToimage(mediaR/nn, mediaG/nn, mediaB/nn))


	return convertArrayToNumpy(newImage)
	
	pass

def applyFilter3x3(img, kernel):
	'''
	Aplica um filtro 3x3 a toda uma imagem
	Parametros:
		kernel: deve ser uma matrix numpy 3x3
	'''
	
	height=len(img)
	width=len(img[0])

	
	# i e j sao a posicao do elemento na matriz
	for i in range(height):
		for j in range(width):
			neighborhood = __buildNeighborhood(img,i,j)
				
			# Multiplicacao de matriz
			img[i][j] = somaElementosMatriz(multiplicaMatrix(neighborhood, kernel))

	return convertArrayToNumpy(img)
	
	
def __buildNeighborhood(img,i,j):
	'''
	Constroi uma matriz de vizinhos que eh aquela que vai ser multiplicada pelo kernel

	Parametros:
		img:
		i: linha do pixel na imagem
		j: coluna do pixel na imagem
	'''
	height = len(img)
	width = len(img[0])

	# matriz que vai ser multiplicada pelo kernel
	neighborhood = np.empty((3, 3, 3), dtype=int)

	
	# elemento central (ele mesmo)
	neighborhood[1][1] = img[i][j]

	# tratando as bordas
	if i == 0:
		# borda superior
		neighborhood[0][1] = img[i][j]
		neighborhood[2][1] = img[i+1][j]

	elif i == height-1:
		# borda inferor
		neighborhood[0][1] = img[i-1][j]
		neighborhood[2][1] = img[i][j]

	else:
		neighborhood[0][1] = img[i-1][j]
		neighborhood[2][1] = img[i+1][j]

	if j == 0:
		# borda esquerda
		neighborhood[1][0] = img[i][j]
		neighborhood[1][2] = img[i][j+1]

	elif j == width-1:
		# Borda direita
		neighborhood[1][2] = img[i][j]
		neighborhood[1][0] = img[i][j-1]

	else:
		neighborhood[1][0] = img[i][j-1]
		neighborhood[1][2] = img[i][j+1]

	# trantando as bordas na extremidade (diagonais)
	# borda cima-esquerda
	if (i, j) == (0, 0):
		neighborhood[0][0] = img[i][j]
	# else:
		# outras 3 bordas
		neighborhood[2][0] = img[i+1][j]
		neighborhood[2][2] = img[i+1][j+1]
		neighborhood[0][2] = img[i][j+1]

	# borda baixo-esquerda
	if (i, j) == (height-1, 0):
		neighborhood[2][0] = img[i][j]
	# else:
		# outras 3 bordas
		neighborhood[0][0] = img[i-1][j]
		neighborhood[2][2] = img[i][j+1]
		neighborhood[0][2] = img[i-1][j+1]


	# borda baixo-direita
	if (i, j) == (height-1, width-1):
		neighborhood[2][2] = img[i][j]
	# else:
		# outras 3 bordas
		neighborhood[0][2] = img[i-1][j]
		neighborhood[0][0] = img[i-1][j-1]
		neighborhood[2][0] = img[i][j-1]

	# borda cima-direita
	if (i, j) == (0, width-1):
		neighborhood[0][2] = img[i][j]
	# else:
		# outras 3 bordas
		neighborhood[0][0] = img[i][j-1]
		neighborhood[2][0] = img[i+1][j-1]
		neighborhood[2][2] = img[i+1][j]
	
	
	return neighborhood

def multiplicaMatrix(matrix1, matrix2):
	'''
	Parametros:
		duas matrizes do tipo numpy
	'''

	return matrix1.dot(matrix2)

def somaElementosMatriz(matriz):
	somaR = 0
	somaG = 0
	somaB = 0	
	for i in range(len(matriz)):
		for j in range(len(matriz[0])):
			somaB += matriz[i][j][0]
			somaG += matriz[i][j][1]
			somaR += matriz[i][j][2]
	
	return [somaB, somaG, somaR]
