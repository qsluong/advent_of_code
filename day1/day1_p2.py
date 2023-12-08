calibration_file = open("puzzle_input.txt", "r")

lines = calibration_file.readlines()

replaced_puzzle_input = []

thousand_digits = []

class NumberSpelledOut:
    def __init__(self, spelled_out, number):
        self.spelled_out = spelled_out
        self.number = number

number_spelled_out = [
    NumberSpelledOut("one",1),
    NumberSpelledOut("two",2),
    NumberSpelledOut("three",3),
    NumberSpelledOut("four",4),
    NumberSpelledOut("five",5),
    NumberSpelledOut("six",6),
    NumberSpelledOut("seven",7),
    NumberSpelledOut("eight",8),
    NumberSpelledOut("nine",9)
]

def get_first_last_digit_from_line(line: str):
    digits = []
    for s in line:
        if s.isdigit():
            digits.append(s)
            # print(s)
    print(digits)
    first_and_last = [digits[i] for i in (0, -1)]
    print(first_and_last)
    first_last_string = f"{first_and_last[0]}{first_and_last[1]}"
    first_last_integer = int(first_last_string)
    print(first_last_integer)
    thousand_digits.append(first_last_integer)

def replace_spelled_out_with_number_indexed(line: str):
    replaced = line
    print(f'Original: {replaced}')
    for nso in number_spelled_out:
        findex = replaced.find(nso.spelled_out)
        if findex > -1:
            replaced = replaced[ : findex + 1] + str(nso.number) + replaced[findex + 1 : ]
            print(f'FirstIndex: {replaced}')
        rindex = replaced.rfind(nso.spelled_out)
        if findex != rindex and rindex > -1: 
            replaced = replaced[ : rindex + 1] + str(nso.number) + replaced[rindex + 1: ]
            print(f'LastIndex: {replaced}')
        occurence = replaced.count(nso.spelled_out)
        print(f'Result: {replaced}')
        print(f'{nso.number} count: {occurence} on index: 1st: {findex}, last: {rindex}')
    return replaced.strip()

count_lines = 1

for line in lines:
    print(count_lines)
    replaced_line = replace_spelled_out_with_number_indexed(line)
    print(replaced_line)
    replaced_puzzle_input.append(replaced_line)
    count_lines += 1

print(replaced_puzzle_input)

count_replaced_lines = 1

for line in replaced_puzzle_input:
    # print(count_replaced_lines)
    get_first_last_digit_from_line(line)
    count_replaced_lines += 1

print(sum(thousand_digits))