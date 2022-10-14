#Beregning av areal og omkrets av en sirkel

#Be bruker fylle inn radius av sirkelen
radius=float(input('Hva er radiusen på sirkelen? '))

#Importer mattematiske symboler i python
import math

#Beregn arealet av sirkelen
areal=math.pi*(radius*radius)

#Beregne omkrets av sirkelen
omkrets=math.pi*(radius*2)

print('Areal: ',areal,'Omkrets: ',omkrets)
