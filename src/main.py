import random
from sys import stdin
from state import *

bad_dave = [ "What are you doing Dave?", "I'm afraid I can't do that Dave.", "Would you like me to sing you a song Dave?" ]

actionMap = {
	"walk": "go",
	"dance": "go",
	"move": "go",
	"go": "go",
	"stab": "stab"
}

nouns = [ "knife", "skeleton", "hat", "left", "right", "up", "down", "forward", "back" ]

while True:
	text = stdin.readline()

	action = None
	objectNoun = None
	subjectNoun = None

	for i in text.rstrip('\n').split(' '):
		if not action and i in actionMap:
			action = actionMap[i]
			print actionMap[i]
		elif not objectNoun and i in nouns:
			objectNoun = i
		elif not subjectNoun and i in nouns:
			subjectNoun = i
		if action and objectNoun and subjectNoun:
			# We have all the things
			break
	print (action, objectNoun, subjectNoun)

	try:
		do_the_thing(action, objectNoun, subjectNoun)
	except Exception:
		print "What are you doing Dave?"
