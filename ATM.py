file = open("balance.txt", "r")
balance = float(file.read())
file.close()

print("Välkommen till banken")
restart=("Y")
chances = 3
balance = 420
#Har gett Y restart, har gett 3 chanser. Printar ut ett välkomnande till att börja med och gett saldot 420.
while chances >= 0:
    pin = int(input("Var vänlig skriv in pinkod"))
    if pin == (1234):
        print("Rätt pinkod")
#Skapat en pinkod
        while restart not in ("n","NO","no","N"):
#Loopen säger att den inte ska restarta om man skriver n NO no eller N
            print("Tryck 1 om du vill se saldo")
            print("Tryck 2 om du vill ta ut pengar")
            print("Tryck 3 om du vill sätta in pengar")
            print("Tryck 4 om du vill ta tillbaka kort")
            option = int(input("Vilket alternativ väljer du?"))
#Printar ut alla alternativ och frågar vilket du väljer
            if option == 1:
                print("Ditt saldo är",balance)
                restart = input("Vill du gå tillbaka?")
                if restart in ("n","NO","no","N"):
                    print("Tack så mycket")
                    break
#Har gjort så att option 1 visar vad ditt saldo ligger på och även alternativet till att gå tillbaka förutom med n NO no N.
            elif option == 2:
                option2 = ("y")
                withdraw = float(input("Hur mycket vill du ta ut?"))
                print("Du kan ta ut 10,20,30,40,50,60,70,80,90,100,200,300,400,420")
                if withdraw in [10,20,30,40,50,60,70,80,90,100,200,300,400,420]:
                    file = open("balance.txt", "w")
                    balance = balance - withdraw
                    file.write(str(balance))
                    print("Ditt saldo är nu Â£",balance)
                    file.close()
                    restart = input("Vill du gå tillbaka?")
                    if restart in ("n","NO","no","N"):
                        print("Tack så mycket")
                        break
#Alternativ två är att ta ut pengar, jag har gjort så att man bara kan ta ut de angivna alternativen och inte vad som helst. 
                elif withdraw != [10,20,30,40,50,50,70,80,90,100,200,300,400,420]:
                    print("Fel belopp, var god försök igen")
                    restart = ("y")
                elif withdraw == 1:
                    withdraw = float(input("Var god skriv in önskat belopp"))
#Om man inte väljer tillgängliga alternativen som belopp så får du fel belopp och måste försöka igen
            elif option == 3:
                Deposition = float(input("Hur mycket vill du lägga in?"))
                file = open("balance.txt", "w")
                balance = balance + Deposition
                file.write(str(balance))
                print("Ditt saldo är nu Â£",balance)
                file.close()
                restart = input("Vill du gå tillbaka?")
                if restart in ("n","NO","no","N"):
                    print("Tack så mycket")
                    break
#balance blir balance plus det du lägger in. Printar vad nya saldot är.
            elif option == 4:
                print("Var god ta ut kort")
                print("Ha en fortsatt trevlig dag")
                exit()
#Tar ut kort sen avbryter allt
            else:
                print("Var god skriv in ett korrekt nummer")
                restart = ("y")
    elif pin != ("1234"):
        print("Fel pinkod")
        chances = chances - 1
        if chances == 0:
            print("Inga fler försök")
            break
