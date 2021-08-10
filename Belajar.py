import os
import time
import tkinter
import tkinter as tk


window=tkinter.Tk()
window.title("Aplikasi")
window.geometry('800x500')
C = tk.Canvas()
filename = tk.PhotoImage(file = "Mountain2560x1600.png")
background_label = tk.Label(image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()


#------------Software----------------------------------------------------
photoexcel=tk.PhotoImage(file="excel.png")
photoword=tk.PhotoImage(file="Microsoft-Word-Logo.png")
photoshop=tk.PhotoImage(file="gf.png")
Chroeme=tk.PhotoImage(file="w.png")



def ofice():
    os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word 2016.lnk")

def excel():
    os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel 2016.lnk")

def photoshoep():
    os.startfile("D:\SteamLibrary1\steamapps\common\MountBlade Warband\mb_warband.exe")

def Chrome():
    os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")


button_1 = tkinter.Button(window,image=photoexcel,width="105",height="100",command=excel)
button_1.place(x=685,y=260)


button_2 = tkinter.Button(window,image=photoword,width="105",height="100",command=ofice)
button_2.place(x=555,y=260)


button_3 = tkinter.Button(window,image=photoshop,width="105",height="100",command=photoshoep)
button_3.place(x=555,y=370)


button_4 = tkinter.Button(window,image=Chroeme,width="105",height="100",command=Chrome)
button_4.place(x=685,y=370)
#------------Software-----------------------------------------------------


#------------Game-----------------------------------------------------
warband=tk.PhotoImage(file="3985057-middle.png")
wogg=tk.PhotoImage(file="PyCharm_Icon.png")
PyCharm=tk.PhotoImage(file="71Ak8xgYSAL.png")
discrod=tk.PhotoImage(file="discord-icon-maker-12 (1).png")

def mbwarband():
    os.startfile("D:\SteamLibrary\steamapps\common\MountBlade Warband\mb_warband.exe")
def wog():
    os.startfile("D:\SteamLibrary\steamapps\common\WOG\disasm.exe")
def pycharm():
    os.startfile("D:\pycarm\PyCharm Community Edition 2021.2\bin\pycharm64.exe")
def discord():
    os.startfile("asd.lnk")

button_5 = tkinter.Button(window,image=warband,width="105",height="100",command=mbwarband)
button_5.place(x=20,y=260,)

button_5 = tkinter.Button(window,image=wogg,width="105",height="100",command=wog)
button_5.place(x=150,y=260,)

button_5 = tkinter.Button(window,image=PyCharm,width="105",height="100",command=pycharm)
button_5.place(x=20,y=370,)

button_dis = tkinter.Button(window,image=discrod,width="105",height="105",command=discord)
button_dis.place(x=150,y=370,)

#---------------------------------Game--------------------------------

#--------------------------------SYSTEM-------------------------------

def quit():
    window.destroy()
def Shutdown(menit, detik):
    total = menit * 60 + detik
    while total:
        mins, secs = divmod(total, 60)
        time.sleep(1)
        total -= 3
    os.system("shutdown /s /t 1")
def restart():
    os.system("shutdown -t 0 -r -f")
def logut():
    os.system("shutdown -l")

button_6 = tkinter.Button(window,text="Shutdown",width="11",height="2",command=Shutdown)
button_6.place(x=310,y=350,)

button_7 = tkinter.Button(window,text="Exit",width="11",height="2",command=quit)
button_7.place(x=420,y=350)

button_8 = tkinter.Button(window,text="restart",width="11",height="2",command=restart)
button_8.place(x=310,y=400)

button_9 = tkinter.Button(window,text="Logout",width="11",height="2",command=logut)
button_9.place(x=420,y=400)

#--------------------------------SYSTEM-------------------------------



tkinter.mainloop()


