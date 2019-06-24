class Hout:
    "Deze class bevat alle eigenschappen van onze houtsoorten"
    aantHout = 0
    
    def _init_(self, naam, gewicht, lengte, breedte):
        self.naam = naam
        self.gewicht = gewicht
        self.lengte = lengte
        self.breedte = breedte
        Hout.aantHout += 1

    def displayCount(self):
        print ("Totaal aantal houtsoorten %d" % Hout.aantHout)

    def  
        print ("naam: ", self.naam,  ", gewicht: ", self.gewicht,   ", lengte:  ", self.lengte,  ", breedte:  self.breedte)

hout1 = Hout("Vurenhout", 10, 1000, 100)
hout2 = Hout("Eikenhout", 15, 1000, 50)

               
