"""
Write a method to replace all spaces in a string with ‘%20’.
"""


REPLACE_STRING = "%20"


# Time Complexity = O(n)
# Space Complexity = O(1)
def replace_space(string):
    return string.replace(" ", REPLACE_STRING)


print(replace_space("Hello word! How's it going?"))
