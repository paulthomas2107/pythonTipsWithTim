words = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
word_counts = {}

for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

print(word_counts)
