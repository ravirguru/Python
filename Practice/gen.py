

def gen_odd():
    num = 1
    while True:
        yield num
        num += 2

gen = gen_odd()

# for i in range(5):
#     print(next(gen))
   
def odd_limit(limit):
    for num in range(1,limit+1, 2):
        yield num


for i in odd_limit(10):
    print(i)


s ="R JESH HA I"

#res = s.replace('\s','&&')

import re
res = re.sub(r"\s",'&&',s)
print(res)

s = "i loVE Python" # i LOve pYTHON
li = []
for word in s.split():
    new_word = ""  # Gets reset for each word here.
    for ch in word:
        if ch.islower():
            new_word += ch.upper()
        elif ch.isupper():
            new_word += ch.lower()
    li.append(new_word) 
print(' '.join(li))     

