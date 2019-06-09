import random

things = (
	'cat',
	'butt',
	'sword',
	'apple',
	'kittie',
	'doggo',
	'fruitful adventures',
	'fruo fruo',
	'snow',
	'ball',
	'snek',
	'snel',
	'boob',
	'head',
	'four',
	'five',
	'leaf',
	'boop',
	'water',
	'fire'
)

def print_numbers(nums=[], i=0, total=10):
	while i < total:
		random_thing = random.choice(things)
		nums.append('%s %s\'s' % (i, random_thing))
		i = i + 1
	print "Numbers: %s " % [num for num in nums]

print_numbers(total=1001)