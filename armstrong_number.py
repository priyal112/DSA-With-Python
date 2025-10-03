n = 153
num = n
total = 0
no_of_digit = len(str(n))

while num > 0:
    ld = num % 10
    total = total + ( ld ** no_of_digit)
    num = num // 10 
    
if (total == n):
        print("Armstrong Number")
    
else:
        print("Not Armstrong Number")