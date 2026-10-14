

'''
define isLeapYear(year)
  if year % 400 == 0
     return true
  otherwise if year % 100  == 0
     return false
  otherwise if year % 4  == 0
     return true
  otherwise 
     return false
  end if
end define

start program
  read year
  set result as isLeapYear(year)
  print(result)
end program
'''
