class Hout:
    "Deze classe bevat al eigenschappen van onze houtsoorten"
    aantHout = 0
 
    def __init__(self, naam, gewicht, lengte, breedte):
        self.naam = naam
        self.gewicht = gewicht
        self.lengte = lengte
        self.breedte = breedte
        Hout.aantHout += 1
 
    def displayCount(self):
        print ("Totaal aantal houtsoorten %d" % Hout.aantHout)
 
    def displayHout(self):
        print ("naam : ", self.naam,  ", gewicht: ", self.gewicht,  ", lengte: ", self.lengte,  ", breedte: ", self.breedte)
 
hout1 = Hout("Vurenhout", 10, 1000, 100)
hout2 = Hout("Eikenhout", 15, 1000, 50)
 
hout1.displayHout()
hout2.displayHout()
print ("Totaal aantal houtsoorten %d" % Hout.aantHout)
