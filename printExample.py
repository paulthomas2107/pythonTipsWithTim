numbers = [1, 2, 3, 4, 5]

print("Default: ")
print(*numbers)

print("\nPrint with diff separators: ")
print(*numbers, sep='-')

print("\nPrint with diff end chars: ")
print(*numbers, end=" <=== End of numbers")

print("\nPrint with diff start & end chars: ")
print(*numbers, sep='=>', end=" <=== End of numbers")
