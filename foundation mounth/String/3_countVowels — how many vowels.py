

'''
define countVowels(s, n)
   set count as 0
   for i in 0 to n-1
     if s[i] = 'a' or s[i] = 'e' or s[i] = 'i' or s[i] = 'o' or s[i] =  'u'
        set count as count + 1
     end if      
   end for
   return count
end define

start program 
  read s
  set n as len(s)
  set result as countVowels(s, n)
  print(result)
end program
'''
