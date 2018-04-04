from util import *
import numpy as np
import math

def questao8_sobel(img):
	'''
	Filtro de deteccao de bordas Sobel
	fonte: https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/image-processing/edge_detection.html
	'''
	width = len(img[0])
	height = len(img)

	img_edge = np.zeros((height, width, 3))
	# fazer todos os pixels
	for x in range(1, width - 1):
		for y in range(1, height - 1):
			# initialise Gx to 0 and Gy to 0 for every pixel
			Gx = 0
			Gy = 0


			# top left pixel
			b, g, r = img[x - 1, y - 1]
			# intensity ranges from 0 to 765 (255 * 3)
			intensity = (r + g + b)
			# accumulate the value into Gx, and Gy
			Gx += -intensity
			Gy += -intensity


			# now we do the same for the remaining pixels, left to right, top to bottom


			# remaining left column
			b, g, r = img[x - 1, y]
			Gx += -2 * (r + g + b)

			b, g, r = img[x - 1, y + 1]
			Gx += -(r + g + b)
			Gy += (r + g + b)


			# middle pixels
			b, g, r = img[x, y - 1]
			Gy += -2 * (r + g + b)

			b, g, r = img[x, y + 1]
			Gy += 2 * (r + g + b)


			# right column
			b, g, r = img[x + 1, y - 1]
			Gx += (r + g + b)
			Gy += -(r + g + b)

			b, g, r = img[x + 1, y]
			Gx += 2 * (r + g + b)

			b, g, r= img[x + 1, y + 1]
			Gx += (r + g + b)
			Gy += (r + g + b)


			# calculate the length of the gradient
			length = math.sqrt((Gx * Gx) + (Gy * Gy))

			# normalise the length of gradient to the range 0 to 255
			length = length / 4328 * 255

			# convert the length to an integer
			length = int(length)

			# draw the length in the edge image
			img_edge[x, y] = length, length, length

	return img_edge

def questao8_laplaciano(img):
	'''
	Filtro de deteccao de bordas laplaciano
	'''
	pass