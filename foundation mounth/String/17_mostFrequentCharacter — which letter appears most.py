
'''
define countOf(s, n, target)
  set count as 0
  for i in 0 to n-1
     if s[i] = target
       set count as count + 1
     end if
  end for 
  return count
end define

define mostFrequentCharacter(s, n)
  set bestChar as s[0]
  set bestCount as 0
  for i in 0 to n-1
    set count as countOf(s, n, s[i])
    if count > bestCount
       set bestCount as count 
       set bestChar as  s[i]   
    end if
  end for
  return bestChar
end define

start program
  read s
  set n as len(s)
  set result as mostFrequentCharacter(s, n)
  print(result)
end program
'''
