marks = [62,88,45,91,78]
highest = marks[0]

for i in range(1, len(marks)):
    if marks[i] > highest:
        highest =  marks[i]
        
print(f"Highest Makrs: {highest}")        
        
        
# SET highest to marks[0]
# FOR each i from 1 to n - 1
#     IF marks[i] > highest
#         SET highest to marks[i]
#     END IF
# END FOR
# PRINT highest        