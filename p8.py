def find_most_frequent_words(filename):
    with open(filename, 'r') as file:
        words = file.read().lower().split()
        word_freq = {}

        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1

        most_frequent_words = [word for word, freq in word_freq.items() if freq == max(word_freq.values())]
        return most_frequent_words, max(word_freq.values())

filename = 'C:\\Users\\Ananya Verma\\Desktop\\python 3011\\Tkinter\\test.txt'

result_words, result_frequency = find_most_frequent_words(filename)
print(f"Most frequent word(s): {result_words}")
print(f"Frequency: {result_frequency}")
