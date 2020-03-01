import re
line = "abbbs"
pattern = re.compile(r"[a-z]+_[a-z]+$")
find = pattern.findall(line)
print(find)