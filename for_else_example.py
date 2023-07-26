numbers = [1, 3, 5, 7, 9]
find = 7

for num in numbers:
    if num == find:
        print(f'Found {find} in list')
        break
else:
    print(f'Found {find} not in list')


count = 5
while count > 0:
    print(count)
    count -= 1
else:
    print("Lift off !")
