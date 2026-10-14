def countDigits(number):
    count = 0
    while number > 0:
        number = number // 10
        count = count + 1
    return count

number = int(input("Enter The Numebr:")) 
result = countDigits(number) 
print(f"Total Count: {result}")  




# DEFINE countDigits(number)
#   set count as 0
#   while number > 0
#      set number as number // 10
#      set count as count+1
#   end while
#   return count
# end define

# start program
#  read number
#  set result as countDigits(number)
#  print(result)
# end program