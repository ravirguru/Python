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

# Matching for email address in a given string.
# s = "abc@def.com, jkl@ert.com, mno@pqsrt.com, office@xyz.co.in, newone@gmail.org, ghi-123 
# findall(r"[\w\.-]+@[\w\.-]+(?:com|in|org)",s)  
#  o/p: 'jkl@ert.com',      
#  'mno@pqsrt.com',    
#  'jkl@ert.com',
#  'mno@pqsrt.com',
#  'office@xyz.co.in',
#  'newone@gmail.org']
# [^a-zA-Z0-9]  this is negation.. except a-zA-Z0-9 match others like spl characters.
d={}
for ch in (findall(r"[^a-zA-Z0-9]","hello@world how are you!!!! the %$&COST**** OF THE book \
                   is $100....")):
    d[ch] = d.get(ch,0) + 1
print(d)
#O/P -> {'@': 1, ' ': 19, '!': 4, '%': 1, '$': 2, '&': 1, '*': 4, '.': 4}
#\w = [a-zA-Z0-9_]
#\d = [0-9]
#Find String at the beginning or at the end of string.
findall(r"^hello$", "hi hello how are you hello")
#o/p []
findall(r"hello$", "hi hello how are you hello")
#o/p ['hello']
findall(r"hello$", "hello")
#o/p ['hello']

#word boundary
# \b - Any transition b/w a word character and non-word character or 
#  non-word character to word character is called word boundary.
# [a-zA-Z0-9_]

#program for counting leading and trailing whitespaces.
def count_leading_trailing_spaces(somestring: str)->list:
    leading_white_spaces = len(findall(r"^\s+",somestring)[0])
    trailing_white_spaces = len(findall(r"\s+$",somestring)[0])
    return (leading_white_spaces,trailing_white_spaces)

print(count_leading_trailing_spaces("     This is for test checking only    "))

#program for find three or 3 digit number.
line = "878 hello there 2788999 hello world welcome to python 665"
res1 = findall(r"\d{3}$", line)
print(res1)

#program for finding 6 digit pincode number.
pincode = "Pincode of Bangalore 560085 your mobile number is 1234567890"
p_code = findall(r"\b\d{6}\b",pincode)
print(p_code)

#program for matching phone numbers of type 800-865-4456 etc.
phone_numbers = "This is a string 900-987-1923 and hello there 800-776-0097 and 700-987-9876"
findall(r"\d",phone_numbers)
findall(r"\d+",phone_numbers)
findall(r"\d{3}-\d{3}-\d{4}",phone_numbers)
group = findall(r"[89]00-\d{3}-\d{4}",phone_numbers) # To match only phone numbers from 800 or 900.
print(group)

So what's the real difference?
Pattern	What it returns	Why
(?=bc)	['']	Lookahead match has length zero (no capturing group)
(?=(bc))	['bc']	Group (bc) captures the text matched inside the lookahead

# Simple explanation
# Without capturing group:
# (?=bc)
# ✔ Lookahead true
# ✖ Returns nothing → gives empty string
# With capturing group:
# (?=(bc))Simple explanation
# Without capturing group:
# (?=bc)
# ✔ Lookahead true
# ✖ Returns nothing → gives empty string
# With capturing group:
# (?=(bc))
# ✔ Lookahead true
# ✔ (bc) is captured
# → findall() returns the captured text
# 🧠 Handy Rule
# Lookahead alone → always returns ''
# Lookahead + capturing group → returns the captured text
# Example:
# (?=(xyz)) → returns 'xyz'
# (?=xyz)   → returns ''
