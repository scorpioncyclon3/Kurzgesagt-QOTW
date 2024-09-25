from get_outputs import split_into_pairs

def find_longest_chain(nums):
    outputs = set()
    outputs = split_into_pairs(nums, outputs)
    to_remove = set()

    # cleans up the set
    # remove items that are not positive integers
    for item in outputs:
        if item <= 0:
            to_remove.add(item)
        elif int(item) != item:
            to_remove.add(item)
    for item in to_remove:
        outputs.remove(item)
    del to_remove
    # converts everything to an integer (in case it's 3.0)
    for item in outputs:
        outputs.remove(item)
        outputs.add(int(item))

    # sorts and prints the outputs
    new = list(outputs)
    new.sort()
    print(new)

    # gets the longest unbroken chain
    count = 0
    unbroken = True
    while unbroken:
        count += 1
        if not count in outputs:
            unbroken = False
    return(count - 1)
