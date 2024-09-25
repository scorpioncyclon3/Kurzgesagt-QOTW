def split_into_pairs(nums, outputs):
    for num_1_index in range(0, len(nums)):
        for num_2_index in range(0, len(nums)):
            if num_1_index != num_2_index:
                outputs = perform_operations(nums, outputs, num_1_index, num_2_index)
    return(outputs)

def perform_operations(nums, outputs, num_1_index, num_2_index):
    for operation in range(0, 4):
        new_nums = nums.copy()
        # pop the number at the first index
        num_1 = new_nums.pop(num_1_index)
        # if the second number has been shifted left by a position, account for it
        if num_2_index > num_1_index:
            num_2 = new_nums.pop(num_2_index-1)
        # otherwise, pop the number at the second index
        else:
            num_2 = new_nums.pop(num_2_index)
        match operation:
            case 0:
                combined = num_1 + num_2
            case 1:
                combined = num_1 - num_2
            case 2:
                combined = num_1 * num_2
            case 3:
                # avoiding division by 0
                if num_2 != 0:
                    combined = num_1 / num_2
                else:
                    combined = None
        # ignore division by 0 cases
        if combined != None:
            # no more pairs to compute
            if len(new_nums) == 0:
                #print(combined)
                outputs.add(combined)
            # at least two numbers remaining to compute
            else:
                new_nums.append(combined)
                outputs = split_into_pairs(new_nums, outputs)
    return outputs
