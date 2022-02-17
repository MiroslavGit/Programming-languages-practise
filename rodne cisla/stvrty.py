from datetime import datetime

rodneCislo = input("Zadaj rodné cislo: ")

str = pohlavie = ""
str = mesiacNazov = ""

currentDay = datetime.now().day
currentMonth = datetime.now().month
currentYear = datetime.now().year


if(len(rodneCislo) > 11):
    print("Nie je to rodné číslo !")
else:
    if(rodneCislo[2] == "1" or rodneCislo[2] == "0"):
        pohlavie = "muž"
        
        mesiac = rodneCislo[2] +rodneCislo[3]

        if(mesiac == "01"):
            mesiacNazov = "Január"
        elif(mesiac == "02"):
            mesiacNazov = "Február"
        elif(mesiac == "03"):
            mesiacNazov = "Marec"
        elif(mesiac == "04"):
            mesiacNazov = "Apríl"
        elif(mesiac == "05"):
            mesiacNazov = "Máj"
        elif(mesiac == "06"):
            mesiacNazov = "Jún"
        elif(mesiac == "07"):
            mesiacNazov = "Júl"
        elif(mesiac == "08"):
            mesiacNazov = "August"
        elif(mesiac == "09"):
            mesiacNazov = "September"
        elif(mesiac == "10"):
            mesiacNazov = "Október"
        elif(mesiac == "11"):
            mesiacNazov = "November"
        elif(mesiac == "12"):
            mesiacNazov = "December"

        rok = rodneCislo[0] + rodneCislo[1]
        rokInt = int(rok)

        mesiac = rodneCislo[2] + rodneCislo[3]
        mesiacInt = int(mesiac)

        den = rodneCislo[4] + rodneCislo[5]
        denInt = int(den)

        if( rokInt < 23 ):
            rok = "20"+rok
            
            mesiacInt = currentMonth - mesiacInt
            denInt = currentDay -denInt
            rokInt = currentYear - rokInt
            
            if(mesiacInt <= 0):
                if(denInt >= 0 and mesiacInt == 0):
                    vek = currentYear - int(rok)
                else:
                    vek = currentYear - int(rok)-1
            else:
                vek = currentYear - int(rok)    
        else:
            rok = "19"+rok
            vek = 2022 - int(rok)
        
        print (pohlavie , ",dátum narodenia: ", rodneCislo[4] + rodneCislo[5], mesiacNazov , rok ,"vek: ",vek ,"rokov.")


    elif(rodneCislo[2] == "5" or rodneCislo[2] == "6"):
        pohlavie = "žena"

        mesiac = rodneCislo[2] +rodneCislo[3]
        mesiacInt = int(mesiac)
        mesiacInt -= 50
       
        if(mesiacInt == 1):
            mesiacNazov = "Január"
        elif(mesiacInt == 2):
            mesiacNazov = "Február"
        elif(mesiacInt == 3):
            mesiacNazov = "Marec"
        elif(mesiacInt == 4):
            mesiacNazov = "Apríl"
        elif(mesiacInt == 5):
            mesiacNazov = "Máj"
        elif(mesiacInt == 6):
            mesiacNazov = "Jún"
        elif(mesiacInt == 7):
            mesiacNazov = "Júl"
        elif(mesiacInt == 8):
            mesiacNazov = "August"
        elif(mesiacInt == 9):
            mesiacNazov = "September"
        elif(mesiacInt == 10):
            mesiacNazov = "Október"
        elif(mesiacInt == 11):
            mesiacNazov = "November"
        elif(mesiacInt == 12):
            mesiacNazov = "December"

        rok = rodneCislo[0] + rodneCislo[1]
        rokInt = int(rok)

        mesiac = rodneCislo[2] + rodneCislo[3]
        mesiacInt = int(mesiac)

        den = rodneCislo[4] + rodneCislo[5]
        denInt = int(den)

        if( rokInt < 23 ):
            rok = "20"+rok
            
            mesiacInt = currentMonth - mesiacInt
            denInt = currentDay -denInt
            rokInt = currentYear - rokInt
            
            if(mesiacInt <= 0):
                if(denInt >= 0 and mesiacInt == 0):
                    vek = currentYear - int(rok)
                else:
                    vek = currentYear - int(rok)-1
            else:
                vek = currentYear - int(rok)  
        else:
            rok = "19"+rok
            vek = 2022 - int(rok)
        
        print (pohlavie , ",dátum narodenia: ", rodneCislo[4] + rodneCislo[5], mesiacNazov , rok ,"vek: ",vek ,"rokov.")

    else:
        print("Nie je to rodné číslo !")

    
