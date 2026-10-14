
'''
define sumOfDigits(number)
      set sum as 0
      while number > 0
         set last_digit as number mod 10
         set sum as sum + last_digit
         set number as number / 10
     end while
     return sum
end define

start Program
  read num
  set result as sumOfDigits(num)
  print(result)
end program
'''
