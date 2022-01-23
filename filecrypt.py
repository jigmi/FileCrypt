#pip install tk
#pip install pycryptodome 
from tkinter import *
from tkinter import filedialog
from Cryptodome.Random import get_random_bytes
from Cryptodome.Protocol.KDF import PBKDF2
from Cryptodome.Cipher import AES 
from Cryptodome.Util.Padding import pad,unpad
import os
def gui_setup():
    global gui
    global v 
    global l
    gui = Tk() 
    gui.title("FileCrypt Application")
    v = StringVar()
    l = StringVar()
    gui.geometry("400x450") 
    gui.iconbitmap("C:\\users\\61478\\desktop\\encrypted.ico")
    selectfile = Button(gui,text = "SELECT FILE", fg = "white",bg = "#1089ff",  command = fileopen, font = (None,10),height = 2, width= 30).place(x = 70, y= 40)
    displaytext = Label(gui,textvariable=v,font = (None,9),bg = "white",height = 2, width = 40).place(x = 55,y = 100)
    enterpasswordtitle = Label(gui,text = "Enter Password",  font = (None,10)).place(x=0, y= 160)
    enterpassword = Entry(gui,width=50,textvariable=l,show = "*").place(x=45,y=190)
    encryptbutton = Button(gui,text = "Encrypt", bg = "#27ae60", fg = "#ffffff",command = encryption,font = (None,10),height = 3, width = 12).place(x=55,y=250)
    decryptbutton = Button(gui,text = "Decrypt",bg = "red", fg = "#ffffff", command = decryption, font = (None,10), height = 3, width = 12).place(x=235, y= 250)
    gui.mainloop()  
def fileopen():
    global root_filename
    root_filename = filedialog.askopenfilename()
    v.set(root_filename) 
def encryption():
    global password
    global global_status
    global_status = StringVar()
    password = l.get()
    salt = get_random_bytes(32)
    key = PBKDF2(password,salt,dkLen=32)
    cipher = AES.new(key,AES.MODE_CBC)
    iv = cipher.iv
    file_path = root_filename
    file_path_encrypted = file_path + ".enc"
    x = open(file_path,"rb")
    o = open(file_path_encrypted,"wb")
    Label(gui,textvariable=global_status,font= (None,10)).place(x=160,y=340)
    global_status.set("Encrypting")
    f = x.read(32)
    o.write(iv)
    o.write(salt)
    o.write(cipher.encrypt(pad(b'valid-file#',32)))
    while (f):
        if len(f) % 32 == 0:
            encrypted = cipher.encrypt(f)
            o.write(encrypted)
        elif len(f) % 32 != 0:
            f = pad(f,32)
            encrypted = cipher.encrypt(f)
            o.write(encrypted)
        else:
            pass
        f = x.read(32)
    x.close()
    o.close()
    global_status.set("Encrypted")
    os.unlink(file_path)
def decryption():
    password = l.get()
    filepath = root_filename
    decrypting_file_reading = open(filepath,"rb")
    iv = decrypting_file_reading.read(16)
    salt = decrypting_file_reading.read(32)
    key = PBKDF2(password,salt,dkLen=32)
    decrypt_cipher = AES.new(key,AES.MODE_CBC,iv)
    decrypted_file = open(filepath.replace(".enc",""),"wb") 
    verify_file = decrypting_file_reading.read(32)
    verify_file = decrypt_cipher.decrypt(verify_file)
    if b'valid-file#' not in verify_file:
        global_status.set("Incorrect Password")
        decrypting_file_reading.close()
        decrypted_file.close()
        os.unlink(filepath.replace(".enc",""))
    else:
        global_status.set("Decrypting")  
        x = decrypting_file_reading.read(32)
        while (x):
            if len(x) % 32 == 0:
                decryptor = decrypt_cipher.decrypt(x)
                decrypted_file.write(decryptor)
            elif len(x) % 32 != 0:
                decryptor = decrypt_cipher.decrypt(x)
                x = unpad(decryptor,32)
                decrypted_file.write(x)
            else:
                pass
            x = decrypting_file_reading.read(32)
        decrypting_file_reading.close()
        decrypted_file.close()
        global_status.set("Decrypted")
        os.unlink(filepath)
gui_setup()
