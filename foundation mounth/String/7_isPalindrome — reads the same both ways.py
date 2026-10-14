'''
define ispalindrom(s, n)
  set i as 0
  set j as n-1
  while i < j
     if s[i] != s[j]
        return false
     end if
     i++
     j--
  end while
  return true
end define

start program
   read s
   set n as len(s)
   set result as ispalindrom(s, n)
   print(result)
end program
'''
