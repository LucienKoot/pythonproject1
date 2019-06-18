import base64
 
original_string = "Dit is heel erg gewone data"
print (original_string)
 
encode2byte = str.encode(original_string)
type(bytes) # Zorgt ervoor dat de string omgezet wordt naar Byte Data (benodigd voor base64).

encoded_string = base64.b64encode(encode2byte)
print (encoded_string)
