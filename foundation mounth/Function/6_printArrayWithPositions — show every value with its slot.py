def printArrayWithPosition(arr,n):
    for i in range(n):
        print(f"Position {i}: {arr[i]}")
        
prices = [120,80,200,50]   

printArrayWithPosition(prices,len(prices))
     




# DEFINE printArrayWithPositions(arr, n)
#    for i in 0 to n-1
#       print("Position" + i + ":" + arr[i])
#   end for
# end define
# start program
# read n
# set prices as len(n)
# for i in 0 to n-1
#   read prices[i]
# end for
# call printArrayWithPositions(prices, n)
# end program

""" 
| Step      | `i` |    Input/Value | Array                |
| --------- | --: | -------------: | -------------------- |
| Input `n` |   — |              4 | —                    |
| Fill      |   0 |            120 | `[120, _, _, _]`     |
| Fill      |   1 |             80 | `[120, 80, _, _]`    |
| Fill      |   2 |            200 | `[120, 80, 200, _]`  |
| Fill      |   3 |             50 | `[120, 80, 200, 50]` |
| Print     |   0 | `arr[0] = 120` | Position 0: 120      |
| Print     |   1 |  `arr[1] = 80` | Position 1: 80       |
| Print     |   2 | `arr[2] = 200` | Position 2: 200      |
| Print     |   3 |  `arr[3] = 50` | Position 3: 50       |

"""

