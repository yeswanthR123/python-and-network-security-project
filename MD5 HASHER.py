import hashlib
  
key = input("Enter the Value To Convert in MD5 :")
result = hashlib.md5(key.encode('utf-8'))
  

print("The hexadecimal equivalent of hash is : ", end ="")
print(result.hexdigest())
print("The byte equivalent of hash is        : ", end ="")
print(result.digest())