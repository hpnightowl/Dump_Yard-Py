import re
line = "zazbbbs aaasdasdz sdasd _ 23123 ASAs "
pattern = re.compile(r"\.[0]*','.'")
find = pattern.findall(line)
print(find)