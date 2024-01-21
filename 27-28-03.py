def swap_min_max(sequence):
    numbers = list(map(int, sequence.split()))
    min_index = numbers.index(min(numbers))
    max_index = len(numbers) - 1 - numbers[::-1].index(max(numbers))
    numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]
    return " ".join(map(str, numbers))
input_sequence = input("Введите последовательность чисел через пробел: ")
result = swap_min_max(input_sequence)
print(result)