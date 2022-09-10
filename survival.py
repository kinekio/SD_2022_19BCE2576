import re





grid = [['-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-']]
curr_grid = grid

print('player 1 please enter your name:')
p1_name = input()
print('player 2 please enter your name:')
p2_name = input()
print(p1_name + ' please enter your pawn positions :')
p1_positions = input()  # Handle wrong input here
p1_positions = p1_positions.split(",")
p1_char_positions = [[4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
print(p2_name + ' please enter your pawn positions :')
p2_positions = input()  # Handle wrong input here
p2_positions = p2_positions.split(",")
p2_char_positions = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]]
for i in range(0, 5):
    curr_grid[0][i] = p2_positions[i]
    curr_grid[4][i] = p1_positions[i]
game_runing = True
chance = 1
def F(x):
    pass


def R(x):
    pass


def L(x):
    pass


def D(x):
    pass

dispatcher = { 'F': F, 'L': L }
while game_runing:
    if chance == 1:
        print(p1_name + ' please Player1 Input')
        command = input()
        # check for wrong input

        # insert
        command = command.split(":")
        movement = command[1]
        char_to_move = command[0].split("-")[1]
        curr_pos = p2_char_positions[p1_positions.index(char_to_move)]
        if re.search("P", char_to_move) is not None:
            try:
                dispatcher[movement](curr_pos)
            except:
                pass
            curr_grid = grid
            for i in range(0, 5):
                curr_grid[0][i] = p2_positions[i]
                curr_grid[4][i] = p1_positions[i]
