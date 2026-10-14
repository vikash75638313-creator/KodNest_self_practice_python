def  sumOfArray(arr,n):
    total = 0
    for i in range(n):
        total = total + arr[i]
    return total 

n = int(input("Enter The number:"))  

prices_ = []
for i in range(n):
    prices = int(input("Enter The price:"))
    prices_.append(prices)
    
result = sumOfArray(prices_,n) 
print(f"Final Sum: {result}")   


# Question ka simple meaning
# Ek shopping cart mein items ke prices diye jayenge.
# Hume sabhi prices ko add karke total bill nikalna hai.

# define sumOfArray(arr, n)
#   set total as 0
#   for i in 0 to n-1
#      set total as total + arr[i]
#   end for 
#   return total
# end define
 
# start program
#   read n 
#   set prices as len(n)
#   for i in 0 to n-1
#     read prices[i]
#   end for
#   set result as sumOfArray(prices, n)
#   print(result)
# end program