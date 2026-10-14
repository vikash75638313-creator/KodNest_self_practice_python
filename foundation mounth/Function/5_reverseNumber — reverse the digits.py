def reverseNumber(number):
    reversed = 0
    while number > 0:
        last_digit = number % 10
        reversed = reversed * 10 + last_digit
        number = number // 10
    return reversed
number = int(input("Enter The number: "))
result = reverseNumber(number)    
print(f"Final Reversed Number: {result}")


# define reverseNumber(number)
#   set reversed as 0
#   while number > 0  
#   set lastDigit as number % 10
#   set reversed as reversed * 10 + lastDigit
#   set number as number / 10
#   end while
#   return reversed
# start program
#  read number
#  set result as reverseNumber(number)
#  print(result)
# end program


"""
Bilkul. Revision ke liye **copy-paste friendly dry-run table** bana deta hoon. Example input `1234` lete hain.

### Dry Run — `reverseNumber(1234)`

```text
INPUT:
number = 1234

FUNCTION CALL:
reverseNumber(1234)

INITIAL:
reversed = 0
```

| Iteration | number (before) | last_digit = number % 10 | reversed = reversed * 10 + last_digit | reversed (after) | number = number // 10 |
| --------- | --------------: | -----------------------: | ------------------------------------: | ---------------: | --------------------: |
| 1         |            1234 |                        4 |                            0 × 10 + 4 |                4 |                   123 |
| 2         |             123 |                        3 |                            4 × 10 + 3 |               43 |                    12 |
| 3         |              12 |                        2 |                           43 × 10 + 2 |              432 |                     1 |
| 4         |               1 |                        1 |                          432 × 10 + 1 |             4321 |                     0 |

### Loop condition

```text
number = 0

while number > 0
0 > 0 → False

Loop STOP
```

### Return

```text
return reversed

reversed = 4321

result = 4321
```

### Final Output

```text
Final Reversed Number: 4321
```

---

### 🔑 Revision Notes

```text
1. number % 10
   → last digit nikalta hai

2. reversed * 10 + last_digit
   → reverse number banata hai

3. number // 10
   → original number ka last digit remove karta hai

4. while number > 0
   → jab tak number mein digits hain, loop chalega
```

### Ek line mein pura logic

```text
1234
 ↓ %10 → 4       reversed = 4
 ↓ //10 → 123

123
 ↓ %10 → 3       reversed = 43
 ↓ //10 → 12

12
 ↓ %10 → 2       reversed = 432
 ↓ //10 → 1

1
 ↓ %10 → 1       reversed = 4321
 ↓ //10 → 0

STOP → 4321
```

Ye table tum directly **VS Code ki `.txt` file ya Python comments** mein revision ke liye rakh sakte ho.

"""
