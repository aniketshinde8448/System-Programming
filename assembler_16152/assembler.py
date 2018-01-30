from sys import *
var=["eax","ebx","ecx","edx","esp","ebp","esi","edi","mov","add","sub","call","section",".data",".bss",".text","global","extern","dword"]
sym=["dd","db","dw","dq","resd","resb","resw","resq"]
num=['1','2','3','4','5','6','7','8','9','0']
arr32=["eax","ebx","ecx","edx","ebp","esp","esi","edi"]
arr16=["ax","bx","cx","dx","bp","sp","si","di"]
arr8=["ah","al","bh","bl","ch","cl","dh","dl"]
arrs32=["movsd","lodsd","scasd","stosd"]
arrs16=["movsw","lodsw","scasw","stosw"]
arrs8=["movsb","lodsb","scasb","stosb"]
def propsymtab2(s):
    disyname=[]
    dcsyname=[]
    uisyname=[]
    ucsyname=[]
    disc=0
    dcsc=0
    uisc=0
    ucsc=0
    flag=0
    flag1=0
    uadr=0
    dadr=0
    #print("Name  |Type  |Size  |U/D ")
    #dsl=len(dsyname)
    #usl=len(usyname)
    fn=open(s,"r+")
    fo=open("opsymtab2.txt","w")
    ln=fn.readline()
    cnt=0
    l=ln.split()
    #print(l)
    lnn=len(l)
    fo.write("\tSymbol Table\nName\t\tNo.\t\tType\t\tSize\t\tU/D\n")
    while(ln!=""):
        for i in range(lnn):
            #labelsp=l[i].split(":")
            #ucsyname.append(labelsp[0])
            #ucsc+=1
            if(l[i]=='dd'):
                if l[i-1] not in disyname:
                    #print (l[i-1],"is redefined")
                #else:
                    disyname.append(l[i-1])
                    disc+=1
                    sl=l[i+1].split(",")
                    sll=len(sl)
                    #print(l[i-1],end="    ")
                    #print("int",end="    ")
                    #print(sll,end="    ")
                    #print("D")
                    cnt+=1
                    fo.write(str(l[i-1]))
                    fo.write("\t\t")
                    fo.write(str(cnt))
                    fo.write("\t\tINT\t\t")
                    fo.write(str(sll))
                    fo.write("\t\tD\t\t")
                    fo.write(str(dadr))
                    fo.write("\n")
                    dadr=dadr+sll*4
            #if l[i] not in var:
               # an=l[i]
                #if l[i] not in sym:
                  #  print(an,"is undefined")

            if(l[i]=='db'):
                if l[i-1] not in dcsyname:
                    #print (l[i-1],"is redefined")
                #else:
                    dcsyname.append(l[i-1])
                    dcsc+=1
                    #print(l[i-1],end="    ")
                    #print("char",end="    ")
                    #print("1",end="    ")
                    #print("D")
                    cnt+=1
                    #print(l[i+1])
                    #sbl=l[i+1].split("\"")
                    #print(sbl)
                    sblen=len(l[i+1])
                    #print(sblen)
                    fo.write(str(l[i-1]))
                    fo.write("\t\t")
                    fo.write(str(cnt))
                    fo.write("\t\tCHAR\t\t")
                    fo.write(str(sblen))
                    fo.write("\t\tD\t\t")
                    fo.write(str(dadr))
                    fo.write("\n")
                    dadr=dadr+sblen*1
            if(l[i]=='resd'):
                if l[i-1] not in uisyname:
                    #print(l[i-1],"is redefined")
                #else:
                    uisyname.append(l[i-1])
                    uisc+=1
                    #print(l[i-1],end="    ")
                    #print("int",end="    ")
                    #print(l[i+1],end="    ")
                    #print("U")
                    cnt+=1
                    fo.write(str(l[i-1]))
                    fo.write("\t\t")
                    fo.write(str(cnt))
                    fo.write("\t\tINT\t\t")
                    fo.write(str(l[i+1]))
                    fo.write("\t\tU\t\t")
                    fo.write(str(uadr))
                    fo.write("\n")
                    uadr=uadr+int(l[i+1])*4
            if(l[i]=='resb'):
                if l[i-1] not in ucsyname:
                    #print(l[i-1],"is redefined")
                #else:
                    ucsyname.append(l[i-1])
                    ucsc+=1
                    #print(l[i-1],end="    ")
                    #print("char",end="    ")
                    #print(l[i+1],end="    ")
                    #print("U")
                    cnt+=1
                    fo.write(str(l[i-1]))
                    fo.write("\t\t")
                    fo.write(str(cnt))
                    fo.write("\t\tCHAR\t\t")
                    fo.write(str(len(l[i+1])))
                    fo.write("\t\tU\t\t")
                    fo.write(str(uadr))
                    fo.write("\n")
                    uadr=uadr+len(l[i+1])*1
            if(l[i]=='global'):
                dcsyname.append(l[i+1])
                dcsc+=1
                #print(l[i+1],end="    ")
                #print("funct",end="    ")
                #print("1",end="    ")
                #print("-")
                cnt+=1
                fo.write(str(l[i+1]))
                fo.write("\t\t")
                fo.write(str(cnt))
                fo.write("\t\tFUNCT\t\t1\t\t-")
                fo.write("\n")
            if(l[i]=='jmp'):
                ucsyname.append(l[i+1])
                ucsc+=1
                #print(l[i+1],end="    ")
                #print("label",end="    ")
                #print("1",end="    ")
                #print("-")
                cnt+=1
                fo.write(str(l[i+1]))
                fo.write("\t\t")
                fo.write(str(cnt))
                fo.write("\t\tLABEL\t\t1\t\t-")
                fo.write("\n")
            if(l[i]=="equ"):
                disyname.append(l[i-1])
                disc+=1
                #print(l[i-1],end="    ")
                #print("int",end="    ")
                #print("1",end="    ")
                #print("D")
                cnt+=1
                fo.write(str(l[i-1]))
                fo.write("\t\t")
                fo.write(str(cnt))
                fo.write("\t\tINT\t\t1\t\tD")
                fo.write("\n")
            if(l[i]=="mov"):
                ul=l[i+1].split(",")
                uld=ul[0].split("[")
                if uld[0]=="dword":
                    uldd=uld[1].split("]")
                    #al=len(disyname)
                    #for d in range(al):
                      #  if (uldd[0]==disyname[i]):

                    if uldd[0] not in disyname:
                        flag1=1
                    if flag1==1:
                        if uldd[0] not in uisyname:
                            #print(uldd[0],"is undefined")
                            break
                else:
                    if ul[0] not in disyname:
                        if ul[0] not in var:
                            #print(ul[0],"is undefined")
                            break
                    elif ul[0] not in dcsyname:
                        if ul[0] not in var:
                            #print(ul[0],"is undefined")
                            break
                    elif ul[0] not in uisyname:
                        if ul[0] not in var:
                            #print(ul[0],"is undefined")
                            break
                    elif ul[0]not in ucsyname:
                        if ul[0] not in var:
                            #print(ul[0],"is undefined")
                            break
                uld=ul[1].split("[")
                if uld[0]=="dword":
                    uldd=uld[1].split("]")
                    if uldd[0] not in disyname:
                        flag1=1
                    if flag1==1:
                        if uldd[0] not in uisyname:
                            #print(uldd[0],"is undefined")
                            break
                    #if uldd[0] not in disyname:
                     #   print(uldd[0],"is undefined")
                      #  break
                    #else:
                     #   if uldd[0] not in uisyname:
                       #     print(uldd[0],"is undefined")
                        #    break
                else:
                    if ul[1] not in disyname:
                        if ul[1] not in var:
                            #print(ul[1],"is undefined")
                            break
                    elif ul[1] not in dcsyname:
                        if ul[1] not in var:
                            #print(ul[1],"is undefined")
                            break
                    elif ul[1] not in uisyname:
                        if ul[1] not in var:
                            #print(ul[1],"is undefined")
                            break
                    elif ul[1]not in ucsyname:
                        if ul[1] not in var:
                            #print(ul[1],"is undefined")
                            break
            if(l[i]=="add"):
                ul=l[i+1].split(",")
                uld=ul[0].split("[")
                if uld[0]=="dword":
                    uldd=uld[1].split("]")
                    #al=len(disyname)
                    #for d in range(al):
                      #  if (uldd[0]==disyname[i]):

                    if uldd[0] not in disyname:
                        flag1=1
                    if flag1==1:
                        if uldd[0] not in uisyname:
                            #print(uldd[0],"is undefined")
                            break
                else:
                    if ul[0] not in disyname:
                        if ul[0] not in var:
                            #print(ul[0],"is undefined")
                            break
                    elif ul[0] not in dcsyname:
                        if ul[0] not in var:
                            #print(ul[0],"is undefined")
                            break
                    elif ul[0] not in uisyname:
                        if ul[0] not in var:
                            #print(ul[0],"is undefined")
                            break
                    elif ul[0]not in ucsyname:
                        if ul[0] not in var:
                            #print(ul[0],"is undefined")
                            break
                uld=ul[1].split("[")
                if uld[0]=="dword":
                    uldd=uld[1].split("]")
                    if uldd[0] not in disyname:
                        flag1=1
                    if flag1==1:
                        if uldd[0] not in uisyname:
                            #print(uldd[0],"is undefined")
                            break
                    #if uldd[0] not in disyname:
                     #   print(uldd[0],"is undefined")
                      #  break
                    #else:
                     #   if uldd[0] not in uisyname:
                       #     print(uldd[0],"is undefined")
                        #    break
                else:
                    if ul[1] in num:
                        break
                    if ul[1] not in disyname:
                        if ul[1] not in var:
                            #print(ul[1],"is undefined")
                            break
                    elif ul[1] not in dcsyname:
                        if ul[1] not in var:
                            #print(ul[1],"is undefined")
                            break
                    elif ul[1] not in uisyname:
                        if ul[1] not in var:
                            #print(ul[1],"is undefined")
                            break
                    elif ul[1]not in ucsyname:
                        if ul[1] not in var:
                            #print(ul[1],"is undefined")
                            break
            if(l[i]=="sub"):
                ul=l[i+1].split(",")
                uld=ul[0].split("[")
                if uld[0]=="dword":
                    uldd=uld[1].split("]")
                    #al=len(disyname)
                    #for d in range(al):
                      #  if (uldd[0]==disyname[i]):

                    if uldd[0] not in disyname:
                        flag1=1
                    if flag1==1:
                        if uldd[0] not in uisyname:
                            #print(uldd[0],"is undefined")
                            break
                else:
                    if ul[0] not in disyname:
                        if ul[0] not in var:
                            #print(ul[0],"is undefined")
                            break
                    elif ul[0] not in dcsyname:
                        if ul[0] not in var:
                            #print(ul[0],"is undefined")
                            break
                    elif ul[0] not in uisyname:
                        if ul[0] not in var:
                            #print(ul[0],"is undefined")
                            break
                    elif ul[0]not in ucsyname:
                        if ul[0] not in var:
                            #print(ul[0],"is undefined")
                            break
                uld=ul[1].split("[")
                if uld[0]=="dword":
                    uldd=uld[1].split("]")
                    if uldd[0] not in disyname:
                        flag1=1
                    if flag1==1:
                        if uldd[0] not in uisyname:
                            #print(uldd[0],"is undefined")
                            break
                    #if uldd[0] not in disyname:
                     #   print(uldd[0],"is undefined")
                      #  break
                    #else:
                     #   if uldd[0] not in uisyname:
                       #     print(uldd[0],"is undefined")
                        #    break
                else:
                    if ul[1] in num:
                        break
                    if ul[1] not in disyname:
                        if ul[1] not in var:
                            #print(ul[1],"is undefined")
                            break
                    elif ul[1] not in dcsyname:
                        if ul[1] not in var:
                            #print(ul[1],"is undefined")
                            break
                    elif ul[1] not in uisyname:
                        if ul[1] not in var:
                            #print(ul[1],"is undefined")
                            break
                    elif ul[1]not in ucsyname:
                        if ul[1] not in var:
                            #print(ul[1],"is undefined")
                            break            

        ln=fn.readline()
        l=ln.split()
        lnn=len(l)
        flag1=0
    print()

def proplittab(s):
    disyname=[]
    dcsyname=[]
    uisyname=[]
    ucsyname=[]
    disc=0
    dcsc=0
    uisc=0
    ucsc=0
    flag=0
    flag1=0
    #print("Name  |Type  |Size  |U/D ")
    #dsl=len(dsyname)
    #usl=len(usyname)
    fn=open(s,"r+")
    fo=open("oplittab.txt","w")
    ln=fn.readline()
    cnt=0
    l=ln.split()
    #print(l)
    lnn=len(l)
    fo.write("\tLiteral Table\nLit Value\tLit No.\n")
    while(ln!=""):
        for i in range(lnn):
            #labelsp=l[i].split(":")
            #ucsyname.append(labelsp[0])
            #ucsc+=1
            if (l[i]=="mov"):
                #print(l[i+1])
                ls=l[i+1].split(",")
                #print(ls)
                #print(ls[0])
                if (ls[0].isdigit()==True):
                    cnt+=1
                    fo.write(ls[0])
                    fo.write("\t\t")
                    fo.write(str(cnt))
                    fo.write("\n")
                    #print(ls[0])
                    #print(cnt)
                elif (ls[1].isdigit()==True):
                    cnt+=1
                    fo.write(ls[1])
                    fo.write("\t\t")
                    fo.write(str(cnt))
                    fo.write("\n")
                    #print(ls[1])
                    #print(cnt)
                        
            if (l[i]=="add"):
                ls=l[i+1].split(",")
                if ls[0] not in var:
                    if (ls[0].isdigit()==True):
                        cnt+=1
                        fo.write(ls[0])
                        fo.write("\t\t")
                        fo.write(str(cnt))
                        fo.write("\n")
                elif ls[1] not in var:
                    if (ls[1].isdigit()==True):
                        cnt+=1
                        fo.write(ls[1])
                        fo.write("\t\t")
                        fo.write(str(cnt))
                        fo.write("\n")

        ln=fn.readline()
        l=ln.split()
        lnn=len(l)


