# TO-DO: Complete the selection_sort() function below 
def selection_sort(l):
  # loop through n-1 elements
  for i in range(len(l)-1):
      smallest_index = i
      # TO-DO: find next smallest element (hint, can do in 3 loc) 
      for j in range(i, len(l)):
        if l[j] < l[smallest_index]:
          smallest_index = j
      #swap
      l[i], l[smallest_index] = l[smallest_index], l[i]
  return l

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(l):
  swap = True
  while swap:
    swap = False
    for i in range(len(l)-1):
      if l[i] > l[i+1]:
        l[i], l[i+1] = l[i+1], l[i]
        swap = True
  return l


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr



def insertion_sort(l):
  for i in range(1, len(l)):
    j = i
    temp = l[j]
    while j > 0 and temp < l[j-1]:
      l[j] = l[j-1]
      j -= 1
    l[j] = temp
  return l