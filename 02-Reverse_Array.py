# 2 Reverse an array without using extra space. 

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

start = 0

end = len(arr) - 1

while start < end:
    #Swap the elements
    arr[start], arr[end] = arr[end], arr[start]
    
    # Move towards the center
    start += 1
    end -= 1

print("The reverse array is: " , arr)



# Alternative One-Liner Approach Python's built-in slicing
# arr = arr[::-1]  # This creates a new reversed list
# print("The reverse array is: " , arr)