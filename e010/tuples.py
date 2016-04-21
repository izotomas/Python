try:
	text = open("romeo.txt")
except:
	print "File romeo.txt not found."
	exit()

words = dict()
for line in text:
		line = line.rstrip().split()
		for word in line:
			words[word] = words.get(word,0) + 1

wordlist = list()
for key,val in words.items():
	wordlist.append((val,key))

wordlist.sort(reverse=True)

for val, key in wordlist[:10]:
	print key, val
