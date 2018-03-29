import numpy as np

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