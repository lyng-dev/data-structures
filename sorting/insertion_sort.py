def insertion_sort(arr):
  # start at idx 1, and move towards len(arr)
  for idx in range(1, len(arr)):
    # put current value in temp variable
    temp = arr[idx]
    # step to previous position
    pos = idx - 1

    # if previous position is inside a valid range
    while pos >= 0:
      # if the value at position is larger than current temp value, then shift position to the right
      if arr[pos] > temp:
        arr[pos + 1] = arr[pos]
        pos = pos - 1
      # otherwise stop comparing
      else:
        break

    # set the current position, which has been shifted, to the temp value
    arr[pos + 1] = temp
    #loop

  # return sorted array
  return arr

print(insertion_sort([10,4,9,2,7,4,0,-1]))