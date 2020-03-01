import re
line = "abbbs"
pattern = re.compile(r"\w+\S*$")
find = pattern.findall(line)
print(find)