puzzle_input_file = open("puzzle_input_day2.txt", "r")

lines = puzzle_input_file.readlines()

possible_ids = []

max_color_cube = {
    'red':12,
    'green':13,
    'blue':14
}

for line in lines:
    possible = True
    game_id_string, game_sets = line.split(":")
    game_id = int(game_id_string[5:])
    cube_sets = game_sets.split(";")
    print(game_id)

    for amount_color_cube_list in cube_sets:
        amount_color_cube = amount_color_cube_list.split(",")
        
        for amount_color in amount_color_cube:
            amount, color = amount_color.strip().split()
            if int(amount) > max_color_cube.get(color):
                possible = False

    if possible:
        possible_ids.append(game_id)

print(sum(possible_ids))