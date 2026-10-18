


'''
define countDigitsInString(s,n)
  set count as 0
  for i in 0 to n-1
    if s[i] >= '0' AND s[i] <= '9'
      set count as count + 1
    end if
  end for
  return count
end define

start program
  read s 
  set n as len(s)
  set result as countDigitsInString(s,n)
  print(result)
end program
'''
