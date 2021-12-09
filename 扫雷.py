import random
End_game = 0
map_data = []
Game_map = []
Limit_map = []
numbers = 0
true_flags = 0

print("Welcome to Minesweeper.")
print("Please choose your difficulty:")
print("  1: Beginner 8 x 8 grid with 10 mines")
print("  2: Intermediate 16 x 16 grid with 40 mines")
print("  3: Expert 24 x 24 grid with 99 mines")

n = input()

def BFS(point_y,point_x):
	global Game_map
	global map_data
	global Limit_map
	global numbers
	if point_y != 0 and point_x != 0 and map_data[point_y-1][point_x-1] != "*" and Limit_map[point_y-1][point_x-1] == 0:
		Limit_map[point_y-1][point_x-1] = 1
		Game_map[point_y-1][point_x-1] = map_data[point_y-1][point_x-1]
		numbers += 1
		if map_data[point_y-1][point_x-1] == 0:
			waitChecklist.append((point_y-1,point_x-1)) 
	if point_y != 0 and map_data[point_y-1][point_x] != "*" and Limit_map[point_y-1][point_x] == 0:   
		Limit_map[point_y-1][point_x] = 1
		Game_map[point_y-1][point_x] = map_data[point_y-1][point_x]
		numbers += 1
		if map_data[point_y-1][point_x] == 0:
			waitChecklist.append((point_y-1,point_x)) 
	if point_y != 0 and point_x != x_len-1 and map_data[point_y-1][point_x+1] != "*" and Limit_map[point_y-1][point_x+1] == 0:
		Limit_map[point_y-1][point_x+1] = 1
		Game_map[point_y-1][point_x+1] = map_data[point_y-1][point_x+1]
		numbers += 1
		if map_data[point_y-1][point_x+1] == 0:
			waitChecklist.append((point_y-1,point_x+1))
	if point_x != 0 and map_data[point_y][point_x-1] != "*" and Limit_map[point_y][point_x-1] == 0:
		Limit_map[point_y][point_x-1] = 1
		Game_map[point_y][point_x-1] = map_data[point_y][point_x-1]
		numbers += 1
		if map_data[point_y][point_x-1] == 0:
			waitChecklist.append((point_y,point_x-1))
	if point_x != 0 and point_y != x_len-1 and map_data[point_y+1][point_x-1] != "*" and Limit_map[point_y+1][point_x-1] == 0:
		Limit_map[point_y+1][point_x-1] = 1
		Game_map[point_y+1][point_x-1] = map_data[point_y+1][point_x-1]
		numbers += 1
		if map_data[point_y+1][point_x-1] == 0:
			waitChecklist.append((point_y+1,point_x-1))
	if point_x != x_len-1 and map_data[point_y][point_x+1] != "*" and Limit_map[point_y][point_x+1] == 0:
		Limit_map[point_y][point_x+1] = 1
		Game_map[point_y][point_x+1] = map_data[point_y][point_x+1]
		numbers += 1
		if map_data[point_y][point_x+1] == 0:
			waitChecklist.append((point_y,point_x+1))
	if point_y != x_len-1 and map_data[point_y+1][point_x] != "*" and Limit_map[point_y+1][point_x] == 0:
		Limit_map[point_y+1][point_x] = 1
		Game_map[point_y+1][point_x] = map_data[point_y+1][point_x]
		numbers += 1
		if map_data[point_y+1][point_x] == 0:
			waitChecklist.append((point_y+1,point_x))
	if point_x != x_len-1 and point_y != x_len-1 and map_data[point_y+1][point_x+1] != "*" and Limit_map[point_y+1][point_x+1] == 0:
		Limit_map[point_y+1][point_x+1] = 1
		Game_map[point_y+1][point_x+1] = map_data[point_y+1][point_x+1]
		numbers += 1
		if map_data[point_y+1][point_x+1] == 0:
			waitChecklist.append((point_y+1,point_x+1))
			
def BFS2(point_y,point_x):
	global waitChecklist
	global Limit_map
	global map_data
	waitChecklist = []
	BFS(point_y,point_x)
	while len(waitChecklist) > 0:
		point_y,point_x = waitChecklist[0]
		if map_data[point_y][point_x] != "*":
			BFS(point_y,point_x)
			del waitChecklist[0]					
	return 0 
	
def Choose(n):
	if n == 1:
		return 8
	if n == 2:
		return 16
	if n == 3:
		return 24
	
def Countmines(n):
	if n == 1:
		return 10
	if n == 2:
		return 40
	if n == 3:
		return 99
	
def print_sheet(map_data):
	num = 0
	for i in range(len(map_data)):
		if i < 10:
			print(" 0" + str(i),end = '')
		else:
			print(" " + str(i),end = '')
	print("")
	for y in map_data:
		for i in range(len(map_data)):
			print("+--",end = '')
		print("")
		for x in y:
			print("| "+str(x),end = "")
		if num < 10:
			print("|",'0' +str(num))
			num += 1
		else:
			print("| " +str(num))
			num += 1
	for i in range(len(map_data)):
			print("+--",end = '')
	print("")

if n not in ['1','2','3']:
	print("Please restart the game and choose the correct difficulty level! ")
