#домашнє по 9 лабораторній
import urllib2
import threading
from Queue import Queue
import sys, os, re

class DownloadThread(object):
	REGEX = {
		'hostname_strip':re.compile('.*\..*?/', re.I)
	}

	class MissingDirectoryException(Exception):
		pass

	class Downloader(threading.Thread):
		def __init__(self, queue, report):
			threading.Thread.__init__(self)
			self.queue = queue
			self.report = report

		def run(self):
			while self.queue.empty() == False:
				url = self.queue.get()
				response = url.download()
				if response == False and url.url_tried < url.url_tries:
					self.queue.put(url)
				elif response == False and url.url_tried == url.url_tries:
					self.report['failure'].append(url)
				elif response == True:
					self.report['success'].append(url)
				self.queue.task_done()

	class URLTarget(object):
		def __init__(self, url, destination, url_tries):
			self.url = url
			self.destination = destination
			self.url_tries = url_tries
			self.url_tried = 0
			self.success = False
			self.error = None

		def download(self):
			self.url_tried = self.url_tried + 1

			try:
				if os.path.exists(self.destination): # раніше завантажений файл
					self.success = True
					return self.success
				remote_file = urllib2.urlopen(self.url)
				package = remote_file.read()
				remote_file.close()
				if os.path.exists(os.path.dirname(self.destination)) == False:
					os.makedirs(os.path.dirname(self.destination))
				dest_file = open(self.destination, 'wb')
				dest_file.write(package)
				dest_file.close()
				self.success = True
			except Exception, e:
				self.error = e
			return self.success

		def __str__(self):
			return 'URLTarget (%(url)s, %(success)s, %(error)s)' % {'url':self.url, 'success':self.success, 'error':self.error}

	def __init__(self, urls=[], destination='.', directory_structure=False, thread_count=5, url_tries=3):
		if os.path.exists(destination) == False:
			raise DownloadThread.MissingDirectoryException('Destination folder does not exist.')

		self.queue = Queue(0) # черга нескінченого розміру
		self.report = {'success':[],'failure':[]}
		self.threads = []
		if destination[-1] != os.path.sep:
			destination = destination + os.path.sep
		self.destination = destination
		self.thread_count = thread_count
		self.directory_structure = directory_structure
		# встановлюємо чергу з будь-якими значеннями, шо нам дались
		for url in urls:
			self.queue.put(DownloadThread.URLTarget(url, self.fileDestination(url), url_tries))

	def fileDestination(self, url):
		if self.directory_structure == False:
			# нема структури каталогів(дисків), а лише файли
			file_destination = '%s%s' % (self.destination, os.path.basename(url))
		elif self.directory_structure == True:
			# відкреслити імя хості, тримати або зьерегти всі інші каталоги
			file_destination =  '%s%s' % (self.destination, DownloadThread.REGEX['hostname_strip'].sub('', url))
		elif hasattr(self.directory_structure, '__len__') and len(self.directory_structure) == 2:
			# користувач надає користувацьку заміну регульрному виразу
			regex = self.directory_structure[0]
			if instanceof(regex, str):
				regex = re.compile(str)
			replace = self.directory_structure[1]
			file_destination =  '%s%s' % (self.destination, regex.sub(replace, url))
		else:
			# не знаємо, що шукаємо, хочемо
			file_destination = None
		if hasattr(file_destination, 'replace'):
			file_destination = file_destination.replace('/', os.path.sep)
		return file_destination

	def addTarget(self, url, url_tries=3):
		self.queue.put(DownloadThread.URLTarget(url, self.fileDestination(url), url_tries))

	def run(self):
		for i in range(self.thread_count):
			thread = DownloadThread.Downloader(self.queue, self.report)
			thread.start()
			self.threads.append(thread)
		if self.queue.qsize() > 0:
			self.queue.join()

if __name__ == "__main__":
	if len(sys.argv) == 1:
		print 'No source URLs given.'
		sys.exit()
	url_source_path = sys.argv[1]
	if not os.path.exists(url_source_path):
		print '`%s` not found.' % url_source_path
		sys.exit()
	# завантаження силок
	url_source = open(url_source_path, 'r')
	urls = [url.strip() for url in url_source.readlines()]
	url_source.close()
	# завантажити пункт призначення
	if len(sys.argv) >= 3:
		destination = sys.argv[2]
		if not os.path.exists(destination):
			print 'Destination `%s` does not exist.'
			sys.exit()
	else:
		destination = '.'
	# кількість тих ниток
	if len(sys.argv) >= 4:
		threads = int(sys.argv[3])
	else:
		threads = 5
	downloader = DownloadThread(urls, destination, True, threads, 3)
	print 'Downloading %s files' % len(urls)
	downloader.run()
	print 'Downloaded %(success)s of %(total)s' % {'success': len(downloader.report['success']), 'total': len(urls)}
	if len(downloader.report['failure']) > 0:
		print '\nFailed urls:'
		for url in downloader.report['failure']:
			print url
