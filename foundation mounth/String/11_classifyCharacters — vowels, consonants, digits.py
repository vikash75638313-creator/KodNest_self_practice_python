

'''
define classifyCharacters(s, n)
  set vowel as 0
  set consonants as 0
  set digits as 0
  for i in 0 to n-1
      if s[i]='a' OR s[i] = 'e' OR s[i] = 'i'OR s[i]= 'o' OR s[i] = 'u'
          set  vowel as vowel + 1 
           
      otherwise if s[i] >= 'a' AND s[i] <= 'z'
                set consonants as consonants + 1     
           
      otherwise if s[i] >= '0' AND s[i] <= '9' 
          set digits as digits + 1
          
      end if  
  end for
  print("Vowels:",vowel)
  print("consonants:",consonants)
  print("digits:",digits)
end define

start program
  read s
  set n as len(s)
  call classifyCharacters(s, n)
end program
'''
