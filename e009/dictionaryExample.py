try:
	text = open("text.txt")
except:
	print "File text.txt not found"
	exit()
text = text.read()
text = text.split()
words = dict()
for word in text:
	words[word] = words.get(word,0) + 1
commonW = None
commonI = None
for w,i in words.items():
	if commonI is None or i > commonI:
		commonW = w
		commonI = i
print commonW, commonI		