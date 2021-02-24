
with open("ascii.txt", "r") as f:
    content = f.read()

finalText = ''
for character in content:
    code = ord(character)
    katoptrikos = chr(128 - code)
    finalText += katoptrikos

utf8 = finalText.encode()
print(utf8[::-1])
