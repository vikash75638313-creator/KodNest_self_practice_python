'''
define countUppercase(s,n)
  set count as 0
  for i in 0 to n-1
    if s[i] >= 'A' AND s[i] <= 'Z'
      set count as count + 1
    end if
  end for
  return count
end define

start program
  read s
  set n as len(s)
  set result as countUppercase(s,n)
  print(result)
end program
'''
