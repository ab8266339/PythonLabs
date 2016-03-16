def cashpoint(truepin,balance):
	if check_PIN(truepin)==True:
		return withdrawal(balance)
	else:
		return ("PIN-error")

			

def check_PIN(truepin):
	Value=raw_input("Please input your PIN:")		
	if Value==truepin:
		return True
	else:
		print"Your Pin is incorrect, would you like try one more time, press 1 to try one more time, 2 to exit"
		x=input()
		if x==1:
			Value=raw_input("Please input your PIN:")		
			if Value==truepin:
				return True
		else:
			return(False)

def withdrawal(balance):
	print "Please choose the following options:"
	x=input("Choose 1 to check balance, Choose 2 to withdrawal money, Choose 3 to pop up your mobile device: ")
	if x==1:
		print "checking your balance"
		print "Your balance is ",balance
		return balance
	elif x==2:
		amount=input("Please input the amount you want to withdraw:")
		if amount <= balance:
			balance = balance-amount
			print "Your balance is:", balance
			return ("withdrawal requested", amount,balance)
		else: 
			print "Your input exceed the balance,please try again"
			withdrawal(balance)	
			return ("Exceed amount")
	elif x==3:
		return topup(balance)

		
		
def topup(balance):
	credit=input("Please input the value you want to top up(no more than 10):")
	if credit > balance:
		print "Your balance is too low"
		return ("error")
	elif credit >10:
		print "Please input no more than 10"
		topup(balance)
		return "exceed amount"
	else:
		balance=balance - credit
		print"You have added:",credit,"to your phone","And your banlace is",balance
		return (credit, balance)
	



