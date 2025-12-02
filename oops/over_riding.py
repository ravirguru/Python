class Point:
    def __init__(self,a, b):
        self.a = a  # p.a = 1  p.__setattr__("a", 1)
        self.b = b  # p.b = 2  p.__setattr__("b", 2)

    #over-riding or redefining __getattribute__ method in child class
    def __getattribute__(self, name):
        print("__getattribute")
        super.__getattribute__(name) #calling object class __getattribute__ method and passing name.
    
    def __setattr__(self, name, value):
        print("__setattr__")
        super.__setattr__(name, value)

class Point1:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __setattr__(self, name, value):  #overriding __setattr__ from object class here.
        if not isinstance(value, (int, float)):
            raise ValueError("Only numbers are allowed")
        if value < 0:
            raise ValueError("Negative values are not allowed")
        print(f"setting the attribute {name} to value {value}")
        super().__setattr__(name, value)


p1 = Point1(9,99)
print(p1.a)

s ="StringCheck123457899STring"
from collections import defaultdict

d = {}

# for ch in s:
#     d[ch] = d.get(ch,0) + 1
# print(d)

d1 = defaultdict(int)

for ch in s:
    d1[ch] += 1
print(d1)

for k,v in d1.items():
    if v == 1:
        print(k,v)


names = ["apple","google","ibm","apple","ibm", "amazon","amazon"]

unique_items = set(names)

for item in unique_items:
    _count = 0
    for name in names:
        if item == name:
            _count += 1
    if _count > 1:
        print(item)

s ="This is a Programming language and Programming education"

d = { word: len(word)  for word in s.split() if s.count(word) == 1}
print(d)

res = sorted(d.items(),key=lambda item:item[-1])[-1]
print(res)