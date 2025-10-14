
def is_prime(n : int):
   return not any ([i%2 == 0 for i in range(2,n)])

print(is_prime(20))

li = [10,22,40,2,40,9,900,1]

res3 = sorted(li)[-1]
print(res3)

[ for item in li if item]