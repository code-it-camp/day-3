import random
import time

def main():
	while input("Play Battleship? (y/n) ").lower() == "y":
		game(int(input("How many players? (1 or 2) ")))

def game(num_users):
	players = ["user" if num_users > 0 else "cpu", "user" if num_users == 2 else "cpu"]

	targets_remaining_1 = [15]
	targets_remaining_2 = [15]

	game_over = False
	winner = 0

	board_1, score_sheet_1, ship_locations_1 = initialize("user" if num_users > 0 else "cpu", 1)
	board_2, score_sheet_2, ship_locations_2 = initialize("user" if num_users == 2 else "cpu", 2)
	
	current_player = 1
	while not game_over:
		board, score_sheet, ship_locations, targets_remaining, player_type = None, None, None, None, None
		if current_player == 1:
			board = board_2
			score_sheet = score_sheet_1
			ship_locations = ship_locations_1
			targets_remaining = targets_remaining_2
			player_type = players[0]
		else:
			board = board_1
			score_sheet = score_sheet_2
			ship_locations = ship_locations_2
			targets_remaining = targets_remaining_1
			player_type = players[1]

		take_turn(board, score_sheet, ship_locations, targets_remaining, player_type, current_player)
		current_player = swith_current_player(current_player)
		winner = check_if_winner(targets_remaining_1, targets_remaining_2)
		if winner != 0:
			break

	print("Player " + str(winner) + " won!")

def take_turn(board, score_sheet, ship_locations, targets_remaining, player_type, current_player):
	"""
	board: a list of lists, contains the ship board of the current player's opponent
	score_sheet: a list of lists, contains all the shots made by the current player and whether
		those shots were hits or misses
	ship_locations: a dictionary containing each boat, and for each boat a list of coordinates which
		correspond to the positions of the boat
	targets_remaining: how many remaining targets the current player's opponent has
	player_type: whether the current player is a "user" or a "cpu"
	current_player: either 1 or 2
	"""

	# our target
	target = ()
	# either True or False
	valid_target = ________

	while not valid_target:
		if player_type == "user":
			target = input("Player " + str(current_player) + " please select a target: ")
		else:
			target = random_target()
		valid_target = valid(________, ________)

	fire(________, ________, ________, ________, ________)
	print("\n\n\n\n\n")

def valid(score_sheet, target):
	"""
	There are three prerequisites for our target to be valid:
		1. The target has two coordinates
		2. The target is on the board
		3. This player hasn't already fired at this target

	Remember that in order to check if prerequisite #2 is satisfied,
	we have to take into account who is the current player.

	Returns:
		a boolean holding either True or False, which represents
		whether or not the target is valid.
	"""
	# Prerequisite 1
	if len(target) != ________ and len(target) != ________:
		print("Invalid target.")
		return False

	# Prerequisite 2
	if target[________:________] not in target_dictionary.keys():
		print("Ship must be on board.")
		return False

	if int(target[________:________]) not in range(________, dimension_2 + ________):
		print("Ship must be on board.")
		return False

	coords = target_convert(target)

	# Prerequisite 3
	score_at_target = score_sheet[________][________]
	if score_at_target == "O" or score_at_target == "X":
		return False

	# If we've gotten to this point, the target has passed
	# all the prerequisites, so it is a valid target.
	return True

def target_convert(target):
	"""
	Assumes target is a target on the board.
	Converts the passed in string into its
	corresponding board-coordinates in tuple form.
	For example, "a5" becomes (0, 4) and "c3" becomes (2, 2).
	
	Returns:
		the tuple of numbers representing the
		target's board coordinates
	"""
	return (target_dictionary[target[________:________].lower()] - ________, int(target[________:________]) - ________)

