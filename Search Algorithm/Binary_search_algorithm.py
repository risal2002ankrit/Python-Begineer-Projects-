# function that takes a list and target parameter
# multiple variables: middle, start, end, steps
# recursion or while loop
# increase steps each iteration is done
# condition to track target position

def binary_search(list, elements):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while(start <= end):
        print("Steps", steps, ":", str(list[start:end+1]))

        steps = steps+1
        middle= int((start+end)/2)

        if elements == list[middle]:
            return middle
        if elements < list[middle]:
            end = middle-1
        else:
            start = middle + 1

    return -1

my_list = [1,2,3,4,5,6,7,8,9]
target = 6

binary_search(my_list, target)

