import re
line = "hello asd adsa asdasd asad"
pattern = re.compile(r"\w{4,5}")
find = pattern.findall(line)
print(find)