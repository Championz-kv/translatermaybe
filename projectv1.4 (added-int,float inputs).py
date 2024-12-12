# READ TEXT FROM THE FILE -> PUT THE LINES IN A LIST
program = []  # this variable will keep the whole program in it linewise
global newprogram
newprogram = []  # the converted program will be put here
filename = input("\n\nEnter the correct filename (should be in same directory and this program) with correct extension\nexample -> filename.txt   or   python.py\n =>")
with open(filename, 'r') as file:  # opens file specified 
    for line in file:  # Read each line in the file
        line = line.strip(" ")
        line = line.rstrip("\n")
        if line == "" :
            line = "\n"
        program.append(line)   # appends each line in program[list]
print("\n",program) #############


# SEPARATE AND EXTRACT OUT THE FUNCTIONS, VARIABLES AND TEXT FROM THE LINE
def cprint(line): # print("text") to printf("text");
    brokent = line.partition("(")  # breaks into ("print","(","text)")
    broken = []
    for i in brokent:
        broken.append(i)              # changes the tuple into list
    broken[0] = "printf"              # print to printf
    newline = "\n"+broken[0]+broken[1]+broken[2]+";"  # compiles all broken parts and adds ;
    newprogram.append(newline)      # appends to final program list

def cinput(line): # a = input("text")
    typ = "c"
    dtyp = "char"
    if "int" in line:
        if line.index("int") <  line.index("input") :
            typ = "d"
            dtyp = "int"
        line = line.partition("int(")########## # a = int(input("text")) => ["a =","int(","input("text"))"]
        x,y,z = line
        z = z.removesuffix(")")
        line = x+z
    if "float" in line:
        if line.index("float") <  line.index("input") :
            typ = "f"
            dtyp = "float"
        line = line.partition("float(")##########  # a = int(input("text")) => ["a =","int(","input("text"))"]
        x,y,z = line
        z = z.removesuffix(")")
        line = x+z
    if "char" in line:
        if line.index("char") <  line.index("input") :
            typ = "c"
            dtyp = "char"
        line = line.partition("chr(")########## # a = int(input("text")) => ["a =","int(","input("text"))"]
        x,y,z = line
        z = z.removesuffix(")")
        line = x+z
    b1 = line.partition("=") # a = input("text") => ("a","=","input(text)")
    b2 = []
    for i in b1 :
        b2.append(i)
    b2.remove("=")
    b2[1] = b2[1].partition("(") #["a",( "input", "(" , "text)" )]
    x,y,z = b2[1]
    b2.pop(1)
    b2.extend([x,z]) # ["a","input", "text)"]
    printmsg = "\nprintf(" + b2[2] + ";"
    declaration = "\n" + dtyp + " " + b2[0] + ";"
    scanmsg = "\nscanf(\"%" + typ + "\",&" + b2[0] + ");"
    broken = [declaration,printmsg,scanmsg]
    newprogram.extend(broken)
    

# ACCESS THE LINES ONE BY ONE AND FIGURE WHICH TYPE OF COMMAND IT IS
for line in program :
    if line[0] == "#":    # comment functions - ignores]
        newline = "\n"+ "//" + line.lstrip("#")   #shifting to next line and indentation
        newprogram.append(newline)   # appending to newprogram
        continue
    if "print" in line :    # print fn
        if "input" not in line :
            cprint(line)
        elif line.index("print") <  line.index("input") :  # if both are there (one in text)
            cprint(line)
    if "input" in line :
        if "print" not in line :
            cinput(line)
        elif line.index("input") <  line.index("print") :  # if both are there (one in text)
            cinput(line)
    if line == "\n" :
        newprogram.append(line)
    else:
        continue  # later to put the same line in code with // and display this line wasn't converted

# STDIO.H AND CONIO.H AND VOID MAIN AND OTHER OPENINGS
print(newprogram) #############
alwaysstart = ["# include <stdio.h>","\n# include <conio.h>","\nvoid main()","\n{"]  # starting part
alwaysend = ["\n\ngetch();","\n}"]   # ending part
newprogram = alwaysstart + newprogram + alwaysend  # concats starting, program and ending
f = open("convertedprogram.txt", "w")   
f.writelines(newprogram)  # writes onto convertedprogram.txt
f.close()
print("\n\nYour program should have been converted for c language, please check convertedprogram.txt in the same directory you entered the file before. Thanks !")