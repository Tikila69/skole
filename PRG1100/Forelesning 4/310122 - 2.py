liste=[]

navnliste=open("fornavn.txt","r")

navn=navnliste.readline()

while navn!="":
    navn=navn.rstrip("\n")
    liste+=[navn]
    navn=navnliste.readline()

print("lista til nå:",liste)
print()

bytte=True
stoppmerke=1

while bytte==True:
    bytte=False

    for x in range (0,len(liste)-stoppmerke,1):
        if liste[x]>liste[x+1]:
            temp=liste[x]
            liste[x]=liste[x+1]
            liste[x+1]=temp
            bytte=True
    
    stoppmerke=stoppmerke+1

print("Lista sortert:",liste)