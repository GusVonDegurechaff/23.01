def remove_elements(sequence, n, values):
    for value in values:
        sequence = [x for x in sequence if x != value]
    return sequence
sequence = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
n = int(input("Введите количество запросов на удаление: "))
values = []
for _ in range(n):
    value = int(input("Введите значение для удаления: "))
    values.append(value)
result = remove_elements(sequence, n, values)
print(result)


