#!/usr/bin/env
from datetime import datetime
import random

RESPONSES = ('OK',
			 'TERRIBLE',
			 'MEH')

print('How can I help you?(To exit program please type EXIT)')

while (1):
	prompt = raw_input(':').upper()

	if (prompt == 'HOW ARE YOU?'):
		resp_index = random.randrange(0,3)
		print(RESPONSES[resp_index]);
	elif(prompt == 'WHAT IS YOUR FAVORITE TEXT EDITOR?'):
		print('Anything that does not contain the word VIM')
	elif(prompt == 'WHAT IS THE DATE?'):
		print(datetime.now())
	elif(prompt == 'EXIT'):
		break;
	else:
		print('I do not understand the question, please try again.')

