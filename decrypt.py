def decrypt(n):
    d=""
    for i in range(len(inp)):
        c=inp[i]
        if c.isupper():
            d+=chr((ord(c)-shift-65)%26+65)
        elif c.islower():
            d+=chr((ord(c)-shift-97)%26+97)
    print("The decrypted value is ",d)

inp=input("Enter a text to decrypt : ")
shift=int(input("Enter the number of shift needed : "))
decrypt(inp)
