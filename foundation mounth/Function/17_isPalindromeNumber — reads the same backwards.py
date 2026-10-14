'''
define isPalindromeNumber(number)
  set original as number
  set reversed as 0
  while number > 0
    set lastDigit as lastDigit = number % 10
    set reversed as reversed = reversed  * 10 + lastDigit
    set number as number / 10
  end while
  if reversed = original
    return true
  otherwise
    return false
  end if
end define

start program
  read number
  set result as isPalindromeNumber(number)
  print(result)
end program
'''
