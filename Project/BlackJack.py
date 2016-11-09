import fuzzywuzzy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import random

while 0==0:
	ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
	suits = ['-Heart','-Diamond','-Clubs','-Spades']
	cards = []
	
	n = raw_input("How many decks do you want to play with? ")
	decks = range(1,n+1)
	print(decks)
	raw_input
	for deck in len(decks):
		for rank in ranks:
			for suit in suits:
				cards.append(rank + suit + deck)
	print len(cards)
	

		

	myhand = [random.choice(rank) + random.choice(suit), random.choice(rank) + random.choice(suit)]
	myhand.sort()
	print(myhand)

	choices = ['Hit', 'Stay', 'Double Down']
	say = raw_input("Hit? Stay? Double Down? ")
	action = choices.index(say)
	print(action)

	if action == 0:
		myhand.append(random.choice(rank) + random.choice(suit))
		myhand.sort()
	elif action == 2:
		myhand.append(random.choice(rank) + random.choice(suit))
		myhand.sort()
	else:
		print("")	
	print(myhand)
	
	

	dealerhand = random.choice(rank) + random.choice(suit)
	#if dealerhand = myhand:
	#	dealerhand = random.choice(rank) + random.choice(suit)
	raw_input()
