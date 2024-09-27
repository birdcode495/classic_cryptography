import math, pyperclip

def main():

	myMessage = input('Enter message to decrypt: ')
	myKey = int(input('Enter key: '))

	plainText = decryptMessage(myKey, myMessage)

	print(plainText + '|')
	pyperclip.copy(plainText)


def decryptMessage(key, message):

	numberOfColumns = math.ceil(len(message) / key)
	numberOfRows = key

	numberOfShadedBoxes = (numberOfColumns * numberOfRows) - len(message)

	plainText = [''] * numberOfColumns

	col = 0
	row = 0

	for symbol in message:

		plainText[col] = plainText[col] + symbol

		col = col + 1

		if (col == numberOfColumns) or (col == numberOfColumns - 1 and row >= numberOfRows - numberOfShadedBoxes):

			col = 0
			row = row + 1


	return ''.join(plainText)


if __name__ == '__main__':

	main()

	
