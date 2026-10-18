
'''
define lastPositionOf(s, n, target)
  for i in n-1 to 0
    if s[i] = target
      return i
    end if
  end for
  return -1
end define

start program
  read s
  read target
  set n as len(s)
  set result as lastPositionOf(s, n, target)
  print(result)
end program
'''