def trans(s1,s2,s3,s4,s5):
    n=0
    a=0
    flag=0
    #address=0000
    fi1=open(s1,"r")
    fi2=open(s2,"r")
    fi3=open(s3,"r")
    fi4=open(s4,"r")
    fi5=open(s5,"r")
    fo=open("opcode1.txt","w")
    ln=fi1.readline()
    lo=fi2.read()
    l3=fi3.read()
    l4=fi4.read()
    l5=fi5.read()
    ls3=l3.split()
    ls4=l4.split()
    ls5=l5.split()
    ls=ln.split()
    ls2=lo.split()
    l=len(ls)
    l2=len(ls2)
    ln3=len(ls3)
    cnt=0
    address=0
    #fo.write("\t\t\t\tOPCODE\n")
    #fo.write("LINE NO.\tOPERATION\tOPERAND_1\tOPERAND_2\tADDRESS\n")
    while ln!="":
        cnt+=1
        for i in range(l):
            if ls[i]=="mov":
                #print(type(address))
                fo.write(str(cnt))
                fo.write("\t")
                ls1=ls[i+1].split(",")
                if ls1[0] in arr32 and ls1[1] in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="mov":
                            if ls5[y+1]=="r32,r32":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                if ls1[0] in arr16 and ls1[1] in arr16:
                    for y in range(len(ls5)):
                        if ls5[y]=="mov":
                            if ls5[y+1]=="r16,r16":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                if ls1[0] in arr8 and ls1[1] in arr8:
                    for y in range(len(ls5)):
                        if ls5[y]=="mov":
                            if ls5[y+1]=="r8,r8":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                elif ls1[0] in arr32 and ls1[1] in ls2:
                    for y in range(len(ls5)):
                        if ls5[y]=="mov":
                            if ls5[y+1]=="r32,m32":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                elif ls1[0] in arr16 and ls1[1] in ls2:
                    for y in range(len(ls5)):
                        if ls5[y]=="mov":
                            if ls5[y+1]=="r16,m16":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                elif ls1[0] in arr8 and ls1[1] in ls2:
                    for y in range(len(ls5)):
                        if ls5[y]=="mov":
                            if ls5[y+1]=="r8,m8":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                elif ls1[0] in arr32 and ls1[1] in ls3:
                    for y in range(len(ls5)):
                        if ls5[y]=="mov":
                            if ls5[y+1]=="r32,i32":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                elif ls1[0] in arr16 and ls1[1] in ls3:
                    for y in range(len(ls5)):
                        if ls5[y]=="mov":
                            if ls5[y+1]=="r16,i16":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                elif ls1[0] in arr8 and ls1[1] in ls3:
                    for y in range(len(ls5)):
                        if ls5[y]=="mov":
                            if ls5[y+1]=="r8,i8":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                elif ls1[0] in ls2 and ls1[1] in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="mov":
                            if ls5[y+1]=="m32,r32":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                elif ls1[0] in ls2 and ls1[1] in arr16:
                    for y in range(len(ls5)):
                        if ls5[y]=="mov":
                            if ls5[y+1]=="m16,r16":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                elif ls1[0] in ls2 and ls1[1] in arr8:
                    for y in range(len(ls5)):
                        if ls5[y]=="mov":
                            if ls5[y+1]=="m8,r8":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                elif ls1[0] in ls2 and ls1[1] in ls3:
                    for y in range(len(ls5)):
                        if ls5[y]=="mov":
                            if ls5[y+1]=="m,i":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                        
                
                if ls1[0] in ls4:
                    for z in range(len(ls4)):
                        if ls1[0]==ls4[z]:
                            fo.write("reg#")
                            fo.write(str(ls4[z+1]))
                            fo.write("\t")
                if ls1[1] in ls4:
                    for z in range(len(ls4)):
                        if ls1[1]==ls4[z]:
                            fo.write("reg#")
                            fo.write(str(ls4[z]))
                            fo.write("\t")
                            #address='{0:04}'.format(address)
                            fo.write(str(address))
                            fo.write("\t")
                            #fo.write(str(ln))
                            fo.write("\n")
                elif ls1[0] in ls2:
                    for p in range(l2):
                        if ls2[p]==ls1[1]:
                            n=ls2[p+1]
                    fo.write("sym#")
                    fo.write(str(n))
                    fo.write("\t")
                elif ls1[1] in ls2:
                    for p in range(l2):
                        if ls2[p]==ls1[1]:
                            n=ls2[p+1]
                    fo.write("sym#")
                    fo.write(str(n))
                    fo.write("\t")
                    #address='{0:04}'.format(address)
                    fo.write(str(address))
                    fo.write("\t")
                    #fo.write(str(ln))
                    fo.write("\n")
                elif ls1[0] in ls3:
                    for q in range(ln3):
                        if ls3[q]==ls1[0]:
                            a=ls3[q+1]
                    fo.write("lit#")
                    fo.write(str(a))
                    fo.write("\t")
                elif ls1[1] in ls3:
                    for q in range(ln3):
                        if ls3[q]==ls1[1]:
                            a=ls3[q+1]
                    fo.write("lit#")
                    fo.write(str(a))
                    fo.write("\t")
                    #address='{0:04}'.format(address)
                    fo.write(str(address))
                    fo.write("\t")
                    #fo.write(str(ln))
                    fo.write("\n")
                if ls1[0] in arr32:
                    address+=2
                #else:
                   # address+=4
                elif ls1[0] in arr16:
                    address+=2
                #else:
                 #   address+=4
                elif ls1[0] in arr8:
                    address+=2
                else:
                    address+=4
                if ls1[1] in arr32:
                    address+=2
                #else:
                 #   address+=4
                elif ls1[1] in arr16:
                    address+=2
                #else:
                 #   address+=4
                elif ls1[1] in arr16:
                    address+=2
                else:
                    address+=4

            if ls[i]=="add":
                fo.write(str(cnt))
                fo.write("\t")
                ls1=ls[i+1].split(",")
                if ls1[0] in arr32 and ls1[1] in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="add":
                            if ls5[y+1]=="r32,r32":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                if ls1[0] in arr16 and ls1[1] in arr16:
                    for y in range(len(ls5)):
                        if ls5[y]=="add":
                            if ls5[y+1]=="r16,r16":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                if ls1[0] in arr8 and ls1[1] in arr8:
                    for y in range(len(ls5)):
                        if ls5[y]=="add":
                            if ls5[y+1]=="r8,r8":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                elif ls1[0] in arr32 and ls1[1] in ls2:
                    for y in range(len(ls5)):
                        if ls5[y]=="add":
                            if ls5[y+1]=="r32,m32":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                elif ls1[0] in arr16 and ls1[1] in ls2:
                    for y in range(len(ls5)):
                        if ls5[y]=="add":
                            if ls5[y+1]=="r16,m16":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                elif ls1[0] in arr8 and ls1[1] in ls2:
                    for y in range(len(ls5)):
                        if ls5[y]=="add":
                            if ls5[y+1]=="r8,m8":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                elif ls1[0] in arr32 and ls1[1] in ls3:
                    for y in range(len(ls5)):
                        if ls5[y]=="add":
                            if ls5[y+1]=="r32,i32":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                elif ls1[0] in arr16 and ls1[1] in ls3:
                    for y in range(len(ls5)):
                        if ls5[y]=="add":
                            if ls5[y+1]=="r16,i16":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                elif ls1[0] in arr8 and ls1[1] in ls3:
                    for y in range(len(ls5)):
                        if ls5[y]=="add":
                            if ls5[y+1]=="r8,i8":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                elif ls1[0] in ls2 and ls1[1] in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="add":
                            if ls5[y+1]=="m32,r32":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                elif ls1[0] in ls2 and ls1[1] in arr16:
                    for y in range(len(ls5)):
                        if ls5[y]=="add":
                            if ls5[y+1]=="m16,r16":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                elif ls1[0] in ls2 and ls1[1] in arr8:
                    for y in range(len(ls5)):
                        if ls5[y]=="add":
                            if ls5[y+1]=="m8,r8":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                elif ls1[0] in ls2 and ls1[1] in ls3:
                    for y in range(len(ls5)):
                        if ls5[y]=="add":
                            if ls5[y+1]=="m,i":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                if ls1[0] in ls4:
                    for z in range(len(ls4)):
                        if ls1[0]==ls4[z]:
                            fo.write("reg#")
                            fo.write(str(ls4[z+1]))
                            fo.write("\t")
                if ls1[1] in ls4:
                    for z in range(len(ls4)):
                        if ls1[1]==ls4[z]:
                            fo.write("reg#")
                            fo.write(str(ls4[z+1]))
                            fo.write("\t")
                            #address='{0:04}'.format(address)
                            fo.write(str(address))
                            fo.write("\t")
                            #fo.write(str(ln))
                            fo.write("\n")
                elif ls1[0] in ls2:
                    for p in range(l2):
                        if ls2[p]==ls1[1]:
                            n=ls2[p+1]
                    fo.write("sym#")
                    fo.write(str(n))
                    fo.write("\t")
                elif ls1[1] in ls2:
                    for p in range(l2):
                        if ls2[p]==ls1[1]:
                            n=ls2[p+1]
                    fo.write("sym#")
                    fo.write(str(n))
                    fo.write("\t")
                    #address='{0:04}'.format(address)
                    fo.write(str(address))
                    fo.write("\t")
                    #fo.write(str(ln))
                    fo.write("\n")
                elif ls1[0] in ls3:
                    for q in range(ln3):
                        if ls3[q]==ls1[0]:
                            a=ls3[q+1]
                    fo.write("lit#")
                    fo.write(str(a))
                    fo.write("\t")
                elif ls1[1] in ls3:
                    for q in range(ln3):
                        if ls3[q]==ls1[1]:
                            a=ls3[q+1]
                    fo.write("lit#")
                    fo.write(str(a))
                    fo.write("\t")
                    print(type(address))
                    #address='{0:04}'.format(address)
                    fo.write(str(address))
                    fo.write("\t")
                    #fo.write(str(ln))
                    fo.write("\n")
                if ls1[0] in arr32:
                    address+=2
                #else:
                 #   address+=4
                elif ls1[0] in arr16:
                    address+=2
                #else:
                 #   address+=4
                elif ls1[0] in arr8:
                    address+=2
                else:
                    address+=4
                if ls1[1] in arr32:
                    address+=2
                #else:
                 #   address+=4
                elif ls1[1] in arr16:
                    address+=2
                #else:
                 #   address+=4
                elif ls1[1] in arr8:
                    address+=2
                else:
                    address+=4

            if ls[i]=="sub":
                fo.write(str(cnt))
                fo.write("\t")
                ls1=ls[i+1].split(",")
                if ls1[0] in arr32 and ls1[1] in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="sub":
                            if ls5[y+1]=="r32,r32":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                if ls1[0] in arr16 and ls1[1] in arr16:
                    for y in range(len(ls5)):
                        if ls5[y]=="sub":
                            if ls5[y+1]=="r16,r16":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                if ls1[0] in arr8 and ls1[1] in arr8:
                    for y in range(len(ls5)):
                        if ls5[y]=="sub":
                            if ls5[y+1]=="r8,r8":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                elif ls1[0] in arr32 and ls1[1] in ls2:
                    for y in range(len(ls5)):
                        if ls5[y]=="sub":
                            if ls5[y+1]=="r32,m32":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                elif ls1[0] in arr16 and ls1[1] in ls2:
                    for y in range(len(ls5)):
                        if ls5[y]=="sub":
                            if ls5[y+1]=="r16,m16":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                elif ls1[0] in arr8 and ls1[1] in ls2:
                    for y in range(len(ls5)):
                        if ls5[y]=="sub":
                            if ls5[y+1]=="r8,m8":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                elif ls1[0] in arr32 and ls1[1] in ls3:
                    for y in range(len(ls5)):
                        if ls5[y]=="sub":
                            if ls5[y+1]=="r32,i32":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                elif ls1[0] in arr16 and ls1[1] in ls3:
                    for y in range(len(ls5)):
                        if ls5[y]=="sub":
                            if ls5[y+1]=="r16,i16":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                elif ls1[0] in arr8 and ls1[1] in ls3:
                    for y in range(len(ls5)):
                        if ls5[y]=="sub":
                            if ls5[y+1]=="r8,i8":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                elif ls1[0] in ls2 and ls1[1] in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="sub":
                            if ls5[y+1]=="m32,r32":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                elif ls1[0] in ls2 and ls1[1] in arr16:
                    for y in range(len(ls5)):
                        if ls5[y]=="sub":
                            if ls5[y+1]=="m16,r16":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                elif ls1[0] in ls2 and ls1[1] in arr8:
                    for y in range(len(ls5)):
                        if ls5[y]=="sub":
                            if ls5[y+1]=="m8,r8":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                elif ls1[0] in ls2 and ls1[1] in ls3:
                    for y in range(len(ls5)):
                        if ls5[y]=="sub":
                            if ls5[y+1]=="m,i":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                if ls1[0] in ls4:
                    for z in range(len(ls4)):
                        if ls1[0]==ls4[z]:
                            fo.write("reg#")
                            fo.write(str(ls4[z+1]))
                            fo.write("\t")
                if ls1[1] in ls4:
                    for z in range(len(ls4)):
                        if ls1[1]==ls4[z]:
                            fo.write("reg#")
                            fo.write(str(ls4[z+1]))
                            fo.write("\t")
                            #address='{0:04}'.format(address)
                            fo.write(str(address))
                            fo.write("\t")
                            #fo.write(str(ln))
                            fo.write("\n")
                elif ls1[0] in ls2:
                    for p in range(l2):
                        if ls2[p]==ls1[1]:
                            n=ls2[p+1]
                    fo.write("sym#")
                    fo.write(str(n))
                    fo.write("\t")
                elif ls1[1] in ls2:
                    for p in range(l2):
                        if ls2[p]==ls1[1]:
                            n=ls2[p+1]
                    fo.write("sym#")
                    fo.write(str(n))
                    fo.write("\t")
                    #address='{0:04}'.format(address)
                    fo.write(str(address))
                    fo.write("\t")
                    #fo.write(str(ln))
                    fo.write("\n")
                elif ls1[0] in ls3:
                    for q in range(ln3):
                        if ls3[q]==ls1[0]:
                            a=ls3[q+1]
                    fo.write("lit#")
                    fo.write(str(a))
                    fo.write("\t")
                elif ls1[1] in ls3:
                    for q in range(ln3):
                        if ls3[q]==ls1[1]:
                            a=ls3[q+1]
                    fo.write("lit#")
                    fo.write(str(a))
                    fo.write("\t")
                    print(type(address))
                    #address='{0:04}'.format(address)
                    fo.write(str(address))
                    fo.write("\t")
                    #fo.write(str(ln))
                    fo.write("\n")
                if ls1[0] in arr32:
                    address+=2
                #else:
                 #   address+=4
                elif ls1[0] in arr16:
                    address+=2
                #else:
                 #   address+=4
                elif ls1[0] in arr8:
                    address+=2
                else:
                    address+=4
                if ls1[1] in arr32:
                    address+=2
                #else:
                 #   address+=4
                elif ls1[1] in arr16:
                    address+=2
                #else:
                 #   address+=4
                elif ls1[1] in arr8:
                    address+=2
                else:
                    address+=4         

            if ls[i]=="mult":
                #print(type(address))
                fo.write(str(cnt))
                fo.write("\t")
                #ls1=ls[i+1]
                if ls[i+1] in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="mult":
                            if ls5[y+1]=="r32":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                if ls[i+1] in arr16:
                    for y in range(len(ls5)):
                        if ls5[y]=="mult":
                            if ls5[y+1]=="r16":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                if ls[i+1] in arr8:
                    for y in range(len(ls5)):
                        if ls5[y]=="mult":
                            if ls5[y+1]=="r8":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                        
                if ls[i+1] in ls4:
                    for z in range(len(ls4)):
                        if ls[i+1]==ls4[z]:
                            fo.write("reg#")
                            fo.write(str(ls4[z+1]))
                            fo.write("\t")
                            fo.write("-\t")
                            fo.write(str(address))
                            fo.write("\t")
                            #fo.write(str(ln))
                            fo.write("\n")
                #if ls1[1] in ls4:
                 #   for z in range(len(ls4)):
                  #      if ls1[1]==ls4[z]:
                   #         fo.write("reg#")
                    #        fo.write(str(ls4[z]))
                     #       fo.write("\t\t")
                            #address='{0:04}'.format(address)
                      #      fo.write(str(address))
                       #     fo.write("\n")
                elif ls[i+1] in ls2:
                    for p in range(l2):
                        if ls2[p]==ls[i+1]:
                            n=ls2[p+1]
                    fo.write("sym#")
                    fo.write(str(n))
                    fo.write("\t")
                    fo.write("-\t")
                    fo.write(str(address))
                    fo.write("\t")
                    #fo.write(str(ln))
                    fo.write("\n")
                #elif ls1[1] in ls2:
                 #   for p in range(l2):
                  #      if ls2[p]==ls1[1]:
                   #         n=ls2[p+1]
                   # fo.write("sym#")
                   # fo.write(str(n))
                   # fo.write("\t\t")
                    #address='{0:04}'.format(address)
                    #fo.write(str(address))
                    #fo.write("\n")
                elif ls[i+1] in ls3:
                    for q in range(ln3):
                        if ls3[q]==ls[i+1]:
                            a=ls3[q+1]
                    fo.write("lit#")
                    fo.write(str(a))
                    fo.write("\t")
                    fo.write("-\t")
                    fo.write(str(address))
                    fo.write("\t")
                    #fo.write(str(ln))
                    fo.write("\n")
                #elif ls1[1] in ls3:
                 #   for q in range(ln3):
                  #      if ls3[q]==ls1[1]:
                   #         a=ls3[q+1]
                  #  fo.write("lit#")
                   # fo.write(str(a))
                   # fo.write("\t\t")
                    #address='{0:04}'.format(address)
                    #fo.write(str(address))
                    #fo.write("\n")
                if ls[i+1] in arr32:
                    address+=2
                #else:
                   # address+=4
                elif ls[i+1] in arr16:
                    address+=2
                #else:
                 #   address+=4
                elif ls[i+1] in arr8:
                    address+=2
                #else:
                 #   address+=4
                #if ls1[1] in arr32:
                 #   address+=2
                #else:
                 #   address+=4
                #elif ls1[1] in arr16:
                #    address+=2
                #else:
                 #   address+=4
                #elif ls1[1] in arr16:
                 #   address+=2
                #else:
                    #address+=4

            if ls[i]=="div":
                #print(type(address))
                fo.write(str(cnt))
                fo.write("\t")
                #ls1=ls[i+1]
                if ls[i+1] in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="div":
                            if ls5[y+1]=="r32":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                if ls[i+1] in arr16:
                    for y in range(len(ls5)):
                        if ls5[y]=="div":
                            if ls5[y+1]=="r16":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                if ls[i+1] in arr8:
                    for y in range(len(ls5)):
                        if ls5[y]=="div":
                            if ls5[y+1]=="r8":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                        
                if ls[i+1] in ls4:
                    for z in range(len(ls4)):
                        if ls[i+1]==ls4[z]:
                            fo.write("reg#")
                            fo.write(str(ls4[z+1]))
                            fo.write("\t")
                            fo.write("-\t")
                            fo.write(str(address))
                            fo.write("\t")
                            #fo.write(str(ln))
                            fo.write("\n")
                #if ls1[1] in ls4:
                 #   for z in range(len(ls4)):
                  #      if ls1[1]==ls4[z]:
                   #         fo.write("reg#")
                    #        fo.write(str(ls4[z]))
                     #       fo.write("\t\t")
                            #address='{0:04}'.format(address)
                      #      fo.write(str(address))
                       #     fo.write("\n")
                elif ls[i+1] in ls2:
                    for p in range(l2):
                        if ls2[p]==ls[i+1]:
                            n=ls2[p+1]
                    fo.write("sym#")
                    fo.write(str(n))
                    fo.write("\t")
                    fo.write("-\t")
                    fo.write(str(address))
                    fo.write("\t")
                    #fo.write(str(ln))
                    fo.write("\n")
                #elif ls1[1] in ls2:
                 #   for p in range(l2):
                  #      if ls2[p]==ls1[1]:
                   #         n=ls2[p+1]
                   # fo.write("sym#")
                   # fo.write(str(n))
                   # fo.write("\t\t")
                    #address='{0:04}'.format(address)
                    #fo.write(str(address))
                    #fo.write("\n")
                elif ls[i+1] in ls3:
                    for q in range(ln3):
                        if ls3[q]==ls[i+1]:
                            a=ls3[q+1]
                    fo.write("lit#")
                    fo.write(str(a))
                    fo.write("\t")
                    fo.write("-\t")
                    fo.write(str(address))
                    fo.write("\t")
                    #fo.write(str(ln))
                    fo.write("\n")
                #elif ls1[1] in ls3:
                 #   for q in range(ln3):
                  #      if ls3[q]==ls1[1]:
                   #         a=ls3[q+1]
                  #  fo.write("lit#")
                   # fo.write(str(a))
                   # fo.write("\t\t")
                    #address='{0:04}'.format(address)
                    #fo.write(str(address))
                    #fo.write("\n")
                if ls[i+1] in arr32:
                    address+=2
                #else:
                   # address+=4
                elif ls[i+1] in arr16:
                    address+=2
                #else:
                 #   address+=4
                elif ls[i+1] in arr8:
                    address+=2
               

            if ls[i]=="push":
                #print(type(address))
                fo.write(str(cnt))
                fo.write("\t")
                #ls1=ls[i+1]
                if ls[i+1] in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="push":
                            if ls5[y+1]=="r32":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                if ls[i+1] in arr16:
                    for y in range(len(ls5)):
                        if ls5[y]=="push":
                            if ls5[y+1]=="r16":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                if ls[i+1] in arr8:
                    for y in range(len(ls5)):
                        if ls5[y]=="push":
                            if ls5[y+1]=="r8":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                if ls[i+1] not in arr8 and ls[i+1] not in arr16 and ls[i+1] not in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="push":
                            if ls5[y+1]=="m":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                        
                if ls[i+1] in ls4:
                    for z in range(len(ls4)):
                        if ls[i+1]==ls4[z]:
                            fo.write("reg#")
                            fo.write(str(ls4[z+1]))
                            fo.write("\t")
                            fo.write("-\t")
                            fo.write(str(address))
                            fo.write("\t")
                            #fo.write(str(ln))
                            fo.write("\n")
                #if ls1[1] in ls4:
                 #   for z in range(len(ls4)):
                  #      if ls1[1]==ls4[z]:
                   #         fo.write("reg#")
                    #        fo.write(str(ls4[z]))
                     #       fo.write("\t\t")
                            #address='{0:04}'.format(address)
                      #      fo.write(str(address))
                       #     fo.write("\n")
                elif ls[i+1] in ls2:
                    for p in range(l2):
                        if ls2[p]==ls[i+1]:
                            n=ls2[p+1]
                    fo.write("sym#")
                    fo.write(str(n))
                    fo.write("\t")
                    fo.write("-\t")
                    fo.write(str(address))
                    fo.write("\t")
                    #fo.write(str(ln))
                    fo.write("\n")
        
                if ls[i+1] in arr32:
                    address+=2
                #else:
                   # address+=4
                elif ls[i+1] in arr16:
                    address+=2
                #else:
                 #   address+=4
                elif ls[i+1] in arr8:
                    address+=2
               

            if ls[i]=="pop":
                #print(type(address))
                fo.write(str(cnt))
                fo.write("\t")
                #ls1=ls[i+1]
                if ls[i+1] in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="pop":
                            if ls5[y+1]=="r32":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                if ls[i+1] in arr16:
                    for y in range(len(ls5)):
                        if ls5[y]=="pop":
                            if ls5[y+1]=="r16":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                if ls[i+1] in arr8:
                    for y in range(len(ls5)):
                        if ls5[y]=="pop":
                            if ls5[y+1]=="r8":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                if ls[i+1] not in arr8 and ls[i+1] not in arr16 and ls[i+1] not in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="pop":
                            if ls5[y+1]=="m":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                        
                if ls[i+1] in ls4:
                    for z in range(len(ls4)):
                        if ls[i+1]==ls4[z]:
                            fo.write("reg#")
                            fo.write(str(ls4[z+1]))
                            fo.write("\t")
                            fo.write("-\t")
                            fo.write(str(address))
                            fo.write("\t")
                            #fo.write(str(ln))
                            fo.write("\n")
                elif ls[i+1] in ls2:
                    for p in range(l2):
                        if ls2[p]==ls[i+1]:
                            n=ls2[p+1]
                    fo.write("sym#")
                    fo.write(str(n))
                    fo.write("\t")
                    fo.write("-\t")
                    fo.write(str(address))
                    fo.write("\t")
                    #fo.write(str(ln))
                    fo.write("\n")
            
                if ls[i+1] in arr32:
                    address+=2
                #else:
                   # address+=4
                elif ls[i+1] in arr16:
                    address+=2
                #else:
                 #   address+=4
                elif ls[i+1] in arr8:
                    address+=2

            if ls[i]=="inc":
                #print(type(address))
                fo.write(str(cnt))
                fo.write("\t")
                #ls1=ls[i+1]
                if ls[i+1] in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="inc":
                            if ls5[y+1]=="r32":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                if ls[i+1] in arr16:
                    for y in range(len(ls5)):
                        if ls5[y]=="inc":
                            if ls5[y+1]=="r16":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                if ls[i+1] in arr8:
                    for y in range(len(ls5)):
                        if ls5[y]=="inc":
                            if ls5[y+1]=="r8":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                        
                if ls[i+1] in ls4:
                    for z in range(len(ls4)):
                        if ls[i+1]==ls4[z]:
                            fo.write("reg#")
                            fo.write(str(ls4[z+1]))
                            fo.write("\t")
                            fo.write("-\t")
                            fo.write(str(address))
                            fo.write("\t")
                            #fo.write(str(ln))
                            fo.write("\n")
               
                if ls[i+1] in arr32:
                    address+=2
                #else:
                   # address+=4
                elif ls[i+1] in arr16:
                    address+=2
                #else:
                 #   address+=4
                elif ls[i+1] in arr8:
                    address+=2
            

            if ls[i]=="dec":
                #print(type(address))
                fo.write(str(cnt))
                fo.write("\t")
                #ls1=ls[i+1]
                if ls[i+1] in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="dec":
                            if ls5[y+1]=="r32":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                if ls[i+1] in arr16:
                    for y in range(len(ls5)):
                        if ls5[y]=="dec":
                            if ls5[y+1]=="r16":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                if ls[i+1] in arr8:
                    for y in range(len(ls5)):
                        if ls5[y]=="dec":
                            if ls5[y+1]=="r8":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                        
                if ls[i+1] in ls4:
                    for z in range(len(ls4)):
                        if ls[i+1]==ls4[z]:
                            fo.write("reg#")
                            fo.write(str(ls4[z+1]))
                            fo.write("\t")
                            fo.write("-\t")
                            fo.write(str(address))
                            fo.write("\t")
                            #fo.write(str(ln))
                            fo.write("\n")
                
                if ls[i+1] in arr32:
                    address+=2
                #else:
                   # address+=4
                elif ls[i+1] in arr16:
                    address+=2
                #else:
                 #   address+=4
                elif ls[i+1] in arr8:
                    address+=2

            if ls[i]=="xor":
                #print(type(address))
                fo.write(str(cnt))
                fo.write("\t")
                #ls1=ls[i+1]
                if ls[i+1] in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="xor":
                            if ls5[y+1]=="r32":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                if ls[i+1] in arr16:
                    for y in range(len(ls5)):
                        if ls5[y]=="xor":
                            if ls5[y+1]=="r16":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                if ls[i+1] in arr8:
                    for y in range(len(ls5)):
                        if ls5[y]=="xor":
                            if ls5[y+1]=="r8":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                        
                if ls[i+1] in ls4:
                    for z in range(len(ls4)):
                        if ls[i+1]==ls4[z]:
                            fo.write("reg#")
                            fo.write(str(ls4[z+1]))
                            fo.write("\t")
                            fo.write("-\t")
                            fo.write(str(address))
                            fo.write("\t")
                            #fo.write(str(ln))
                            fo.write("\n")
               
                if ls[i+1] in arr32:
                    address+=2
                #else:
                   # address+=4
                elif ls[i+1] in arr16:
                    address+=2
                #else:
                 #   address+=4
                elif ls[i+1] in arr8:
                    address+=2

            if ls[i]=="or":
                #print(type(address))
                fo.write(str(cnt))
                fo.write("\t")
                #ls1=ls[i+1]
                if ls[i+1] in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="or":
                            if ls5[y+1]=="r32":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                if ls[i+1] in arr16:
                    for y in range(len(ls5)):
                        if ls5[y]=="or":
                            if ls5[y+1]=="r16":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                if ls[i+1] in arr8:
                    for y in range(len(ls5)):
                        if ls5[y]=="or":
                            if ls5[y+1]=="r8":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                        
                if ls[i+1] in ls4:
                    for z in range(len(ls4)):
                        if ls[i+1]==ls4[z]:
                            fo.write("reg#")
                            fo.write(str(ls4[z+1]))
                            fo.write("\t")
                            fo.write("-\t")
                            fo.write(str(address))
                            fo.write("\t")
                            #fo.write(str(ln))
                            fo.write("\n")
               
                if ls[i+1] in arr32:
                    address+=2
                #else:
                   # address+=4
                elif ls[i+1] in arr16:
                    address+=2
                #else:
                 #   address+=4
                elif ls[i+1] in arr8:
                    address+=2

            if ls[i]=="and":
                #print(type(address))
                fo.write(str(cnt))
                fo.write("\t")
                #ls1=ls[i+1]
                if ls[i+1] in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="and":
                            if ls5[y+1]=="r32":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                if ls[i+1] in arr16:
                    for y in range(len(ls5)):
                        if ls5[y]=="and":
                            if ls5[y+1]=="r16":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                if ls[i+1] in arr8:
                    for y in range(len(ls5)):
                        if ls5[y]=="and":
                            if ls5[y+1]=="r8":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                        
                if ls[i+1] in ls4:
                    for z in range(len(ls4)):
                        if ls[i+1]==ls4[z]:
                            fo.write("reg#")
                            fo.write(str(ls4[z+1]))
                            fo.write("\t")
                            fo.write("-\t")
                            fo.write(str(address))
                            fo.write("\t")
                            #fo.write(str(ln))
                            fo.write("\n")
               
                if ls[i+1] in arr32:
                    address+=2
                #else:
                   # address+=4
                elif ls[i+1] in arr16:
                    address+=2
                #else:
                 #   address+=4
                elif ls[i+1] in arr8:
                    address+=2


            if ls[i]=="jmp":
                #print(type(address))
                fo.write(str(cnt))
                fo.write("\t")
                #ls1=ls[i+1]
                for y in range(len(ls5)):
                    if ls5[y]=="jmp":
                        fo.write("op#")
                        fo.write(str(ls5[y+1]))
                        fo.write("\t\t")
                        
                if ls[i+1] in ls2:
                    for z in range(len(ls2)):
                        if ls[i+1]==ls2[z]:
                            fo.write("sym#")
                            fo.write(str(ls2[z+1]))
                            fo.write("\t")
                            fo.write("-\t")
                            fo.write(str(address))
                            fo.write("\t")
                            #fo.write(str(ln))
                            fo.write("\n")
               
                if ls[i+1] in arr32:
                    address+=2
                #else:
                   # address+=4
                elif ls[i+1] in arr16:
                    address+=2
                #else:
                 #   address+=4
                elif ls[i+1] in arr8:
                    address+=2

            if ls[i]=="jne":
                #print(type(address))
                fo.write(str(cnt))
                fo.write("\t")
                #ls1=ls[i+1]
                for y in range(len(ls5)):
                    if ls5[y]=="jne":
                        fo.write("op#")
                        fo.write(str(ls5[y+1]))
                        fo.write("\t\t")
                        
                if ls[i+1] in ls2:
                    for z in range(len(ls2)):
                        if ls[i+1]==ls2[z]:
                            fo.write("sym#")
                            fo.write(str(ls2[z+1]))
                            fo.write("\t")
                            fo.write("-\t")
                            fo.write(str(address))
                            fo.write("\t")
                            #fo.write(str(ln))
                            fo.write("\n")
                
                            
                if ls[i+1] in arr32:
                    address+=2
                #else:
                   # address+=4
                elif ls[i+1] in arr16:
                    address+=2
                #else:
                 #   address+=4
                elif ls[i+1] in arr8:
                    address+=2

            if ls[i]=="je":
                #print(type(address))
                fo.write(str(cnt))
                fo.write("\t")
                #ls1=ls[i+1]
                for y in range(len(ls5)):
                    if ls5[y]=="je":
                        fo.write("op#")
                        fo.write(str(ls5[y+1]))
                        fo.write("\t\t")
                        
                if ls[i+1] in ls2:
                    for z in range(len(ls2)):
                        if ls[i+1]==ls2[z]:
                            fo.write("sym#")
                            fo.write(str(ls2[z+1]))
                            fo.write("\t")
                            fo.write("-\t")
                            fo.write(str(address))
                            fo.write("\t")
                            #fo.write(str(ln))
                            fo.write("\n")
                
                            
                if ls[i+1] in arr32:
                    address+=2
                #else:
                   # address+=4
                elif ls[i+1] in arr16:
                    address+=2
                #else:
                 #   address+=4
                elif ls[i+1] in arr8:
                    address+=2

            if ls[i]=="jge":
                #print(type(address))
                fo.write(str(cnt))
                fo.write("\t")
                #ls1=ls[i+1]
                for y in range(len(ls5)):
                    if ls5[y]=="jge":
                        fo.write("op#")
                        fo.write(str(ls5[y+1]))
                        fo.write("\t\t")
                        
                if ls[i+1] in ls2:
                    for z in range(len(ls2)):
                        if ls[i+1]==ls2[z]:
                            fo.write("sym#")
                            fo.write(str(ls2[z+1]))
                            fo.write("\t")
                            fo.write("-\t")
                            fo.write(str(address))
                            fo.write("\t")
                            #fo.write(str(ln))
                            fo.write("\n")
                
                            
                if ls[i+1] in arr32:
                    address+=2
                #else:
                   # address+=4
                elif ls[i+1] in arr16:
                    address+=2
                #else:
                 #   address+=4
                elif ls[i+1] in arr8:
                    address+=2

            if ls[i]=="jg":
                #print(type(address))
                fo.write(str(cnt))
                fo.write("\t")
                #ls1=ls[i+1]
                for y in range(len(ls5)):
                    if ls5[y]=="jg":
                        fo.write("op#")
                        fo.write(str(ls5[y+1]))
                        fo.write("\t\t")
                        
                if ls[i+1] in ls2:
                    for z in range(len(ls2)):
                        if ls[i+1]==ls2[z]:
                            fo.write("sym#")
                            fo.write(str(ls2[z+1]))
                            fo.write("\t")
                            fo.write("-\t")
                            fo.write(str(address))
                            fo.write("\t")
                            #fo.write(str(ln))
                            fo.write("\n")
                
                            
                if ls[i+1] in arr32:
                    address+=2
                #else:
                   # address+=4
                elif ls[i+1] in arr16:
                    address+=2
                #else:
                 #   address+=4
                elif ls[i+1] in arr8:
                    address+=2

            if ls[i]=="jle":
                #print(type(address))
                fo.write(str(cnt))
                fo.write("\t")
                #ls1=ls[i+1]
                for y in range(len(ls5)):
                    if ls5[y]=="jle":
                        fo.write("op#")
                        fo.write(str(ls5[y+1]))
                        fo.write("\t\t")
                        
                if ls[i+1] in ls2:
                    for z in range(len(ls2)):
                        if ls[i+1]==ls2[z]:
                            fo.write("sym#")
                            fo.write(str(ls2[z+1]))
                            fo.write("\t")
                            fo.write("-\t")
                            fo.write(str(address))
                            fo.write("\t")
                            #fo.write(str(ln))
                            fo.write("\n")
                
                            
                if ls[i+1] in arr32:
                    address+=2
                #else:
                   # address+=4
                elif ls[i+1] in arr16:
                    address+=2
                #else:
                 #   address+=4
                elif ls[i+1] in arr8:
                    address+=2

            if ls[i]=="jl":
                #print(type(address))
                fo.write(str(cnt))
                fo.write("\t")
                #ls1=ls[i+1]
                for y in range(len(ls5)):
                    if ls5[y]=="jl":
                        fo.write("op#")
                        fo.write(str(ls5[y+1]))
                        fo.write("\t\t")
                        
                if ls[i+1] in ls2:
                    for z in range(len(ls2)):
                        if ls[i+1]==ls2[z]:
                            fo.write("sym#")
                            fo.write(str(ls2[z+1]))
                            fo.write("\t")
                            fo.write("-\t")
                            fo.write(str(address))
                            fo.write("\t")
                            #fo.write(str(ln))
                            fo.write("\n")
                
                            
                if ls[i+1] in arr32:
                    address+=2
                #else:
                   # address+=4
                elif ls[i+1] in arr16:
                    address+=2
                #else:
                 #   address+=4
                elif ls[i+1] in arr8:
                    address+=2

            if ls[i]=="jz":
                #print(type(address))
                fo.write(str(cnt))
                fo.write("\t")
                #ls1=ls[i+1]
                for y in range(len(ls5)):
                    if ls5[y]=="jz":
                        fo.write("op#")
                        fo.write(str(ls5[y+1]))
                        fo.write("\t\t")
                        
                if ls[i+1] in ls2:
                    for z in range(len(ls2)):
                        if ls[i+1]==ls2[z]:
                            fo.write("sym#")
                            fo.write(str(ls2[z+1]))
                            fo.write("\t")
                            fo.write("-\t")
                            fo.write(str(address))
                            fo.write("\t")
                            #fo.write(str(ln))
                            fo.write("\n")
                
                            
                if ls[i+1] in arr32:
                    address+=2
                #else:
                   # address+=4
                elif ls[i+1] in arr16:
                    address+=2
                #else:
                 #   address+=4
                elif ls[i+1] in arr8:
                    address+=2

            if ls[i]=="rep":
                fo.write(str(cnt))
                fo.write("\t")
                for q in range(len(ls5)):
                    if ls[i+1]==ls5[q] and ls5[q-1]=="rep":
                        fo.write("op#")
                        fo.write(str(ls5[q+1]))
                        fo.write("\t\t-\t-\t")
                        fo.write(str(address))
                        fo.write("\t")
                        #fo.write(str(ln))
                        fo.write("\n")
                        break
                if ls[i+1] in arrs32:
                    address+=8
                elif ls[i+1] in arrs16:
                    address+=4
                elif ls[i+1] in arrs8:
                    address+=2
                            


            if ls[i]=="repe":
                fo.write(str(cnt))
                fo.write("\t")
                for q in range(len(ls5)):
                    if ls[i+1]==ls5[q] and ls5[q-1]=="repe":
                        fo.write("op#")
                        fo.write(str(ls5[q+1]))
                        fo.write("\t\t-\t-\t")
                        fo.write(str(address))
                        fo.write("\t")
                        #fo.write(str(ln))
                        fo.write("\n")
                        break
                if ls[i+1] in arrs32:
                    address+=8
                elif ls[i+1] in arrs16:
                    address+=4
                elif ls[i+1] in arrs8:
                    address+=2

            if ls[i]=="repne":
                fo.write(str(cnt))
                fo.write("\t")
                for q in range(len(ls5)):
                    if ls[i+1]==ls5[q] and ls5[q-1]=="repne":
                        fo.write("op#")
                        fo.write(str(ls5[q+1]))
                        fo.write("\t\t-\t-\t")
                        fo.write(str(address))
                        fo.write("\t")
                        #fo.write(str(ln))
                        fo.write("\n")
                        break
                if ls[i+1] in arrs32:
                    address+=8
                elif ls[i+1] in arrs16:
                    address+=4
                elif ls[i+1] in arrs8:
                    address+=2

            if ls[i]=="repz":
                fo.write(str(cnt))
                fo.write("\t")
                for q in range(len(ls5)):
                    if ls[i+1]==ls5[q] and ls5[q-1]=="repz":
                        fo.write("op#")
                        fo.write(str(ls5[q+1]))
                        fo.write("\t\t-\t-\t")
                        fo.write(str(address))
                        fo.write("\t")
                        #fo.write(str(ln))
                        fo.write("\n")
                        break
                if ls[i+1] in arrs32:
                    address+=8
                elif ls[i+1] in arrs16:
                    address+=4
                elif ls[i+1] in arrs8:
                    address+=2

            if ls[i]=="repnz":
                fo.write(str(cnt))
                fo.write("\t")
                for q in range(len(ls5)):
                    if ls[i+1]==ls5[q] and ls5[q-1]=="repnz":
                        fo.write("op#")
                        fo.write(str(ls5[q+1]))
                        fo.write("\t\t-\t-\t")
                        fo.write(str(address))
                        fo.write("\t")
                        #fo.write(str(ln))
                        fo.write("\n")
                        break
                if ls[i+1] in arrs32:
                    address+=8
                elif ls[i+1] in arrs16:
                    address+=4
                elif ls[i+1] in arrs8:
                    address+=2

            if ls[i]=="call":
                fo.write(str(cnt))
                fo.write("\t")
                fo.write("op#")
                if ls[i] in ls5:
                    for k in range(len(ls5)):
                        if ls5[k]==ls[i]:
                            fo.write(str(ls5[k+1]))
                            fo.write("\t\t-\t-\t")
                            fo.write(str(address))
                            fo.write("\t")
                            fo.write("\n")
                            #fo.write(str(ln))
           
        ln=fi1.readline()
        ls=ln.split()
        #ls2=lo.split()
        l=len(ls)

   

