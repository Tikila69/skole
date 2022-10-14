# første og siste element i en liste skal bytte plass
talliste=[5,3,2,1,4]

print('Lista før byttet er:',talliste)
print('Første og siste element i lista skal bytte plass')
print()

#bytte er bytteveraibelen vi bruker for å ta vare på første verdi
bytte=talliste[0]

#talliste[0] får verdien til talliste[4]
talliste[0]=talliste[4]

#talliste[4] får verdien som vi tok vare på i byttevariabelen
talliste[4]=bytte

#lista etter bytte er
print('Lista etter byttet er:',talliste)