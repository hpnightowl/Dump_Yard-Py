import re
line = ""
pattern = re.compile(r"ab*")
find = pattern.findall(line)
print(find)