def repl(s):
    for i in s:
        if i=="x":
            s=s.replace(i,"0")
    return s.upper()
def caladdr(s):
    cn=0
    ls=["[","]","(",")"]
    for i in s:
        if i not in ls:
            cn+=1
    c=cn/2
    return int(c)
def trans1(s1,s2,s3,s4,s5,s6):
    n=0
    a=0
    flag=0
    #address=0000
    fi1=open(s1,"r")
    fi2=open(s2,"r")
    fi3=open(s3,"r")
    fi4=open(s4,"r")
    fi5=open(s5,"r")
    fi6=open(s6,"r")
    fo=open("opcode2.txt","w")
    ln=fi1.readline()
    lo=fi2.read()
    l3=fi3.read()
    l4=fi4.read()
    l5=fi5.read()
    l6=fi6.read()
    ls3=l3.split()
    ls4=l4.split()
    ls5=l5.split()
    ls6=l6.split()
    ls=ln.split()
    ls2=lo.split()
    l=len(ls)
    l2=len(ls2)
    ln3=len(ls3)
    cnt=0
    address=0
    ad=[]
    #fo.write("\t\t\t\tOPCODE\n")
    #fo.write("LINE NO.\tOPERATION\tOPERAND_1\tOPERAND_2\tADDRESS\n")
    while ln!="":
        cnt+=1
        if ln==" ":
            fo.write("\t")
            fo.write(str(cnt))
        for i in range(l):
            if ls[i]=="section":
                fo.write("\t")
                fo.write(str(cnt))
                fo.write(" ")
                fo.write("\t \t\t\t")
                fo.write(str(ln))
                #fo.write("\n")
            if ls[i]=="dd":
                fo.write("\t")
                fo.write(str(cnt))
                fo.write(" ")
                if ls[i-1] in ls2:
                    for k in range(len(ls2)):
                        if ls2[k]==ls[i-1]:
                            fo.write(str(ls2[k+5]).zfill(8))
                            fo.write(" ")
                            fo.write(str(ls[i+1]).zfill(8))
                            fo.write("\t\t")
                            fo.write(str(ln))
                            #fo.write("\n")

            #if ls[i]=="  ":
             #   fo.write("\t")
              #  fo.write(str(cnt))
                

            if ls[i]=="db":
                fo.write("\t")
                fo.write(str(cnt))
                fo.write(" ")
                if ls[i-1] in ls2:
                    for k in range(len(ls2)):
                        if ls2[k]==ls[i-1]:
                            fo.write(str(ls2[k+5]).zfill(8))
                            fo.write(" ")
                            fo.write(str(1000).zfill(8))
                            fo.write("\t\t")
                            fo.write(str(ln))
                            #fo.write("\n")

            if ls[i]=="resd":
                fo.write("\t")
                fo.write(str(cnt))
                fo.write(" ")
                if ls[i-1] in ls2:
                    for k in range(len(ls2)):
                        if ls2[k]==ls[i-1]:
                            fo.write(str(ls2[k+5]).zfill(8))
                            fo.write(" ")
                            fo.write("<res ")
                            fo.write(str(int(ls[i+1])*4).zfill(8))
                            fo.write(">")
                            fo.write("\t")
                            fo.write(str(ln))
                            #fo.write("\n")

            if ls[i]=="resb":
                fo.write("\t")
                fo.write(str(cnt))
                fo.write(" ")
                if ls[i-1] in ls2:
                    for k in range(len(ls2)):
                        if ls2[k]==ls[i-1]:
                            fo.write(str(ls2[k+5]).zfill(8))
                            fo.write(" ")
                            fo.write("<res ")
                            fo.write(str(int(ls[i+1])*1).zfill(8))
                            fo.write(">")
                            fo.write("\t")
                            fo.write(str(ln))
                            #fo.write("\n")

            if ls[i]=="global":
                fo.write("\t")
                fo.write(str(cnt))
                fo.write(" ")
                fo.write("\t \t\t\t")
                fo.write(str(ln))
                #fo.write("\n")

            if ls[i]=="extern":
                fo.write("\t")
                fo.write(str(cnt))
                fo.write(" ")
                fo.write("\t \t\t\t")
                fo.write(str(ln))
                #fo.write("\n")

            if ls[i]=="main:":
                fo.write("\t")
                fo.write(str(cnt))
                fo.write(" ")
                fo.write("\t \t\t\t")
                fo.write(str(ln))
                #fo.write("\n")

                            
            if ls[i]=="mov":
                #print(type(address))
                fo.write("\t")
                fo.write(str(cnt))
                fo.write(" ")
                fo.write(repl(str(hex(address)).zfill(8)))
                fo.write(" ")
                ls1=ls[i+1].split(",")
                if ls1[0] in arr32 and ls1[1] in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="mov":
                            if ls5[y+1]=="r32,r32":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                for k in range(len(ls6)):
                                    if ls6[k]==ls1[0]:
                                        if ls6[k+1]==ls1[1]:
                                            fo.write(str(ls6[k+2]))
                                            ad.append(ls6[k+2])
                                            fo.write("\t")
                                            fo.write(str(ln))
                                #fo.write("\t\t")
                if ls1[0] in arr16 and ls1[1] in arr16:
                    for y in range(len(ls5)):
                        if ls5[y]=="mov":
                            if ls5[y+1]=="r16,r16":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                for k in range(len(ls6)):
                                    if ls6[k]==ls1[0]:
                                        if ls6[k+1]==ls1[1]:
                                            fo.write(str(ls6[k+2]))
                                            ad.append(ls6[k+2])
                                            fo.write("\t")
                                            fo.write(str(ln))
                                #fo.write("\t\t")
                if ls1[0] in arr8 and ls1[1] in arr8:
                    for y in range(len(ls5)):
                        if ls5[y]=="mov":
                            if ls5[y+1]=="r8,r8":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                for k in range(len(ls6)):
                                    if ls6[k]==ls1[0]:
                                        if ls6[k+1]==ls1[1]:
                                            fo.write(str(ls6[k+2]))
                                            ad.append(ls6[k+2])
                                            fo.write("\t")
                                            fo.write(str(ln))
                                #fo.write("\t\t")
                elif ls1[0] in arr32 and ls1[1] in ls2:
                    for y in range(len(ls5)):
                        if ls5[y]=="mov":
                            if ls5[y+1]=="r32,m32":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                fo.write("[")
                                for k in range(len(ls2)):
                                    if ls2[k]==ls1[1]:
                                        fo.write(str(ls2[k+5]).zfill(8))
                                        ad.append("00000000")
                                        fo.write("]")
                                        fo.write("\t")
                                        fo.write(str(ln))
                                #fo.write("\t\t")
                elif ls1[0] in arr16 and ls1[1] in ls2:
                    for y in range(len(ls5)):
                        if ls5[y]=="mov":
                            if ls5[y+1]=="r16,m16":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                fo.write("[")
                                for k in range(len(ls2)):
                                    if ls2[k]==ls1[1]:
                                        fo.write(str(ls2[k+5]).zfill(8))
                                        ad.append("00000000")
                                        fo.write("]")
                                        fo.write("\t")
                                        fo.write(str(ln))
                                #fo.write("\t\t")
                elif ls1[0] in arr8 and ls1[1] in ls2:
                    for y in range(len(ls5)):
                        if ls5[y]=="mov":
                            if ls5[y+1]=="r8,m8":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                fo.write("[")
                                for k in range(len(ls2)):
                                    if ls2[k]==ls1[1]:
                                        fo.write(str(ls2[k+5]).zfill(8))
                                        ad.append("00000000")
                                        fo.write("]")
                                        fo.write("\t")
                                        fo.write(str(ln))
                                #fo.write("\t\t")
                elif ls1[0] in arr32 and ls1[1] in ls3:
                    for y in range(len(ls5)):
                        if ls5[y]=="mov":
                            if ls5[y+1]=="r32,i32":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                fo.write("\t\t")
                elif ls1[0] in arr16 and ls1[1] in ls3:
                    for y in range(len(ls5)):
                        if ls5[y]=="mov":
                            if ls5[y+1]=="r16,i16":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                fo.write("\t\t")
                elif ls1[0] in arr8 and ls1[1] in ls3:
                    for y in range(len(ls5)):
                        if ls5[y]=="mov":
                            if ls5[y+1]=="r8,i8":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                fo.write("\t\t")
                elif ls1[0] in ls2 and ls1[1] in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="mov":
                            if ls5[y+1]=="m32,r32":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                elif ls1[0] in ls2 and ls1[1] in arr16:
                    for y in range(len(ls5)):
                        if ls5[y]=="mov":
                            if ls5[y+1]=="m16,r16":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                elif ls1[0] in ls2 and ls1[1] in arr8:
                    for y in range(len(ls5)):
                        if ls5[y]=="mov":
                            if ls5[y+1]=="m8,r8":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                elif ls1[0] in ls2 and ls1[1] in ls3:
                    for y in range(len(ls5)):
                        if ls5[y]=="mov":
                            if ls5[y+1]=="m,i":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                        
                #print(ad)
                addd="".join(ad)
                address=caladdr(addd)
                #if ls1[0] in arr32:
                 #   address+=2
                #else:
                   # address+=4
                #elif ls1[0] in arr16:
                 #   address+=2
                #else:
                 #   address+=4
                #elif ls1[0] in arr8:
                  #  address+=2
                #else:
                 #   address+=4
                #if ls1[1] in arr32:
                  #  address+=2
                #else:
                 #   address+=4
                #elif ls1[1] in arr16:
                   # address+=2
                #else:
                 #   address+=4
                #elif ls1[1] in arr16:
                 #   address+=2
                #else:
                 #   address+=4
                #fo.write(str(ln))


            if ls[i]=="add":
                #print(type(address))
                fo.write("\t")
                fo.write(str(cnt))
                fo.write(" ")
                fo.write(repl(str(hex(address)).zfill(8)))
                fo.write(" ")
                ls1=ls[i+1].split(",")
                if ls1[0] in arr32 and ls1[1] in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="add":
                            if ls5[y+1]=="r32,r32":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                for k in range(len(ls6)):
                                    if ls6[k]==ls1[0]:
                                        if ls6[k+1]==ls1[1]:
                                            fo.write(str(ls6[k+2]))
                                            ad.append(ls6[k+2])
                                            fo.write("\t\t")
                                            fo.write(str(ln))
                                #fo.write("\t\t")
                if ls1[0] in arr16 and ls1[1] in arr16:
                    for y in range(len(ls5)):
                        if ls5[y]=="add":
                            if ls5[y+1]=="r16,r16":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                for k in range(len(ls6)):
                                    if ls6[k]==ls1[0]:
                                        if ls6[k+1]==ls1[1]:
                                            fo.write(str(ls6[k+2]))
                                            ad.append(ls6[k+2])
                                            fo.write("\t\t")
                                            fo.write(str(ln))
                                #fo.write("\t\t")
                if ls1[0] in arr8 and ls1[1] in arr8:
                    for y in range(len(ls5)):
                        if ls5[y]=="add":
                            if ls5[y+1]=="r8,r8":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                for k in range(len(ls6)):
                                    if ls6[k]==ls1[0]:
                                        if ls6[k+1]==ls1[1]:
                                            fo.write(str(ls6[k+2]))
                                            ad.append(ls6[k+2])
                                            fo.write("\t\t")
                                            fo.write(str(ln))
                                #fo.write("\t\t")
                elif ls1[0] in arr32 and ls1[1] in ls2:
                    for y in range(len(ls5)):
                        if ls5[y]=="add":
                            if ls5[y+1]=="r32,m32":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                fo.write("[")
                                for k in range(len(ls2)):
                                    if ls2[k]==ls1[1]:
                                        fo.write(str(ls2[k+5]).zfill(8))
                                        ad.append("00000000")
                                        fo.write("]")
                                        fo.write("\t")
                                        fo.write(str(ln))
                                #fo.write("\t\t")
                elif ls1[0] in arr16 and ls1[1] in ls2:
                    for y in range(len(ls5)):
                        if ls5[y]=="add":
                            if ls5[y+1]=="r16,m16":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                fo.write("[")
                                for k in range(len(ls2)):
                                    if ls2[k]==ls1[1]:
                                        fo.write(str(ls2[k+5]).zfill(8))
                                        ad.append("00000000")
                                        fo.write("]")
                                        fo.write("\t")
                                        fo.write(str(ln))
                                #fo.write("\t\t")
                elif ls1[0] in arr8 and ls1[1] in ls2:
                    for y in range(len(ls5)):
                        if ls5[y]=="add":
                            if ls5[y+1]=="r8,m8":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                fo.write("[")
                                for k in range(len(ls2)):
                                    if ls2[k]==ls1[1]:
                                        fo.write(str(ls2[k+5]).zfill(8))
                                        ad.append("00000000")
                                        fo.write("]")
                                        fo.write("\t")
                                        fo.write(str(ln))
                                #fo.write("\t\t")
                elif ls1[0] in arr32 and ls1[1] in ls3:
                    for y in range(len(ls5)):
                        if ls5[y]=="add":
                            if ls5[y+1]=="r32,i32":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                fo.write("\t\t")
                elif ls1[0] in arr16 and ls1[1] in ls3:
                    for y in range(len(ls5)):
                        if ls5[y]=="add":
                            if ls5[y+1]=="r16,i16":
                                fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                fo.write("\t\t")
                elif ls1[0] in arr8 and ls1[1] in ls3:
                    for y in range(len(ls5)):
                        if ls5[y]=="add":
                            if ls5[y+1]=="r8,i8":
                                fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                fo.write("\t\t")
                elif ls1[0] in ls2 and ls1[1] in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="add":
                            if ls5[y+1]=="m32,r32":
                                fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                fo.write("\t\t")
                elif ls1[0] in ls2 and ls1[1] in arr16:
                    for y in range(len(ls5)):
                        if ls5[y]=="add":
                            if ls5[y+1]=="m16,r16":
                                fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                fo.write("\t\t")
                elif ls1[0] in ls2 and ls1[1] in arr8:
                    for y in range(len(ls5)):
                        if ls5[y]=="add":
                            if ls5[y+1]=="m8,r8":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                elif ls1[0] in ls2 and ls1[1] in ls3:
                    for y in range(len(ls5)):
                        if ls5[y]=="add":
                            if ls5[y+1]=="m,i":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                        
                addd="".join(ad)
                address=caladdr(addd)
                #if ls1[0] in arr32:
                 #   address+=2
                #else:
                   # address+=4
                #elif ls1[0] in arr16:
                 #   address+=2
                #else:
                 #   address+=4
                #elif ls1[0] in arr8:
                 #   address+=2
                #else:
                 #   address+=4
                #if ls1[1] in arr32:
                 #   address+=2
                #else:
                 #   address+=4
                #elif ls1[1] in arr16:
                 #   address+=2
                #else:
                 #   address+=4
                #elif ls1[1] in arr16:
                 #   address+=2
                #else:
                 #   address+=4

            if ls[i]=="sub":
                #print(type(address))
                fo.write("\t")
                fo.write(str(cnt))
                fo.write(" ")
                fo.write(repl(str(hex(address)).zfill(8)))
                fo.write(" ")
                ls1=ls[i+1].split(",")
                if ls1[0] in arr32 and ls1[1] in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="sub":
                            if ls5[y+1]=="r32,r32":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                for k in range(len(ls6)):
                                    if ls6[k]==ls1[0]:
                                        if ls6[k+1]==ls1[1]:
                                            fo.write(str(ls6[k+2]))
                                            ad.append(ls6[k+2])
                                            fo.write("\t")
                                            fo.write(str(ln))
                                #fo.write("\t\t")
                if ls1[0] in arr16 and ls1[1] in arr16:
                    for y in range(len(ls5)):
                        if ls5[y]=="sub":
                            if ls5[y+1]=="r16,r16":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                for k in range(len(ls6)):
                                    if ls6[k]==ls1[0]:
                                        if ls6[k+1]==ls1[1]:
                                            fo.write(str(ls6[k+2]))
                                            ad.append(ls6[k+2])
                                            fo.write("\t")
                                            fo.write(str(ln))
                                #fo.write("\t\t")
                if ls1[0] in arr8 and ls1[1] in arr8:
                    for y in range(len(ls5)):
                        if ls5[y]=="sub":
                            if ls5[y+1]=="r8,r8":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                for k in range(len(ls6)):
                                    if ls6[k]==ls1[0]:
                                        if ls6[k+1]==ls1[1]:
                                            fo.write(str(ls6[k+2]))
                                            ad.append(ls6[k+2])
                                            fo.write("\t")
                                            fo.write(str(ln))
                                #fo.write("\t\t")
                elif ls1[0] in arr32 and ls1[1] in ls2:
                    for y in range(len(ls5)):
                        if ls5[y]=="sub":
                            if ls5[y+1]=="r32,m32":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                fo.write("[")
                                for k in range(len(ls2)):
                                    if ls2[k]==ls1[1]:
                                        fo.write(str(ls2[k+5]).zfill(8))
                                        ad.append("00000000")
                                        fo.write("]")
                                        fo.write("\t\t")
                                        fo.write(str(ln))
                                #fo.write("\t\t")
                elif ls1[0] in arr16 and ls1[1] in ls2:
                    for y in range(len(ls5)):
                        if ls5[y]=="sub":
                            if ls5[y+1]=="r16,m16":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                fo.write("[")
                                for k in range(len(ls2)):
                                    if ls2[k]==ls1[1]:
                                        fo.write(str(ls2[k+5]).zfill(8))
                                        ad.append("00000000")
                                        fo.write("]")
                                        fo.write("\t\t")
                                        fo.write(str(ln))
                                #fo.write("\t\t")
                elif ls1[0] in arr8 and ls1[1] in ls2:
                    for y in range(len(ls5)):
                        if ls5[y]=="sub":
                            if ls5[y+1]=="r8,m8":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                fo.write("[")
                                for k in range(len(ls2)):
                                    if ls2[k]==ls1[1]:
                                        fo.write(str(ls2[k+5]).zfill(8))
                                        ad.append("00000000")
                                        fo.write("]")
                                        fo.write("\t\t")
                                        fo.write(str(ln))
                                #fo.write("\t\t")
                elif ls1[0] in arr32 and ls1[1] in ls3:
                    for y in range(len(ls5)):
                        if ls5[y]=="sub":
                            if ls5[y+1]=="r32,i32":
                                fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                fo.write("\t\t")
                elif ls1[0] in arr16 and ls1[1] in ls3:
                    for y in range(len(ls5)):
                        if ls5[y]=="sub":
                            if ls5[y+1]=="r16,i16":
                                fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                fo.write("\t\t")
                elif ls1[0] in arr8 and ls1[1] in ls3:
                    for y in range(len(ls5)):
                        if ls5[y]=="sub":
                            if ls5[y+1]=="r8,i8":
                                fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                fo.write("\t\t")
                elif ls1[0] in ls2 and ls1[1] in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="sub":
                            if ls5[y+1]=="m32,r32":
                                fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                fo.write("\t\t")
                elif ls1[0] in ls2 and ls1[1] in arr16:
                    for y in range(len(ls5)):
                        if ls5[y]=="sub":
                            if ls5[y+1]=="m16,r16":
                                fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                fo.write("\t\t")
                elif ls1[0] in ls2 and ls1[1] in arr8:
                    for y in range(len(ls5)):
                        if ls5[y]=="sub":
                            if ls5[y+1]=="m8,r8":
                                fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                fo.write("\t\t")
                elif ls1[0] in ls2 and ls1[1] in ls3:
                    for y in range(len(ls5)):
                        if ls5[y]=="sub":
                            if ls5[y+1]=="m,i":
                                fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                fo.write("\t\t")
                        
                addd="".join(ad)
                address=caladdr(addd)
                #if ls1[0] in arr32:
                 #   address+=2
                #else:
                   # address+=4
                #elif ls1[0] in arr16:
                 #   address+=2
                #else:
                 #   address+=4
                #elif ls1[0] in arr8:
                 #   address+=2
                #else:
                 #   address+=4
                #if ls1[1] in arr32:
                 #   address+=2
                #else:
                 #   address+=4
                #elif ls1[1] in arr16:
                 #   address+=2
                #else:
                 #   address+=4
                #elif ls1[1] in arr16:
                 #   address+=2
                #else:
                 #   address+=4

            if ls[i]=="push":
                fo.write("\t")
                fo.write(str(cnt))
                fo.write(" ")
                fo.write(repl(str(hex(address)).zfill(8)))
                fo.write(" ")
                if ls[i+1] in arr32:
                    for k in range(len(ls5)):
                        if ls5[k]==ls[i]:
                            if ls5[k+1]=="r32":
                                fo.write(str(ls5[k+3]))
                                ad.append(ls5[k+3])
                                fo.write("\t\t\t")
                                fo.write(str(ln))
                if ls[i+1] in arr16:
                    for k in range(len(ls5)):
                        if ls5[k]==ls[i]:
                            if ls5[k+1]=="r16":
                                fo.write(str(ls5[k+3]))
                                ad.append(ls5[k+3])
                                fo.write("\t\t\t")
                                fo.write(str(ln))
                if ls[i+1] in arr8:
                    for k in range(len(ls5)):
                        if ls5[k]==ls[i]:
                            if ls5[k+1]=="r8":
                                fo.write(str(ls5[k+3]))
                                ad.append(ls5[k+3])
                                fo.write("\t\t\t")
                                fo.write(str(ln))
                if ls[i+1] in ls2:
                    for k in range(len(ls5)):
                        if ls5[k]==ls[i]:
                            if ls5[k+1]=="m":
                                fo.write(str(ls5[k+3]))
                                ad.append(ls5[k+3])
                                fo.write("[")
                    for l in range(len(ls2)):
                        if ls2[l]==ls[i+1]:
                            fo.write(str(ls2[l+5]).zfill(8))
                            ad.append("00000000")
                            fo.write("]")
                            fo.write("\t")
                            fo.write(str(ln))
                addd="".join(ad)
                address=caladdr(addd)

            if ls[i]=="call":
                fo.write("\t")
                fo.write(str(cnt))
                fo.write(" ")
                fo.write(repl(str(hex(address)).zfill(8)))
                fo.write(" ")
                for k in range(len(ls5)):
                    if ls5[k]==ls[i]:
                        fo.write(str(ls5[k+2]))
                        ad.append(ls5[k+2])
                        fo.write("(00000000)\t")
                        ad.append("00000000")
                        fo.write(str(ln))
                addd="".join(ad)
                address=caladdr(addd)


            if ls[i]=="mult":
                fo.write("\t")
                fo.write(str(cnt))
                fo.write(" ")
                fo.write(repl(str(hex(address)).zfill(8)))
                fo.write(" ")
                if ls[i+1] in arr32:
                    for k in range(len(ls5)):
                        if ls5[k]==ls[i]:
                            if ls5[k+1]=="r32":
                                fo.write(str(ls5[k+3]))
                                ad.append(ls5[k+3])
                                fo.write("\t\t\t")
                                fo.write(str(ln))
                if ls[i+1] in arr16:
                    for k in range(len(ls5)):
                        if ls5[k]==ls[i]:
                            if ls5[k+1]=="r16":
                                fo.write(str(ls5[k+3]))
                                ad.append(ls5[k+3])
                                fo.write("\t\t\t")
                                fo.write(str(ln))
                if ls[i+1] in arr8:
                    for k in range(len(ls5)):
                        if ls5[k]==ls[i]:
                            if ls5[k+1]=="r8":
                                fo.write(str(ls5[k+3]))
                                ad.append(ls5[k+3])
                                fo.write("\t\t\t")
                                fo.write(str(ln))
                #if ls[i+1] in ls2:
                 #   for k in range(len(ls5)):
                  #      if ls5[k]==ls[i]:
                   #         if ls5[k+1]=="m":
                    #            fo.write(str(ls5[k+3]))
                     #           ad.append(ls5[k+3])
                      #          fo.write("[")
                    #for l in range(len(ls2)):
                     #   if ls2[l]==ls[i+1]:
                      #      fo.write(str(ls2[l+5]).zfill(8))
                       #     ad.append("00000000")
                       #     fo.write("]")
                        #    fo.write("\t")
                         #   fo.write(str(ln))
                addd="".join(ad)
                address=caladdr(addd)
            

            if ls[i]=="div":
                #print(type(address))
                fo.write(str(cnt))
                fo.write("\t")
                #ls1=ls[i+1]
                if ls[i+1] in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="div":
                            if ls5[y+1]=="r32":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                if ls[i+1] in arr16:
                    for y in range(len(ls5)):
                        if ls5[y]=="div":
                            if ls5[y+1]=="r16":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                if ls[i+1] in arr8:
                    for y in range(len(ls5)):
                        if ls5[y]=="div":
                            if ls5[y+1]=="r8":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\t\t")
                        
                if ls[i+1] in ls4:
                    for z in range(len(ls4)):
                        if ls[i+1]==ls4[z]:
                            fo.write("reg#")
                            fo.write(str(ls4[z+1]))
                            fo.write("\t")
                            fo.write("-\t")
                            fo.write(str(address))
                            fo.write("\n")
                #if ls1[1] in ls4:
                 #   for z in range(len(ls4)):
                  #      if ls1[1]==ls4[z]:
                   #         fo.write("reg#")
                    #        fo.write(str(ls4[z]))
                     #       fo.write("\t\t")
                            #address='{0:04}'.format(address)
                      #      fo.write(str(address))
                       #     fo.write("\n")
                elif ls[i+1] in ls2:
                    for p in range(l2):
                        if ls2[p]==ls[i+1]:
                            n=ls2[p+1]
                    fo.write("sym#")
                    fo.write(str(n))
                    fo.write("\t")
                    fo.write("-\t")
                    fo.write(str(address))
                    fo.write("\n")
                #elif ls1[1] in ls2:
                 #   for p in range(l2):
                  #      if ls2[p]==ls1[1]:
                   #         n=ls2[p+1]
                   # fo.write("sym#")
                   # fo.write(str(n))
                   # fo.write("\t\t")
                    #address='{0:04}'.format(address)
                    #fo.write(str(address))
                    #fo.write("\n")
                elif ls[i+1] in ls3:
                    for q in range(ln3):
                        if ls3[q]==ls[i+1]:
                            a=ls3[q+1]
                    fo.write("lit#")
                    fo.write(str(a))
                    fo.write("\t")
                    fo.write("-\t")
                    fo.write(str(address))
                    fo.write("\n")
                #elif ls1[1] in ls3:
                 #   for q in range(ln3):
                  #      if ls3[q]==ls1[1]:
                   #         a=ls3[q+1]
                  #  fo.write("lit#")
                   # fo.write(str(a))
                   # fo.write("\t\t")
                    #address='{0:04}'.format(address)
                    #fo.write(str(address))
                    #fo.write("\n")
                if ls[i+1] in arr32:
                    address+=2
                #else:
                   # address+=4
                elif ls[i+1] in arr16:
                    address+=2
                #else:
                 #   address+=4
                elif ls[i+1] in arr8:
                    address+=2
               

            if ls[i]=="pop":
                fo.write("\t")
                fo.write(str(cnt))
                fo.write(" ")
                fo.write(repl(str(hex(address)).zfill(8)))
                fo.write(" ")
                if ls[i+1] in arr32:
                    for k in range(len(ls5)):
                        if ls5[k]==ls[i]:
                            if ls5[k+1]=="r32":
                                fo.write(str(ls5[k+3]))
                                ad.append(ls5[k+3])
                                fo.write("\t\t\t")
                                fo.write(str(ln))
                if ls[i+1] in arr16:
                    for k in range(len(ls5)):
                        if ls5[k]==ls[i]:
                            if ls5[k+1]=="r16":
                                fo.write(str(ls5[k+3]))
                                ad.append(ls5[k+3])
                                fo.write("\t\t\t")
                                fo.write(str(ln))
                if ls[i+1] in arr8:
                    for k in range(len(ls5)):
                        if ls5[k]==ls[i]:
                            if ls5[k+1]=="r8":
                                fo.write(str(ls5[k+3]))
                                ad.append(ls5[k+3])
                                fo.write("\t\t\t")
                                fo.write(str(ln))
                if ls[i+1] in ls2:
                    for k in range(len(ls5)):
                        if ls5[k]==ls[i]:
                            if ls5[k+1]=="m":
                                fo.write(str(ls5[k+3]))
                                ad.append(ls5[k+3])
                                fo.write("[")
                    for l in range(len(ls2)):
                        if ls2[l]==ls[i+1]:
                            fo.write(str(ls2[l+5]).zfill(8))
                            ad.append("00000000")
                            fo.write("]")
                            fo.write("\t")
                            fo.write(str(ln))
                addd="".join(ad)
                address=caladdr(addd)


            if ls[i]=="inc":
                #print(type(address))
                fo.write("\t")
                fo.write(str(cnt))
                fo.write(" ")
                fo.write(repl(str(hex(address)).zfill(8)))
                fo.write(" ")
                #ls1=ls[i+1]
                if ls[i+1] in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="inc":
                            if ls5[y+1]=="r32":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                fo.write("\t\t\t")
                                fo.write(str(ln))
                if ls[i+1] in arr16:
                    for y in range(len(ls5)):
                        if ls5[y]=="inc":
                            if ls5[y+1]=="r16":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                fo.write("\t\t\t")
                                fo.write(str(ln))
                if ls[i+1] in arr8:
                    for y in range(len(ls5)):
                        if ls5[y]=="inc":
                            if ls5[y+1]=="r8":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                #fo.write("\t\t\t")
                                fo.write(str(ln))
                if ls[i+1] in ls4:
                    for z in range(len(ls4)):
                        if ls[i+1]==ls4[z]:
                            #fo.write("reg#")
                            fo.write(str(ls4[z+1]))
                            ad.append(ls4[z+1])
                            fo.write("\t\t\t")
                            fo.write(str(ln))

                addd="".join(ad)
                address=caladdr(addd)


            if ls[i]=="dec":
                #print(type(address))
                fo.write("\t")
                fo.write(str(cnt))
                fo.write(" ")
                fo.write(repl(str(hex(address)).zfill(8)))
                fo.write(" ")
                #ls1=ls[i+1]
                if ls[i+1] in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="dec":
                            if ls5[y+1]=="r32":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                fo.write("\t\t\t")
                                fo.write(str(ln))
                if ls[i+1] in arr16:
                    for y in range(len(ls5)):
                        if ls5[y]=="dec":
                            if ls5[y+1]=="r16":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                fo.write("\t\t\t")
                                fo.write(str(ln))
                if ls[i+1] in arr8:
                    for y in range(len(ls5)):
                        if ls5[y]=="dec":
                            if ls5[y+1]=="r8":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                #fo.write("\t\t\t")
                                fo.write(str(ln))
                if ls[i+1] in ls4:
                    for z in range(len(ls4)):
                        if ls[i+1]==ls4[z]:
                            #fo.write("reg#")
                            fo.write(str(ls4[z+1]))
                            ad.append(ls4[z+1])
                            fo.write("\t\t\t")
                            fo.write(str(ln))

                addd="".join(ad)
                address=caladdr(addd)


            if ls[i]=="xor":
                #print(type(address))
                fo.write("\t")
                fo.write(str(cnt))
                fo.write(" ")
                fo.write(repl(str(hex(address)).zfill(8)))
                fo.write(" ")
                #ls1=ls[i+1]
                if ls[i+1] in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="xor":
                            if ls5[y+1]=="r32":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                fo.write("\t\t\t")
                                fo.write(str(ln))
                if ls[i+1] in arr16:
                    for y in range(len(ls5)):
                        if ls5[y]=="xor":
                            if ls5[y+1]=="r16":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                fo.write("\t\t\t")
                                fo.write(str(ln))
                if ls[i+1] in arr8:
                    for y in range(len(ls5)):
                        if ls5[y]=="xor":
                            if ls5[y+1]=="r8":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                #fo.write("\t\t\t")
                                fo.write(str(ln))
                if ls[i+1] in ls4:
                    for z in range(len(ls4)):
                        if ls[i+1]==ls4[z]:
                            #fo.write("reg#")
                            fo.write(str(ls4[z+1]))
                            ad.append(ls4[z+1])
                            fo.write("\t\t\t")
                            fo.write(str(ln))

                addd="".join(ad)
                address=caladdr(addd)

            if ls[i]=="or":
                #print(type(address))
                fo.write("\t")
                fo.write(str(cnt))
                fo.write(" ")
                fo.write(repl(str(hex(address)).zfill(8)))
                fo.write(" ")
                #ls1=ls[i+1]
                if ls[i+1] in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="or":
                            if ls5[y+1]=="r32":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                fo.write("\t\t\t")
                                fo.write(str(ln))
                if ls[i+1] in arr16:
                    for y in range(len(ls5)):
                        if ls5[y]=="or":
                            if ls5[y+1]=="r16":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                fo.write("\t\t\t")
                                fo.write(str(ln))
                if ls[i+1] in arr8:
                    for y in range(len(ls5)):
                        if ls5[y]=="or":
                            if ls5[y+1]=="r8":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                #fo.write("\t\t\t")
                                fo.write(str(ln))
                if ls[i+1] in ls4:
                    for z in range(len(ls4)):
                        if ls[i+1]==ls4[z]:
                            #fo.write("reg#")
                            fo.write(str(ls4[z+1]))
                            ad.append(ls4[z+1])
                            fo.write("\t\t\t")
                            fo.write(str(ln))

                addd="".join(ad)
                address=caladdr(addd)


            if ls[i]=="and":
                #print(type(address))
                fo.write("\t")
                fo.write(str(cnt))
                fo.write(" ")
                fo.write(repl(str(hex(address)).zfill(8)))
                fo.write(" ")
                #ls1=ls[i+1]
                if ls[i+1] in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="and":
                            if ls5[y+1]=="r32":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                fo.write("\t\t\t")
                                fo.write(str(ln))
                if ls[i+1] in arr16:
                    for y in range(len(ls5)):
                        if ls5[y]=="and":
                            if ls5[y+1]=="r16":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                fo.write("\t\t\t")
                                fo.write(str(ln))
                if ls[i+1] in arr8:
                    for y in range(len(ls5)):
                        if ls5[y]=="and":
                            if ls5[y+1]=="r8":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                #fo.write("\t\t\t")
                                fo.write(str(ln))
                if ls[i+1] in ls4:
                    for z in range(len(ls4)):
                        if ls[i+1]==ls4[z]:
                            #fo.write("reg#")
                            fo.write(str(ls4[z+1]))
                            ad.append(ls4[z+1])
                            fo.write("\t\t\t")
                            fo.write(str(ln))

                addd="".join(ad)
                address=caladdr(addd)



            if ls[i]=="jmp":
                fo.write("\t")
                fo.write(str(cnt))
                fo.write(" ")
                fo.write(repl(str(hex(address)).zfill(8)))
                fo.write(" ")
                for y in range(len(ls5)):
                    if ls5[y]=="jmp":
                        #fo.write("op#")
                        fo.write(str(ls5[y+2]))
                        ad.append(ls5[y+2])
                        #fo.write("\t\t")
                        
                if ls[i+1] in ls2:
                    fo.write("[")
                    for z in range(len(ls2)):
                        if ls[i+1]==ls2[z]:
                            #fo.write("sym#")
                            fo.write(str(ls2[z+1]).zfill(8))
                            fo.write("]")
                            fo.write("\t\t")
                            fo.write(str(ln))
                            

                addd="".join(ad)
                address=caladdr(addd)


            if ls[i]=="jne":
                fo.write("\t")
                fo.write(str(cnt))
                fo.write(" ")
                fo.write(repl(str(hex(address)).zfill(8)))
                fo.write(" ")
                for y in range(len(ls5)):
                    if ls5[y]=="jne":
                        #fo.write("op#")
                        fo.write(str(ls5[y+2]))
                        ad.append(ls5[y+2])
                        #fo.write("\t\t")
                        
                if ls[i+1] in ls2:
                    fo.write("[")
                    for z in range(len(ls2)):
                        if ls[i+1]==ls2[z]:
                            #fo.write("sym#")
                            fo.write(str(ls2[z+1]).zfill(8))
                            fo.write("]")
                            fo.write("\t\t")
                            fo.write(str(ln))
                            

                addd="".join(ad)
                address=caladdr(addd)

                
            if ls[i]=="je":
                fo.write("\t")
                fo.write(str(cnt))
                fo.write(" ")
                fo.write(repl(str(hex(address)).zfill(8)))
                fo.write(" ")
                for y in range(len(ls5)):
                    if ls5[y]=="je":
                        #fo.write("op#")
                        fo.write(str(ls5[y+2]))
                        ad.append(ls5[y+2])
                        #fo.write("\t\t")
                        
                if ls[i+1] in ls2:
                    fo.write("[")
                    for z in range(len(ls2)):
                        if ls[i+1]==ls2[z]:
                            #fo.write("sym#")
                            fo.write(str(ls2[z+1]).zfill(8))
                            fo.write("]")
                            fo.write("\t\t")
                            fo.write(str(ln))
                            

                addd="".join(ad)
                address=caladdr(addd)


            if ls[i]=="jge":
                fo.write("\t")
                fo.write(str(cnt))
                fo.write(" ")
                fo.write(repl(str(hex(address)).zfill(8)))
                fo.write(" ")
                for y in range(len(ls5)):
                    if ls5[y]=="jge":
                        #fo.write("op#")
                        fo.write(str(ls5[y+2]))
                        ad.append(ls5[y+2])
                        #fo.write("\t\t")
                        
                if ls[i+1] in ls2:
                    fo.write("[")
                    for z in range(len(ls2)):
                        if ls[i+1]==ls2[z]:
                            #fo.write("sym#")
                            fo.write(str(ls2[z+1]).zfill(8))
                            fo.write("]")
                            fo.write("\t\t")
                            fo.write(str(ln))
                            

                addd="".join(ad)
                address=caladdr(addd)


            if ls[i]=="jg":
                fo.write("\t")
                fo.write(str(cnt))
                fo.write(" ")
                fo.write(repl(str(hex(address)).zfill(8)))
                fo.write(" ")
                for y in range(len(ls5)):
                    if ls5[y]=="jg":
                        #fo.write("op#")
                        fo.write(str(ls5[y+2]))
                        ad.append(ls5[y+2])
                        #fo.write("\t\t")
                        
                if ls[i+1] in ls2:
                    fo.write("[")
                    for z in range(len(ls2)):
                        if ls[i+1]==ls2[z]:
                            #fo.write("sym#")
                            fo.write(str(ls2[z+1]).zfill(8))
                            fo.write("]")
                            fo.write("\t\t")
                            fo.write(str(ln))
                            

                addd="".join(ad)
                address=caladdr(addd)


            if ls[i]=="jle":
                fo.write("\t")
                fo.write(str(cnt))
                fo.write(" ")
                fo.write(repl(str(hex(address)).zfill(8)))
                fo.write(" ")
                for y in range(len(ls5)):
                    if ls5[y]=="jle":
                        #fo.write("op#")
                        fo.write(str(ls5[y+2]))
                        ad.append(ls5[y+2])
                        #fo.write("\t\t")
                        
                if ls[i+1] in ls2:
                    fo.write("[")
                    for z in range(len(ls2)):
                        if ls[i+1]==ls2[z]:
                            #fo.write("sym#")
                            fo.write(str(ls2[z+1]).zfill(8))
                            fo.write("]")
                            fo.write("\t\t")
                            fo.write(str(ln))
                            

                addd="".join(ad)
                address=caladdr(addd)


            if ls[i]=="jl":
                fo.write("\t")
                fo.write(str(cnt))
                fo.write(" ")
                fo.write(repl(str(hex(address)).zfill(8)))
                fo.write(" ")
                for y in range(len(ls5)):
                    if ls5[y]=="jl":
                        #fo.write("op#")
                        fo.write(str(ls5[y+2]))
                        ad.append(ls5[y+2])
                        #fo.write("\t\t")
                        
                if ls[i+1] in ls2:
                    fo.write("[")
                    for z in range(len(ls2)):
                        if ls[i+1]==ls2[z]:
                            #fo.write("sym#")
                            fo.write(str(ls2[z+1]).zfill(8))
                            fo.write("]")
                            fo.write("\t\t")
                            fo.write(str(ln))
                            

                addd="".join(ad)
                address=caladdr(addd)


            if ls[i]=="jz":
                fo.write("\t")
                fo.write(str(cnt))
                fo.write(" ")
                fo.write(repl(str(hex(address)).zfill(8)))
                fo.write(" ")
                for y in range(len(ls5)):
                    if ls5[y]=="jz":
                        #fo.write("op#")
                        fo.write(str(ls5[y+2]))
                        ad.append(ls5[y+2])
                        #fo.write("\t\t")
                        
                if ls[i+1] in ls2:
                    fo.write("[")
                    for z in range(len(ls2)):
                        if ls[i+1]==ls2[z]:
                            #fo.write("sym#")
                            fo.write(str(ls2[z+1]).zfill(8))
                            fo.write("]")
                            fo.write("\t\t")
                            fo.write(str(ln))
                            

                addd="".join(ad)
                address=caladdr(addd)


            if ls[i]=="rep":
                fo.write(str(cnt))
                fo.write("\t")
                for q in range(len(ls5)):
                    if ls[i+1]==ls5[q] and ls5[q-1]=="rep":
                        fo.write("op#")
                        fo.write(str(ls5[q+1]))
                        fo.write("\t\t-\t-\t")
                        fo.write(str(address))
                        fo.write("\n")
                        break
                if ls[i+1] in arrs32:
                    address+=8
                elif ls[i+1] in arrs16:
                    address+=4
                elif ls[i+1] in arrs8:
                    address+=2
                            


            if ls[i]=="repe":
                fo.write(str(cnt))
                fo.write("\t")
                for q in range(len(ls5)):
                    if ls[i+1]==ls5[q] and ls5[q-1]=="repe":
                        fo.write("op#")
                        fo.write(str(ls5[q+1]))
                        fo.write("\t\t-\t-\t")
                        fo.write(str(address))
                        fo.write("\n")
                        break
                if ls[i+1] in arrs32:
                    address+=8
                elif ls[i+1] in arrs16:
                    address+=4
                elif ls[i+1] in arrs8:
                    address+=2

            if ls[i]=="repne":
                fo.write(str(cnt))
                fo.write("\t")
                for q in range(len(ls5)):
                    if ls[i+1]==ls5[q] and ls5[q-1]=="repne":
                        fo.write("op#")
                        fo.write(str(ls5[q+1]))
                        fo.write("\t\t-\t-\t")
                        fo.write(str(address))
                        fo.write("\n")
                        break
                if ls[i+1] in arrs32:
                    address+=8
                elif ls[i+1] in arrs16:
                    address+=4
                elif ls[i+1] in arrs8:
                    address+=2

            if ls[i]=="repz":
                fo.write(str(cnt))
                fo.write("\t")
                for q in range(len(ls5)):
                    if ls[i+1]==ls5[q] and ls5[q-1]=="repz":
                        fo.write("op#")
                        fo.write(str(ls5[q+1]))
                        fo.write("\t\t-\t-\t")
                        fo.write(str(address))
                        fo.write("\n")
                        break
                if ls[i+1] in arrs32:
                    address+=8
                elif ls[i+1] in arrs16:
                    address+=4
                elif ls[i+1] in arrs8:
                    address+=2

            if ls[i]=="repnz":
                fo.write(str(cnt))
                fo.write("\t")
                for q in range(len(ls5)):
                    if ls[i+1]==ls5[q] and ls5[q-1]=="repnz":
                        fo.write("op#")
                        fo.write(str(ls5[q+1]))
                        fo.write("\t\t-\t-\t")
                        fo.write(str(address))
                        fo.write("\n")
                        break
                if ls[i+1] in arrs32:
                    address+=8
                elif ls[i+1] in arrs16:
                    address+=4
                elif ls[i+1] in arrs8:
                    address+=2
            
           
        ln=fi1.readline()
        ls=ln.split()
        #ls2=lo.split()
        l=len(ls)

