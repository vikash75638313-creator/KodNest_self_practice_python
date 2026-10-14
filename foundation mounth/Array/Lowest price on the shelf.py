prices = [120,80,200,50,95]

lowest = prices[0]
for i in range(1,len(prices)):
    if prices[i] < lowest:
        lowest = prices[i]
        
print(f"Lowest prices:{lowest}")        




# SET lowest to prices[0]
# FOR each i from 1 to n - 1
#     IF prices[i] < lowest
#         SET lowest to prices[i]
#     END IF
# END FOR
# PRINT lowest