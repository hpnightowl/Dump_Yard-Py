import re
line = "azbbbs asdasd "
pattern = re.compile(r"\w*z.\w*")
find = pattern.findall(line)
print(find)