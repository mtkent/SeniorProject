import math
import random

#crossover: will either take binary bit from parent 1 or two

def cross_mutate(n, m):
	encoding1 = str(bin(n))[2:] #12 long - max is 4095
	encoding2 = str(bin(m))[2:]
	# print ("1 ", encoding1, " 2 ", encoding2)
	if (len(encoding1) > len(encoding2)):
		encoding2 = ('0' * (len(encoding1) - len(encoding2))) + encoding2
	else:
		encoding1 = ('0' * (len(encoding2) - len(encoding1))) + encoding1
	
	crossover = ''
	rate = 50

	for idx, val in enumerate(encoding1):
		rand = random.randint(0, 100)
		if rand < rate:
			crossover += str(encoding1[idx])
		else:
			crossover += str(encoding2[idx])


	# mutation: will maybe invert bit, low probability - maybe 1/20
	mutation = ''
	mrate = 5
	# print ("crossover", crossover)
	for idx, val in enumerate(crossover):
		rand = random.randint(0, 100)
		if rand > mrate:
			mutation += crossover[idx]
		else:
			if val == '1':
				mutation += '0'
			else:
				mutation += '1' 
	# print ("mutation ", mutation)

	final = int(mutation, base=2)

	# print("final ", final)
	return final

def cross_mutate_neg(n, m):
	num = cross_mutate(n, m)

	rand = random.randint(0, 100)

	if rand < 50:
		num = num * -1

	return num

