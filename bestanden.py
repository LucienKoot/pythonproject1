bestand = open("test.txt", "wb")
bestand.write(bytes("Dit is de eerste tekst in het bestand.\n", "UTF-8"))
bestand.close()

print (bestand.mode)
print (bestand.name)

