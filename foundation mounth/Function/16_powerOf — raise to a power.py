
'''
define powerOf(base, exponent)
  set result as 1
  for i in 1 to  exponent
     set result as result * base
  end for
  return result
end define

start program
  read base
  read exponent
  set result_ as powerOf(base,exponent)
  print(set result_)
end program
'''
