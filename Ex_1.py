n = int(input('Задайте натуральное число N '))
result = []
for i in range(2, n + 1):
    while n % i == 0:
        result.append(i)
        n //= i
print(result)