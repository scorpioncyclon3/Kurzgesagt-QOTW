from find_longest_chain import find_longest_chain

highes_nums = []
highest = 0
for d in range(4, 10):
    for c in range (3, d):
        for b in range(2, c):
            for a in range(1, b):
                nums = [a, b, c, d]
                hightest_from_nums = find_longest_chain(nums)
                if highest < hightest_from_nums:
                    highest_nums = nums
                    highest = hightest_from_nums

print("Set with longest unbroken chain: ", highest_nums)
print("Chain length: ", highest)
