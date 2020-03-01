import re
line = "zazbbbs aaasdasdz sdasd "
pattern = re.compile(r"^\Bz\B")
find = pattern.findall(line)
print(find)