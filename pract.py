#Function to check fibonacci.

def fibo(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        series = fibo(n-1)
        series.append(series[-1] + series[-2])
        return series

res = fibo(10)
print(res)

from collections import Counter
def finddupnumbers(lst):
    counts = Counter(lst)
    return [item for item, value in counts.items() if value > 1]

print(finddupnumbers([12,34,34,5,6,99,12]))

s= "programming"    

seen = set()
duplicates = set()

for ch in s:
    if ch in seen:
        duplicates.add(ch)
    else:
        seen.add(ch)

print("Duplicate letters:", list(duplicates))

s4 = 'programming'

counts = Counter(s4)
print(counts.elements)
print(counts.most_common(2)) # gives top two letters here.

d = {'a':'hello','b':100, 'c':10.1,'d':'world'}

res = { k:v[::-1] if isinstance(v,str) else v for k,v in d.items() }
print(res)

nums = [1,2,3,4]

result = ['even' if x % 2 == 0 else 'odd' for x in nums ]
print(result)

names = [["alice", "bob"], ["charlie", "dan"], ["eve", "frank"]]

processed = [ name.capitalize() if len(name) > 4 else "Short" for group in names for name in group]
print(processed)

#Count the numbers in a given string.

s = "Sony12India567Pvt2ltd"
import re
total = 0.0
item = re.findall(r'\d+',s)
print(item)

for num in item:
    total += float(num)
print(total)

a = ['abc','12','hello','23']

for item in a:
    if isinstance(item, str) and item.isnumeric():
        print(item)

s = 'heloo world welcome to python'

alternate_chars = [ ch for ch in s[::2]]
print(alternate_chars)

names = ['apple','yahoo','google','gmail','walmart','flipkart','facebook','amazon']
new_lst = [ name for name in names if len(name) % 2 == 0]
print(new_lst)

names2 = ['apple','yahoo','google','gmail','walmart','flipkart','facebook','amazon']
new_dic = {name:len(name) for name in names2 if len(name) % 2 == 0}
print(new_dic)

#square the numbers.
a = [1,2,3,4]

def squares(item):
    return item **2

m = map(squares, a)
print(list(m))

li =['4/5','6/7','8/9','10/1','100/2']

def get_divisor(string: str) -> list:
    '''
    Here, sorted() internally calls get_divisor() on each individual item in li.
    So get_divisor('4/5'), get_divisor('6/7'), etc. — each call gets a string, not the whole list.
    '''
    return int(string.split('/')[1])
    

result = sorted(li, key=get_divisor)
print(result)

'''
To define a custom exception in Python, you create a new class that inherits from the built-in Exception class. This allows you to create exceptions tailored to your specific needs. Here's a concise example:
Python, Define a custom exception '''
class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)

# Example usage
try:
    raise CustomException("This is a custom exception!")
except CustomException as e:
    print(f"Caught an exception: {e}")

#Key Points:
'''
Inheritance: Your custom exception class must inherit from Exception or one of its subclasses.
Customization: You can add attributes or methods to provide additional functionality if needed.
Usage: Use raise to trigger the exception and try-except blocks to handle it.
1This approach ensures your custom exception integrates seamlessly with Python's 
exception-handling system.
'''
