
'''
define stringsAreEqual(s1, n1, s2, n2)
  if n1 != n2
    return false
  end 
  for i in 0 to n1 - 1
    if s1[i] != s2[i]
      return false
    end if
  end for
  return true
end define

start program
  read s1
  read s2
  set n1 as len(s1)
  set n2 as len(s2)
  set result as stringsAreEqual(s1, n1, s2, n2)
  print(result)
end program
'''
