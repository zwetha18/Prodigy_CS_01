def encrypt(n):
    e=""
    for i in range(len(inp)):
        c=inp[i]
        if c.isupper():
            e+=chr((ord(c)+shift-65)%26+65)
        elif c.islower():
            e+=chr((ord(c)+shift-97)%26+97)
    print("The encrypted value is ",e)
inp=input("Enter a text to decrypt : ")
shift=int(input("Enter the number of shift needed : "))
encrypt(inp)
