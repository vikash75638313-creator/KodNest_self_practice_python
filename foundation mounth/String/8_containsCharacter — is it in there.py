
'''
define containsCharacter(s, n, target)
   set found as false
   for i in 0 to n-1
       if s[i] = target
          set found as true
       end if
   end for
   return found
end define

start program
  read s
  read target
  set n as len(s)
  set result as containsCharacter(s, n, target)
  print(result)
end program
'''