def add_space(s):
    s1=[s[i:i+2] for i in range(0,len(s),2)]
    r=" ".join(s1)
    return r

def objcode(s1,s2,s3,s4,s5,s6):
    n=0
    a=0
    flag=0
    dataaddr=705600
    bssaddr=805600
    textaddr=905600
    mainaddr=804800
    #address=0000
    fi1=open(s1,"r")
    fi2=open(s2,"r")
    fi3=open(s3,"r")
    fi4=open(s4,"r")
    fi5=open(s5,"r")
    fi6=open(s6,"r")
    fo=open("objcode.txt","w")
    ln=fi1.readline()
    lo=fi2.read()
    l3=fi3.read()
    l4=fi4.read()
    l5=fi5.read()
    l6=fi6.read()
    ls3=l3.split()
    ls4=l4.split()
    ls5=l5.split()
    ls6=l6.split()
    ls=ln.split()
    ls2=lo.split()
    l=len(ls)
    l2=len(ls2)
    ln3=len(ls3)
    cnt=0
    address=0
    ad=[]
    vararr=[]
    while ln!="":
        cnt+=1
        if ln==" ":
            fo.write("\t")
            fo.write(str(cnt))
        for i in range(l):
            if ls[i]=="section":
                if ls[i+1]==".data":
                    fo.write(str(dataaddr))
                    fo.write("\t")
                    fo.write("<data_start>:\n")
                elif ls[i+1]==".bss":
                    fo.write(str(bssaddr))
                    fo.write("\t")
                    fo.write("<data_bss>:\n")
                #elif ls[i+1]==".text":
                 #   fo.write(str(textaddr))
                 #   fo.write("\t")
                 #   fo.write("data_text>:\n")
                    
            if ls[i]=="dd":
                fo.write("\t")
                if ls[i-1] in ls2:
                    vararr.append(ls[i-1])
                    for k in range(len(ls2)):
                        if ls2[k]==ls[i-1]:
                            fo.write(str(dataaddr+int(ls2[k+5])))
                            vararr.append(dataaddr+int(ls2[k+5]))
                            fo.write("  00 ")
                            fo.write(str(ls[i+1]).zfill(2))
                            fo.write("\n")
                            #fo.write(str(ln))
                            #fo.write("\n")

                

            if ls[i]=="db":
                fo.write("\t")
                #fo.write(str(cnt))
                #fo.write(" ")
                string='a000'
                if ls[i-1] in ls2:
                    vararr.append(ls[i-1])
                    for k in range(len(ls2)):
                        if ls2[k]==ls[i-1]:
                            fo.write(str(dataaddr+int(ls2[k+5])))
                            vararr.append(dataaddr+int(ls2[k+5]))
                            fo.write("  00 ")
                            fo.write(str(add_space(string)))
                            fo.write("\n")
                            #fo.write(str(ln))
                            #fo.write("\n")

            if ls[i]=="resd":
                fo.write("\t")
                if ls[i-1] in ls2:
                    vararr.append(ls[i-1])
                    for k in range(len(ls2)):
                        if ls2[k]==ls[i-1]:
                            fo.write(str(bssaddr+int(ls2[k+5])))
                            vararr.append(bssaddr+int(ls2[k+5]))
                            fo.write("  ")
                            #fo.write("<res ")
                            fo.write(str(add_space('0000')))
                            #fo.write(">")
                            fo.write("\n")
                            #fo.write(str(ln))
                            #fo.write("\n")

            if ls[i]=="resb":
                fo.write("\t")
                if ls[i-1] in ls2:
                    vararr.append(ls[i-1])
                    for k in range(len(ls2)):
                        if ls2[k]==ls[i-1]:
                            fo.write(str(bssaddr+int(ls2[k+5])))
                            vararr.append(bssaddr+int(ls2[k+5]))
                            fo.write("  ")
                            #fo.write("<res ")
                            fo.write(str(add_space('0000')))
                            #fo.write(">")
                            fo.write("\n")
                            #fo.write(str(ln))
                            #fo.write("\n")

            #if ls[i]=="global":
             #   fo.write("\t")
             #   fo.write(str(cnt))
              #  fo.write(" ")
              #  fo.write("\t \t\t\t")
              #  fo.write(str(ln))
                #fo.write("\n")

            #if ls[i]=="extern":
             #   fo.write("\t")
             #   fo.write(str(cnt))
             #   fo.write(" ")
             #   fo.write("\t \t\t\t")
             #   fo.write(str(ln))
                #fo.write("\n")

            if ls[i]=="main:":
                fo.write(str(mainaddr))
                fo.write("\t")
                fo.write("<main>:")
                fo.write("\n")
                #fo.write(str(ln))
                #fo.write("\n")

                
            if ls[i]=="mov":
                #print(type(address))
                #fo.write("\t")
                #fo.write(str(cnt))
                #fo.write(" ")
                fo.write(repl(str(mainaddr)))
                fo.write(":\t")
                ls1=ls[i+1].split(",")
                if ls1[0] in arr32 and ls1[1] in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="mov":
                            if ls5[y+1]=="r32,r32":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                fo.write(" ")
                                ad.append(ls5[y+3])
                                for k in range(len(ls6)):
                                    if ls6[k]==ls1[0]:
                                        if ls6[k+1]==ls1[1]:
                                            fo.write(str(add_space(str(ls6[k+2]))))
                                            ad.append(ls6[k+2])
                                            fo.write("\n")
                                            #fo.write(str(ln))
                                #fo.write("\t\t")
                if ls1[0] in arr16 and ls1[1] in arr16:
                    for y in range(len(ls5)):
                        if ls5[y]=="mov":
                            if ls5[y+1]=="r16,r16":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                for k in range(len(ls6)):
                                    if ls6[k]==ls1[0]:
                                        if ls6[k+1]==ls1[1]:
                                            fo.write(str(add_space(str(ls6[k+2]))))
                                            ad.append(ls6[k+2])
                                            fo.write("\n")
                                            #fo.write(str(ln))
                                #fo.write("\t\t")
                if ls1[0] in arr8 and ls1[1] in arr8:
                    for y in range(len(ls5)):
                        if ls5[y]=="mov":
                            if ls5[y+1]=="r8,r8":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                for k in range(len(ls6)):
                                    if ls6[k]==ls1[0]:
                                        if ls6[k+1]==ls1[1]:
                                            fo.write(str(add_space(str(ls6[k+2]))))
                                            ad.append(ls6[k+2])
                                            fo.write("\n")
                                            #fo.write(str(ln))
                                #fo.write("\t\t")
                elif ls1[0] in arr32 and ls1[1] in ls2:
                    for y in range(len(ls5)):
                        if ls5[y]=="mov":
                            if ls5[y+1]=="r32,m32":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                fo.write(" ")
                                ad.append(ls5[y+3])
                                #fo.write("[")
                                for k in range(len(vararr)):
                                    if vararr[k]==ls1[1]:
                                        fo.write(str(add_space(str(vararr[k+1]))))
                                        ad.append("00000000")
                                        #fo.write("]")
                                        fo.write("\n")
                                        #fo.write(str(ln))
                                #fo.write("\t\t")
                elif ls1[0] in arr16 and ls1[1] in ls2:
                    for y in range(len(ls5)):
                        if ls5[y]=="mov":
                            if ls5[y+1]=="r16,m16":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                fo.write(" ")
                                ad.append(ls5[y+3])
                                #fo.write("[")
                                for k in range(len(vararr)):
                                    if vararr[k]==ls1[1]:
                                        fo.write(str(add_space(str(vararr[k+1]))))
                                        ad.append("00000000")
                                        #fo.write("]")
                                        fo.write("\n")
                                        #fo.write(str(ln))
                                #fo.write("\t\t")
                elif ls1[0] in arr8 and ls1[1] in ls2:
                    for y in range(len(ls5)):
                        if ls5[y]=="mov":
                            if ls5[y+1]=="r8,m8":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                fo.write(" ")
                                ad.append(ls5[y+3])
                                #fo.write("[")
                                for k in range(len(vararr)):
                                    if vararr[k]==ls1[1]:
                                        fo.write(str(add_space(str(vararr[k+1]))))
                                        ad.append("00000000")
                                        #fo.write("]")
                                        fo.write("\n")
                                        #fo.write(str(ln))
                                #fo.write("\t\t")
                elif ls1[0] in arr32 and ls1[1] in ls3:
                    for y in range(len(ls5)):
                        if ls5[y]=="mov":
                            if ls5[y+1]=="r32,i32":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                fo.write("\n")
                elif ls1[0] in arr16 and ls1[1] in ls3:
                    for y in range(len(ls5)):
                        if ls5[y]=="mov":
                            if ls5[y+1]=="r16,i16":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                fo.write("\n")
                elif ls1[0] in arr8 and ls1[1] in ls3:
                    for y in range(len(ls5)):
                        if ls5[y]=="mov":
                            if ls5[y+1]=="r8,i8":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                fo.write("\n")
                elif ls1[0] in ls2 and ls1[1] in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="mov":
                            if ls5[y+1]=="m32,r32":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\n")
                elif ls1[0] in ls2 and ls1[1] in arr16:
                    for y in range(len(ls5)):
                        if ls5[y]=="mov":
                            if ls5[y+1]=="m16,r16":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\n")
                elif ls1[0] in ls2 and ls1[1] in arr8:
                    for y in range(len(ls5)):
                        if ls5[y]=="mov":
                            if ls5[y+1]=="m8,r8":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\n")
                elif ls1[0] in ls2 and ls1[1] in ls3:
                    for y in range(len(ls5)):
                        if ls5[y]=="mov":
                            if ls5[y+1]=="m,i":
                                fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\n")
                        
                
                addd="".join(ad)
                mainaddr+=caladdr(addd)
                ad=[]


            if ls[i]=="add":
                #print(type(address))
                #fo.write("\t")
                #fo.write(str(cnt))
                #fo.write(" ")
                fo.write(repl(str(mainaddr)))
                fo.write(":\t")
                ls1=ls[i+1].split(",")
                if ls1[0] in arr32 and ls1[1] in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="add":
                            if ls5[y+1]=="r32,r32":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                fo.write(" ")
                                ad.append(ls5[y+3])
                                for k in range(len(ls6)):
                                    if ls6[k]==ls1[0]:
                                        if ls6[k+1]==ls1[1]:
                                            fo.write(str(ls6[k+2]))
                                            ad.append(ls6[k+2])
                                            fo.write("\n")
                                            #fo.write(str(ln))
                                #fo.write("\t\t")
                if ls1[0] in arr16 and ls1[1] in arr16:
                    for y in range(len(ls5)):
                        if ls5[y]=="add":
                            if ls5[y+1]=="r16,r16":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                fo.write(" ")
                                ad.append(ls5[y+3])
                                for k in range(len(ls6)):
                                    if ls6[k]==ls1[0]:
                                        if ls6[k+1]==ls1[1]:
                                            fo.write(str(ls6[k+2]))
                                            ad.append(ls6[k+2])
                                            fo.write("\n")
                                            #fo.write(str(ln))
                                #fo.write("\t\t")
                if ls1[0] in arr8 and ls1[1] in arr8:
                    for y in range(len(ls5)):
                        if ls5[y]=="add":
                            if ls5[y+1]=="r8,r8":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                fo.write(" ")
                                ad.append(ls5[y+3])
                                for k in range(len(ls6)):
                                    if ls6[k]==ls1[0]:
                                        if ls6[k+1]==ls1[1]:
                                            fo.write(str(ls6[k+2]))
                                            ad.append(ls6[k+2])
                                            fo.write("\n")
                                            #fo.write(str(ln))
                                #fo.write("\t\t")
                elif ls1[0] in arr32 and ls1[1] in ls2:
                    for y in range(len(ls5)):
                        if ls5[y]=="add":
                            if ls5[y+1]=="r32,m32":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                #fo.write("[")
                                for k in range(len(vararr)):
                                    if vararr[k]==ls1[1]:
                                        fo.write(str(add_space(vararr[k+1])))
                                        ad.append("00000000")
                                        #fo.write("]")
                                        fo.write("\n")
                                        #fo.write(str(ln))
                                #fo.write("\t\t")
                elif ls1[0] in arr16 and ls1[1] in ls2:
                    for y in range(len(ls5)):
                        if ls5[y]=="add":
                            if ls5[y+1]=="r16,m16":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                #fo.write("[")
                                for k in range(len(vararr)):
                                    if vararr[k]==ls1[1]:
                                        fo.write(str(add_space(vararr[k+1])))
                                        ad.append("00000000")
                                        #fo.write("]")
                                        fo.write("\n")
                                        #fo.write(str(ln))
                                #fo.write("\t\t")
                elif ls1[0] in arr8 and ls1[1] in ls2:
                    for y in range(len(ls5)):
                        if ls5[y]=="add":
                            if ls5[y+1]=="r8,m8":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                #fo.write("[")
                                for k in range(len(vararr)):
                                    if vararr[k]==ls1[1]:
                                        fo.write(str(add_space(vararr[k+1])))
                                        ad.append("00000000")
                                        #fo.write("]")
                                        fo.write("\n")
                                        #fo.write(str(ln))
                                #fo.write("\t\t")
                elif ls1[0] in arr32 and ls1[1] in ls3:
                    for y in range(len(ls5)):
                        if ls5[y]=="add":
                            if ls5[y+1]=="r32,i32":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                fo.write("\n")
                elif ls1[0] in arr16 and ls1[1] in ls3:
                    for y in range(len(ls5)):
                        if ls5[y]=="add":
                            if ls5[y+1]=="r16,i16":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                fo.write("\n")
                elif ls1[0] in arr8 and ls1[1] in ls3:
                    for y in range(len(ls5)):
                        if ls5[y]=="add":
                            if ls5[y+1]=="r8,i8":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                fo.write("\n")
                elif ls1[0] in ls2 and ls1[1] in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="add":
                            if ls5[y+1]=="m32,r32":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                fo.write("\n")
                elif ls1[0] in ls2 and ls1[1] in arr16:
                    for y in range(len(ls5)):
                        if ls5[y]=="add":
                            if ls5[y+1]=="m16,r16":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                fo.write("\n")
                elif ls1[0] in ls2 and ls1[1] in arr8:
                    for y in range(len(ls5)):
                        if ls5[y]=="add":
                            if ls5[y+1]=="m8,r8":
                                #fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\n")
                elif ls1[0] in ls2 and ls1[1] in ls3:
                    for y in range(len(ls5)):
                        if ls5[y]=="add":
                            if ls5[y+1]=="m,i":
                                #fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\n")
                        
                addd="".join(ad)
                mainaddr+=caladdr(addd)
                ad=[]
               

            if ls[i]=="sub":
                #print(type(address))
                fo.write(repl(str(mainaddr)))
                fo.write(":\t")
                ls1=ls[i+1].split(",")
                if ls1[0] in arr32 and ls1[1] in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="sub":
                            if ls5[y+1]=="r32,r32":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                fo.write(" ")
                                ad.append(ls5[y+3])
                                for k in range(len(ls6)):
                                    if ls6[k]==ls1[0]:
                                        if ls6[k+1]==ls1[1]:
                                            fo.write(str(ls6[k+2]))
                                            ad.append(ls6[k+2])
                                            fo.write("\n")
                                            #fo.write(str(ln))
                                #fo.write("\t\t")
                if ls1[0] in arr16 and ls1[1] in arr16:
                    for y in range(len(ls5)):
                        if ls5[y]=="sub":
                            if ls5[y+1]=="r16,r16":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                fo.write(" ")
                                ad.append(ls5[y+3])
                                for k in range(len(ls6)):
                                    if ls6[k]==ls1[0]:
                                        if ls6[k+1]==ls1[1]:
                                            fo.write(str(ls6[k+2]))
                                            ad.append(ls6[k+2])
                                            fo.write("\n")
                                            #fo.write(str(ln))
                                #fo.write("\t\t")
                if ls1[0] in arr8 and ls1[1] in arr8:
                    for y in range(len(ls5)):
                        if ls5[y]=="sub":
                            if ls5[y+1]=="r8,r8":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                fo.write(" ")
                                ad.append(ls5[y+3])
                                for k in range(len(ls6)):
                                    if ls6[k]==ls1[0]:
                                        if ls6[k+1]==ls1[1]:
                                            fo.write(str(ls6[k+2]))
                                            ad.append(ls6[k+2])
                                            fo.write("\n")
                                            #fo.write(str(ln))
                                #fo.write("\t\t")
                elif ls1[0] in arr32 and ls1[1] in ls2:
                    for y in range(len(ls5)):
                        if ls5[y]=="sub":
                            if ls5[y+1]=="r32,m32":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                fo.write(" ")
                                ad.append(ls5[y+3])
                                #fo.write("[")
                                for k in range(len(ls2)):
                                    if ls2[k]==ls1[1]:
                                        fo.write(str(ls2[k+5]))
                                        ad.append("00000000")
                                        #fo.write("]")
                                        fo.write("\n")
                                        #fo.write(str(ln))
                                #fo.write("\t\t")
                elif ls1[0] in arr16 and ls1[1] in ls2:
                    for y in range(len(ls5)):
                        if ls5[y]=="sub":
                            if ls5[y+1]=="r16,m16":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                fo.write(" ")
                                ad.append(ls5[y+3])
                                #fo.write("[")
                                for k in range(len(ls2)):
                                    if ls2[k]==ls1[1]:
                                        fo.write(str(ls2[k+5]))
                                        ad.append("00000000")
                                        #fo.write("]")
                                        fo.write("\n")
                                        #fo.write(str(ln))
                                #fo.write("\t\t")
                elif ls1[0] in arr8 and ls1[1] in ls2:
                    for y in range(len(ls5)):
                        if ls5[y]=="sub":
                            if ls5[y+1]=="r8,m8":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                fo.write(" ")
                                ad.append(ls5[y+3])
                                #fo.write("[")
                                for k in range(len(ls2)):
                                    if ls2[k]==ls1[1]:
                                        fo.write(str(ls2[k+5]))
                                        ad.append("00000000")
                                        #fo.write("]")
                                        fo.write("\n")
                                        #fo.write(str(ln))
                                #fo.write("\t\t")
                elif ls1[0] in arr32 and ls1[1] in ls3:
                    for y in range(len(ls5)):
                        if ls5[y]=="sub":
                            if ls5[y+1]=="r32,i32":
                                fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                fo.write("\n")
                elif ls1[0] in arr16 and ls1[1] in ls3:
                    for y in range(len(ls5)):
                        if ls5[y]=="sub":
                            if ls5[y+1]=="r16,i16":
                                fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                fo.write("\n")
                elif ls1[0] in arr8 and ls1[1] in ls3:
                    for y in range(len(ls5)):
                        if ls5[y]=="sub":
                            if ls5[y+1]=="r8,i8":
                                fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                fo.write("\n")
                elif ls1[0] in ls2 and ls1[1] in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="sub":
                            if ls5[y+1]=="m32,r32":
                                fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                fo.write("\n")
                elif ls1[0] in ls2 and ls1[1] in arr16:
                    for y in range(len(ls5)):
                        if ls5[y]=="sub":
                            if ls5[y+1]=="m16,r16":
                                fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                fo.write("\n")
                elif ls1[0] in ls2 and ls1[1] in arr8:
                    for y in range(len(ls5)):
                        if ls5[y]=="sub":
                            if ls5[y+1]=="m8,r8":
                                fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                fo.write("\n")
                elif ls1[0] in ls2 and ls1[1] in ls3:
                    for y in range(len(ls5)):
                        if ls5[y]=="sub":
                            if ls5[y+1]=="m,i":
                                fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                fo.write("\n")
                        
                addd="".join(ad)
                mainaddr+=caladdr(addd)
                ad=[]
                

            if ls[i]=="push":
                fo.write(repl(str(mainaddr)))
                fo.write(":\t")
                if ls[i+1] in arr32:
                    for k in range(len(ls5)):
                        if ls5[k]==ls[i]:
                            if ls5[k+1]=="r32":
                                fo.write(str(ls5[k+3]))
                                ad.append(ls5[k+3])
                                fo.write("\n")
                                #fo.write(str(ln))
                if ls[i+1] in arr16:
                    for k in range(len(ls5)):
                        if ls5[k]==ls[i]:
                            if ls5[k+1]=="r16":
                                fo.write(str(ls5[k+3]))
                                ad.append(ls5[k+3])
                                fo.write("\n")
                                #fo.write(str(ln))
                if ls[i+1] in arr8:
                    for k in range(len(ls5)):
                        if ls5[k]==ls[i]:
                            if ls5[k+1]=="r8":
                                fo.write(str(ls5[k+3]))
                                ad.append(ls5[k+3])
                                fo.write("\n")
                                #fo.write(str(ln))
                if ls[i+1] in ls2:
                    for k in range(len(ls5)):
                        if ls5[k]==ls[i]:
                            if ls5[k+1]=="m":
                                fo.write(str(ls5[k+3]))
                                ad.append(ls5[k+3])
                                fo.write(" ")
                                #fo.write("\n")
                    for l in range(len(vararr)):
                        if vararr[l]==ls[i+1]:
                            fo.write(str(add_space(str(vararr[l+1]))))
                            ad.append("00000000")
                            #fo.write("]")
                            fo.write("\n")
                            #fo.write(str(ln))
                addd="".join(ad)
                mainaddr+=caladdr(addd)
                ad=[]

            if ls[i]=="call":
                fo.write(repl(str(mainaddr)))
                fo.write(":\t")
                for k in range(len(ls5)):
                    if ls5[k]==ls[i]:
                        fo.write(str(ls5[k+2]))
                        ad.append(ls5[k+2])
                        fo.write("\n")
                        ad.append("00000000")
                        #fo.write(str(ln))
                addd="".join(ad)
                address=caladdr(addd)
                ad=[]


            if ls[i]=="mult":
                fo.write(repl(str(mainaddr)))
                fo.write(":\t")
                if ls[i+1] in arr32:
                    for k in range(len(ls5)):
                        if ls5[k]==ls[i]:
                            if ls5[k+1]=="r32":
                                fo.write(str(ls5[k+3]))
                                ad.append(ls5[k+3])
                                fo.write("\n")
                                #fo.write(str(ln))
                if ls[i+1] in arr16:
                    for k in range(len(ls5)):
                        if ls5[k]==ls[i]:
                            if ls5[k+1]=="r16":
                                fo.write(str(ls5[k+3]))
                                ad.append(ls5[k+3])
                                fo.write("\n")
                                #fo.write(str(ln))
                if ls[i+1] in arr8:
                    for k in range(len(ls5)):
                        if ls5[k]==ls[i]:
                            if ls5[k+1]=="r8":
                                fo.write(str(ls5[k+3]))
                                ad.append(ls5[k+3])
                                fo.write("\n")
                                #fo.write(str(ln))
                #if ls[i+1] in ls2:
                 #   for k in range(len(ls5)):
                  #      if ls5[k]==ls[i]:
                   #         if ls5[k+1]=="m":
                    #            fo.write(str(ls5[k+3]))
                     #           ad.append(ls5[k+3])
                      #          fo.write("[")
                    #for l in range(len(ls2)):
                     #   if ls2[l]==ls[i+1]:
                      #      fo.write(str(ls2[l+5]).zfill(8))
                       #     ad.append("00000000")
                       #     fo.write("]")
                        #    fo.write("\t")
                         #   fo.write(str(ln))
                addd="".join(ad)
                mainaddr+=caladdr(addd)
                ad=[]
            

            if ls[i]=="div":
                fo.write(repl(str(mainaddr)))
                fo.write(":\t")
                if ls[i+1] in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="div":
                            if ls5[y+1]=="r32":
                                #fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\n")
                if ls[i+1] in arr16:
                    for y in range(len(ls5)):
                        if ls5[y]=="div":
                            if ls5[y+1]=="r16":
                                #fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\n")
                if ls[i+1] in arr8:
                    for y in range(len(ls5)):
                        if ls5[y]=="div":
                            if ls5[y+1]=="r8":
                                #fo.write("op#")
                                fo.write(str(ls5[y+2]))
                                fo.write("\n")
                        
                if ls[i+1] in ls4:
                    for z in range(len(ls4)):
                        if ls[i+1]==ls4[z]:
                            fo.write("reg#")
                            fo.write(str(ls4[z+1]))
                            fo.write("\t")
                            fo.write("-\t")
                            fo.write(str(address))
                            fo.write("\n")
                #if ls1[1] in ls4:
                 #   for z in range(len(ls4)):
                  #      if ls1[1]==ls4[z]:
                   #         fo.write("reg#")
                    #        fo.write(str(ls4[z]))
                     #       fo.write("\t\t")
                            #address='{0:04}'.format(address)
                      #      fo.write(str(address))
                       #     fo.write("\n")
                elif ls[i+1] in ls2:
                    for p in range(l2):
                        if ls2[p]==ls[i+1]:
                            n=ls2[p+1]
                    fo.write("sym#")
                    fo.write(str(n))
                    fo.write("\t")
                    fo.write("-\t")
                    fo.write(str(address))
                    fo.write("\n")
                #elif ls1[1] in ls2:
                 #   for p in range(l2):
                  #      if ls2[p]==ls1[1]:
                   #         n=ls2[p+1]
                   # fo.write("sym#")
                   # fo.write(str(n))
                   # fo.write("\t\t")
                    #address='{0:04}'.format(address)
                    #fo.write(str(address))
                    #fo.write("\n")
                elif ls[i+1] in ls3:
                    for q in range(ln3):
                        if ls3[q]==ls[i+1]:
                            a=ls3[q+1]
                    fo.write("lit#")
                    fo.write(str(a))
                    fo.write("\t")
                    fo.write("-\t")
                    fo.write(str(address))
                    fo.write("\n")
                #elif ls1[1] in ls3:
                 #   for q in range(ln3):
                  #      if ls3[q]==ls1[1]:
                   #         a=ls3[q+1]
                  #  fo.write("lit#")
                   # fo.write(str(a))
                   # fo.write("\t\t")
                    #address='{0:04}'.format(address)
                    #fo.write(str(address))
                    #fo.write("\n")
                if ls[i+1] in arr32:
                    address+=2
                #else:
                   # address+=4
                elif ls[i+1] in arr16:
                    address+=2
                #else:
                 #   address+=4
                elif ls[i+1] in arr8:
                    address+=2
               

            if ls[i]=="pop":
                fo.write(repl(str(mainaddr)))
                fo.write(":\t")
                if ls[i+1] in arr32:
                    for k in range(len(ls5)):
                        if ls5[k]==ls[i]:
                            if ls5[k+1]=="r32":
                                fo.write(str(ls5[k+3]))
                                ad.append(ls5[k+3])
                                fo.write("\n")
                                #fo.write(str(ln))
                if ls[i+1] in arr16:
                    for k in range(len(ls5)):
                        if ls5[k]==ls[i]:
                            if ls5[k+1]=="r16":
                                fo.write(str(ls5[k+3]))
                                ad.append(ls5[k+3])
                                fo.write("\n")
                                #fo.write(str(ln))
                if ls[i+1] in arr8:
                    for k in range(len(ls5)):
                        if ls5[k]==ls[i]:
                            if ls5[k+1]=="r8":
                                fo.write(str(ls5[k+3]))
                                ad.append(ls5[k+3])
                                fo.write("\n")
                                #fo.write(str(ln))
                if ls[i+1] in ls2:
                    for k in range(len(ls5)):
                        if ls5[k]==ls[i]:
                            if ls5[k+1]=="m":
                                fo.write(str(ls5[k+3]))
                                ad.append(ls5[k+3])
                                #fo.write("[")
                    for l in range(len(ls2)):
                        if ls2[l]==ls[i+1]:
                            fo.write(str(ls2[l+5]))
                            ad.append("00000000")
                            #fo.write("]")
                            fo.write("\n")
                            #fo.write(str(ln))
                addd="".join(ad)
                mainaddr+=caladdr(addd)
                ad=[]


            if ls[i]=="inc":
                fo.write(repl(str(mainaddr)))
                fo.write(":\t")
                if ls[i+1] in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="inc":
                            if ls5[y+1]=="r32":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                fo.write("\n")
                                #fo.write(str(ln))
                if ls[i+1] in arr16:
                    for y in range(len(ls5)):
                        if ls5[y]=="inc":
                            if ls5[y+1]=="r16":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                fo.write("\n")
                                #fo.write(str(ln))
                if ls[i+1] in arr8:
                    for y in range(len(ls5)):
                        if ls5[y]=="inc":
                            if ls5[y+1]=="r8":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                fo.write("\n")
                                #fo.write(str(ln))
                if ls[i+1] in ls4:
                    for z in range(len(ls4)):
                        if ls[i+1]==ls4[z]:
                            #fo.write("reg#")
                            fo.write(str(ls4[z+1]))
                            ad.append(ls4[z+1])
                            fo.write("\n")
                            #fo.write(str(ln))

                addd="".join(ad)
                address=caladdr(addd)
                ad=[]


            if ls[i]=="dec":
                fo.write(repl(str(mainaddr)))
                fo.write(":\t")
                if ls[i+1] in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="dec":
                            if ls5[y+1]=="r32":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                fo.write("\n")
                                #fo.write(str(ln))
                if ls[i+1] in arr16:
                    for y in range(len(ls5)):
                        if ls5[y]=="dec":
                            if ls5[y+1]=="r16":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                fo.write("\n")
                                #fo.write(str(ln))
                if ls[i+1] in arr8:
                    for y in range(len(ls5)):
                        if ls5[y]=="dec":
                            if ls5[y+1]=="r8":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                fo.write("\n")
                                #fo.write(str(ln))
                if ls[i+1] in ls4:
                    for z in range(len(ls4)):
                        if ls[i+1]==ls4[z]:
                            #fo.write("reg#")
                            fo.write(str(ls4[z+1]))
                            ad.append(ls4[z+1])
                            fo.write("\n")
                            #fo.write(str(ln))

                addd="".join(ad)
                address=caladdr(addd)
                ad=[]


            if ls[i]=="xor":
                fo.write(repl(str(mainaddr)))
                fo.write(":\t")
                if ls[i+1] in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="xor":
                            if ls5[y+1]=="r32":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                fo.write("\n")
                                #fo.write(str(ln))
                if ls[i+1] in arr16:
                    for y in range(len(ls5)):
                        if ls5[y]=="xor":
                            if ls5[y+1]=="r16":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                fo.write("\n")
                                #fo.write(str(ln))
                if ls[i+1] in arr8:
                    for y in range(len(ls5)):
                        if ls5[y]=="xor":
                            if ls5[y+1]=="r8":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                fo.write("\n")
                                #fo.write(str(ln))
                if ls[i+1] in ls4:
                    for z in range(len(ls4)):
                        if ls[i+1]==ls4[z]:
                            #fo.write("reg#")
                            fo.write(str(ls4[z+1]))
                            ad.append(ls4[z+1])
                            fo.write("\n")
                            #fo.write(str(ln))

                addd="".join(ad)
                address=caladdr(addd)
                ad=[]

            if ls[i]=="or":
                fo.write(repl(str(mainaddr)))
                fo.write(":\t")
                if ls[i+1] in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="or":
                            if ls5[y+1]=="r32":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                fo.write("\n")
                                #fo.write(str(ln))
                if ls[i+1] in arr16:
                    for y in range(len(ls5)):
                        if ls5[y]=="or":
                            if ls5[y+1]=="r16":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                fo.write("\n")
                                #fo.write(str(ln))
                if ls[i+1] in arr8:
                    for y in range(len(ls5)):
                        if ls5[y]=="or":
                            if ls5[y+1]=="r8":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                fo.write("\n")
                                #fo.write(str(ln))
                if ls[i+1] in ls4:
                    for z in range(len(ls4)):
                        if ls[i+1]==ls4[z]:
                            #fo.write("reg#")
                            fo.write(str(ls4[z+1]))
                            ad.append(ls4[z+1])
                            fo.write("\n")
                            #fo.write(str(ln))

                addd="".join(ad)
                address=caladdr(addd)
                ad=[]


            if ls[i]=="and":
                fo.write(repl(str(mainaddr)))
                fo.write(":\t")
                if ls[i+1] in arr32:
                    for y in range(len(ls5)):
                        if ls5[y]=="and":
                            if ls5[y+1]=="r32":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                fo.write("\n")
                                #fo.write(str(ln))
                if ls[i+1] in arr16:
                    for y in range(len(ls5)):
                        if ls5[y]=="and":
                            if ls5[y+1]=="r16":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                fo.write("\n")
                                #fo.write(str(ln))
                if ls[i+1] in arr8:
                    for y in range(len(ls5)):
                        if ls5[y]=="and":
                            if ls5[y+1]=="r8":
                                #fo.write("op#")
                                fo.write(str(ls5[y+3]))
                                ad.append(ls5[y+3])
                                fo.write("\n")
                                #fo.write(str(ln))
                if ls[i+1] in ls4:
                    for z in range(len(ls4)):
                        if ls[i+1]==ls4[z]:
                            #fo.write("reg#")
                            fo.write(str(ls4[z+1]))
                            ad.append(ls4[z+1])
                            fo.write("\n")
                            #fo.write(str(ln))

                addd="".join(ad)
                address=caladdr(addd)
                ad=[]



            if ls[i]=="jmp":
                fo.write(repl(str(mainaddr)))
                fo.write(":\t")
                for y in range(len(ls5)):
                    if ls5[y]=="jmp":
                        #fo.write("op#")
                        fo.write(str(ls5[y+2]))
                        ad.append(ls5[y+2])
                        #fo.write("\t\t")
                        
                if ls[i+1] in ls2:
                    #fo.write("[")
                    for z in range(len(ls2)):
                        if ls[i+1]==ls2[z]:
                            #fo.write("sym#")
                            fo.write(str(ls2[z+1]).zfill(8))
                            #fo.write("]")
                            fo.write("\n")
                            #fo.write(str(ln))
                            

                addd="".join(ad)
                address=caladdr(addd)
                ad=[]


            if ls[i]=="jne":
                fo.write(repl(str(mainaddr)))
                fo.write(":\t")
                for y in range(len(ls5)):
                    if ls5[y]=="jne":
                        #fo.write("op#")
                        fo.write(str(ls5[y+2]))
                        ad.append(ls5[y+2])
                        #fo.write("\t\t")
                        
                if ls[i+1] in ls2:
                    #fo.write("[")
                    for z in range(len(ls2)):
                        if ls[i+1]==ls2[z]:
                            #fo.write("sym#")
                            fo.write(str(ls2[z+1]).zfill(8))
                            #fo.write("]")
                            fo.write("\n")
                            #fo.write(str(ln))
                            

                addd="".join(ad)
                address=caladdr(addd)
                ad=[]

                
            if ls[i]=="je":
                fo.write(repl(str(mainaddr)))
                fo.write(":\t")
                for y in range(len(ls5)):
                    if ls5[y]=="je":
                        #fo.write("op#")
                        fo.write(str(ls5[y+2]))
                        ad.append(ls5[y+2])
                        #fo.write("\t\t")
                        
                if ls[i+1] in ls2:
                    #fo.write("[")
                    for z in range(len(ls2)):
                        if ls[i+1]==ls2[z]:
                            #fo.write("sym#")
                            fo.write(str(ls2[z+1]).zfill(8))
                            #fo.write("]")
                            fo.write("\n")
                            #fo.write(str(ln))
                            

                addd="".join(ad)
                address=caladdr(addd)
                ad=[]


            if ls[i]=="jge":
                fo.write(repl(str(mainaddr)))
                fo.write(":\t")
                for y in range(len(ls5)):
                    if ls5[y]=="jge":
                        #fo.write("op#")
                        fo.write(str(ls5[y+2]))
                        ad.append(ls5[y+2])
                        #fo.write("\t\t")
                        
                if ls[i+1] in ls2:
                    #fo.write("[")
                    for z in range(len(ls2)):
                        if ls[i+1]==ls2[z]:
                            #fo.write("sym#")
                            fo.write(str(ls2[z+1]).zfill(8))
                            #fo.write("]")
                            fo.write("\n")
                            #fo.write(str(ln))
                            

                addd="".join(ad)
                address=caladdr(addd)
                ad=[]


            if ls[i]=="jg":
                fo.write(repl(str(mainaddr)))
                fo.write(":\t")
                for y in range(len(ls5)):
                    if ls5[y]=="jg":
                        #fo.write("op#")
                        fo.write(str(ls5[y+2]))
                        ad.append(ls5[y+2])
                        #fo.write("\t\t")
                        
                if ls[i+1] in ls2:
                    #fo.write("[")
                    for z in range(len(ls2)):
                        if ls[i+1]==ls2[z]:
                            #fo.write("sym#")
                            fo.write(str(ls2[z+1]))
                            #fo.write("]")
                            fo.write("\n")
                            #fo.write(str(ln))
                            

                addd="".join(ad)
                address=caladdr(addd)
                ad=[]


            if ls[i]=="jle":
                fo.write(repl(str(mainaddr)))
                fo.write(":\t")
                for y in range(len(ls5)):
                    if ls5[y]=="jle":
                        #fo.write("op#")
                        fo.write(str(ls5[y+2]))
                        ad.append(ls5[y+2])
                        #fo.write("\t\t")
                        
                if ls[i+1] in ls2:
                    #fo.write("[")
                    for z in range(len(ls2)):
                        if ls[i+1]==ls2[z]:
                            #fo.write("sym#")
                            fo.write(str(ls2[z+1]).zfill(8))
                            #fo.write("]")
                            fo.write("\n")
                            #fo.write(str(ln))
                            

                addd="".join(ad)
                address=caladdr(addd)
                ad=[]


            if ls[i]=="jl":
                fo.write(repl(str(mainaddr)))
                fo.write(":\t")
                for y in range(len(ls5)):
                    if ls5[y]=="jl":
                        #fo.write("op#")
                        fo.write(str(ls5[y+2]))
                        ad.append(ls5[y+2])
                        #fo.write("\t\t")
                        
                if ls[i+1] in ls2:
                    #fo.write("[")
                    for z in range(len(ls2)):
                        if ls[i+1]==ls2[z]:
                            #fo.write("sym#")
                            fo.write(str(ls2[z+1]))
                            #fo.write("]")
                            fo.write("\n")
                            #fo.write(str(ln))
                            

                addd="".join(ad)
                address=caladdr(addd)
                ad=[]


            if ls[i]=="jz":
                fo.write(repl(str(mainaddr)))
                fo.write(":\t")
                for y in range(len(ls5)):
                    if ls5[y]=="jz":
                        #fo.write("op#")
                        fo.write(str(ls5[y+2]))
                        ad.append(ls5[y+2])
                        #fo.write("\t\t")
                        
                if ls[i+1] in ls2:
                    #fo.write("[")
                    for z in range(len(ls2)):
                        if ls[i+1]==ls2[z]:
                            #fo.write("sym#")
                            fo.write(str(ls2[z+1]).zfill(8))
                            #fo.write("]")
                            fo.write("\n")
                            #fo.write(str(ln))
                            

                addd="".join(ad)
                address=caladdr(addd)
                ad=[]


            if ls[i]=="rep":
                fo.write(str(cnt))
                fo.write("\t")
                for q in range(len(ls5)):
                    if ls[i+1]==ls5[q] and ls5[q-1]=="rep":
                        fo.write("op#")
                        fo.write(str(ls5[q+1]))
                        fo.write("\t\t-\t-\t")
                        fo.write(str(address))
                        fo.write("\n")
                        break
                if ls[i+1] in arrs32:
                    address+=8
                elif ls[i+1] in arrs16:
                    address+=4
                elif ls[i+1] in arrs8:
                    address+=2
                            


            if ls[i]=="repe":
                fo.write(str(cnt))
                fo.write("\t")
                for q in range(len(ls5)):
                    if ls[i+1]==ls5[q] and ls5[q-1]=="repe":
                        fo.write("op#")
                        fo.write(str(ls5[q+1]))
                        fo.write("\t\t-\t-\t")
                        fo.write(str(address))
                        fo.write("\n")
                        break
                if ls[i+1] in arrs32:
                    address+=8
                elif ls[i+1] in arrs16:
                    address+=4
                elif ls[i+1] in arrs8:
                    address+=2

            if ls[i]=="repne":
                fo.write(str(cnt))
                fo.write("\t")
                for q in range(len(ls5)):
                    if ls[i+1]==ls5[q] and ls5[q-1]=="repne":
                        fo.write("op#")
                        fo.write(str(ls5[q+1]))
                        fo.write("\t\t-\t-\t")
                        fo.write(str(address))
                        fo.write("\n")
                        break
                if ls[i+1] in arrs32:
                    address+=8
                elif ls[i+1] in arrs16:
                    address+=4
                elif ls[i+1] in arrs8:
                    address+=2

            if ls[i]=="repz":
                fo.write(str(cnt))
                fo.write("\t")
                for q in range(len(ls5)):
                    if ls[i+1]==ls5[q] and ls5[q-1]=="repz":
                        fo.write("op#")
                        fo.write(str(ls5[q+1]))
                        fo.write("\t\t-\t-\t")
                        fo.write(str(address))
                        fo.write("\n")
                        break
                if ls[i+1] in arrs32:
                    address+=8
                elif ls[i+1] in arrs16:
                    address+=4
                elif ls[i+1] in arrs8:
                    address+=2

            if ls[i]=="repnz":
                fo.write(str(cnt))
                fo.write("\t")
                for q in range(len(ls5)):
                    if ls[i+1]==ls5[q] and ls5[q-1]=="repnz":
                        fo.write("op#")
                        fo.write(str(ls5[q+1]))
                        fo.write("\t\t-\t-\t")
                        fo.write(str(address))
                        fo.write("\n")
                        break
                if ls[i+1] in arrs32:
                    address+=8
                elif ls[i+1] in arrs16:
                    address+=4
                elif ls[i+1] in arrs8:
                    address+=2
            
           
        ln=fi1.readline()
        ls=ln.split()
        #ls2=lo.split()
        l=len(ls)   


if __name__ == '__main__':
    ss=argv[1]
    propsymtab2(ss)
    proplittab(ss)
    trans(ss,"opsymtab.txt","oplittab.txt","reg.txt","instr.txt")
    trans1(ss,"opsymtab2.txt","oplittab.txt","reg.txt","instr.txt","mod.txt")
    objcode(ss,"opsymtab2.txt","oplittab.txt","reg.txt","instr.txt","mod.txt")

