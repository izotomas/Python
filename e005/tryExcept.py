n = -1;
while (n <= 0 or n > 5):
	try:
	 n = float(raw_input("Enter number between 1-5: "))
	except:
		print "Number Input Error!"
print "Number yo've picked is ", n			