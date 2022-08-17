dirList = []
stepList = []

with open("02_input.txt") as file:
        data = file.read().splitlines()
        for word in data:
            spl = word.split()
            dirList.append(spl[0])
            stepList.append(spl[1])


def part1():
    totalHor = 0
    totalDep = 0

    # List comprehension = ideal for this?
    # result = [totalHor+1 if hor =='forward'
    #                     else totalDep+1
    # for hor, dep in zip(dir,steps)]

    for dir, step in zip(dirList,stepList):
        if dir == 'forward':
            totalHor+=int(step)
        elif dir =='up':
            totalDep-=int(step)
        elif dir =='down':
            totalDep+=int(step)


    print(totalHor * totalDep)


# part1()

def part2():
    totalHor = 0
    totalDep = 0
    aim = 0

    for dir, step in zip(dirList,stepList):
        print(aim, totalDep, totalHor)
        if dir =='up':
            aim-=int(step)
        elif dir =='down':
            aim+=int(step)
        elif dir == 'forward':
            totalHor+=int(step)
            totalDep+=int(step)*aim

    print(totalHor * totalDep)

part2()
