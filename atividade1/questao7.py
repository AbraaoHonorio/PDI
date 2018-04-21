from util import *

def questao7B(img, n):

	height=len(img)
	width=len(img[0])
	
	nn = n/2
	# Usar metodo pixel a pixel
	newImage=[]
	
	for i in range(1,height-1):
		newImage.append([])
		for j in range(1,width-1):
			medianaR = [0] * n * n
			medianaG = [0] * n * n
			medianaB = [0] * n * n
			k = -1
			for h in range(i-nn, i+nn):
				for w in range(j-nn, j+nn):
					k = k+1
					if (h >= 0 and h < height and w >= 0 and w < width):
						medianaR[k] = img[h][w][0]
						medianaG[k] = img[h][w][1]
						medianaB[k] = img[h][w][2]
					else:
						medianaR[k] = 0
						medianaG[k] = 0
						medianaB[k] = 0

			colorR = mediana(medianaR)
			colorG = mediana(medianaG)
			colorB = mediana(medianaB)
			newImage[-1].append(ArrayToimage(colorB,colorG, colorR))


	return convertArrayToNumpy(newImage)

def questao7(img, n):
	'''
	Aplica o filtro de media
	parametros:
		img: imagem original
		n: tamanho do kernel (TODO: eh isso mesmo?)
		
	'''


	height=len(img)
	width=len(img[0])
	k = n/2
	nn = n*n
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
			newImage[-1].append(ArrayToimage(mediaB/nn, mediaG/nn, mediaR/nn))


	return convertArrayToNumpy(newImage)

def questao7A_v2(img):
	kernel = np.array(([1/9,1/9,1/9],[1/9,1/9, 1/9],[ 1/9, 1/9, 1/9]))
	applyFilter3x3(img, kernel)

def mediana(vector):  
	vectorOrder=sorted(vector)
    
	n = len(vectorOrder)/2
	middle= n/2

	if n %2==0:
		mediana=(int(vectorOrder[middle+1]) + int(vectorOrder[middle+2])) / 2
	else:
		mediana=vectorOrder[middle+1]*1

	return(mediana)