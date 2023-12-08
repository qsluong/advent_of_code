calibration_file = open("puzzle_input.txt", "r")

lines = calibration_file.readlines()

thousand_digits = []

def get_first_last_digit_from_line(line: str):
    digits = []
    for s in line:
        if s.isdigit():
            digits.append(s)
            # print(s)
    # print(digits)
    first_and_last = [digits[i] for i in (0, -1)]
    # print(first_and_last)
    first_last_string = f"{first_and_last[0]}{first_and_last[1]}"
    first_last_integer = int(first_last_string)
    # print(first_last_integer)
    thousand_digits.append(first_last_integer)
    

count = 1

for line in lines:
    print(count)
    get_first_last_digit_from_line(line)
    count += 1
    # print(line)

print(sum(thousand_digits))