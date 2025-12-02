
def is_palin(any_string: str) -> bool:
    return any_string == any_string[::-1]
    
print(is_palin("racerrcar"))

# ? - 0 or 1 maximum
# * - 0 or any number of previous character or expression
# + - 1 or any
# . - will match anything and everything. (if h. then it will match h<with one character after this>)
# h. - h followed by any one single character.
# a followed by b and b followed by c - following pattern is very very important.

#\w = [a-zA-Z0-9_]

import re
s = "12347899 abc@123.com  xyz@123.com1234  def@123.com"
#result = re.findall(r"\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b",s)
result = re.findall(r"\b[\w\.-]+@[\w\.-]+\.(?:com|in|org|net)\b",s)
print(result)

#                 r"\b[\w\.-]+@[\w\.-]+\.(com|in|org|net)\b"
# Syntax	Purpose
# (abc)	Capturing group
# (?:abc)	Non-capturing group
# `	`	OR operator inside group
# :	Part of ?: to disable capture
# What ?: Means in Regex
# () → creates a capturing group: it stores the matched value
# (?:...) → creates a non-capturing group: it matches the pattern but does not store it
# ✅ Why Use ?:
# When you want to:
# Group alternatives (like com|in|org|net)
#But don’t want re.findall() to return just the group
# (?:...) tells Python to match but not capture
# Now re.findall() will return the full email address
# \b matches a transition between a word character (\w) and a non-word character
# Word characters: [a-zA-Z0-9_]
# Non-word characters: anything else (like space, punctuation)

