INPUT = "Inputs\\Day 8.txt"

import itertools

matrix_dimensions = [0, 0]
antenna_positions = {}
nodes = {}

def main():
    with open(INPUT, 'r') as file:
        lines = file.readlines()
        matrix_dimensions[0] = len(lines)
        matrix_dimensions[1] = len(lines[0].strip())
        for y, line in enumerate(lines):
            for x, char in enumerate(line.strip()):
                if char != ".":
                    if char not in antenna_positions:
                        antenna_positions[char] = []
                    antenna_positions[char].append((x, y))
    
    for key in antenna_positions:
        combos = itertools.combinations(antenna_positions[key], 2)
        for combo in combos:
            x_diff = combo[0][0] - combo[1][0]
            y_diff = combo[0][1] - combo[1][1]
            if combo[0][0] + x_diff >= 0 and combo[0][0] + x_diff < matrix_dimensions[1] and combo[0][1] + y_diff >= 0 and combo[0][1] + y_diff < matrix_dimensions[0]:
                nodes[(combo[0][0] + x_diff, combo[0][1] + y_diff)] = True
            if combo[1][0] - x_diff >= 0 and combo[1][0] - x_diff < matrix_dimensions[1] and combo[1][1] - y_diff >= 0 and combo[1][1] - y_diff < matrix_dimensions[0]:
                nodes[(combo[1][0] - x_diff, combo[1][1] - y_diff)] = True
    print(len(nodes))


if __name__ == "__main__":
    main()