y=[]
def sum_list(x):
	sum=0
	y=[]
	for val in x:
		sum=sum+val
		print 'the value',sum
	return y

        


def tri(x):
	sum=0
	y=[]
	for val in range(x):
		sum=sum+val
		print sum
	return y

def squ(x):
	sum=0
	y=[]
	for val in x:
		sum=val*val
		print sum
	return y

sum_list(range(0,100))#tri(x),squ(x)
print y

