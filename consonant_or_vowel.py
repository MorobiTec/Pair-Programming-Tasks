import binascii

hex_string = "g66=q=x=w7k=z6=p=oo6=w76euw76kIWFhO".replace("=", "")
try:
    decoded_bytes = binascii.unhexlify(hex_string)
    decoded_string = decoded_bytes.decode('utf-8')
    print(decoded_string)
except Exception as e:
    print("Error decoding:", e)
