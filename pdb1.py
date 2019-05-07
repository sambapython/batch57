a=10
b=20
c=a+b
print(a,b,c)
def fun(y):
	print(y)
	res=10/y
	print("res=",res)
import pdb; pdb.set_trace()
for i in [10,20,0,-1,2,3,4]:
	if i!=0:
		fun(i)
print("thanks")