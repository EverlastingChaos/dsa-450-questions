# minimum number of jump to reach end of an array
# https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1


def min_jump(arr, n):
    if n == 1:
        return 0
    
    if arr[0] == 0:
        return -1
    
    jump = 1  # amount of jumps necessary to reach that position
    max_reach = arr[0]  # stores the maximal reachable position in the array
    step = arr[0]  # stores the amount of steps we can still take
    
    for i in range(1, n):
        if i == n - 1:
            return jump
        max_reach = max(max_reach, i + arr[i])
        step -= 1  # We used up a step to get to the current index, so steps has to be decreased. 
        
        # If no more steps are remaining i.e. steps=0, 
        # then we must have used a jump. Therefore increase jump. 
        # Since we know that it is possible somehow to reach maxReach, 
        # we initialize the steps to the amount of steps to reach maxReach from position i.
        if step == 0:
            if i >= max_reach:
                return -1
            jump += 1
            step = max_reach - i
            


arr = [1, 0, 0, 8]    
length = len(arr)
print(min_jump(arr, length))
    
