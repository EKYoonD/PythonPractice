str_answer = ""
string_practice = "Hi my name is Katie"
string_practice = string_practice.split(" ")

for i in range(len(string_practice)):
    if i == len(string_practice)-1:
        string_practice[i] = "".join(reversed(string_practice[i]))
        str_answer += string_practice[i]
    else:
        string_practice[i] = "".join(reversed(string_practice[i]))
        str_answer += string_practice[i]
        str_answer += "_"

print(str_answer)

str_practice = "abcde"
str_practice = str_practice[::-1]
print(str_practice)
print("-".join(str_practice))