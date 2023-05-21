# Imports
import os
import urllib.request
# Welcome message
print('Download random stock images from picsum.photos\n(* images download to the current directory)')

# Paths
# get current working directory
cwd = os.getcwd()

# Images
image_num = int(input('Enter number of images: '))
image_dim = input('Enter image size (e.g. 1920x1080): ').split('x')

# change directory to current working directory
# os.path.join(a,b) if you want to allow custom paths
os.chdir(cwd)


for i in range(1, image_num + 1):
	i = str(i)
	file_name = f'stock-image-{i}.jpg'
	print(f'Downloading {file_name}...')
	urllib.request.urlretrieve(f'https://picsum.photos/{image_dim[0]}/{image_dim[1]}?random', f'./training_set/{file_name}',)