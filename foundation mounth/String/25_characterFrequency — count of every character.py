''' 
define countOf(s, n, target)
  set count as 0
  for i in 0 to n - 1
    if s[i] = target
      set count as count + 1
    end if
  end for
  return count
end define

define firstPositionOf(s, n, target)
  for i in 0 to n - 1
    if s[i] = target
      return i
    end if
  end for
  return -1
end define

define characterFrequency(s, n)
  for i in 0 to n - 1
    if i = firstPositionOf(s, n, s[i])
      set times as countOf(s, n, s[i])
      print(s[i] + ":" + times)
    end if
  end for
end define

start program
  read s
  set n as len(s)
  characterFrequency(s, n)
end program
'''
