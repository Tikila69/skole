# Lag et program som leser inn studentnr, fornavn og studium for studenter ved Campus Ringerike. Det skal leses inn opplysninger om minst en student og
# programmet skal etter innlesningen av studentopplysninger for en student spørre om det skal leses inn opplysninger om en ny student. Opplysningene om en
# student legges i lista student etter følgende struktur:
# student = [<studentnr1> ,<fornavn1>,<studium1>,<studentnr2> ,<fornavn2>,<studium2>, …osv],
# se Gaddis s 384 for «A list holding different types».
# Inndata for studium er enten "Bachelor IT", "Bachelor økad" eller "Bachelor jus".

# Programmet skal så be brukeren oppgi et studentnr og skrive ut studentnr, fornavn og studium for denne studenten, evt en melding om at studenten ikke
# finnes hvis det ikke er registrert noen studenter med oppgitt studentnr.

# Til slutt skal programmet be brukeren oppgi et studium/studieprogram og skrive ut studentnr, fornavn (og studium) for alle studenter som er
# registrert på dette studiumet/studieprogrammet.

lokke = "ja"

while lokke == "ja":
    studenter = []
    student = []
    fortsette = "ja"

    while fortsette == "ja":
        navn = input('Fyll inn fornavn: ')
        studie = input('Fyll inn studie: ')
        studentnr = int(input('Fyll inn studentnummer: '))
        student += [studentnr]+[navn]+[studie]
        studenter += [student]
        student = []
        fortsette = input(
            'Ønsker du å skrive inn informasjon på en ny student? ')

    sokStudentnr = "ja"
    while sokStudentnr == "ja":
        feilNummer = True
        while feilNummer == True:
            sok1 = int(input('Oppgi studentnr til studenten du leter etter: '))
            listeStudentnr = []
            for i in range(0, len(studenter), 1):
                if studenter[i][0] == sok1:
                    listeStudentnr += studenter[i]
            if listeStudentnr != []:
                print(listeStudentnr)
                feilNummer = False
            else:
                print('Ingen studenter funnet')

        sokStudentnr = input('Ønsker du foreta flere søk? ')

    sokStudie = "ja"
    while sokStudie == "ja":
        feilStudie = True
        while feilStudie == True:
            sok2 = input('Hvilket studie ønsker du å se deltakere i? ')
            listeStudier = []
            for n in range(0, len(studenter), 1):
                if studenter[n][2] == sok2:
                    listeStudier += [studenter[n]]
            if listeStudier != []:
                print(listeStudier)
                feilStudie = False
            else:
                print('Ingen studenter ved dette studie er funnet')
        sokStudie = input('Ønsker du å foreta ett nytt søk? ')

    lokke = input('Ønsker du å fortsette programmet? ')
