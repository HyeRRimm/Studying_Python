file= open("callingfile.txt", "w")
file.write("각자도생")
file.close()

with open("callingfile.txt"."w") as file:
    file.write("각자도생")

-----------------------------------------------

file=open("callingfile.txt", "r")
print(file.read())
file.close()

with open("callingfile.txt"."r") as file:
    print(file.read())

