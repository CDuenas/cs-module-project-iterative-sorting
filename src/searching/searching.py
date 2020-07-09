def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        #look for a match
        if arr[i] == target:
            #return the index
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    #Start at First element
    begin_index = 0

    #End at last element
    end_index = len(arr) - 1

    #Start our loop

    while begin_index <= end_index:
        #find our midpoint by adding the beginning plus how many items remain in the list and dividing by 2
        midpoint = begin_index + (end_index - begin_index) // 2
        #return the value instead of the position
        midpoint_value = arr[midpoint]
        #if we find our target return that position
        if midpoint_value == target:
            return midpoint

        #If our target is to the left of the midpoint
        elif target < midpoint_value:
            #We change our endpoint to the left of the midpoint because we only need to 
            #search the beginning half of the list
            end_index = midpoint - 1

        #If our target is to the right of the midpoint
        else:
            #we change our beginning to the number to the right
            #because our target will only be after the midpoint
            begin_index = midpoint + 1

    return -1  # not found
