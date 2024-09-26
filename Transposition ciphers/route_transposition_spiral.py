import pyperclip


# def main():

# 	myMessage = input('Enter the message to encrypt: ')
# 	myKey = int(input('Enter key: '))

# 	cipherText = encryptMessage(myKey, myMessage)
# 	print(cipherText)

# 	pyperclip.copy(cipherText)


def encryptMessage(key, message):

	cipherText = ''

	g = len(message) % key

	pointer = 0

	while pointer < key:

		cipherText = cipherText + message[pointer]
		pointer = pointer + 1

	
	print(pointer)

	pointer = pointer + (key - 1)
	print(pointer)

	while pointer < len(message):

		cipherText = cipherText + message[pointer]
		pointer = pointer + key
		

	print(pointer)

	if g > 0:

		pointer = pointer - (key - g)

		while pointer >= len(message) - g:

			cipherText = cipherText + message[pointer]
			pointer = pointer - 1

	elif g == 0:

		pointer = pointer - (key + 1)

		while pointer >= len(message) - key:

			cipherText = cipherText + message[pointer]
			pointer = pointer - 1


	# while pointer > 0:

	# 	cipherText = cipherText + message[pointer]
	# 	pointer = pointer - key

	return cipherText
 

# if __name__ == '__main__':

# 	main()

myMessage = input('Enter the message to encrypt: ')
myKey = int(input('Enter key: '))

cipherText = encryptMessage(myKey, myMessage)

print(cipherText)








	
		
	



