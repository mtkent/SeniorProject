def convertToBinary(n):
	if n > 1:
		convertToBinary(n//2)
	print(n % 2,end = '')

# # decimal number
# dec = 4530 # = 13 bit number

convertToBinary(100)

# binary = 11001
# decimal = 0
# for digit in binary:
#     decimal = decimal*2 + int(digit)
# print (decimal)

# bin = str(101001)
# toPrint = int(bin, base=2)
# print(" and ", toPrint)

