# Imports
import os
import urllib.request
from io import BytesIO

from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
from google_auth_oauthlib.flow import InstalledAppFlow

# Load credentials
# credentials = service_account.Credentials.from_service_account_file('credentials.json')
scope = ['https://www.googleapis.com/auth/drive']
creds = None
flow = InstalledAppFlow.from_client_secrets_file('credentials.json', scope)
creds = flow.run_local_server(port=8000)

# Authenticate and authorize
drive_service = build('drive', 'v3', credentials=creds)

folder_id = '1FQTnycyAjryIE9_VmidkZ_A-6n-4IMCG'


def download_image():
	cwd = os.getcwd()


	image_num = int(input('Enter number of images: '))
	image_dim = input('Enter image size (e.g. 1920x1080): ').split('x')

	# change directory to current working directory
	# os.path.join(a,b) if you want to allow custom paths
	os.chdir(cwd)


	for i in range(1, image_num + 1):
		i = str(i)
		file_name = f'colorize-image-data-v6-{i}.jpg'
		print(f'Downloading {file_name}...')
		url = f'https://picsum.photos/{image_dim[0]}/{image_dim[1]}?random'
		response = urllib.request.urlopen(url)
		image_data = response.read()
		file_metadata = {"name": file_name, "parents": [folder_id]}
		media = MediaIoBaseUpload(BytesIO(image_data), mimetype='image/jpeg')
		file_ = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
		print('File ID:', file_.get('id'))


def main():
	download_image()

if __name__ == '__main__':
	main()