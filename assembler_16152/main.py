#!/usr/bin/env python

from sys import argv
from subprocess import call
from subprocess import *
from assembler import *


def options():
    p1=check_output(["echo","FORMAT: \n \t python3 python_filename asm_filename [options]"], universal_newlines=True)
    print(p1)
    p2=check_output(["echo", "COMMAND LINE OPTIONS:"], universal_newlines=True)
    print(p2)
    p3=check_output(["echo", "\t -s \t Display Symbol Table"], universal_newlines=True)
    print(p3)
    p4=check_output(["echo", "\t -l \t Display Literal Table"], universal_newlines=True)
    print(p4)
    p5=check_output(["echo", "\t -i \t Display Intermediate Code"], universal_newlines=True)
    print(p5)
    p6=check_output(["echo", "\t -lst \t Display lst Code"], universal_newlines=True)
    print(p6)
    p7=check_output(["echo", "\t -obj \t Display Object Code"], universal_newlines=True)
    print(p7)
    
def disp_option(x):
    if x=='-s':
        call(["less","opsymtab2.txt"])

    if x=='-l':
        call(["less","oplittab.txt"])

    if x=='-i':
        call(["less","opcode1.txt"])

    if x=='-lst':
        call(["less","opcode2.txt"])
    
    if x=='-obj':
        call(["less","objcode.txt"])
        
    
if __name__ == "__main__":

    if len(argv)==1:
        printf=check_output(["echo", "Please enter .asm file name"], universal_newlines=True)
        print(printf)
        options()
        exit()
    filename=argv[1]

    if len(argv)==2:
        call(["python3","assembler.py",filename])
        printf=check_output(["echo", "Please enter options [-s/-l/-i/-lst/-obj]"], universal_newlines=True)
        print(printf)
        options()
        exit()

    if len(argv)>= 3:
        list1=argv[2:]
        if len(list1)<2:
            for i in list1:
                if i not in ['-s','-l','-i','-lst','-obj']:
                    pp=check_output(["echo", "Please enter options [-s/-l/-i/-lst/-obj]"], universal_newlines=True)
                    print(pp)
                    options()
                    exit()

            for i in list1:
                disp_option(i)
                exit()
        
    
