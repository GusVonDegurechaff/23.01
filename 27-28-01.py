def words_in_lexicographic_order(input_string):
    words = input_string.split()
    words.sort()
    for word in words:
        print(word)
input_string = input("Введите строку с произвольным количеством слов, разделенных пробелом: ")
words_in_lexicographic_order(input_string)

