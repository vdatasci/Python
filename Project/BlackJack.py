import fuzzywuzzy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import random

while 0==0:
	#ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
	ranks = range(2,14)
	#suits = ['-Heart','-Diamond','-Clubs','-Spades']
	suits = ['d','h','c','s']
	cards = []
	tests = []
	
	
	n = raw_input("How many decks do you want to play with? ")
	decks = range(1,int(n)+1)
	print len(decks)

	for deck in decks:
		for rank in ranks:
			for suit in suits:
				cards.append(str(rank) + '|' + str(suit) + '.' + str(deck))
	print len(cards)
	

	card1 = random.choice(cards)
	cards.remove(card1)
	card2 = random.choice(cards)
	cards.remove(card2)
	print len(cards)
	
	dcard1 = random.choice(cards)
	cards.remove(dcard1)
	dcard2 = random.choice(cards)
	cards.remove(dcard2)
	print len(cards)


	myhand = [card1, card2]
	dhand = [dcard1, dcard2]
	myhand.sort()
	dhand.sort()



	print(myhand)
	print(dhand)

	playervalue = int(card1.partition("|")[0]) + int(card2.partition("|")[0])
	print(playervalue)
	dealervalue = int(dcard1.partition("|")[0]) + int(dcard2.partition("|")[0])
	print(dealervalue)



	
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
	
	


	#if dealerhand = myhand:
	#	dealerhand = random.choice(rank) + random.choice(suit)
	raw_input()
