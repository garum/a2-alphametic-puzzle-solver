import os 
import re
import sys

def parse_input( command):
    list_char =[char for char in command] 
    numbers=[]
    number=""
    for char in  command:
        if (char in "+-="):
            numbers.append(number)
            number=""+char
        else :
            number = number + char  
    numbers.append(number)
    return numbers


def get_distinct_list(command):
    numbers=re.split(r'[+=-]',command)
    all_digits="".join(numbers)
    distinct=list(set(all_digits))
    ret=",".join(distinct)
    return "["+ret + ",10]."

def get_exceptions(numbers):

    exceptions=[]
    for number in numbers:
        if (number[0] in "+-="):
            exceptions.append(number[1]+"!=0.")
        else :
            exceptions.append(number[0]+"!=0.")
    return "\n".join(exceptions)


    
def transfrom(number):
    list_char =[char for char in number] 
    zeroes = len(list_char)-1
    string = "(" + list_char[0] +"*" + str(10**(zeroes))
    for i in range(1,len(list_char)):
        string = string + "+" + list_char[i] + "*" + str(10**(zeroes-i)) 
    string = string + ")"
    return string
    
def get_condtions(numbers):
    text= ""
    for number in numbers:
        print(number)
        if (number[0] in "+="):
            text =  text + number[0] +  transfrom(number[1:])
        elif (number[0] == '-' ):
              text =  text + "+-" +  transfrom(number[1:])
        else :
            text =  text +  transfrom(number)
    return text +"."

def generate_mace4(outputfile):
    f = open("template.txt", "r")
    input1  = input()
    print(input1)
    template = f.read()
    exc =parse_input(input1)
    text =template.format(get_distinct_list(input1) ,get_exceptions(exc),get_condtions(exc) )
    print (text)
    fout = open(outputfile,"w")
    fout.write(text)
    f.close()
    fout.close()

def call_mace4(outputfile):
    cmd="mace4 -c -f " + outputfile
    print(cmd)
    os.system(cmd)

def main():
    #print(sys.argv)
    outputfile="a.in"
    if len(sys.argv) == 2:
        outputfile = sys.argv[1]
    
       

    generate_mace4(outputfile)
    call_mace4(outputfile)
    

if  __name__ == "__main__":
    main()