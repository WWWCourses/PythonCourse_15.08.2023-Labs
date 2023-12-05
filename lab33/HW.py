# --------------------------------- Homework --------------------------------- #
# From the given `text`, get list (`matched_words`) of all "words" which starts
# and ends with same symbol.
#
# Note: a word is a string in `text`, separated by spaces
#
# ------------------------------------- - ------------------------------------ #
import re

# GIVEN:
text = """
kjjkdjfd madam kjjkdjfd
jksjdk@abc@345jk 1abc1 fdskj
!ok! @abc@
a434#)43a
"""

# YOUR CODE HERE


# TEST:
print(matched_words)

# EXPECTED OUTPUT:
['madam', '1abc1', '!ok!', '@abc@', 'a434#)43a']