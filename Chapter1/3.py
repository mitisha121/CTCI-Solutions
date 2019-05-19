"""
Design an algorithm and write code to remove the duplicate characters in a string
without using any additional buffer. NOTE: One or two additional variables are fine.
An extra copy of the array is not.
FOLLOW UP
Write the test cases for this method.
"""


def remove_duplicate_characters(string):

    unique_chars_count = len(set(string))

    for i in range(unique_chars_count):
        for j in range(unique_chars_count):
            if i != j and string[i] == string[j]:
                # REMOVE CHAR AT INDEX

    return string


remove_duplicate_characters("recepient")
