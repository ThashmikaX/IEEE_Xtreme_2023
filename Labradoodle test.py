import re

word = "labradoodle"
pattern = r"labrador"

if re.search(pattern, word):
    print(f"{word} contains '{pattern}' as a part of it.")
else:
    print(f"{word} does not contain '{pattern}' as a part of it.")
