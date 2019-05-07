import sys
if len(sys.argv)>2:
	 username=  sys.argv[1]
	 password=sys.argv[2]
	 print(f"user:{username}, password:{password}")
else:
	print("info: python cmdargs.py <username> <password>")