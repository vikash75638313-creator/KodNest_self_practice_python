
'''
define countWords(s, n)
   set spaces as 0
   for i in 0 to n-1
      if s[i] = ' '
          set spaces as spaces + 1
      end if
   end for
   return spaces + 1
end define

start program
  read s
  set n as len(s)
  set result as countWords(s, n)
  print(result)
end program
'''
