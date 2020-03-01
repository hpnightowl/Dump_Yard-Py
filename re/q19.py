import re
line = "This is For fox and bear and dog"
pattern = re.compile(r"fox|bear|dog")
find = pattern.findall(line)
print(find)