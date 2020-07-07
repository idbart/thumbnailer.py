import os
import sys
import getopt
from PIL import Image

def usage():
	print("thumbnailer.py -r <rootDirectory> -o <outputDirectory> -w <thumbnailWidth> -h <thumbnailHeight>")

# resize the image by width 
def thumbnailByWidth(image, width):
	# get the ratio of new width to original width
	ratio = float(width/image.size[0])
	# multiply original height by said ratio to get new ratio 
	height = int(image.size[1] * ratio)

	# resize image!
	return image.resize((width, height))

# same thing but by height
def thumbnailByHeight(image, height):
	ratio = float(height/image.size[1])
	width = int(image.size[0] * ratio)

	return image.resize((width, height))

# resize by both height and width
def thumbnailByWidthAndHeight(image, width, height):
	# try height first
	if width >= int(float(height/image.size[1]) * image.size[0]):
		return thumbnailByHeight(image, height)
	# then go by width if that does not work
	else:
		return thumbnailByWidth(image, width)

def main(arguments):
	# init the root directory to this one  
	dir = "./"
	outputDir = None
	# init the width and height to none
	width = None
	height = None

	# parse the users input
	try:
		optList, args = getopt.getopt(arguments, 'w:h:r:o:')
	except getopt.GetoptError as err:
		print(err)
		usage()
		sys.exit(2)

	for option, value in optList:
		if option == "-w":
			width = int(value)
		elif option == "-h":
			height = int(value)
		elif option == "-r" and os.path.isdir(value):
			dir = value
		elif option == "-o" and os.path.isdir(value):
			outputDir = value
	
	# exit the process if the user does not provide a width or height for the thumbnails
	if width == None and height == None:
		print("ERROR: thumbnailer.py requires a height or width")
		usage()
		sys.exit(2)

	# set the output directory if the user does not do it manually
	if outputDir == None:
		outputDir = os.path.join(dir, "thumbnails")

	# create the output directory if it does not already exist
	if not os.path.isdir(outputDir):
		os.mkdir(outputDir)


	# loop through all of the photos in the root dir
	for filename in os.listdir(dir):
		print("processing: " + filename)

		# filter out files that are not images
		try:
			img = Image.open(os.path.join(dir, filename))
		except Exception as err:
			print(filename + " is not an image")
			continue

		# create the thumbnails baised on which metrics the user provided 
		if width != None and height != None:
			img = thumbnailByWidthAndHeight(img, width, height)
		elif width != None and height == None:
			img = thumbnailByWidth(img, width)
		elif width == None and height != None:
			img = thumbnailByHeight(img, height)
			
		# and save the new thumbnail image in the output dir
		img.save(os.path.join(outputDir, filename))

	print("Done!")
	

if __name__ == "__main__":
	main(sys.argv[1:])