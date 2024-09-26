print('Hello world!')
print('九九乘法表：')
for i in range(1, 10):
    for t_count in range(1, i):
        print(end='         \t')
    for j in range(i, 10):
        print(f'{i} * {j} = {i * j}', end='\t')
        if j == 9:
            print(end='\n')


print('Hello world!')
print('九九乘法表：')
for i in range(1, 10):
    for j in range(i, 10):
        print(f'{i} * {j} = {i * j}', end='\t')
        if j == 9:
            print(end='\n')