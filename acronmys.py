user_input = str(input("Enter a Pharse:"))
text = user_input.split()
Acronyms = " "
for i in text:
    Acronyms = Acronyms+str(i[0]).upper()
    print(Acronyms)

