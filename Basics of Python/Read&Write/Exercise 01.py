# Open the file "poem.txt" in read mode
with open("E:\\data\\funny.txt", "r") as file:
    # Read the contents of the file
    contents = file.read()

# Split the contents into words
words = contents.split()

# Create an empty dictionary to store the word frequencies
word_freq = {}

# Iterate over each word in the words list
for word in words:
    # If the word is already in the word_freq dictionary, increment its count
    if word in word_freq:
        word_freq[word] += 1
    # If the word is not in the dictionary, add it with a count of 1
    else:
        word_freq[word] = 1

# Find the maximum frequency
print(word_freq)
max_freq = max(word_freq.values())

# Create a list of words with the maximum frequency
max_words = [word for word, freq in word_freq.items() if freq == max_freq]

# Print the list of words with the maximum frequency
print('Words with maximum occurrence:', max_words)
