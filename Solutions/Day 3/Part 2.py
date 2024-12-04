INPUT = "Inputs\\Day 3.txt"

import re

def main():
    regex = r"mul\(\d{1,3}\,\d{1,3}\)"
    enableRe = r"do\(\)"
    disableRe = r"don't\(\)"

    with open(INPUT, 'r') as file:
        lines = file.readlines()
        total = 0
        for line in lines:
            while True:
                enable_match = re.search(enableRe, line)
                disable_match = re.search(disableRe, line)
                if not disable_match:
                    break
                if not enable_match:
                    line = line[:disable_match.start()]
                    break
                if enable_match.start() > disable_match.start():
                    line = line[:disable_match.start()] + line[enable_match.end():]
                else:
                    break

            matches = re.findall(regex, line)
            for match in matches:
                nums = match.split("(")[1].split(")")[0].split(",")
                result = int(nums[0]) * int(nums[1])
                total += result
        print(total)

if __name__ == "__main__":
    main()