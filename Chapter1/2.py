"""
Write code to reverse a C-Style String. (C-String means that “abcd” is represented as
five characters, including the null character.)
"""


# Time Complexity = O(n)
# Space Complexity = O(1)
def reverse_c_style_string(string):
    return string[::-1]


print(reverse_c_style_string("abcd+"))
