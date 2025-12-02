import re

def count_vow_con(s: str) -> tuple:
    vowels = re.findall(r"[aeiouAEIOU]", s) #This matches either of aeiouAEIOU
    consonant = re.findall(r"[^aeiouAEIOU]",s) #This matches except aeiouAEIOU
    return (len(vowels), len(consonant))
print(count_vow_con("RaaaviiiBhaaai"))
