# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(A, B):
    merged_arr = []
    # TO-DO
    while len(A) + len(B) > 0:
      if len(A) == 0:
        merged_arr.append(B.pop(0))
      elif len(B) == 0:
        merged_arr.append(A.pop(0))
      else:
        if A[0] < B[0]:
          merged_arr.append(A.pop(0))
        else:
          merged_arr.append(B.pop(0))
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(l):
    A, B = l[:len(l)//2], l[len(l)//2:]
    while len(A) > 1 or len(B) > 1:
        return merge(merge_sort(A), merge_sort(B))
    return merge(A,B)


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
