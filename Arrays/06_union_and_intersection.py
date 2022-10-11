# find union and intersection of two arrays
# https://www.geeksforgeeks.org/union-and-intersection-of-two-sorted-arrays-2/


def do_union(arr1, arr2):
    union_set = set()
    for i in arr1:
        union_set.add(i)
    
    for i in arr2:
        union_set.add(i)

    for s in union_set:
        print(s, end = " ")


def do_intersection(arr1, arr2):
    intersection_set = set()
    if len(arr1) < len(arr2):
        for i in arr1:
            if i in arr2:
                intersection_set.add(i)
    else:
        for i in arr2:
            if i in arr1:
                intersection_set.add(i)
    
    for s in intersection_set:
        print(s, end=" ")


if __name__ == '__main__':
    arr1 = [1, 2, 4, 5, 6]
    arr2 = [2, 3, 5, 7]
    do_union(arr1, arr2)
    print()
    do_intersection(arr1, arr2)
