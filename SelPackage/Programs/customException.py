class Error(Exception):
	pass
class ValueTooSmallException(Error):
	pass
class ValueTooLargeException(Error):
	pass
number =10
while True:
	value = int(input("Enter the number to guess :"))
	try:
		if value<number:
			raise ValueTooSmallException
		elif value>number:
			raise ValueTooLargeException
		break
	except ValueTooSmallException:
		print("Value too small exception")
	except ValueTooLargeException:
		print("Value too large exception")
print("Congrats u guessed it correct")