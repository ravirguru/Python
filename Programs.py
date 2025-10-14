print("hi World")

for i in range(7):
    print(i)

s = "apple kayak level mom dad malayalam"

palindrome = [word for word in s.split() if word == word[::-1]]
print(palindrome)

result = {
    'palindrome': [ word for word in s.split() if word == word [::-1]],
    'notpalindrome' : [word for word in s.split() if word != word [::-1]]
}

print(result)

def greet(name,/,*,age,company):
    return(name,age,company)

result= greet('ravi',age=32,company='myown')
print(result)

'''Fibonacci'''

def fibo(n):
    if n == 1:
        return [0]
    elif n== 2:
        return [0, 1]
    else:
        series = fibo(n-1)
        series.append(series[-1] + series[-2])
        return series

res = fibo(8)
print(res)
  



'''first non repeating character'''

s = 'swiss'
from collections import Counter

count = Counter(s)
print(count)

for ch in s:
    if count[ch] == 1:
        print("First non-repeating character :", ch)
        break

def rotate(arr,k):
    k = k % len(arr)
    return arr[k:] + arr[:k]

arr = [1,2,34,56]

res = rotate(arr,2)
print(res)

def rotateright(arr,n):
    n = n % len(arr)
    return arr[-n:]  + arr [:-n]

arr = [100,56,7,89,90]
res2 = rotateright(arr,2)
print(res2)

from collections import Counter

def find_duplicates(lst):
    counts = Counter(lst)
    return [item for item, count in counts.items() if count == 1]

print(find_duplicates([13,4,5,1,13,1]))



def reverse(string: str) ->  str:
    try:
        if string is None or string.strip()=="":
            raise ValueError("Input string is empty")
        string = string.lower()
        return string[::-1]
    except AttributeError:
        raise TypeError("Input must be a String")
print(reverse("ravi"))


def convert_alphb(any_string : str) -> str:
    li = []
    for ch in any_string:
        temp = ord(ch)
        if temp >= 97 and temp <=122:
            li.append(chr(temp-32))
        else:
            if temp >=65 and temp <=90:
                li.append(chr(temp+32))
    return "".join(li)

print(convert_alphb("Hello World"))

def check_str_int_float(li : list) -> list:
    for item in li:
        if isinstance(item, (int, float)):
            temp = str(item)
            print(temp[::-1])
        else:
            print(item)

print(check_str_int_float(['apple','yahoo','1234',100,22.3,45,'26.3']))

pattern = r"\b(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\." \
          r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\."  \
          r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\." \
          r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\b"

import re
def check_ip(any_string: str) -> dict:
    ips = re.findall(pattern,any_string)
    return {"ips" : [".".join(ip) for ip in ips]} if ips else "Not a valid IP"

any_string = "SkyWalk 192.34.5.90"
print(check_ip(any_string))            

pattern1 = r"\b(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?|[0-9])\." \
           r"\b(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?|[0-9])\." \
           r"\b(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?|[0-9])\." \
           r"\b(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?|[0-9])\b"


def _is_ip_valid(any_string : str) -> dict:
    ips = re.findall(pattern,any_string)
    return { "ips" :  [ ".".join(ip) for ip in ips ] } if ips else "Not an Valid IP"

any_string2 = "Sonicwall 99.5.6.9  Ivanti 34.56.9.0"
print(_is_ip_valid(any_string2))
import logging

logging.basicConfig(filename='test.log',level=logging.INFO)
logging.info("Test started")
logging.warning("Something looks off")
logging.error("Test failed")


li = ['4/5', '6/7', '10/1']
'''
In sorted(li, key=...), Python automatically passes each item of the list (li) into the key function 
— one at a time.
'''
res3 = sorted(li, key=lambda x: int(x.split('/')[0])/ int(x.split('/')[1]))
sorted(li, key=lambda x: int(x.split('/')[0]) / int(x.split('/')[1]))
print(res3)

r"\b(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\."
r"\b(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\."


r"\b(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\."

s = "helloworld"

res = { ch: s.count(ch) for ch in s if s.count(ch) > 1}
print(res)