import sys

try:
    tallfil=open("tallfil.txt","r")
except IOError:
    print("Filen finnes ikke i målet")
else:

    x=0

    tall=tallfil.readline()

    while tall!="":

        try:
            tallInt=int(tall)
        except ValueError:
            print(tall.rstrip("\n"),"er ikke et tall og kan derfor ikke summeres")
        else:
            total=x+tallInt
            x=total

        tall=tallfil.readline()
        
    print(total)