puzzle_input_file = open("puzzle_input_day2.txt", "r")

lines = puzzle_input_file.readlines()

game_power = []

for line in lines:
    possible = True
    game_id_string, game_sets = line.split(":")
    game_id = int(game_id_string[5:])
    cube_sets = game_sets.split(";")
    print(game_id)

    current_max = {
        'red': 0,
        'blue': 0,
        'green': 0
    }

    for amount_color_cube_list in cube_sets:
        amount_color_cube = amount_color_cube_list.split(",")
        
        for amount_color in amount_color_cube:
            amount, color = amount_color.strip().split()

            amount_int = int(amount)

            if amount_int > current_max.get(color):
                current_max.update({color: amount_int})

    print(current_max)
    min_red = current_max.get('red')
    min_blue = current_max.get('blue')
    min_green = current_max.get('green')
    power = min_red * min_blue * min_green
    print(power)
    game_power.append(power)
    # if possible:
    #     possible_ids.append(game_id)

print(sum(game_power))