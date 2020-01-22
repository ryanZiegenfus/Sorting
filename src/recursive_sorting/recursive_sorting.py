# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    print(arrA, arrB)
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements

    index_M = 0
    index_A = 0
    index_B = 0

    for _ in range(0, elements):
        if index_A == len(arrA) and index_M < elements:
            merged_arr[index_M] = arrB[index_B]
            index_B += 1
            index_M += 1
        elif index_B == len(arrB) and index_M < elements:
            merged_arr[index_M] = arrA[index_A]
            index_A += 1
            index_M += 1
        elif arrA[index_A] <= arrB[index_B]:
            merged_arr[index_M] = arrA[index_A]
            index_A += 1
            index_M += 1
        elif arrB[index_B] <= arrA[index_A]:
            merged_arr[index_M] = arrB[index_B]
            index_B += 1
            index_M += 1


    # # TO-DO
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        A = arr[:mid]
        B = arr[mid:]
        return merge(merge_sort(A), merge_sort(B))
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr

merge([4], [8])
merge([1, 2, 9], [3, 4, 7])
merge([1, 3, 5, 8, 16, 19], [3, 4, 7, 10, 12, 17])