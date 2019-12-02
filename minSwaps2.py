def minimumSwaps(arr):
    ref_arr = sorted(arr)
    index_dict = {value: key for key, value in enumerate(arr)}
    print(index_dict)
    swaps = 0
    
    for index, value in enumerate(arr):
        # correct value is the sorted array value for the key
        correct_value = ref_arr[index]
        # if the value isn't in its sorted position
        if value != correct_value:
            # get the correct index from sorted array
            to_swap_ix = index_dict[correct_value]
            # swap correct index value with current index value
            arr[to_swap_ix],arr[index] = arr[index], arr[to_swap_ix]
            swaps += 1
            
    return swaps

myArr = [7,1,3,2,4,5,6]
print(minimumSwaps(myArr))