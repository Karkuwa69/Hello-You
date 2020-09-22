import random
import time
print("Welkom dit is mijn Casino spel!")
time.sleep(1)
print("Kies je Difficulty! \n Easy: $2000 \n Medium: $1000 \n Hard: $100")
time.sleep(1)

hajs = 0

while True:                                                     # Difficulty keuze
    odp01 = input()
    
    if odp01 == "Easy":
        hajs = 2000
        nummer = random.randrange(1, 6)
        print("Je hebt Easy gekozen! Jouw saldo is: $", hajs)
        rnd = "1, 5"
        break
    elif odp01 == "Medium":
        hajs = 1000
        nummer = random.randrange(1, 11)
        print("Je hebt Medium gekozen! Jouw saldo is: $", hajs)
        rnd = "1, 10"
        break
    elif odp01 == "Hard":
        hajs = 100
        nummer = random.randrange(1, 21)
        print("Je hebt Hard gekozen! Jouw saldo is: $", hajs)
        rnd = "1, 20"
        break
    else:
        print("Je hebt een typ fout gemaakt! Probeer nog een keer.")



while True:

    if odp01 == "Easy":                                     # Nummer generator
        nummer = random.randrange(1, 6)
    elif odp01 == "Medium":
        nummer = random.randrange(1, 11)
    elif odp01 == "Hard":
        nummer = random.randrange(1, 21)

    if hajs == 10000:                                       # Win
        print("Gewonnen!")
        break
    elif hajs == 0:                                         # Lose
        print("Verloren!")
        break
    else:
        print("Wat wil je doen? \n A: Saldo checken \n B: Spelen \n C: Quit")

    odp02 = input()
    
    if odp02 == "A":                                        # Saldo bekijken
        print("Jouw saldo is: $", hajs)
        time.sleep(1)
        continue
    elif odp02 == "B":                                      # Verder spelen
        print("Hoeveel wil je gokken?""[$", hajs,"]")

        obs = input()

        print("Op welke nummer?""[", rnd,"]")

        num = input()
        
        if int(num) == nummer:                              # Je hebt verloren/gewonnen
            hajs = hajs - int(obs)
            obs = int(obs) * 2
            hajs = hajs + int(obs)
            print("Het nummer is:", nummer,"je hebt:", obs,"gewonnen")
            time.sleep(1)
            print("Jouw saldo is: $", hajs)
            time.sleep(1)
        else:
            hajs = hajs - int(obs)
            print("Het nummer is:", nummer,"\nJe hebt:",obs,"verloren")
            time.sleep(1)
            print("Jouw saldo is: $",hajs)
        continue
    elif hajs == 10000:
        print("Gewonnen!")
        break
    elif hajs == 0:
        print("Verloren!")
        break
    elif odp02 == "C":                                  # Quit
        break
