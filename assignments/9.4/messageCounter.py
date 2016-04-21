'''
Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
text = open(name)
wordsBag = dict()
for line in text:
	line = line.rstrip()
	if line.startswith("From "):
		token = line.split()
		wordsBag[token[1]] = wordsBag.get(token[1],0) + 1
maxW = None
maxI = None
for w,i in wordsBag.items():
	if maxI is None or i > maxI:
		maxW = w
		maxI = i
print maxW, maxI		
