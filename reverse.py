string = input("Enter your string ")

string2 = ("")
for i in string:
    string2 = i + string2

print(f"The original string is {string}")
print(f"The reversed string is {string2}")
