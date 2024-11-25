# READ TEXT FROM THE FILE -> PUT THE LINES IN A LIST
program = []  # this variable will keep the whole program in it linewise
global newprogram
newprogram = []  # the converted program will be put here
filename = input("\n\nEnter the correct filename (should be in same directory and this program) with correct extension\nexample -> filename.txt   or   python.py\n =>")
with open(filename, 'r') as file:  # opens file specified 
    for line in file:  # Read each line in the file
        program.append(line.strip())   # appends each line in program[list]
print(program) #############

# SEPARATE AND EXTRACT OUT THE FUNCTIONS, VARIABLES AND TEXT FROM THE LINE
def cprint(line): # print("text") to printf("text");
    brokent = line.partition("(")  # breaks into ("print","(","text)")
    broken = []
    for i in brokent:
        broken.append(i)              # changes the tuple into list
    broken[0] = "printf"              # print to printf
    newline = "\n\t"+broken[0]+broken[1]+broken[2]+";"  # compiles all broken parts and adds ;
    newprogram.append(newline)      # appends to final program list

def cinput(line):
    brokent1 = line.split("=")  # breaks into a = input("text") into brokent2 = ['a','input','"text")']
    brokent2 = []
    for i in brokent1 :
        part = (i.split("("))
        for j in part:
            brokent2.append(part.strip())
    printmsg = "\n\tprintf(" + brokent2[2] + ";"
    declaration = "\n\ttype ???????"
    scanmsg = type????????
    broken = [declaration,printmsg,scanmsg]
    

# ACCESS THE LINES ONE BY ONE AND FIGURE WHICH TYPE OF COMMAND IT IS
for line in program :
    if line[0] == "#":    # comment functions - ignores
        newline = "\n\t"+ line   #shifting to next line and indentation
        newprogram.append(newline)   # appending to newprogram
        continue
    if "print" in line :    # print fn
        cprint(line)

# STDIO.H AND CONIO.H AND VOID MAIN AND OTHER OPENINGS
print(newprogram) #############
alwaysstart = ["# include <stdio.h>","\n# include <conio.h>","\nvoid main()","\n{"]  # starting part
alwaysend = ["\n\tgetch();","\n}"]   # ending part
newprogram = alwaysstart + newprogram + alwaysend  # concats starting, program and ending
f = open("convertedprogram.txt", "w")   
f.writelines(newprogram)  # writes onto convertedprogram.txt
f.close()
print("\n\nYour program should have been converted for c language, please check convertedprogram.txt in the same directory you entered the file before. Thanks !")