#Definerer lista
venner=[]
print(venner)
print()

#Åpner lista i "read"
venneliste=open("venner.txt","r")

#Leser første linja i fila og definerer denne som "fornavn"
fornavn=venneliste.readline()

#mens "fornavn" ikke er en tom linje:
while fornavn!="":
    #Fjern "new-line" fra "fornavn"
    fornavn=fornavn.rstrip("\n")
    #Definer Etternavn og Epost som neste linje i fila og fjernr "new-line" merket
    etternavn=venneliste.readline().rstrip("\n")
    epost=venneliste.readline().rstrip("\n")
    #Skriver "fornan", "Etternavn" og "epost" til lista "venner" 
    venner+=[[fornavn,etternavn,epost]]
    #Leser neste linje i fila og definerer den som "fornavn"
    fornavn=venneliste.readline()

#Printer resultatet av lista etter endt skriving
print("Resultatet ble: ",venner)
print()

#printer 5. lista i lista "venner"
print(venner[4])
print()

#printer 3. del av 5. lista i "venner"
print(venner[4][2])
print()

#printer lengden av lista "venner"
listelengde=len(venner)
print(listelengde)
print()



print("Etternavn:")
#definerere c=1
c=1

for r in range (listelengde):

    #printer 2. del av 1./2./3. lista i lista venner, basert på indeksen til for-løkka
    print(venner[r][c])
print()

print("Etternavn og epost adresse")
#definerer c=1
c=1 
for r in range (listelengde):
    #printer 1. og 2. del av 1./2./3. lista i lista venner basert på indeksen til for-løkka
    print(venner[r][c],"har e-postadresse",venner[r][c+1])
print()