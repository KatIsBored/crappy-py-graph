from random import randint
from time import sleep
from math import sin, cos, tan, pi
from os import get_terminal_size, system
ran=False

graphchar="+"

system("cls")
system("title Crappy graphing tool :P")
start = input("press enter to start script (resize your window first) ")
system("cls")
while True:
    
    width=get_terminal_size().columns-10
    height=get_terminal_size().lines-5
    print(height)
    liz=[]
    pointz = []
    gnum=0
    for _ in range(height):
        liz.append("#"+" "*width)

    def lizout(inp1):
        for comorbidcunt in range(len(liz)):
            print(liz[height-comorbidcunt-1])
        print("0"+"#"*width+" "+str(inp1))


    lizout(width)
    y=input("Enter Y value > ")
    pc=int(input("Points calculated > "))
    

    def prais(inp1):
        __builtins__.sin = sin
        __builtins__.cos = cos
        __builtins__.tan = tan
        __builtins__.pi = pi
        var2=eval(inp1)
        return(var2)

    def findgreatest(input, input2):
        if input >= input2:
            return(input)
        else:
            return (input2)

    x=1
    for _ in range(pc):
        yrez=prais(str(y))
        print(f"{_+1} corresponds to ( {_+1} ; {yrez} )")
        pointz.append(f"{_+1} {yrez}")
        print(pointz)
        gnum=findgreatest(gnum, yrez)
        x=x+1

    print(f"greatest Y value > {gnum}")
    print(f"greatest X value > {pc}")
    

    for _ in range(len(pointz)):
        allocpnt=pointz[_]
        vls=allocpnt.split()
        print(vls)
        if float(vls[0]) < 1:
            vls[0] = 1
        if float(vls[1]) < 1:
            vls[1] = 1
        ex=round(float(vls[0])*(width/pc))
        wy=round(float(vls[1])*(height/gnum))
        print(f"{ex}, {wy}")
        liz[wy-1]=str(liz[wy-1])[:ex]+graphchar+str(liz[wy-1])[ex+1:]
    
    system("cls")
    print(gnum)
    lizout(pc)
    print(f"Enter Y value > {y}                "[:35]+" | For smoother lines use higher point counts ")
    print(f"Points calculated > {str(pc)}                "[:35]+" |  (god this is so poorly made)")
    buffer2=input("You done? (press enter to clear)")
    

