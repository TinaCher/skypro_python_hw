lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
total_sum = sum(lst)
print(total_sum)



lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
total_sum = 0
for number in lst:
    total_sum += number

print("Sum of all elements:", total_sum)