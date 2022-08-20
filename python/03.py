numList = []
def read():
    with open("03_input.txt") as file:
        data = file.read().splitlines()
        for num in data:
            numList.append(num)

read()

gammaRate = []
epsilonRate = []


def part1():
    for column in range(0, len(numList[0])):
        zeros = 0
        ones = 0
        for bitString in numList:
            if bitString[column] == '0':
                zeros+=1
            if bitString[column] == '1':
                ones+=1  
        # print("Zeros in column: " + str(column) + " are " + str(zeros))       
        # print("Ones in column: " + str(column) + " are " + str(ones))     
        # print("Checking, total is " + str(ones + zeros))  
        if zeros>ones:
            gammaRate.append(0)
            epsilonRate.append(1)
        else:
            gammaRate.append(1)
            epsilonRate.append(0)

part1()

gammaStr =""
epsilonStr =""

#converting a list to a string
for ele in gammaRate:
    gammaStr+=str(ele)

for ele in epsilonRate:
    epsilonStr+=str(ele)

#converting to decimal
# print(gammaRate)
print(int(gammaStr,2) * int(epsilonStr,2))
# print(epsilonRate)

numListFiltered =[]
def part2():
    # for column in range(0, len(numList[0])):
    #     zeros = 0
    #     ones = 0
    #     for bitString in numList:
    #         if bitString[column] == '0':
    #             zeros+=1
    #         if bitString[column] == '1':
    #             ones+=1   
    #     if zeros>ones:
    #         numListFiltered.append(bitString)
    #     else:

        
    # return 0
    pass

part2()

