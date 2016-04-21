email  = raw_input("Enter your email: ")
atpos = email.find('@')
length = len(email)
domain = email[atpos+1:length]
print domain