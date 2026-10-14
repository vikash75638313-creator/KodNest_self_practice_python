marks = [80,90,70,60]

total = marks[0]
for i in range(1,len(marks)):
    total = total + marks[i]
    
average = total/len(marks)  
print(f"Avarage Marks is :{average:.2f}")


# set total as 0
# for i in 0 to n-1
#    set total as total + marks[i]
# end for
# set average as total/n
# print(average)