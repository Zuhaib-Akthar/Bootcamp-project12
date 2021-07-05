###pthon program to generate md5 of string data
import hashlib

result = hashlib.md5(b"zuhaib MD5").hexdigest()
print(result)