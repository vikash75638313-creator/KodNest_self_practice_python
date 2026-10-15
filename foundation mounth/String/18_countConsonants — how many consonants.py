'''
define countConsonants(s,n)
  set count as 0
  for i in 0 to n-1
    if s[i] >= 'a' AND s[i] <= 'z'
      if s[i] !='a' and s[i] != 'e' and s[i] != 'i' and s[i] != 'o' and s[i] != 'u' 
       set count as count + 1
      end if
    end if
  end for
  return count
end define

start program 
  read s
  set n as len(s)
  set result as countConsonants(s,n)
  print(result)
end program
'''
