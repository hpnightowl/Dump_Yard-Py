import re
line = "abbbs"
pattern = re.compile(r"ab{3}")
find = pattern.findall(line)
print(find)