'''
define lowestArray(arr, n)
  set lowest as arr[0]
  for i in 1 to n-1
    if arr[i] < lowest
       set lowest as arr[i]
    end if
  end for
  return lowest
end define

start program
  read n
  set prices as len(n)
  for i in 0 to n-1
    read prices[i]
  end for
  set result as  lowestArray(prices, n)
  print(result)
end program
'''
