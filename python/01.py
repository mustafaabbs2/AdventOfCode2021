#Get data
# f = open("01_input.txt", "r")
# print(f.read())

with open("01_input.txt") as file:
    data = [int(line.rstrip()) for line in file]

# print(data)
# print(sum(data))

def part1():
    result = [firstNum < secondNum for firstNum, secondNum in zip(data, data[1:])]
    return sum(result)

def part2():
    allSums = [sum(tuples) for tuples in zip(data,data[1:],data[2:])]
    result = [firstSum < secondSum for firstSum, secondSum in zip(allSums, allSums[1:])]
    return sum(result);

# print(zip(data, data[1:]))

print(part1())
print(part2())


