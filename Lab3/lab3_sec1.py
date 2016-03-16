def factorial(n):
	fac=1
	while n>0:
		print fac
		fac=fac*n
		n=n-1
	if n==0:
		fac=1
		print fac
	return fac
	
factorial(0)