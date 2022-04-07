import os
import sys
import time
import shutil
import threading
import requests
import urllib
import os
import shutil

# url = sys.argv[1]
conns = 8
dl_dir = os.getcwd()



def get_filename_from_url(url):
	return urllib.parse.urlsplit(url).path.split('/')[-1]

def download(url, start, this_chunk_size, part, tmp_dir):
	r = requests.get(url, headers={'Range':'bytes=%d-%d' % (start, start + this_chunk_size-1)}, stream=True)
	filename = '_%d' % part + get_filename_from_url(url)
	filepath = os.path.join(tmp_dir, filename)
	print( 'Downloading %s' % filepath)
	with open(filepath, 'wb') as f:
		for chunk in r.iter_content(chunk_size=1024):
			if chunk:
				f.write(chunk)
	print( 'Downloaded %s' % filepath)

def downloader(url): #, dl_dir):
	# check if URL accept ranges
	tmp_dir = dl_dir + '/tmp'
	if os.path.isdir(tmp_dir):
		shutil.rmtree(tmp_dir)	
	os.mkdir(tmp_dir)
	r = requests.head(url)
	
	accept_ranges = 'accept-ranges' in r.headers and 'bytes' in r.headers['accept-ranges']
	if not accept_ranges:
		return 'URL does not accept byte ranges.'
		quit()

	# download chunks
	size = int(r.headers['Content-Length'])
	print(r.headers)
	print(size)
	chunk_size = (size / conns)
	remainder = (size % conns)
	threads = []
	for start in range(0, size, int(chunk_size)):
		part = len(threads)
		this_chunk_size = chunk_size if part != conns-1 else chunk_size + remainder
		t = threading.Thread(target=download, args=(url, start, this_chunk_size, part, tmp_dir))
		threads.append(t)
		t.daemon = True
		t.start()
	print("waiting on merge")
	# merge into a single file
	while threading.active_count() > 1:
		time.sleep(0.1)

	print('All parts downloaded. Joining files...')

	filename = get_filename_from_url(url)
	filepath = os.path.join(dl_dir, filename)
	with open(filepath, 'wb') as f:
		for i in range(conns):
			tmp_filename = '_%d' % i + filename
			tmp_filepath = os.path.join(tmp_dir, tmp_filename)
			shutil.copyfileobj(open(tmp_filepath, 'rb'), f)
			os.remove(tmp_filepath)
			print(tmp_filename)
	print("download finished")
	shutil.rmtree(tmp_dir)

	return 'Joining complete. File saved in ' + filepath

print("hoo")