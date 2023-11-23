from ast import main
import requests
from requests import HTTPError, RequestException
import time
import threading
from concurrent.futures import ThreadPoolExecutor
import os, shutil
import logging
import asyncio
import aiohttp
import aiofiles
from aiohttp import ClientError

logging.basicConfig(level=logging.INFO)

class ImageDownloader:
	def __init__(self, urls:list=[], folder='./Downloads', clean=True) -> None:
		self.urls = urls
		self.download_folder = folder

		# Prepare Download Folder:
		path = self.download_folder
		try:
			if not os.path.isdir(path):
				os.makedirs(path)
				logging.info(f"Directory '{path}' created.")
			else:
				self.__cleanup_download_folder()

		except OSError as error:
			logging.error(f"Error creating directory '{path}': {error}")


	def __cleanup_download_folder(self):
		if os.path.exists(self.download_folder):
			# Remove all files in the download folder
			for filename in os.listdir(self.download_folder):
				file_path = os.path.join(self.download_folder, filename)
				try:
					if os.path.isfile(file_path) or os.path.islink(file_path):
						os.unlink(file_path)
					elif os.path.isdir(file_path):
						shutil.rmtree(file_path)
				except Exception as e:
					logging.error(f'Failed to delete {file_path}. Reason: {e}')

	def download_image(self, url):
		print(f'Downloading {url}')
		try:
			r = requests.get(url)
			# raise error if HTTP problems
			r.raise_for_status()

			# get image bytes:
			image = r.content
			# get image name from url:
			filename = os.path.basename(url)
			path = os.path.join(self.download_folder, filename)

			try:
				with open(path, 'wb') as f:
					f.write(image)
			except Exception as e:
				logging.error(f'Can not write to file: {filename}: {str(e)}')

		except HTTPError as http_err:
			logging.error(f"HTTP error: {http_err}")
		except RequestException as req_err:
			logging.error(f"Request error: {req_err}")
		except Exception as err:
			logging.error(f"Other error occurred: {err}")

	def download_all_sequential(self):
		for url in self.urls:
			self.download_image(url)

	def download_all_threads(self):
		tr_pool = []
		for i in range(len(self.urls)):
			tr = threading.Thread(target=self.download_image, args=(self.urls[i],))
			tr_pool.append(tr)
			tr.start()

		for tr in tr_pool:
			tr.join()

	def download_all_threadpool_executor(self):
		with ThreadPoolExecutor(max_workers=10) as executor:
			executor.map(self.download_image, self.urls)

	async def download_image_async(self, session, url):
		# print(f'Downloading {url}')
		try:
			async with session.get(url) as response:
				response.raise_for_status()  # Raises exception for HTTP errors

				# Get image bytes:
				image = await response.read()

				# Get image name from url and create full path:
				filename = os.path.basename(url)
				path = os.path.join(self.download_folder, filename)

				try:
					async with aiofiles.open(path, mode='wb') as file:
						await file.write(image)
				except Exception as e:
					logging.error(f'Can not write to file: {filename}: {str(e)}')
		except aiohttp.ClientResponseError as http_err:
			logging.error(f"HTTP error: {http_err}")
		except ClientError as req_err:
			logging.error(f"Request error: {req_err}")
		except Exception as err:
			logging.error(f"Other error occurred: {err}")

	async def __download_all_async(self):
		async with aiohttp.ClientSession() as session:
			tasks = [self.download_image_async(session, url) for url in self.urls]
			await asyncio.gather(*tasks)

	def download_all_async(self):
		asyncio.run(self.__download_all_async())

	def measure_execution_time(self, method_name):
		start_time = time.perf_counter()

		# Dynamically call the method based on the method name
		getattr(self, method_name)()

		end_time = time.perf_counter()
		return end_time - start_time

	def summarize_execution_times(self):
		download_methods = [
			'download_all_sequential',
			'download_all_threads',
			'download_all_threadpool_executor',
			'download_all_async'
		]

		# run each download method and get execution time
		# times = {method: self.measure_execution_time(method) for method in download_methods}
		times = {}
		for method in download_methods:
			times[method]=self.measure_execution_time(method)
			self.__cleanup_download_folder()
			time.sleep(2)

		# print the execution times
		print('*'*30)
		for method, time_taken in times.items():
			print(f'{method} took {time_taken:.2f} seconds')
		print('*'*30)


if __name__=='__main__':
	urls = [
		'https://cdn.pixabay.com/photo/2017/08/30/01/05/milky-way-2695569_1280.jpg',
		'https://cdn.pixabay.com/photo/2017/02/01/22/02/mountain-landscape-2031539_1280.jpg',
		'https://cdn.pixabay.com/photo/2015/12/01/20/28/road-1072823_1280.jpg',
		'https://cdn.pixabay.com/photo/2015/07/27/20/16/book-863418_1280.jpg',
		'https://cdn.pixabay.com/photo/2016/03/27/22/22/fox-1284512_1280.jpg',
		'https://cdn.pixabay.com/photo/2018/08/14/13/23/ocean-3605547_1280.jpg',
		'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg',
		'https://cdn.pixabay.com/photo/2013/10/02/23/03/mountains-190055_1280.jpg',
		'https://cdn.pixabay.com/photo/2015/06/19/21/24/avenue-815297_1280.jpg',
		'https://cdn.pixabay.com/photo/2016/10/20/18/35/earth-1756274_1280.jpg',
		'https://cdn.pixabay.com/photo/2013/07/18/10/56/railroad-163518_1280.jpg',
		'https://cdn.pixabay.com/photo/2014/08/15/11/29/beach-418742_1280.jpg',
		'https://cdn.pixabay.com/photo/2014/02/27/16/10/tree-276014_1280.jpg',
	]

	img_downloader = ImageDownloader(urls, './Downloads')
	img_downloader.summarize_execution_times()