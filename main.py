import re

def count_words(content):
    split_array = content.split()
    return len(split_array)    

def count_letters(content):
    lower_case =  content.lower()
    regex_match = re.findall("[a-z]", lower_case)

    letter_count = {}

    for match in regex_match:
        if match in letter_count:
            letter_count[match] = letter_count[match] + 1
        else:
            letter_count[match] = 1 

    return letter_count

with open("./books/frankenstein.txt") as book_file:
    file_content = book_file.read()

print(file_content)

print("==================")
word_count = count_words(file_content)
print("There are " + str(word_count))

letter_count = count_letters(file_content)
for value in letter_count:
    print("The '" + value + "' character was found " + str(letter_count[value]) + " times")
