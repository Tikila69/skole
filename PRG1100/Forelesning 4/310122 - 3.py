liste=[]

navnliste=open("fornavn.txt","r",encoding="utf-8")

navn=navnliste.readline()

while navn!="":
    navn=navn.rstrip("\n")
    liste+=[navn]
    navn=navnliste.readline()

print("lista til nå:",liste)
print()

for i in range (1,len(liste),1):

    j=i

    while j>0 and liste[j-1]>liste[j]:
        temp=liste[j-1]
        liste[j-1]=liste[j]
        liste[j]=temp

        j=j-1

print("Listen sortert;",liste)
navnliste.close()


navnlisteSortert=open("fornavn sortert.txt","w",encoding="utf-8")

for x in range (0,len(liste),1):
    navnlisteSortert.write(liste[x]+("\n"))

print("Skriving til fil fullført")