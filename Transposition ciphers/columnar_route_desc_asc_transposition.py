import pyperclip


def main():

	myMessage = input('Enter the message to encrypt: ')
	myKey = int(input('Enter key: '))

	cipherText = encryptMessage(myKey, myMessage)
	print(cipherText + '|')

	pyperclip.copy(cipherText)


def encryptMessage(key, message):

	cipherText = [''] * key

	remaining_rows = len(message) // key

	for col in range(key):

		pointer = col

		if col % 2 == 0:

			while pointer < len(message):

				cipherText[col] = cipherText[col] + message[pointer]
				pointer = pointer + key

		elif col % 2 != 0:

			pointer = pointer + (key * remaining_rows)

			if pointer >= len(message):

				pointer = pointer - key

			while pointer >= col:

				cipherText[col] = cipherText[col] + message[pointer]
				pointer = pointer - key

	return ''.join(cipherText)


if __name__ == '__main__':

	main()

