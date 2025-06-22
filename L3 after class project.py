import os
if os.path.exists("L3 after class project file for file handling"):
    print("He(the file) forgot to tell you that he exists")
else:
    print("")



with open("L3 after class project file for file handling","w") as f:
    f.write("Hi!")

with open("L3 after class project file for file handling", "a") as add:
    add.write("OH... i forgot to tell you that i exist as a file")

