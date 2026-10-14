

'''
define reverseString(s, n)
  set result as ""
  for i in n-1 to 0
     set result as result + s[i]
  end for
  return result
end define

start program
  read s
  set n as len(s)
  set result__ as reverseString(s, n)
  print(result__)
end program
'''
