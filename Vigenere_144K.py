from tkinter import *


root=Tk()
root.title('Vigenere_144K (By Dacops)')


def encode():
    global delete1
    try:
        delete1()
    except:
        pass
    try:
        delete2()
    except:
        pass
    try:
        delete3()
    except:
        pass


    def encoded():
        global Encoded1
        message = Message1.get()
        password = Password1.get()
        encoded, x1 = 0, 0
        for i1 in range(round(len(message)/len(password))+1):
            for i2 in range(len(password)):
                try:
                    value1 = ord(message[i2+x1])+ord(password[i2])
                    if value1 > 143859:
                        rest = value1 - 143859
                        value1 = chr(-1+rest)
                    else:
                        value1 = chr(value1)
                    encoded = str(encoded) + str(value1)
                except:
                    pass
            x1 = x1 + len(password)
        encoded = encoded[1:]
        Encoded1=Entry(root, width=60, borderwidth=5)
        Encoded1.insert(0, encoded)
        Encoded1.grid(row=8, column=0, columnspan=3)


    def random():
        import random
        message = Message1.get()
        pw = 0
        for i in range(len(message)):
            rand = random.randint(0, 143859)
            rand = chr(rand)
            pw = str(pw) + str(rand)
        pw = pw[1:]
        Password1.delete(0, END)
        Password1.insert(0, str(pw))


    Text1=Label(root, text='VIGENERE_144K ENCODER:', width=80, height=5, anchor='sw')
    Text1.grid(row=1, column=0, columnspan=5, rowspan=4, sticky=SW)
    Password1=Entry(root, width=60, borderwidth=5)
    Password1.insert(0, 'Enter the Password:')
    Password1.grid(row=5, column=0, columnspan=3)
    Message1=Entry(root, width=60, borderwidth=5)
    Message1.insert(0, 'Enter the Message:')
    Message1.grid(row=6, column=0, columnspan=3)
    Encoded=Label(root, text='Encoded Text:', width=45, height=3, anchor='sw')
    Encoded.grid(row=7, column=0, columnspan=3, sticky=SW)
    Encoded1=Entry(root, width=60, borderwidth=5)
    Encoded1.insert(0, '')
    Encoded1.grid(row=8, column=0, columnspan=3)
    Random=Button(root, text='RANDOM PASSWORD\n(RECOMMENDED)\n(USE AFTER WRITTING THE MESSAGE)', command=random, width=30, height=4, borderwidth=5)
    Random.grid(row=5, column=3, rowspan=2)
    Encoded2=Button(root, text='ENCODE\nTHE\nTEXT', command=encoded, width=30, height=6, borderwidth=5)
    Encoded2.grid(row=7, column=3, rowspan=2)


    def delete1():
        Text1.grid_forget()
        Password1.grid_forget()
        Message1.grid_forget()
        Encoded.grid_forget()
        Encoded1.grid_forget()
        Encoded2.grid_forget()
        Random.grid_forget()


def decode():
    global delete2
    try:
        delete1()
    except:
        pass
    try:
        delete2()
    except:
        pass
    try:
        delete3()
    except:
        pass


    def decoded():
        global Decoded1
        message = Message2.get()
        password = Password2.get()
        encoded, x1 = 0, 0
        for i1 in range(round(len(message)/len(password))+1):
            for i2 in range(len(password)):
                try:
                    value1 = ord(message[i2+x1])-ord(password[i2])
                    if value1 < 0:
                        rest = 0 - value1
                        value1 = chr(143860-rest)
                    else:
                        value1 = chr(value1)
                    encoded = str(encoded) + str(value1)
                except:
                    pass
            x1 = x1 + len(password)
        encoded = encoded[1:]
        Decoded1=Entry(root, width=60, borderwidth=5)
        Decoded1.insert(0, encoded)
        Decoded1.grid(row=8, column=0, columnspan=3)


    Text2=Label(root, text='VIGENERE_144K DECODER:', width=80, height=5, anchor='sw')
    Text2.grid(row=1, column=0, columnspan=5, rowspan=4, sticky=SW)
    Password2=Entry(root, width=60, borderwidth=5)
    Password2.insert(0, 'Enter the Password:')
    Password2.grid(row=5, column=0, columnspan=3)
    Message2=Entry(root, width=60, borderwidth=5)
    Message2.insert(0, 'Enter the Message:')
    Message2.grid(row=6, column=0, columnspan=3)
    Decoded=Label(root, text='Decoded text:', width=45, height=3, anchor='sw')
    Decoded.grid(row=7, column=0, columnspan=3, sticky=SW)
    Decoded1=Entry(root, width=60, borderwidth=5)
    Decoded1.insert(0, '')
    Decoded1.grid(row=8, column=0, columnspan=3)
    Decoded2=Button(root, text='DECODE\nTHE\nTEXT', command=decoded, width=30, height=10, borderwidth=5)
    Decoded2.grid(row=5, column=3, rowspan=5)


    def delete2():
        Text2.grid_forget()
        Password2.grid_forget()
        Message2.grid_forget()
        Decoded.grid_forget()
        Decoded1.grid_forget()
        Decoded2.grid_forget()


def what():
    global delete3
    try:
        delete1()
    except:
        pass
    try:
        delete2()
    except:
        pass
    try:
        delete3()
    except:
        pass

    Explain1=Label(root, text='''This is a variant of the Classical Vigenere, but it accepts 143,859 Unicode characters, instead of the normal''', width=80, height=1, anchor='w')
    Explain1.grid(row=1, column=0, columnspan=5, sticky=W)
    Explain2=Label(root, text='''26 Alphabet letters. Keep in mind that the majority of symbols may not appear, only a ? in a box, don't''', width=80, height=1, anchor='w')
    Explain2.grid(row=2, column=0, columnspan=5, sticky=W)
    Explain3=Label(root, text='''worry it's still working, this only needs the numerical value associated to it.''', width=80, height=1, anchor='w')
    Explain3.grid(row=3, column=0, columnspan=5, sticky=W)
    Explain4=Label(root, text='''(Check Wikipedia Article 'List of Unicode characters' where all these symbols are listed)''', width=80, height=1, anchor='w')
    Explain4.grid(row=4, column=0, columnspan=5, sticky=W)

    def delete3():
        Explain1.grid_forget()
        Explain2.grid_forget()
        Explain3.grid_forget()
        Explain4.grid_forget()


Encode=Button(root, text='ENCODER', command=encode, width=15, height=2, borderwidth=5)
Encode.grid(row=0, column=0)
Decode=Button(root, text='DECODER', command=decode, width=15, height=2, borderwidth=5)
Decode.grid(row=0, column=1)
What=Button(root, text='What is this?', command=what, width=15, height=2, borderwidth=5)
What.grid(row=0, column=2)
Blank=Label(root, text='', width=30, height=2)
Blank.grid(row=0, column=3)

root.mainloop()
