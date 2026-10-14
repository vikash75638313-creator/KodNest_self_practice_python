
''' 
define countEvensInArray(arr, n)
  set count as 0
  for i in 0 to n-1
    if arr[i] mod 2 = 0
       set count as count + 1
    end if
  end for
  return count
end define

start program
  read n
  set numbers as len(n)
  for i in 0 to n-1
     read numbers[i]
  end for
  set result as countEvensInArray(numbers, n)
  print(result)
end program
'''