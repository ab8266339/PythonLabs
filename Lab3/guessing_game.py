from random import randint

def guess(attempts,range):
	number = randint(1,range)
	attempts
	while attempts>0:
		print "Welcome! Can you guess my secret number?"
		n = input("Make a guess:")
		if n<= range:
			if n< number:
				print "too low"
				attempts=attempts-1
				print "you got:",attempts,"attempts left"
				continue
			elif n==number:
				print"you Got it" 
				return attempts
			elif n>number:
				print"too high"
				attempts=attempts-1
				print "you got:",attempts,"attempts left"
				continue
			
		else: 
			print "please type new value"
			return guess(attempts,range)
	if attempts == 0:
		print "The number is",number
		print "You used up your chances,"
		print "bad luck,END-OF-GAME: thanks for playing!"

guess(3,10)