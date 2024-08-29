# Listcomps, também conhecidos como list compreehension é a forma utilizada da sintaxe Python para criar listas

# exemplo de list comprehension
numbers = [number for number in range(1, 6)]

print(numbers)

# exemplo de list comprehension com condicional
evenNumbers = [number for number in range(1, 6) if number % 2 == 0]
print('even:')
print(evenNumbers)

# exemplo do for normal

numbers_for = []
for number in range(1, 6):
    numbers_for.append(number)
print()
print('for:')
print(numbers_for)