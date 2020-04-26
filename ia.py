import json

'''
This script will create a map to improve the moving in the origin map
This script build a path
We will use for index the ID of a carrefour and for value the list of carrefour near

A_____B
|	  |
D_____C
carrefour_data = {'A':['B','D'],'B':['A','C'],'C':['B','D'],'D':['A','C']}
result> [['A'], ['A', 'B'], ['A', 'B', 'C'], ['A', 'B', 'C', 'D'], ['A', 'D'], ['A', 'D', 'C'], ['A', 'D', 'C', 'B'], ['C'], ['C', 'B'], ['C', 'B', 'A'], ['C', 'B', 'A', 'D'], ['C', 'D'], ['C', 'D', 'A'], ['C', 'D', 'A', 'B'], ['B'], ['B', 'A'], ['B', 'A', 'D'], ['B', 'A', 'D', 'C'], ['B', 'C'], ['B', 'C', 'D'], ['B', 'C', 'D', 'A'], ['D'], ['D', 'A'], ['D', 'A', 'B'], ['D', 'A', 'B', 'C'], ['D', 'C'], ['D', 'C', 'B'], ['D', 'C', 'B', 'A']]

A_____D______G
|	  | 	 |
B_____E______H
|	  |		 |
C_____F______I
carrefour_data = {'A':['D','B'],'B':['A','E','C'],'C':['B','F'],'D':['A','E','G'],'E':['D','B','F','H'],'F':['E','C','I'],'G':['D','H'],'H':['G','E','I'],'I':['H','F']}
'''

# We draw the map
_map = [
	['A','D','G'],
	['B','E','H'],
	['C','F','I'],
]

# We build the carrefour
carrefour_data = {}
height = len(_map)

for y in range(height):
	width = len(_map[y])
	for x in range(width):
		index = _map[y][x]
		carrefour_data[index] = []
		if y-1 >= 0 and x < len(_map[y-1]):
			carrefour_data[index].append(_map[y-1][x])
		if x+1 < width:
			carrefour_data[index].append(_map[y][x+1])
		if x-1 >= 0:
			carrefour_data[index].append(_map[y][x-1])
		if y+1 < height and x < len(_map[y+1]):
			carrefour_data[index].append(_map[y+1][x])

paths = []

def generated_path_for(carrefour, first_carrefour='', path=[]):
	global paths
	paths.append(path)
	extern_carrefours = carrefour_data[carrefour]
	for extern_carrefour in extern_carrefours:
		if extern_carrefour == first_carrefour or path.count(extern_carrefour):
			pass
		else:
			generated_path_for(extern_carrefour, first_carrefour, path+[extern_carrefour])
	return path

for carrefour in carrefour_data:
	generated_path_for(carrefour, carrefour, [carrefour])


# Demo
while 1:
	print("---------------")
	for y in _map:
		for x in y:
			print(x, end=' ')
		print('')
	print("---------------")
	cpos = input('Enter your current position: ')
	epos = input('Enter your destination: ')
	for path in paths:
		if path[0] == cpos and path[-1] == epos:
			print(path)
