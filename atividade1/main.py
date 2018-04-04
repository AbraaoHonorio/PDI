import cv2  # openCV
# Importante!!! open CV usa modelo BGR e nao RGB
import config
# from colour import Color
from questao1 import *
from questao2 import *
from questao3 import *
from questao4 import *
from questao5 import *
from questao6 import *
from questao7 import *
from questao8 import *
from questao9 import *


def main():
	# ler imagem.
	# A imagem lida eh um array[linha][coluna]
	img = cv2.imread(config.imageToRead)
	# img = cv2.cvtColor(cv2.imread(config.imageToRead),  cv2.COLOR_BGR2RGB)

	# Chama cada questao de forma isolada
	imageResult1 = questao1(img)
	imageResult2_a = questao2(img, 'blue')
	imageResult2_b = questao2(img, 'gray')
	imageResult2_c = questao2(img, 'red')
	imageResult2_d = questao2(img, 'green')
	imageResult3 = questao3(img)
	imageResult4 = questao4(img, 100)
	imageResult5 = questao5(img, 2)
	imageResult6_a = questao6A(img, 140)
	imageResult6_b = questao6B(img)
	imageResult7_a = questao7(img, 3)
	imageResult7_b = questao7B(img, 3)
	# imageResult8_a = questao8_sobel(img)
	imageResult9_a = questao9A(img)
	imageResult9_b = questao9B(img)
	# imageResult9_test_a = questao9ATest(img)
	# imageResult9_test_b = questao9BTest(img)


	# salvar arquivo transformado
	cv2.imwrite('imageResult1.png',imageResult1)
	cv2.imwrite('imageResult2_a.png',imageResult2_a)
	cv2.imwrite('imageResult2_b.png',imageResult2_b)
	cv2.imwrite('imageResult2_c.png',imageResult2_c)
	cv2.imwrite('imageResult2_d.png',imageResult2_d)
	cv2.imwrite('imageResult3.png',imageResult3)
	cv2.imwrite('imageResult4.png',imageResult4)
	cv2.imwrite('imageResult5.png',imageResult5)
	cv2.imwrite('imageResult6_a.png',imageResult6_a)
	cv2.imwrite('imageResult6_b.png',imageResult6_b)
	cv2.imwrite('imageResult7_a.png',imageResult7_a)
	cv2.imwrite('imageResult7_b.png',imageResult7_b)
	# cv2.imwrite('imageResult8_a.png',imageResult8_a)

	cv2.imwrite('imageResult9_a.png',imageResult9_a)
	cv2.imwrite('imageResult9_b.png',imageResult9_b)
	# cv2.imwrite('imageResult9_test_a.png',imageResult9_test_a)
	# cv2.imwrite('imageResult9_test_b.png',imageResult9_test_b)

if __name__ == '__main__':
	main()
