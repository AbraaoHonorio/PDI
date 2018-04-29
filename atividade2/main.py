# -*- coding: utf-8 -*-
from copy import deepcopy
import cv2  # openCV
# Importante!!! open CV usa modelo BGR e nao RGB
import config
from questao2 import *
from questao3 import *



def main():
	# Ler a imagem a ser processada
	img = cv2.imread(config.imageToRead)
	
	# ==> Executar as questoes uma a uma e salvar
	# Questao 2
	resultImage2_a1 = questao2_a1(deepcopy(img),1,1)
	cv2.imwrite('imagens/resultImage2_a1.png', resultImage2_a1)
	resultImage2_a2 = questao2_a2(deepcopy(img),1,1)
	cv2.imwrite('imagens/resultImage2_a2.png', resultImage2_a2)

	resultImage2_b1 = questao2_b1(deepcopy(img))
	cv2.imwrite('imagens/resultImage2_b1.png', resultImage2_b1)
	resultImage2_b2 = questao2_b2(deepcopy(img))
	cv2.imwrite('imagens/resultImage2_b2.png', resultImage2_b2)
	resultImage2_b3 = questao2_b3(deepcopy(img))
	cv2.imwrite('imagens/resultImage2_b3.png', resultImage2_b3)
	resultImage2_b4 = questao2_b4(deepcopy(img))
	cv2.imwrite('imagens/resultImage2_b4.png', resultImage2_b4)
	
	
	# resultImage2_c1 = questao2_c1(deepcopy(img))
	# resultImage2_c2 = questao2_c2(deepcopy(img))
	# resultImage2_c3 = questao2_c3(deepcopy(img))
	# cv2.imwrite('imagens/resultImage2_c1.png', resultImage2_c1)
	# cv2.imwrite('imagens/resultImage2_c2.png', resultImage2_c2)
	# cv2.imwrite('imagens/resultImage2_c3.png', resultImage2_c3)

	# Questao 3:
	resultImage3_a1 = questao3_a1(deepcopy(img))
	cv2.imwrite('imagens/resultImage3_a1.png', resultImage3_a1)
	
	resultImage3_b1 = questao3_b1(deepcopy(img))
	cv2.imwrite('imagens/resultImage3_b1.png', resultImage3_b1)



if __name__ == '__main__':
	main()
