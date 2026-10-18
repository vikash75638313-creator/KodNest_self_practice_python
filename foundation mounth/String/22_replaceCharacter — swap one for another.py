

'''
define replaceCharacter(s, n, oldChar, newChar)
  set result as ""
  for i in 0 to n-1
    if s[i] = oldChar
      set result as result + newChar
    otherwise 
      set result as result + s[i]
    end if
  end for 
  return result
end define

start program
  read s
  read oldChar
  read newChar
  set n as len(s)
  set result_ as replaceCharacter(s, n, oldChar, newChar)
  print(result_)
end program
'''