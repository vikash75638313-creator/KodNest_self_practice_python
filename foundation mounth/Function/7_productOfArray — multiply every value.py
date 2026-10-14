def product_of_array(arr, n):
    product = 1

    for i in range(n):
        product = product * arr[i]

    return product


n = int(input("Enter The Number: "))

numbers = []

for i in range(n):
    number = int(input(f"Enter number {i}: "))
    numbers.append(number)

result = product_of_array(numbers, n)

print("Product:", result)  

# define productOfArray(arr, n)
#    set product as 1
#    for i in 0 to n-1
#      set product as product * arr[i]
#    end for
#    return product
# end define
# start program
#   read n
#   set numbers as len(n)
#   for i in 0 to n-1
#      read numbers[i]
#   end for
#   set result as  productOfArray(numbers, n)
#   print(result)
# end program