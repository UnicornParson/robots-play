import mmap
import tqdm

def get_num_lines(file_path):
	fp = open(file_path, "r+")
	buf = mmap.mmap(fp.fileno(), 0)
	lines = 0
	while buf.readline():
		lines += 1
	return lines

def firstNotNull(l: list):
	for item in l:
		if item != 0:
			return item
 
def notNull(l: list) -> list:
	ret = []
	for item in l:
		if item != 0:
			ret.append(item)
	return ret

def getDiff(l: list, r: list):
	if not r or not l:
		return []
	d = []
	sz = min(len(l), len(r))
	for i in range(0, sz):
		d.append(r[i] - l[i])
	return d

def normalize(l:list)->list:
	if not l:
		return []
	ret = []
	nn = notNull(l)
	if not nn:
		return []
	base = min(nn)
	for item in l:
		if item != 0:
			ret.append(item - base)
		else:
			ret.append(0)
	return ret

def chunks(L, n):
	for i in range(0, len(L), n):
		yield L[i:i+n]


def loadMarkers(fname:str, marker:str, extractor) -> list:
	result = []
	lcount = get_num_lines(fname)
	with open(fname, 'r') as f:
		for line in tqdm.tqdm(f, total=lcount):
			line = line.strip() 
			if marker in line:
				pos =  line.find(marker) + len(marker)
				tail = line[pos:].strip()
				#parts = tail.split(":")
				try:
					m = extractor(tail)
					result.append(m)
				except Exception as e:
					print("invalid line ( ", line, ")", str(e))
					continue