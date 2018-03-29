import numpy as np

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