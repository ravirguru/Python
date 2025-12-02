# #Regex Notes.
# "abcd" - Its like a followed by b, b followed by c and c followed by d.  it has to match this only.
# [] - This is character set or character class in regex, and  '-' inside is range actually
# In character set or class it has to match either one of them. for e.g. [abcd] - either a or b or c or d
from re import findall
#count for lower and upper case
def count_letters(some_string: str)-> tuple:
    lowercase = len(findall(r"[a-z]", some_string))
    uppercase = len(findall(r"[A-Z]",some_string))
    return (lowercase, uppercase)
print(count_letters("The RARE rabbit clothing"))

def count_spaces(some_string):
    return  len(findall(r"\s", some_string))

print(count_spaces("this is a new string with spaces         "))

# + is a meta character it will continue to match as long there is a match.
# + is like, It matches with 1 or more occurences of previous expression.
# >>> findall("an+a", "hello annnnnnnnnnnnnnna how are you doing")
# ['annnnnnnnnnnnnnna']
# so mininum one n should be there for this, "an+a"
# before + there is n so it will try to match atleast one n and after that any number of n's.

sentence ="Python123 hello world 56 how are you37"

numbers = findall(r"[0-9]",sentence)
total=0
for num in numbers:
    total += int(num)
print(total)
wholenumbers = findall(r"[0-9]+",sentence)

_total=0
for num in wholenumbers:
    _total += int(num)
print(_total)

#? - Indicates 0 or max one occurence of previous expression.
# + represents one or more occurences.
result = findall(r"colou?r", "what colour do you like")
print(result)

result2 = findall(r"https?","http://www.google.com")
print(result2)



