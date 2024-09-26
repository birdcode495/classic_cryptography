import pyperclip


def main():

	myMessage = input('Enter the message to encrypt: ')
	myKey = int(input('Enter key: '))

	cipherText = encryptMessage(myKey, myMessage)
	print(cipherText)

	pyperclip.copy(cipherText)


def encryptMessage(key, message):

	cipherText = ''
	g = len(message) % key
	pointer = 0
	#pointer = pointer_b
	#key = key_b

	ne = key

	if g > 0:

		se = len(message) - g

	elif g == 0:

	 	se = len(message)

	no = 0



	while len(cipherText) < len(message):

		print(pointer)

		while pointer < ne:

			cipherText = cipherText + message[pointer]
			pointer = pointer + 1

	
		print(pointer)

		pointer = pointer + (key - 1)
		print(pointer)

		while pointer < se:

			cipherText = cipherText + message[pointer]
			pointer = pointer + key
		

		print(pointer)

		if g > 0:

			pointer = pointer - (key - g)

			while pointer >= se:

				cipherText = cipherText + message[pointer]
				pointer = pointer - 1

		elif g == 0:

			pointer = pointer - (key + 1)
			print(pointer)

			while pointer >= se - key:

				cipherText = cipherText + message[pointer]
				pointer = pointer - 1

		print(pointer)

		pointer = pointer - (key - 1)


		while pointer > no:

			cipherText = cipherText + message[pointer]
			pointer = pointer - key

		if len(cipherText) == len(message):

			break

		print(pointer)



		pointer = pointer + (key + 1)
		no = no + (key + 1)
		ne = key + (key - 1)
		#key = key - 2
		g = 0

		if g > 0:

			se = len(message) - g - 1

		elif g == 0:

	 		se = len(message) - (key - 1)

	return cipherText
 

if __name__ == '__main__':

	main()

