

'''
define countSpace(s,n)
  set count as 0
  for i in 0 to n-1
      if s[i] = ' '
         set count as count + 1
      end if
  end for
end define

start program
  read s
  set n as len(s)
  set result as countSpace(s, n)
  print(result)
end program
'''
