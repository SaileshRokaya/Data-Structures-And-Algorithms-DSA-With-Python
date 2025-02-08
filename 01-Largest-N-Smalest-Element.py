# 1) Find the largest and smallest element in an array.

# a) The largest element in an array.
arr = [30, 20, 15, 40, 10]

max_val = arr[0]

n = len(arr)

for i in range(1, n):
    if arr[i] > max_val:
        max_val = arr[i]

print("Largest element is:", max_val)

# b) The smallest element in an array.
arr = [30, 20, 15, 40, 10]

min_val = arr[0]

n = len(arr)

for i in range(1, n):
    if arr[i] < min_val:
        min_val = arr[i]

print("Smallest element is:", min_val)