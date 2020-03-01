import re
line = "zazbbbs aaasdasdz sdasd _ 23123 ASAs "
pattern = re.compile(r"\w+")
find = pattern.findall(line)
print(find)