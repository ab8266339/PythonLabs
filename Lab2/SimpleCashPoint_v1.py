
def cashpoint(truepin,balance):
#truepin="1234"
#balance=5000
	Value=raw_input("Please input your PIN:")
	truepin
	balance
	if Value==truepin:
		print "Please choose the following options"
		x=input("Choose 1 to check balance, Choose 2 to withdrawal money, Choose 3 to pop up your mobile device")
		if x==1:
			print "checking your balance"
			print "Your balance is ",balance
		elif x==2:
			print balance
		elif x==3:
			print"function not available"
	else:
		print"Your Pin is incorrect"

