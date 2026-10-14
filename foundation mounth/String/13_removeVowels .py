

'''
define removeVowels(s, n)
  set result as ""
  for i in 0 to n-1
      if s[i] != 'a' AND s[i] != 'e' AND s[i] != 'i' AND s[i] != 'o' And s[i] != 'u' 
          set result as result + s[i]
      end if
  end for
  return result
end define

start program 
   read s
   set n as len(s)
   set result__  removeVowels(s, n)
   print(result__)
end program
'''
