
'''
define isVowelHeavy(s, n)
  set vowels as vowels 0
  set consonant as consonant 0 
  for i in 0 to n-1
    if s[i] = 'a' or s[i] = 'e' or s[i] = 'i' or s[i] = 'o' or s[i] = 'u' 
      set vowels as vowels + 1
    otherwise if s[i] >= 'a' AND s[i] <= 'z'
      set consonant as consonant + 1  
    end if    
  end for
  if vowels > consonant
    return true
  else 
    return false
  end if
end define 

start program
  read s
  set n as len(s)
  set result as isVowelHeavy(s, n)
  print(result) 
end program
'''
