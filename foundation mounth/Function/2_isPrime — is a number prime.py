def isPrime(number):
    for d in range(2,number):
        if number % d == 0:
            return False
        
    return True

num = int(input("Enter The Number:"))
result = isPrime(num)  
print(f"Result: {result}")  


# DEFINE isPrime(number)
#   for d in 2 to number-1
#     if number % d == 0
#        return false
#     end if
#   end for
#   return true
# end define
# start program
#  read num
#  set result as isPrime(num)
#  print(result)
# end program