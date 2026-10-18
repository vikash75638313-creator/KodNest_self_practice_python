
'''
define firstPositionOf(s, n, target)
  for i in 0 to n-1
    if s[i] = target
      return i
    end if
  end for
  return -1
end define

define removeDuplicateCharacters(s, n) 
  set result as ""
  for i in 0 to n-1
    if i = firstPositionOf(s, n, s[i])
      set result as result + s[i]
    end if
  end for
  return result
end define

start program
  read s
  set n as len(s)
  set result as removeDuplicateCharacters(s, n)
  print(result)
end program
'''