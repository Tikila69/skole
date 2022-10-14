from tkinter import *

def hentInfo(event):
    valg=lstStudent.get(lstStudent.curselection())

    funnet=False
    radnr=0

    while funnet==False and radnr<=len(student)-1:
        if valg[0]==student[radnr][0]:
            info.set(student[radnr][1]+" "+student[radnr][2]+", "+student[radnr][3]+", "+student[radnr][6])
            funnet=True
        else:
            radnr+=1
    

student=[]

studentfil=open("studenter.txt","r",encoding="UTF-8")

studentnr=studentfil.readline()

while studentnr!="":
    studentnr=studentnr.rstrip("\n")
    fornavn=studentfil.readline().rstrip("\n")
    etternavn=studentfil.readline().rstrip("\n")
    epost=studentfil.readline().rstrip("\n")
    fodselsdato=studentfil.readline().rstrip("\n")
    kjonn=studentfil.readline().rstrip("\n")
    studium=studentfil.readline().rstrip("\n")

    student+=[[studentnr,fornavn,etternavn,epost,fodselsdato,kjonn,studium]]

    studentnr=studentfil.readline()

studentfil.close()

studnrOgFornavn=[]

for x in range (len(student)):
    studnrOgFornavn+=[[student[x][0],student[x][1]]]

window=Tk()
window.title=("Studentliste")

yScroll=Scrollbar(window,orient=VERTICAL)
yScroll.grid(row=0,column=2,rowspan=5,padx=(0,100),pady=5,sticky=NS)

innholdLstStudent=StringVar()
lstStudent=Listbox(window,width=10,height=5,listvariable=innholdLstStudent,yscrollcommand=yScroll.set)
lstStudent.grid(row=0,column=1,rowspan=5,padx=(100,0),pady=5,sticky=E)
innholdLstStudent.set(tuple(studnrOgFornavn))
yScroll["command"]=lstStudent.yview

info=StringVar()
entInfo=Entry(window,width=60,state="readonly",textvariable=info)
entInfo.grid(row=0,column=3,sticky=E)
lstStudent.bind("<<ListboxSelect>>",hentInfo)

window.mainloop()
