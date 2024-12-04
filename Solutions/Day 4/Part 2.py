INPUT = "Inputs\\Day 4.txt"

def checkAllAdjacentFor(target, x, y, array, directions):
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(array[0]) and 0 <= ny < len(array) and array[ny][nx] == target:
            if target == "M":
                if checkAllAdjacentFor("S", x, y, array, [(-dx, -dy)]):
                    return True
            elif target == "S":
                return True
    return False


def main():
    fileArray = []
    total = 0
    directions = [(-1, -1), (1, -1), (-1, 1), (1, 1)]
    with open(INPUT, 'r') as file:
        lines = file.readlines()
        for line in lines:
            fileArray.append(list(line.strip()))
    for y, line in enumerate(fileArray):
        for x, char in enumerate(line):
            if char == "A":
                successes = []
                for direction in directions:
                    if checkAllAdjacentFor("M", x, y, fileArray, [direction]):
                        successes.append(direction)
                if len(successes) >= 2 and successes[0] != (-successes[1][0], -successes[1][1]):
                    total += 1
    print(total)




if __name__ == "__main__":
    main()