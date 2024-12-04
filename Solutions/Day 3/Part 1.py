INPUT = "Inputs\\Day 3.txt"

import re

def main():
    regex = r"mul\(\d{1,3}\,\d{1,3}\)"

    with open(INPUT, 'r') as file:
        lines = file.readlines()
        total = 0
        for line in lines:
            matches = re.findall(regex, line)
            for match in matches:
                nums = match.split("(")[1].split(")")[0].split(",")
                result = int(nums[0]) * int(nums[1])
                total += result
        print(total)



if __name__ == "__main__":
    main()