def factorail(number):
    fact = 1
    for i in range(1,number+1):
        fact = fact*i
    return fact

num = int(input("Enter The Number: "))  
result = factorail(num)  
print(f"Factorial: {result}")




# DEFINE factorial(number)
#    set fact as 1
#    for i in 1 to number
#        set fact as fact*i
#    end for  
#    return fact
# end define

# start program
#  read num
#  set result as factorial(num)
#  print(result)