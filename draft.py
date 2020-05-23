#importing image
print('Enter the path of image you want to process:-')
path = input('')
img = plt.imread(path)
plt.imshow(img)