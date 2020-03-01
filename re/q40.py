import re
text1 = ' hteref   asdasd '
print("Without extra spaces:",re.sub(r'\s+', '',text1))