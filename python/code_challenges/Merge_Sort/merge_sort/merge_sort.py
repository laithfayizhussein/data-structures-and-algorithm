def Mergesort(arr):
  n=len(arr)

  if n > 1:
    mid = n//2
    left = arr[0:mid]
    right = arr[mid:n]

    Mergesort(left)
    Mergesort(right)
    Merge(left, right, arr)

  return arr

def Merge(left,right,arr):
  i=0 ,j=0,n=0

  while i < len(left) and j<len(right):
    if left[i] <= right[j]:
      arr[n] = left[i]
      i=i+1
    else:
      arr[n]=right[j]
      j=j+1
      n=n+1
  while i < len(left):
    arr[n] = left[i]
    i += 1
    n += 1
  while j<len(right):
    arr[n] = right[j]
    j += 1
    n += 1
