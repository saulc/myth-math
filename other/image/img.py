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
grey = (222, 222, 222)
colors = (red, orange, yellow, green, teal, blue, pink, pur, grey)
co = 1
fn = "./m16.png"
# fn, co = checkCommandArgs()
print("input file: " + fn)
print("Running img filter...")
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
		a = 220
		if n < (a,a,a):
			n = (200, 30 , 30)
			out.putpixel((i, k), pink)
			out.putpixel((int(i+im.width*1), k ), teal)
			out.putpixel((int(i+im.width*2), k ), pur)
			out.putpixel((i, k+im.height), n)
			out.putpixel((int(i+im.width*1), k+im.height), orange)
			out.putpixel((int(i+im.width*2), k+im.height), blue)
		w = 220
		if n > (w,w,w):
			n =  grey
			out.putpixel(( i, k ), n)
			out.putpixel((int(i+im.width*1), k ), n)
			out.putpixel((int(i+im.width*2), k ), n)
			out.putpixel((i, k+im.height), pink)
			out.putpixel((int(i+im.width*1), k+im.height), pink)
			out.putpixel((int(i+im.width*2), k+im.height), pink)

			# for l in range(0, 2):
			# 	for j in range(0, 3):
			# 		out.putpixel((i+im.width*j, k+im.height*l), colors[(j+l+co)%8])
		if( n>= (a,a,a) and n <= (w,w,w)):

			out.putpixel((i, k), n)
			out.putpixel((i, k*1), n)
			# for j in range(0, 5):
			# 	out.putpixel((i+im.width*j%3, k+im.height*j//3), colors[(j)])
			# out.putpixel((int(i+1), k), blue)
			# out.putpixel((int(i+im.width*1), k), pur)
			# out.putpixel((int(i+im.width*2), k), pink)
			# out.putpixel((int(i+im.width*0), k+im.height), pink)
			# out.putpixel((int(i+im.width*1.05), int(k+im.height*.95)), green)
			# out.putpixel((int(i+im.width*1.99), k+im.height), red)
# out.save("muse3.jpg")
out.show()
