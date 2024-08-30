fibonacci = []

x = 0
y = 1

z = int(input('Digite um valor de repetição: '))

for _ in range(z):
    fibonacci.append(x)
    fibonacci.append(y)
    soma = x + y
    x = soma
    y = soma + y

print(fibonacci)