else:
	n = int(n)
	x_len = Choose(n)
	mines_count = Countmines(n)
	flags_count = 0
	NVsquares_count = x_len ** 2
	
	Game_map = [[" " for i in range(x_len)] for i in range(x_len)]
	Limit_map = [[0 for i in range(x_len)] for i in range(x_len)]
	map_data = [[0 for i in range(x_len)] for i in range(x_len)]
	tmp = [i for i in range(x_len**2)]
	mines = random.sample(tmp,mines_count)
	
	for count_y,i in enumerate(map_data):
		for count_x,i2 in enumerate(i):
			if x_len*count_y+count_x in mines:
				map_data[count_y][count_x] = "*"
				if count_y != 0 and count_x != 0 and map_data[count_y-1][count_x-1] != "*":
					a1 = int(map_data[count_y-1][count_x-1]) + 1
					map_data[count_y-1][count_x-1] = str(a1)
				if count_y != 0 and map_data[count_y-1][count_x] != "*":    
					a2 = int(map_data[count_y-1][count_x]) + 1
					map_data[count_y-1][count_x] = str(a2)
				if count_y != 0 and count_x != x_len-1 and map_data[count_y-1][count_x+1] != "*":
					a3 = int(map_data[count_y-1][count_x+1]) + 1
					map_data[count_y-1][count_x+1] = str(a3)
				if count_x != 0 and map_data[count_y][count_x-1] != "*":
					a4 = int(map_data[count_y][count_x-1]) + 1
					map_data[count_y][count_x-1] = str(a4)
				if count_x != 0 and count_y != x_len-1 and map_data[count_y+1][count_x-1] != "*":
					a5 = int(map_data[count_y+1][count_x-1]) + 1
					map_data[count_y+1][count_x-1] = str(a5)
				if count_x != x_len-1 and map_data[count_y][count_x+1] != "*":
					a6 = int(map_data[count_y][count_x+1]) + 1
					map_data[count_y][count_x+1] = str(a6)
				if count_y != x_len-1 and map_data[count_y+1][count_x] != "*":
					a7 = int(map_data[count_y+1][count_x]) + 1
					map_data[count_y+1][count_x] = str(a7)
				if count_x != x_len-1 and count_y != x_len-1 and map_data[count_y+1][count_x+1] != "*":
					a8 = int(map_data[count_y+1][count_x+1]) + 1
					map_data[count_y+1][count_x+1] = str(a8)
	##print_sheet(map_data)       ## a Final map
	while End_game != 1:
		try:
			NVsquares_count = x_len ** 2 - numbers
			print("Mines:",mines_count,"     Flags:",flags_count,"     No visible squares:",NVsquares_count)
			print_sheet(Game_map)
			Move_key = input("Please enter your move:")
			Move_key = Move_key.replace('(','')
			Move_key = Move_key.replace(')','')
			list_key = []
			list_key = list(Move_key)
			if list_key[0] != 'F':
				point_x = int(list_key[0])
				if list_key[1] != ',':
					point_x = point_x * 10 + int(list_key[1])
					point_y = int(list_key[3])
					try:
						point_y = point_y * 10 +int(list_key[4])
					except:
						pass
				else:
					point_y = int(list_key[2])
					try:
						point_y = point_y * 10 +int(list_key[3])
					except:
						pass
				
				if map_data[point_y][point_x] == '*':
					Game_map[point_y][point_x] = map_data[point_y][point_x]
					NVsquares_count -= 1
					print("Mines:",mines_count,"     Flags:",flags_count,"     No visible squares:",NVsquares_count)
					print_sheet(Game_map)
					print("GAME OVER!")
					End_game = 1
				if map_data[point_y][point_x] == 0:
					Game_map[point_y][point_x] = map_data[point_y][point_x]	
					BFS2(point_y,point_x)
				if map_data[point_y][point_x] != '*' and map_data[point_y][point_x] != 0:
					numbers += 1
					Game_map[point_y][point_x] = map_data[point_y][point_x]	
				if numbers == x_len ** 2 - Countmines(n):
					End_game = 1
					print_sheet(map_data)
					print("Congratulations! You have finished the game!")
			elif list_key[0] == 'F':
				if flags_count < mines_count:
					point_x = int(list_key[1])
					if list_key[2] != ' ': 
						point_x = point_x * 10 + int(list_key[2])
						point_y = int(list_key[4])
						try:
							point_y = point_y * 10 +int(list_key[5])
						except:
							pass
					else:
						point_y = int(list_key[3])
						try:
							point_y = point_y * 10 +int(list_key[4])
						except:
							pass
					if Game_map[point_y][point_x] == 'F':
						Game_map[point_y][point_x] = " "
						flags_count -= 1
						if map_data[point_y][point_x] == '*':
							true_flags -= 1
					elif  Game_map[point_y][point_x] == ' ':
						Game_map[point_y][point_x] = 'F'
						flags_count += 1
						if map_data[point_y][point_x] == '*':
							true_flags += 1
					if true_flags == Countmines(n):
						End_game = 1
						print_sheet(map_data)
						print("Congratulations! You have finished the game!")
				else:
					print("The number of flags exceeds the limit!")
		except:
			print("IndexError!")
			print("If you want to select the grid square, please use the input format of (a,b)")
			print("If you want to place a flag, please use the input format of Fa b")
			print("So, please enter you move again!")