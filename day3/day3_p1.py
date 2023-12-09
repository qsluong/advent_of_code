puzzle_input_file = open("puzzle_input_day3.txt", "r")

lines = puzzle_input_file.readlines()

start_row = 0
last_row = range(len(lines))

lines_number = []

for row_index in range(len(lines)):
    print(f'{row_index}: {lines[row_index]}')
    current = lines[row_index]
    
    start_col = 0
    last_col = range(len(current))

    number = ""

    for col_index in range(len(current)):
        print(f'{col_index}: {current[col_index]}')
        item = current[col_index]
        if item != ".":
            if item.isnumeric():
                print(f'Numeric: {item} on index: row: {row_index} col: {col_index}')
            else:
                print(f'Symbol: {item} on index: row: {row_index} col: {col_index}')
    
    # print(f'FULLNUMBER {number}')