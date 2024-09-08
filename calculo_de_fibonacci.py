fibonacci = []

x = 0
y = 1

num = int(input('Digite um número: '))

for _ in range(num):
    fibonacci.append(x)
    fibonacci.append(y)
    soma = x + y
    x = soma
    y = soma + y

if (num in fibonacci):
    print(f'O número {num} está na sequência de Fibonacci')
else:
    print(f'O número {num} não está na sequência de Fibonacci')