def fire(board, score_sheet, ship_locations, targets_remaining, target):
	coords = target_convert(target)
	ship_at_target = board[________][________]	

	print("Fire!")
	if ship_at_target:
		score_sheet[________][________] = "X"
		ship_sunk, ship_name = check_if_ship_sunk(score_sheet, ship_locations, coords)

		if ship_sunk:
			print("The " + ship_name + " has been sunk!")
		else:
			print("Target hit at " + target + "!")

		targets_remaining[0] -= 1
	else:
		score_sheet[________][________] = "O"
		print("Target missed at " + target + ".")

	print_board(score_sheet)

def check_if_ship_sunk(score_sheet, ship_locations, coords):
	targeted_ship = None
	for ship in ship_locations.keys():
		if coords in ship_locations[ship]:
			targeted_ship = ship

	for coord in ship_locations[targeted_ship]:
		if score_sheet[coord[0]][coord[1]] != "X":
			return (False, targeted_ship)

	return (True, targeted_ship)

def check_if_winner(targets_remaining_1, targets_remaining_2):
	if targets_remaining_1[0] == 0:
		game_over = True
		return ________
	elif targets_remaining_2[0] == 0:
		game_over = True
		return ________
	else:
		return 0

def swith_current_player(current_player):
	if current_player == 1:
		return ________
	else:
		return ________


# ------------------- Variables you can use and edit in your code ------------------- #

# ------------------- Leave the section below as is ------------------- #

alphabet = "abcdefghijklmnopqrstuvwxyz"
target_dictionary = {}

boat_lengths = {
	"Aircraft Carrier": 5,
	"Battleship": 4,
	"Light Missile Cruiser": 3,
	"Submarine": 3
}

targets = []

dimension_1, dimension_2 = 10, 14

def init_spot_valid(board, target):
	"""
	There are three prerequisites for our target to be valid:
		1. The target has two coordinates
		2. The target is on the board
		3. This player hasn't already fired at this target

	Remember that in order to check if prerequisite #2 is satisfied,
	we have to take into account who is the current player.

	Returns:
		a boolean holding either True or False, which represents
		whether or not the target is valid.
	"""
	# Prerequisite 1
	if len(target) != 2 and len(target) != 3:
		print("Invalid board position.")
		return False

	# Prerequisite 2
	if target[:1] not in target_dictionary.keys():
		print("Position must be on board.")
		return False
	if int(target[1:]) not in range(1, dimension_2 + 1):
		print("Position must be on board.")
		return False

	coords = target_convert(target)

	score_at_target = None

	# Prerequisite 3
	if board[coords[0]][coords[1]] == True:
		print("A ship is already occupying this spot.")
		return False

	# If we've gotten to this point, the target has passed
	# all the prerequisites, so it is a valid target.
	return True

def init_ship_valid(board, boat_name, start, end):
	"""
	Ensures that we can place this ship on the board
	without overlapping on any other ships.
	"""
	start = target_convert(start)
	end = target_convert(end)
	delta_y, delta_x = end[0] - start[0], end[1] - start[1]

	# Prerequiste 1: No diagonal ships.
	if delta_y != 0 and delta_x != 0:
		print("Ships must be either horizontal or vertical.")
		return False

	# Prerequisite 2: Does not intersect any existing ships.
	if delta_y != 0:
		if delta_y + 1 != boat_lengths[boat_name]:
			print("Your " + boat_name + " must be " + str(boat_lengths[boat_name]) + " positions long.")
			return False
		for y in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
			if board[y][start[1]] == True:
				print("Ships cannot intersect.")
				return False
	elif delta_x != 0:
		if delta_x + 1 != boat_lengths[boat_name]:
			print("Your " + boat_name + " must be " + str(boat_lengths[boat_name]) + " positions long.")
			return False
		for x in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
			if board[start[0]][x] == True:
				print("Ships cannot intersect.")
				return False

	if delta_y == 0 and delta_x == 0:
		print("Your " + boat_name + " must be " + str(boat_lengths[boat_name]) + " positions long.")
		return False

	return True

