# Reverse the array
# https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/


orignal_list = [1,2,3,4,5,6]
start = len(orignal_list) - 1
reversed_list = [orignal_list[i] for i in range(start, -1, -1)]
print(f"orignal list: {orignal_list}")
print(f"reversed list: {reversed_list}")
