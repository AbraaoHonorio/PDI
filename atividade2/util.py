# -*- coding: utf-8 -*-

'''
Metodos a serem usados em mais de uma questao serao colocados aqui
'''
# Definicao de metodos


def truncar(valor):
	if(valor < 0.0):
		return 0.0
	elif(valor > 255.0):
		return 255.0
	return valor
