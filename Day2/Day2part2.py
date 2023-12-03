import re
"""
--- Part Two ---
The Elf says they've stopped producing snow because they aren't getting any water! He isn't sure why the water stopped; however, he can show you how to get to the water source to check it out for yourself. It's just up ahead!

As you continue your walk, the Elf poses a second question: in each game you played, what is the fewest number of cubes of each color that could have been in the bag to make the game possible?

Again consider the example games from earlier:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. If any color had even one fewer cube, the game would have been impossible.
Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
Game 4 required at least 14 red, 3 green, and 15 blue cubes.
Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.
The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five powers produces the sum 2286.

For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?
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

#input a array 
def multiplyAllInArray(array): 
	result = 1
	for x in array:
		result = result * x
	return result

f = open("input2.txt", "r")
text = f.read()
arrayOflines = splitLinesIntoArray(text)
allGames = []
for line in arrayOflines:
	gameId = int(re.search(r'\d+', line).group())
	print(gameId)
	sets = line.split(';')
	sets[0] = sets[0][sets[0].find(':') + 1: len(sets[0])]
	print(sets)
	gs = gameSet(sets)
	g = game(gameId,gs)
	allGames.append(g)

idSum = 0
biggestRed = 0
biggestGreen = 0
biggestBlue = 0
allBiggestColors = []
biggestColorInSet = []
finalNumber = 0
for game in allGames:
	biggestCubeOfGame = []
	for gameId, gamesets in game.items():
		for gameset in gamesets:
			if gameset['red'] > biggestRed:
				biggestRed = gameset['red']
			if gameset['green'] > biggestGreen:
				biggestGreen = gameset['green']
			if gameset['blue'] > biggestBlue:
				biggestBlue = gameset['blue']
		allBiggestColors.append(biggestRed)
		allBiggestColors.append(biggestGreen)
		allBiggestColors.append(biggestBlue)
		finalNumber += multiplyAllInArray(allBiggestColors)
		print(finalNumber)
		allBiggestColors = []
		biggestRed = 0
		biggestGreen = 0
		biggestBlue = 0

		

