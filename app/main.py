def fun(x,y):
	"""
	x=10,y=20 -->30
	x=10,y="str1"--> None
	x="str2", y=20 --> None
	x="str1", y="str2" --> str1str2
	"""
	try:
		return x+y
	except:
		return None