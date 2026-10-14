'''
define averageOfArray(arr, n)
  set total as 0
  for i in 0 to n-1
     set total as total + arr[i]
  end for
  set total as total / n
  return total
end define

start program
  read n
  set marks as len(n)
  for i in 0 to n-1
     read marks[i]
  end for
  set result as averageOfArray(marks, n)
  print(result)
end program
'''
