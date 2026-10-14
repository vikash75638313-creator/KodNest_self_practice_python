'''
DEFINE countAboveAverage(arr, n)
  set total as 0
  for i in 0 to n-1
     set total as total + arr[i]
  end for
  set average as total/n

  set count as 0
  for i in 0 to n-1
    if arr[i] > average
       set count as count + 1
    end if
  end for
  return count
end define

start program
  read n
  set marks as len(n)
  for i in 0 to n-1
     read marks[i]
  end for
  set result as countAboveAverage(marks, n)
  print(result)
end program
'''
