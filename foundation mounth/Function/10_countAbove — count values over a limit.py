def count_above(arr, n, limit):
  count = 0
  for i in range(n):
    if arr[i] > limit:
      count = count + 1
  return count

n = int(input("Enter the Number:"))
limit = int(input("Enter The limit: "))
marks_empthy = []
for i in range(n):
  marks_input = int(input("Enter The marks:"))
  marks_empthy.append(marks_input)
  
result = count_above(marks_empthy, n, limit)
print(f"final Count above: {result}")  

    
"""
define countAbove(arr, n, limit)
  set count as 0
  for i in 0 to n-1
    if arr[i] > limit
      set count as count + 1
    end if
  end for
  return count
end define

start program
  read n
  set marks as len(n)
  read limit
  for i in 0 to n-1
    read marks[i]
  end for
  set result as countAbove(marks, n, limit)
  print(result)
end program
"""
