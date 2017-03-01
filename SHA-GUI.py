import hashlib
from tkinter import *

root = Tk()
intro = Label(root, text = "DATA")
intro.pack()

data = Text(root, height=10, width=60)
data.pack()
data.insert(END, "")

text2 = Label(root, text = "SHA 256 Encoded Text")
text2.pack()

SHA = Text(root, height=4, width=60)
SHA.pack()
SHA.insert(END, "")


def SHA_encoder(encodedStr):
    sData = data.get('1.0', INSERT)
    eData = sData.encode('utf-8')
    #print(type(eData))
    encodedStr = hashlib.sha3_256()
    encodedStr.update(eData)
    #print(type(encodedStr))
    SHA.delete('1.0', END)
    SHA.insert(END, encodedStr.hexdigest())
    print(eData)
    print(encodedStr.hexdigest())

data.bind("<Key>", SHA_encoder)

#print(sData)
mainloop()
