import re
handl = open("text.txt")
#for line in handl:
result = list()
for line in handl:
	# several looking up methods:
	#y = re.findall('^From (\S+@+\S+)',line)	# emails
	y = re.findall('^From .*@([^ ]*)',line)		# domains
	if len(y) != 0:
		result.append(y)
print result