def place_ship(board, ship_locations, boat_name, start, end):
	start = target_convert(start)
	end = target_convert(end)
	delta_y, delta_x = end[0] - start[0], end[1] - start[1]

	# Prerequisite 2: Does not intersect any existing ships.
	if delta_y != 0:
		for y in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
			board[y][start[1]] = True
			ship_locations[boat_name].append((y, start[1]))
	elif delta_x != 0:
		for x in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
			board[start[0]][x] = True
			ship_locations[boat_name].append((start[0], x))

def print_board(board):

	print("  " + " ".join([(str(i)) if i >= 10 else (" " + str(i)) for i in range(1, dimension_2 + 1)]))

	if board[0][0] == False or board[0][0] == True:
		for letter in target_dictionary.keys():
			i = target_dictionary[letter] - 1
			print(letter + " " + " ".join([(" +") if board[i][j] else " -" for j in range(dimension_2)]))
	else:
		for letter in target_dictionary.keys():
			i = target_dictionary[letter] - 1
			print(letter + " " + " ".join([(" " + board[i][j]) if board[i][j] else " -" for j in range(dimension_2)]))
	print()

def random_target():
	return targets[int(random.random() * len(targets))][int(random.random() * len(targets[0]))]

def initialize(player_type, player_num):
	board = [[False for i in range(dimension_2)] for j in range(dimension_1)]
	score_sheet = [["-" for i in range(dimension_2)] for j in range(dimension_1)]
	ship_locations = {
		"Aircraft Carrier": [],
		"Battleship": [],
		"Light Missile Cruiser": [],
		"Submarine": []
	}

	if player_type == "user":
		for boat in boat_lengths.keys():
			print("Player " + str(player_num) + ", place your " + boat)
			start, end = None, None
			valid_ship_placement = False
			while not valid_ship_placement:
				start = input("Start of ship coordinate: ").strip()
				while not init_spot_valid(board, start):
					start = input("Start of ship coordinate: (e.g. a5 or c3) ").strip()
				end = input("End of ship coordinate: ").strip()
				while not init_spot_valid(board, end):
					end = input("End of ship coordinate: (e.g. a5 or c3) ").strip()
				valid_ship_placement = init_ship_valid(board, boat, start, end)
			place_ship(board, ship_locations, boat, start, end)
			print_board(board)
		print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	else:
		for boat in boat_lengths.keys():
			length = boat_lengths[boat]
			start, end = None, None
			valid_ship_placement = False
			while not valid_ship_placement:
				start = random_target()
				while not init_spot_valid(board, start):
					start = random_target()

				possible_ends = []
				try:
					y, x = target_dictionary[start[0]] - length, int(start[1:]) - 1
					if y < 0 or x < 0:
						raise AssertionError
					possible_ends.append(targets[y][x])
				except:
					pass
				try:
					possible_ends.append(targets[target_dictionary[start[0]] + length - 2][int(start[1:]) - 1])
				except:
					pass
				try:
					y, x = target_dictionary[start[0]] - 1, int(start[1:]) - length
					if y < 0 or x < 0:
						raise AssertionError
					possible_ends.append(targets[y][x])
				except:
					pass
				try:
					possible_ends.append(targets[target_dictionary[start[0]] - 1][int(start[1:]) + length - 2])
				except:
					pass
				valid_end = False

				for i in random.sample(range(len(possible_ends)), len(possible_ends)):
					end = possible_ends[i]
					if init_spot_valid(board, end):
						valid_end = True
						break
				if valid_end and init_ship_valid(board, boat, start, end):
					place_ship(board, ship_locations, boat, start, end)
					valid_ship_placement = True

	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	return (board, score_sheet, ship_locations)

if __name__ == '__main__':
	target_dictionary = {alphabet[i]: (i + 1) for i in range(dimension_1)}
	for key in target_dictionary.keys():
		targets.append([key + str(i + 1) for i in range(dimension_2)])
	main()
