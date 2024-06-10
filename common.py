import mmap
import tqdm
import statistics
def get_num_lines(file_path) -> int:
	fp = open(file_path, "r+")
	buf = mmap.mmap(fp.fileno(), 0)
	lines = 0
	while buf.readline():
		lines += 1
	return lines

def first_not_null(l: list):
	for item in l:
		if item != 0:
			return item
 
def not_null(l: list) -> list:
	ret = []
	for item in l:
		if item != 0:
			ret.append(item)
	return ret

def get_diff(l: list, r: list):
	if not r or not l:
		return []
	d = []
	sz = min(len(l), len(r))
	for i in range(0, sz):
		d.append(r[i] - l[i])
	return d


def nb_diff(l) -> list:
	if not l or len(l) < 2:
		return []
	diff = []
	prev = l[0]
	for v in l[1:]:
		diff.append(v - prev)
		prev = v
	return diff

def normalize(l:list)->list:
	if not l:
		return []
	ret = []
	nn = not_null(l)
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

def stats(l) -> str:
	_min = min(l)
	_max = max(l)
	_mid = statistics.median(l)
	return "{} - {} - {} len:{} range:{}".format(_min, _mid, _max, len(l), (_max - _min))

def load_markers(fname: str, marker: str, extractor) -> list:
	result = []
	lcount = get_num_lines(fname)
	with open(fname, 'r') as f:
		for line in tqdm.tqdm(f, total=lcount):
			line = line.strip() 
			if marker in line:
				pos = line.find(marker) + len(marker)
				tail = line[pos:].strip()
				try:
					m = extractor(tail)
					result.append(m)
				except Exception as e:
					print("invalid line ( ", line, ")", str(e))
					continue
	return result
