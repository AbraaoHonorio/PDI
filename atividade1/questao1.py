from math import trunc

def BGRtoYIQ(b,g,r):
	y = 0.299*r + 0.587*g + 0.114*b
	i = 0.596*r - 0.274*g - 0.322*b
	q = 0.211*r - 0.523*g + 0.312*b


	return [y,i,q]

def YIQtoBGR(y,i,q):
	r = (y + 0.956*i + 0.621*q)
	if r > 255:
		r = 255
	elif r < 0:
		r = 0

	g = (y - 0.272*i - 0.647*q)
	if g > 255:
		g = 255
	elif g < 0:
		g = 0

	b = (y - 1.106*i + 1.703*q)
	if b > 255:
		b = 255
	elif b < 0:
		b = 0

	return [trunc(b),trunc(g),trunc(r)]