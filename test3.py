data = []
sum = 0
for i in range (99):
    while i > 1:
        digit = i % 10
        sum = sum + digit
        i = i // 10
        break
    if ( i % sum == 0):
        data.append(i)
print(data)


array = 
