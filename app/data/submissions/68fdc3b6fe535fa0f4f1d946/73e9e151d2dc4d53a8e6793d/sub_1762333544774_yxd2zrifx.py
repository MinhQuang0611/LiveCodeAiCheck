s = input()
special_chars = "!@#$%^&*()\"/-+`~.{}[]|_-?<>'"
for char in special_chars:
    s = s.replace(char, "")
_list = s.strip().title().split()
new_s = " ".join(_list)
print(new_s)
