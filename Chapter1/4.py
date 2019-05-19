"""
Write a method to decide if two strings are anagrams or not
"""


# Time Complexity = O(n)
# Space Complexity = O(2n)
def are_anagrams(string1, string2):

    if len(string1) != len(string2):
        return False

    string1_char_count = {}
    string2_char_count = {}

    for char in string1:
        if char not in string1_char_count.keys():
            string1_char_count[char] = 0
        else:
            string1_char_count[char] = string1_char_count[char] + 1

    for char in string2:
        if char not in string2_char_count.keys():
            string2_char_count[char] = 0
        else:
            string2_char_count[char] = string2_char_count[char] + 1

    for char in string1_char_count.keys():
        if char not in string2_char_count.keys():
            return False
        elif string1_char_count[char] != string2_char_count[char]:
            return False

    return True


print(are_anagrams("stab", "bats"))
