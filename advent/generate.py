from advent.models import *
import random, datetime

def surprises():
	array = [{"gift_type": "action", "gift": "A homecooked, candlelit dinner just for us"},
			{"gift_type": "material", "gift": "1 pack of your favorite cigarettes!"},
			{"gift_type": "compliment", "gift": "I could not imagine life without you. Every day we spend together is a joy, and every day I love you even more."},
			{"gift_type": "action", "gift": "A clean tub and a beautifully prepared hot bath"},
			{"gift_type": "material", "gift": "A pint of your favorite ice cream!"},
			{"gift_type": "compliment", "gift": "Did I tell you you're the most beautiful woman in the world? No?!? You're the most beatiful woman in the universe!"},
			{"gift_type": "action", "gift": "A full head to toe massage! Get out the oils and get on the bed!"},
			{"gift_type": "material", "gift": "A zipcar day trip wherever you want to go!"},
			{"gift_type": "compliment", "gift": "Every day you impress me, entertain me, and show me love. You are brilliant, hilarious, and an endless source of inspiration."},
			{"gift_type": "action", "gift": "Cuddling and stroking- all you want!"},
			{"gift_type": "material", "gift": "A romantic dinner at a restaurant of your choice"},
			{"gift_type": "compliment", "gift": "I feel so close to you. It hurts to be away."},
			{"gift_type": "action", "gift": "Cleaning one thing in the house of your choice"},
			{"gift_type": "material", "gift": "Any bag of chips you want!"},
			{"gift_type": "compliment", "gift": "Without you, there is no me. You are my family, my best friend, and my lover."},
			{"gift_type": "material", "gift": "Dumplings! Let's get dumplings at Jing Fong!"},
			{"gift_type": "material", "gift": "Any candy you want!"},
			{"gift_type": "action", "gift": "A trip to any museum you want!"},
			{"gift_type": "action", "gift": "A trip to yoga together!"},
			{"gift_type": "material", "gift": "A fancy cocktail at any cool bar"},
			{"gift_type": "action", "gift": "A sightseeing trip anywhere you want in the city!"},
			{"gift_type": "material", "gift": "Brunch together wherever you want!"},
			{"gift_type": "action", "gift": "Making out for however long you want! Oooh baby!"},
			{"gift_type": "compliment", "gift": "You make my life more beautiful than it's ever been. You are my treasure."}]
	random.shuffle(array)
	return array

def gifts(surprises, user):
	date = datetime.datetime(datetime.datetime.now().year, 12, 1)
	for gift in surprises:
		day = Calendar(name = user.username, date = date, user = user, gift = gift['gift'], gift_type = gift['gift_type'])
		day.save()
		date += datetime.timedelta(1)
	return True