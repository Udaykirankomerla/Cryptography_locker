
from tkinter import *
from tkinter import messagebox
import base64
import os





def Mainscreen():
    def decrypt():
        passcode = cde.get()
        if passcode == "1234":
            msg = text1.get(1.0, END)
            decodemsg = msg.encode("ascii")
            b64byt = base64.b64decode(decodemsg)
            decrypt = b64byt.decode("ascii")

            text2.insert(END, decrypt)
        elif passcode == "":
            messagebox.showerror("Decryption", "Enter Passcode!")
        elif passcode != "1234":
            messagebox.showerror("Decryption", "You have entered \n wrong passcode")

    def encrypt():
        passcode = cde.get()
        if passcode == "1234":
            msg = text1.get(1.0, END)
            encodemsg = msg.encode("ascii")
            b64byt = base64.b64encode(encodemsg)
            encrypt = b64byt.decode("ascii")

            text2.insert(END, encrypt)
        elif passcode == "":
            messagebox.showerror("Encryption","Enter Passcode!")
        elif passcode != "1234":
            messagebox.showerror("Encryption", "You have entered \n wrong passcode")

    screen = Tk()
    screen.geometry("400x400")

    img_icon=PhotoImage(file="locker.png")
    screen.iconphoto(False,img_icon)
    screen.title("Cryptography")

    def reset():
        cde.set("")
        text1.delete(1.0,END)

    Label(text="ENTER TEXT BELOW TO ENCRYPT AND DECRYPT",fg="black",font=("Arial 11 bold")).place(x=10,y=16)
    text1=Text(font="Robote 11",bg="white",relief=GROOVE,wrap=WORD,bd=0,borderwidth=5)
    text1.place(x=10,y=55,width=377,height=44)

    text2=Text(font="Robote 11",bg="white",relief=GROOVE,wrap=WORD,bd=0,borderwidth=5)
    text2.place(x=10, y=110,width=377,height=44)

    Label(text="ENTER PASSCODE",fg="black",font=("Arial 11 bold")).place(x=120,y=160)

    cde=StringVar()
    Entry(textvariable=cde,width=15,bd=0,font=("Robote 18"),show="*",borderwidth=4).place(x=88,y=185)
    Button(text="SHOW \n PIN",height="2",width=8,bg="black",fg="white",bd=0).place(x=310,y=184)

    Button(text="ENCRYPT",height="2",width=23,bg="black",fg="white",bd=0,command=encrypt).place(x=10,y=250)
    Button(text="DECRYPT", height="2", width=23,bg="black",fg="white",bd=0,command=decrypt).place(x=219, y=250)
    Button(text="RESET",height="2",width=30,bg="black",fg="white",bd=0,command=reset).place(x=83,y=300)
    screen.mainloop()

Mainscreen()