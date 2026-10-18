
'''
define isAllDigits(s, n)
  for i in 0 to n - 1
    if s[i] < '0' or s[i] > '9'
      return false 
    end if
  end for
  return true
end define

start program
  read s
  set n as len(s)
  set result as isAllDigits(s, n)
  print(result)
end program
'''
