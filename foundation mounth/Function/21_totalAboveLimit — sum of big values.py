

'''
define totalAboveLimit(arr, n, limit)
  set total as 0
  for i in 0 to n-1
     if arr[i] > limit
        set total as total + arr[i]
     end if
  end for
  return total
end define

start program 
  read n
  set orders as len(n)
  for i in 0 to n-1
    read orders[i]
  end for
  read limit
  set result as totalAboveLimit(orders, n, limit)
  print(result)
end program
'''
