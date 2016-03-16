def roots(A):
	
	return (mysqrt(A),myqubr(A))
	
def mysqrt(A):
	x = 1.000#input("x initial value:")
	E=  0.0001
	while abs(x*x-A)>= E:
		#print x
		x = x - (x*x-A)/(2*x) 
		if abs(x*x-A)< E:
			break
	print "the x value of square root is: ",x


def myqubr(A):
	x=1.000
	E=0.0001
	while abs(x*x*x-A)>=E:
		#print x
		x= x - (x*x*x-A)/(3*x*x)
		if abs(x*x*x-A)<E:
				break
	print "the x value of qubic root is",x

roots(64)
