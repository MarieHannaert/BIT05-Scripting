import os
for n in os.walk("/home/guest/Shared/BIT05-scripting/AA"):
    print(n)

print(os.listdir("/home/guest/Shared/BIT05-scripting/AA"))

for b in os.listdir("/home/guest/Shared/BIT05-scripting/AA"):
    print(b)

import tempfile

print(tempfile.gettempdir())

import os.path
print(os.path.split("/home/guest/Shared/BIT05-scripting/AA/BB/A"))
print(os.path.dirname("/home/guest/Shared/BIT05-scripting/AA/BB/A"))
print(os.path.basename("/home/guest/Shared/BIT05-scripting/AA/BB/A"))
print(os.path.exists("/home/guest/Shared/BIT05-scripting/AA/BB/A"))
print(os.path.isfile("/home/guest/Shared/BIT05-scripting/AA/BB/A"))
print(os.path.isdir("/home/guest/Shared/BIT05-scripting/AA/BB/A"))
print(os.path.getsize("/home/guest/Shared/BIT05-scripting/AA/BB/A"))