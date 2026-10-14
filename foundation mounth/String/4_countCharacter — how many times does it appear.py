

'''
define countCharacter(s, n, target)
   set count as 0
   for i in 0 to n-1
      if s[i] = target
         set count as count + 1 
      end if
   end for
   return count
end define

start program 
  read s
  read target
  set n as len(s)
  set result as countCharacter(s, n, target)
  print(result)
end program
'''
