
def solution():
    print("Hello World")

    largestValue = 0

    with open("input.txt") as fp:
        data = fp.readlines()
        localMaximum = 0  # how much each elf is carrying
        for line in data:
            print(line)
            if line == "\n":
                if localMaximum > largestValue:
                    largestValue = localMaximum
                localMaximum = 0
            else:
                localMaximum += int(line)

    return largestValue


def solution_part_two():
    print("Hello World")

    largest_value = 0
    second_largest = 0
    third_largest = 0

    with open("input.txt") as fp:
        data = fp.readlines()
        local_maximum = 0  # how much each elf is carrying
        for line in data:
            # print(line)
            if line == "\n":
                if local_maximum > largest_value:
                    third_largest = second_largest
                    second_largest = largest_value
                    largest_value = local_maximum
                elif local_maximum > second_largest:
                    third_largest = second_largest
                    second_largest = local_maximum
                elif local_maximum > third_largest:
                    third_largest = local_maximum

                local_maximum = 0
            else:
                local_maximum += int(line)

    return largest_value + second_largest + third_largest


returnValue = solution()

print(returnValue)

returnValue = solution_part_two()

print(returnValue)
