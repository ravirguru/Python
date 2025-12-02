
s1 = "1234abc@xyz.com, xyz@gmail.com, uk@global.com, ggg@gmail.com"
import re

result1 = re.findall(r"[a-zA-Z-]+@[\w\.-]+\.(?:com|in|org|net)",s1)
print(result1)

