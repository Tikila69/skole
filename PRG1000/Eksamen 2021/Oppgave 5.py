
import os
def dekk_slett():
    slette=input('Ønsker du å slette alle utleverte dekke? (j/n): ')

    if slette=='j':
        oppbevaring=open('oppbevaring.txt','r')
        tempfilOppbevaring=open('tempfilOppbevaring.txt','w')
        tempfilDekksett=open('tempfilDekksett.txt','w')

        mobilnrOppbevaring=oppbevaring.readline()

        while mobilnrOppbevaring!='':
            regnroppbevaring=oppbevaring.readline()
            innDato=oppbevaring.readline()
            utDato=oppbevaring.readline()
            hylle=oppbevaring.readline()
            pris=oppbevaring.readline()

            if utDato.rstrip('\n')=='X':
                tempfilOppbevaring.write(mobilnrOppbevaring+regnroppbevaring+innDato+utDato+hylle+pris)

                dekksett=open('dekksett.txt','r')
                mobilnrDekksett=dekksett.readline()

                while mobilnrDekksett!='':
                    regnrDekksett=dekksett.readline()

                    if regnrDekksett==regnroppbevaring:
                        tempfilDekksett.write(mobilnrDekksett+regnrDekksett)

                    mobilnrDekksett=dekksett.readline()

                dekksett.close()      

            mobilnrOppbevaring=oppbevaring.readline()
            
        oppbevaring.close()
        tempfilOppbevaring.close()
        tempfilDekksett.close()

        os.remove('dekksett.txt')
        os.remove('oppbevaring.txt')
        os.rename('tempfilOppbevaring.txt','oppbevaring.txt')
        os.rename('tempfilDekksett.txt','dekksett.txt')

        print()
        print('Sletting gjennomført')

dekk_slett()