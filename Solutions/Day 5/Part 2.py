INPUT = "Inputs\\Day 5.txt"

cannot_before = {}

total = 0
def fix_order(line):
    nums = line.strip().split(",")
    newline = ""
    while len(nums) > 0:
        for num in nums:
            valid = True
            if num not in cannot_before:
                newline += num + ","
                nums.remove(num)
                break
            for not_allowed in cannot_before[num]:
                if not_allowed in nums:
                    valid = False
                    break
            if valid:
                newline += num + ","
                nums.remove(num)
                break
    global total
    total += int(newline[:-1].split(",")[len(newline[:-1].split(","))//2])

def main():
    with open(INPUT, 'r') as file:
        lines = file.readlines()
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
                            fix_order(line)
                            break
                    if not valid:
                        break
    print(total)





if __name__ == "__main__":
    main()