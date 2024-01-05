from PIL import Image

import argparse

def checkCommandArgs():
	print("Command arg check starting. . .")
	parser = argparse.ArgumentParser()
	parser.add_argument("-n", help="image name .type jpg/png")
	parser.add_argument("-c", type=int, help="color offset")
	args = parser.parse_args()
	return args.n, args.c
	# s = []
	# for a in range(1, length(args)):
	# 	print (i, "  " , args[a])
	# if(length(args) > 1):
		# return args[0]
	# return "filename.jpg"
	# 	s.append(a)
	# return s

red = (220, 0, 0)
orange = (220, 100, 0)
yellow = (220, 200, 0)
blue = (50, 200, 120)
teal = (0, 120, 100)
green = (30, 180, 0)
pink = (230, 60, 120)
pur = (130, 60, 220)
colors = (red, orange, yellow, green, teal, blue, pink, pur, red)
co = 1
fn, co = checkCommandArgs()
print(fn)
im = Image.open(fn)
l = im.getcolors()
out = Image.new('RGB', (1000, 1000))
t = im.height /500
ww = int(im.width //t)
ns = (333, 500)
im = im.resize(ns)
for k in range(im.height):
	if k%100==0: print('.')
	#print("\n\r")
	for i in range(im.width):
		n = im.getpixel((i, k))
		#print(str(n) + " ")
		a = 130
		if n < (a,a,a):
			n = (200, 0 , 0)
			out.putpixel((i, k), pink)
		w = 220
		if n > (w,w,w):
			n =  (255, 255 , 255)
			# out.putpixel((i, k), colors[i%8])

			for l in range(0, 2):
				for j in range(0, 3):
					out.putpixel((i+im.width*j, k+im.height*l), colors[(j+l+co)%8])
		if( n>= (a,a,a) and n <= (w,w,w)):
			# for j in range(0, 5):
			# 	out.putpixel((i+im.width*j%3, k+im.height*j//3), colors[(j)])
			out.putpixel((i, k), blue)
			out.putpixel((i+im.width, k), pur)
			out.putpixel((i+im.width*2, k), pink)
			out.putpixel((i+im.width*0, k+im.height), pink)
			out.putpixel((i+im.width*1, k+im.height), green)
			out.putpixel((i+im.width*2, k+im.height), red)
out.save("muse3.jpg")


out.show()
