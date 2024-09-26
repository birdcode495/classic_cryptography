# Reverse cipher

message = input('Enter the message to encrypt: ')

translated = ''

i = len(message) - 1

while i >= 0:

	translated = translated + message[i]
	i = i - 1

print('Your translated message is: ', translated)

