

'''
DEFINE removeCharacter(s, n, target)
   set result as ""
   for i in 0 to n-1
       if s[i] != target
          set result as result + s[i]
       end if
   end for
   return result
end define

start program
  read s
  read target
  set n as len(s)
  set result as removeCharacter(s, n, target)
  print(result)
end program
'''
