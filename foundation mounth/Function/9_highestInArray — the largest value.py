def highestInArray(arr,n):
  highest = arr[0]
  
  for i in range(n):
    if arr[i] > highest:
     highest = arr[i]
  return highest

n = int(input("Enter The How many array: "))

marks_empthy = []

for i in range(n):
  marks_input = int(input("Enter the marks: ")) 
  marks_empthy.append(marks_input)
  
result = highestInArray(marks_empthy,n)
print(f"Final Heighest Array: {result}")    

"""
define highestInArray(arr,n)
  set highest as arr[0]
  for i in 0 to n-1
    if arr[i] > highest
      set highest as arr[i]
    end if
  end for
  return highest
end define

start program
  read n
  set marks as len(n)
  for i in 0 to n-1
    read marks[i]
  end for
  set result as highestInArray(marks,n)
  print(result)
end program
"""