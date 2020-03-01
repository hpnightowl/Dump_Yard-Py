import re
line = "abbbs"
pattern = re.compile(r"a.+b$")
find = pattern.findall(line)
print(find)