marks = [62,88,45,91,78]

highest = marks[0]
position = 0

for i in range(1,len(marks)):
    if marks[i] > highest:
        highest = marks[i]
        position = i
        
print(f"Highest marks:{highest}")  
print(f"Position: {position}")      



# SET highest to marks[0]
# SET position to 0
# FOR each i from 1 to n - 1
#     IF marks[i] > highest
#         SET highest to marks[i]
#         SET position to i
#     END IF
# END FOR
# PRINT position
# PRINT highest