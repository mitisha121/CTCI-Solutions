"""
Assume you have a method isSubstring which checks if one word is a substring of
another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using
only one call to isSubstring (i.e., “waterbottle” is a rotation of “erbottlewat”).
"""


# Time Complexity = O(n)
# Space Complexity = O(n)
def is_substring(string1, string2):

    if string2 in string1:
        return True

    if len(string1) != len(string2):
        return False

    unique_chars = set(string1)

    for i in range(len(string1)):
        if string1[i] in unique_chars:
            first_unique_char = string1[i]
            first_unique_char_index = i
            break

    index_of_first_unique_char_in_string2 = string2.index(first_unique_char)
    rotation = abs(first_unique_char_index - index_of_first_unique_char_in_string2)
    length_of_string = len(string1)

    if string1[length_of_string-rotation:] + string1[:length_of_string-rotation] == string2:
        return True

    return False


print(is_substring("waterbottle", "erbottlewat"))
