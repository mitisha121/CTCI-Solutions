"""
Implement an algorithm to determine if a string has all unique characters. What if
you can not use additional data structures?
"""


# With additional data structures
# Time Complexity = O(n)
# Space Complexity = O(n)
def has_unique_characters_with_ds(string):

    if len(string) <= 1:
        return False

    unique_chars = set(string)

    if len(string) != len(unique_chars):
        return True

    return False


# Without additional data structure
# Time Complexity = O(n^2)
# Space Complexity = O(1)
def has_unique_characters(string):

    if len(string) <= 1:
        return False

    for i in range(len(string)):
        for j in range(len(string)):
            if i != j and string[i] == string[j]:
                return True

    return False


print(has_unique_characters("part"))
