from PIL import Image

import argparse

def checkCommandArgs():
	print("Popart image starting. . .")
	parser = argparse.ArgumentParser()
	parser.add_argument("-n", help="image name .type jpg/png")
	parser.add_argument("-c", type=int, help="color offset")
	args = parser.parse_args()
	return args.n, args.c


red = (220, 0, 0)
orange = (220, 100, 0)
yellow = (220, 200, 0)
green = (50, 200, 120)
teal = (0, 120, 100)
blue = (30, 180, 0)
pink = (230, 60, 120)
pur = (130, 60, 220)

colors = (red, orange, yellow, green, teal, blue, pink, pur, red)
co = 1
fn, co = checkCommandArgs()
print(fn)
im = Image.open(fn)
l = im.getcolors()
out = Image.new('RGB', (1000, 1000), (155, 155 , 155))
t = im.height /500
ww = int(im.width //t)
ns = (500, 500)
im = im.resize(ns)
for k in range(im.height):
	if k%100==0: print('.')
	#print("\n\r")
	for i in range(im.width):
		n = im.getpixel((i, k))
		#print(str(n) + " ")
		a = 130
		w = 220
		if( n>= (a,a,a) and n <= (w,w,w)):
			out.putpixel((i, k), colors[(co)%8])
			out.putpixel((i+500, k), colors[(co+1)%8])
			out.putpixel((i, 500+k), colors[(co+2)%8])
			out.putpixel((i+500, 500+k), colors[(co+3)%8])
		if n < (a,a,a):
			n = (250, 0 , 0)
			out.putpixel((i, k), n)
		if n > (w,w,w):
			n =  (255, 111 , 155)
				# n =  (255, 255 , 255)
			out.putpixel((i, k), n)
		# if( n>= (a,a,a) and n <= (w,w,w)):
# out.save("www.jpg")
out.show()
