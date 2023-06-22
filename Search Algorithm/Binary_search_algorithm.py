# function that takes a list and target parameter
# multiple variables: middle, start, end, steps
# recursion or while loop
# increase steps each iteration is done
# condition to track target position

def binary_search(list, elements):
    middle = 0
    start = 0
    end =len(list)
    steps = 0

    while(start<=end):
        print("Steps",steps, ":" ,str(list[start:end+1]))
        steps = steps+1
        middle= (start+end)/2
