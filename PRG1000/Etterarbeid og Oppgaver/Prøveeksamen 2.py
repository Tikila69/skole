l1=[1,2,3,4,5]
l2=[6,7,8,9,10,11,12]
nyListe=[]

print(l1)
print()
print(l2)
print()
print(nyListe)
print()

for i in range (0,len(l1),1):
    nyListe+=[l1[i]]

for n in range (0,len(l2),1):
    nyListe+=[l2[n]]

print(nyListe)