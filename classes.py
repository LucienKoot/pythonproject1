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
