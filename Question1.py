# # # Question 1: -
# # # Write a program that takes a string as input, and counts the frequency of each word in the string, there might
# # # be repeated characters in the string. Your task is to find the highest frequency and returns the length of the
# # # highest-frequency word.
# # # Note - You have to write at least 2 additional test cases in which your program will run successfully and provide
# # # an explanation for the same.
# # # Example input - string = “write write write all the number from from from 1 to 100”
# # # Example output - 5
# # # Explanation - From the given string we can note that the most frequent words are “write” and “from” and
# # # the maximum value of both the values is “write” and its corresponding length is 5

def highest_frequency_word_length(string):
    words = string.split()
    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    max_frequency = max(word_counts.values())
    max_length = 0

    for word, frequency in word_counts.items():
        if frequency == max_frequency and len(word) > max_length:
            max_length = len(word)

    return max_length



# test case1
string = "write write write all the number from from from 1 to 100"
print(string)
print('1)',highest_frequency_word_length(string)) 

#  test case 2
string = "a a a b b c c c c"
print(string)
print('2)',highest_frequency_word_length(string))   

#test case 3
string = "hello world hello world hello world hello"
print(string)
print('3)',highest_frequency_word_length(string)) 
