import re
line = "abbbs"
pattern = re.compile(r"ab{2,3}")
find = pattern.findall(line)
print(find)