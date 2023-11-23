from concurrent.futures import ThreadPoolExecutor, as_completed
import os
import shutil
# import re
from pytube import Playlist, YouTube
import threading
from typing import List

class VideoDownloader:
	def __init__(self, url:str, download_dir:str) -> None:
		self.url = url
		self.video = YouTube(self.url)

		self.download_dir = download_dir or os.getcwd()
		if not os.path.exists(self.download_dir):
			raise Exception(f'Error: {download_dir} does not exists!')


	def get_meta_data(self) -> dict:
		return {
			"author": self.video.author,
			"description":self.video.description,
			"keywords": self.video.keywords,
			"length": self.video.length,
			"publish_date":self.video.publish_date,
			"rating":self.video.rating,
			"title":self.video.title,
			"vid_info":self.video.vid_info,
			"views":self.video.views,
			"meta": self.video.metadata
		}

	def download(self, highest_res=False) -> None:
		print(f"Downloading: {self.video.title}...")

		if highest_res:
			stream = self.video.streams.get_highest_resolution()
		else:
			stream = self.video.streams.get_lowest_resolution()

		if stream:
			stream.download(self.download_dir)

		# print("Video Download complete!")


	def list_metadata(self):
		if self.video.metadata:
			print(self.video.metadata.raw_metadata)
			print(self.video.metadata._metadata)
		else:
			print(f"No metadata available for {self.video.title}.")


import os
import shutil
from pytube import Playlist

class PlaylistDownloader:
	def __init__(self, url, base_download_dir=None, n=None):
		self.url = url
		self.playlist = Playlist(self.url)
		self.video_urls = self.playlist.video_urls[:n] if n else self.playlist.video_urls

		self.base_download_dir = base_download_dir or os.getcwd()

		self.playlist_download_dir = os.path.join(
			self.base_download_dir,
			self._safe_dir_name(self.playlist.title))

		self._prepare_download_directory()

	def _safe_dir_name(self, name)->str:
		# Replace or remove invalid characters for a directory name
		return "".join(char if char.isalnum() or char in "_-()" else "_" for char in name)

	def _prepare_download_directory(self):
		if os.path.exists(self.playlist_download_dir):
			shutil.rmtree(self.playlist_download_dir)
		os.makedirs(self.playlist_download_dir, exist_ok=True)


	def list_videos(self):
		for video in self.playlist.videos:
			print(video.title)

	def download(self, highest_res=False):
		# Download each video in the playlist
		for video_url in self.video_urls:
			# Create a YouTube object
			video = VideoDownloader(
				url=video_url,
				download_dir=self.playlist_download_dir)

			video.download(highest_res=highest_res)


	def parallel_download_threads(self, highest_res=False):
		# Download each video in the playlist using separate threads
		threads = []
		for video_url in self.video_urls:
			video = VideoDownloader(
				url=video_url,
				download_dir=self.playlist_download_dir)

			thread = threading.Thread(
				target=video.download,
				kwargs={'highest_res':highest_res})
			thread.start()
			threads.append(thread)

		# Wait for all threads to finish
		for thread in threads:
			thread.join()

		print("Playlist download complete!")

	def parallel_download(self, highest_res=False):
		videos = [ VideoDownloader(url, self.playlist_download_dir) for url in self.video_urls ]

		with ThreadPoolExecutor(max_workers=5) as executor:
			tasks = [executor.submit(video.download) for video in videos]
			for task in as_completed(tasks):
				try:
					task.result()
				except Exception as e:
					print(f'Error: {e}')





if __name__=='__main__':
	playlist_url = 'https://www.youtube.com/watch?v=x7T2XNeWTSI&list=PLHr3FWbW-hj6s13V_lFbwR6_V6PFDiBW4&ab_channel=TheAcademyofWisdom'

	pl1 = PlaylistDownloader(url=playlist_url, base_download_dir='./downloads/', n=10)

	# pl1.list_videos()
	# pl1.download()
	pl1.parallel_download()
