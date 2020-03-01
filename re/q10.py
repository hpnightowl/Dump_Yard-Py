import re
line = "abbbs"
pattern = re.compile(r"\bab")
find = pattern.findall(line)
print(find)