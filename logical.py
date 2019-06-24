# fietsenhandel

leeftijd = 66

if (leeftijd >= 1) and (leeftijd <=4):
    print ("Achter op bij pappa of mamma !")

elif (leeftijd >=5) and (leeftijd <=11):
    print ("Jij krijgt een kinderfiets !")

elif (leeftijd >=12) and (leeftijd <=20):
    print ("Wij reserveren een ATB !")

elif  (leeftijd >=22) and (leeftijd<=59):
    print ("Wij reserveren een volwassenen fiets.")

elif (leeftijd == 21) or (leeftijd == 60):
    print ("Dat wordt reserveren voor een bierfiets")

elif not (leeftijd<= 61):
    print ("Dat wordt een rollator")

else:
    print ("Alles is verhuurd")
