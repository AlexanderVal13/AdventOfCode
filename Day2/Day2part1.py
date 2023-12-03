import re
"""
--- Day 2: Cube Conundrum ---
You're launched high into the atmosphere! The apex of your trajectory just barely reaches the surface of a large island floating in the sky. You gently land in a fluffy pile of leaves. It's quite cold, but you don't see much snow. An Elf runs over to greet you.

The Elf explains that you've arrived at Snow Island and apologizes for the lack of snow. He'll be happy to explain the situation, but it's a bit of a walk, so you have some time. They don't get many visitors up here; would you like to play a game in the meantime?

As you walk, the Elf shows you a small bag and some cubes which are either red, green, or blue. Each time you play this game, he will hide a secret number of cubes of each color in the bag, and your goal is to figure out information about the number of cubes.

To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.

You play several games and record the information from each game (your puzzle input). Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

For example, the record of a few games might look like this:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have been possible, you get 8.

Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
"""
#Splits a text. Returning strings of lines into an array. 
def splitLinesIntoArray(text):
  return re.split('\n', text)

#creates a game set, takes an array of gamesets
def gameSet(gamesets):
	gameSetsComplete = []
	gameset = {"red": 0, "green": 0, "blue": 0}
#example: [' 5 red, 1 green', ' 6 red, 3 blue', ' 9 red', ' 1 blue, 1 green, 4 red', ' 1 green, 2 blue', ' 2 blue, 1 red']
#s would be  5 red, 1 green
	for s in gamesets:
		gameset = {"red": 0, "green": 0, "blue": 0}
		cubes = s.split(',')
		#c would be  5 red
		for c in cubes:
			if 'red' in c:
				gameset["red"] = int(re.search(r'\d+', c).group())
			if 'green' in c:
				gameset["green"] = int(re.search(r'\d+', c).group())
			if 'blue' in c:
				gameset["blue"] = int(re.search(r'\d+', c).group())
		gameSetsComplete.append(gameset)
	return gameSetsComplete

#creates a game, needs game id and all sets in that game
def game(id, gameSet):
	g = {}
	for gs in gameSet:
		g.update({id: gameSet})
	return g

f = open("input2.txt", "r")
text = f.read()
arrayOflines = splitLinesIntoArray(text)
allGames = []
for line in arrayOflines:
	gameId = int(re.search(r'\d+', line).group())
	sets = line.split(';')
	sets[0] = sets[0][7:len(sets[0])]
	gs = gameSet(sets)
	g = game(gameId,gs)
	allGames.append(g)

idSum = 0
impossible = False
for game in allGames:
	for gameId, gamesets in game.items():
		impossible = False
		for gameset in gamesets:
			if gameset['red'] > 12:
				impossible = True
				break
			if gameset['green'] > 13:
				impossible = True
				break
			if gameset['blue'] > 14:
				impossible = True
				break
		if not impossible:
			idSum += gameId
print(idSum)
	




