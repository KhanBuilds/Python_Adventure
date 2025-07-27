import imageio.v3 as iio #this is the modern imageio library
filenames = ['team-pic1.png', 'team-pic2.png'] #list of the files we're going to use
images = [] #list to hold the images during looping
for filename in filenames: #the loop to read the images
    images.append(iio.imread(filename)) #read each image and append to the list
iio.imwrite('team.gif', images, duration=500, loop = 0) #write the images to a gif file with specified duration and loop count