
'''
DEFINE countOf(s, n, target)
  set count as 0
  for i in 0 to n-1
     if s[i] = target
       set count as count + 1
     end if
  end for
  return count
end define

DEFINE areAnagrams(s1, n1, s2, n2)
  if n1 != n2
     return false
  end if
  for i in 0 to n1 - 1 
      set c1 as countOf(s1, n1, s1[i]) 
      set c2 as countOf(s2, n2, s1[i])
      if c1 != c2
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
  set result_ as areAnagrams(s1, n1, s2, n2)
  print(result_)
end program
'''
