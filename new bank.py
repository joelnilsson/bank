print("Välkommen till banken")
restart=("Y")
chances = 3
balance = 420
while chances >= 0:
    pin = int(input("Var vänlig skriv in pinkod"))
    if pin == (1234):
        print("Rätt pinkod")
        while restart not in ("n","NO","no","N"):
            print("Tryck 1 om du vill se saldo")
            print("Tryck 2 om du vill ta ut pengar")
            option = int(input("Vilket alternativ väljer du?"))
            if option == 1:
                print("Ditt saldo är",balance)
                restart = input("Vill du gå tillbaka?")
                if restart in ("n","NO","no","N"):
                    print("Tack så mycket")
                    break
            elif option == 2:
                option2 = ("y")
                withdraw = float(input("Hur mycket vill du ta ut?"))
                if withdraw in [10,50,100]:
                    balance = balance - withdraw
                    print("Ditt saldo är nu Â£",balance)
                    restart = input("Vill du gå tillbaka?")
                    if restart in ("n","NO","no","N"):
                        print("Tack så mycket")
                        break
                elif withdraw != [10,50,100]:
                    print("Fel belopp, var god försök igen")
                    restart = ("y")
                elif withdraw == 1:
                    withdraw = float(input("Var god skriv in önskat belopp"))
            elif option == 3:
                Deposition = float(input("Hur mycket vill du lägga in?"))
                balance = balance + Deposition
                print("Ditt saldo är nu Â£",balance)
                restart = input("Vill du gå tillbaka?")
                if restart in ("n","NO","no","N"):
                    print("Tack så mycket")
                    break
            elif option == 4:
                print("Var god ta ut kort")
                print("Ha en fortsatt trevlig dag")
                break
            else:
                print("Var god skriv in ")



#file = open("balance.txt", "r+")
#test = file.read()
#print(test)
#test = input("Testar om det fungerar")
#file.write(test)
#file.close()
