import os
import requests


def download_image(url):
	response = requests.get(url)
	return response.content

def prepare_download_folder():
	cwd = os.getcwd()
	download_folder = os.path.join(cwd, 'Download')
	print(download_folder)

	if not os.path.exists(download_folder):
		os.makedirs(download_folder)

	return download_folder



if __name__=='__main__':

	urls = [
		'https://cdn.pixabay.com/photo/2017/08/30/01/05/milky-way-2695569_1280.jpg',
		'https://cdn.pixabay.com/photo/2017/02/01/22/02/mountain-landscape-2031539_1280.jpg',
		'https://cdn.pixabay.com/photo/2015/12/01/20/28/road-1072823_1280.jpg'
	]

	for url in urls:
		download_folder = prepare_download_folder()
		content = download_image(url)
		file_name = os.path.basename(url)
		path = os.path.join(download_folder,file_name)

		with open(path, 'wb') as f:
			f.write(content)





