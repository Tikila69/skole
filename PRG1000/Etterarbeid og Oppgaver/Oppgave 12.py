#Joe trader bitcoin, hvor mye penger har han tapt?

#Input detaljer rundt kjøp av aksjer
aksjerKjøpt=int(input('Hvor mange aksjer har du kjøpt? '))
aksjerPrisKjøp=float(input('Hvor mye kostet hver aksje? '))
kommisjonKjøp=float(input('Hvor mange prosent kommisjon betalte du for kjøpet? '))

#Beregn forbruket
forbrukAksjer=aksjerKjøpt*aksjerPrisKjøp
kommisjon=forbrukAksjer/100*kommisjonKjøp
forbruk=forbrukAksjer+kommisjon

#Print resultatet av forbruket
print('Joe har brukt',forbruk,'på aksjer, hvorav',kommisjon,'er kommisjon.')

#Input detaljer rundt salg av aksjer
aksjerSolgt=int(input('Hvor mange aksjer solgte du? '))
aksjerPrisSalg=float(input('Hvor mye solgte du hver aksje for? '))
kommisjonSalg=float(input('Hvor mange prosent kommisjon betalte du for salget? '))

#Beregne salg av aksjer
inntjeningAksjer=aksjerSolgt*aksjerPrisSalg
kommisjonTap=inntjeningAksjer/100*kommisjonSalg
inntjening=inntjeningAksjer-kommisjonTap

#Print resultatet av forbruket
print('Joe har solgt aksjer for',inntjening,'hvorav',kommisjonTap,'er kommisjion')

#Beregn om Joe tapte eller tjente penger på dette

fortjeneste=inntjening-forbruk

#Print resultatet
print('Joe sitter igjen med',fortjeneste,'etter salget')
