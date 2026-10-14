
'''
define firstPositionOf(s, n, target)
   for i in 0 to n-1
      if s[i] = target
         return i
      end if
   end for
   return -1
end define

start program
  read s
  read target
  set n as len(s)
  set result as firstPositionOf(s, n, target)
  print(result)
end program
'''
