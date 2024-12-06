INPUT = "Inputs\\Day 4.txt"

cannot_before = {}

def main():
    with open(INPUT, 'r') as file:
        lines = file.readlines()
        total = 0
        for line in lines:
            if line == "\n":
                continue
            if line[2] == "|":
                key = line[0:2]
                if key not in cannot_before:
                    cannot_before[key] = []
                cannot_before[key].append(line[-3:-1])
            elif line[2] == ",":
                valid = True
                for number in reversed(line.strip().split(",")):
                    infront = line[0:line.index(number)]
                    if number not in cannot_before:
                        continue
                    for not_allowed in cannot_before[number]:
                        if not_allowed in infront:
                            valid = False
                            break
                    if not valid:
                        break
                if valid:
                    total += int(line.split(",")[len(line.split(","))//2])
        print(total)





if __name__ == "__main__":
    main()