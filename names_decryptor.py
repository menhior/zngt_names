import re

with open('test.txt', 'r') as file:
    text = file.read()
    str_text = str(text)
    print(str_text)
    listed = re.sub( r"([A-Z])", r" \1", str_text).split()
    print(listed)
    #for line in file:
        #print(line)