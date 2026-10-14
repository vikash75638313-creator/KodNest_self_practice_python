'''
define containsValue(arr, n, target)
  set flag as false
  for i in 0 to n-1
     if arr[i] = target
        set flag as true
     end if
  end for
  return flag
end define

start program
  read n
  set guests as len(n)
 
  for i in 0 to n-1
      read guests[i]   
  end for
  read target
  set result as containsValue(guests, n, target)
  print(result)
end program
'''
