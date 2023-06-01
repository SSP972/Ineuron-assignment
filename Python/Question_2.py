from collections import Counter

def is_valid_string(s):
    freq = Counter(s)  # Count the frequency of each character in the string

    # Count the frequency of frequencies
    freq_count = Counter(freq.values())

    if len(freq_count) == 1:
        # If all characters have the same frequency, the string is valid
        return "YES"
    elif len(freq_count) == 2:
        # If there are two different frequencies, check if removing one character can make the string valid
        freq_values = list(freq_count.values())
        freq_keys = list(freq_count.keys())
        
        if (freq_values[0] == 1 and freq_keys[0] == 1) or (freq_values[1] == 1 and freq_keys[1] == 1):
            # If one of the frequencies is 1, removing one character can make the string valid
            return "YES"

    return "NO"  # If none of the conditions are met, the string is not valid





# test case 1
s = "abc"
print('test case 1')
print(is_valid_string(s))  # Output: YES

# test case 2
s = "abcc"
print('test case 2')
print(is_valid_string(s))  # Output: NO

# test case 3
s = "aabbccdd"
print('test case 3')
print(is_valid_string(s))  # Output: YES
# Explanation: In this case, all characters have the same frequency (2), so the string is valid.

# test case 4
s = "a"*10**6
print('test case 4')
print(is_valid_string(s))  # Output: YES
# Explanation: In this case, removing the character 'x' will make the remaining characters have the same frequency (2), so the string is valid.
