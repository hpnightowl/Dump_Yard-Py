import re
line = "This"
pattern = re.compile(r"\w+")
find = pattern.findall(line)
print(find)