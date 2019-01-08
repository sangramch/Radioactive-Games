'''Copyright 2016 RadioActive Games Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.'''


from Tkinter import *
from cb_mod import *
import tkMessageBox
import time

k=0
l1=[]
clist=[]
blist=[]
cheat_use=False
limit=lim()

def destruct(roor,root):
    roor.destroy()
    root.destroy()

def root_destroy(root):
    f=tkMessageBox.askyesno("Are you sure?", "Are you sure you want to quit??")
    if f==True:
        root.destroy()

def btnf(no,entr1,root):

    no1=no.get()
               
    if len(no1)==0:
        tkMessageBox.showerror("Empty Input!!","You Have Entered Nothing...")
               
    elif no1=="%reveal":
        global cheat_use
        cheat_use=True
        entr1.delete(0, 'end')
        roor=Tk()
        roor.geometry("300x200+550+100")
        roor.overrideredirect(1)
        roor.tkraise()
        roor.focus_force()
        roor.bind('<Return>',lambda x:roor.destroy())
        
        ch_lbl=Label(roor,text="Cheat Accepted\n{}".format(k),font=("Agency FB",25,"bold"), pady=20)
        ch_lbl.pack()
        Button(roor,text="Okay",command=lambda:roor.destroy(),relief='flat',bg='red',fg='white',borderwidth=1).place(y=150,x=100,width=100,height=25)
               
    else:
        global limit
        global clist
        global blist
        global l1
        truth=num_check(no1,k)
               
        if truth==True:
            if win(no1,k)==True:
                roor=Toplevel()
                roor.geometry("300x200+550+100")
                roor.overrideredirect(1)
                roor.tkraise()
                roor.focus_force()
                roor.bind('<Return>',lambda x:destruct(roor,root))
                
                entr1.delete(0, 'end')
                Label(roor,text="You Win!",font=("broadway",25,"bold"),pady=30).pack()
                if cheat_use==True:
                    Label(roor,text="WITH CHEAT").pack()
                Button(roor,text="Okay",command=lambda:destruct(roor,root),relief='flat',bg='red',fg='white',borderwidth=1).place(y=150,x=100,width=100,height=25)
            elif limit<=25:
                limit+=1
                l1.append(no1)
                roor=Toplevel()
                roor.geometry("300x230+550+90")
                roor.overrideredirect(1)
                roor.tkraise()
                roor.focus_force()
                roor.bind('<Return>',lambda x:roor.destroy())
                
                Label(roor,text="Cows",font=("broadway",25,"bold")).place(x=30,y=130)
                Label(roor,text="Bulls",font=("broadway",25,"bold")).place(x=165,y=130)
                Label(roor,text="{}".format(cow(no1,k)),font=("broadway",25,"bold")).place(x=70,y=90)
                Label(roor,text="{}".format(bull(no1,k)),font=("broadway",25,"bold")).place(x=205,y=90)

                cowimg=PhotoImage(file='cow.gif')
                bullimg=PhotoImage(file='bull.gif')

                cowlbl=Label(roor,image=cowimg,height=70,width=125)
                cowlbl.image=cowimg
                cowlbl.place(x=10,y=10)
                
                bulllbl=Label(roor,image=bullimg,height=70,width=125)
                bulllbl.image=bullimg
                bulllbl.place(x=165,y=10)
                
                clist.append("Cows = {}".format(cow(no1,k)))
                blist.append("Bulls = {}".format(bull(no1,k)))
                entr1.delete(0, 'end')
                Label(roor,text="Chances Left:  {}".format(27-limit),justify='center').place(width=300,y=180)
                Button(roor,text="Okay",command=lambda:roor.destroy(),relief='flat',bg='red',fg='white',borderwidth=1).place(x=100,y=200,width=100,height=25)
                roor.mainloop()
            else:
                win2=Toplevel()
                win2.tkraise()
                win2.geometry("300x200+550+100")
                win2.overrideredirect(1)
                win2.focus_force()
                root.destroy()
                Label(win2,text="You have lost all 25 turns.\nTime to end the game.\n\nThe Number Was\n{}".format(k),font=('comic sans ms',15,'bold')).pack()
                win2.bind('<Return>',lambda x:win2.destroy())
                Button(win2,text="Okay",command=lambda:win2.destroy(),relief='flat',bg='red',fg='white').place(y=150,x=100,width=100,height=25)
        else:
            roor=Toplevel()
            roor.geometry("300x100+550+150")
            roor.overrideredirect(1)
            roor.tkraise()
            roor.focus_force()
            roor.bind('<Return>',lambda x:roor.destroy())
            Label(roor,text="You have entered {} which contains\nletters or is of more than 4 digits...".format(no1),font=('-size 12')).pack()
            Button(roor,text="Okay",command=lambda:roor.destroy(),relief='flat',bg='red',fg='white',borderwidth=1).place(x=100,y=70,width=100,height=25)
            entr1.delete(0, 'end')

def maingame():
    
    root=Toplevel()
    root.title("Bulls and Cows")
    root.geometry("410x500+500+80")
    root.overrideredirect(1)
    root.tkraise()
    root.focus_force()

    cover =PhotoImage(file='cowbullcover.gif')
    cvr_lbl = Label(root,image=cover)
    cvr_lbl.pack()
    cvr_lbl.image=cover

    no=StringVar()
    
    Label(root,text="We have selected a random no for you to play.\nType in a number and we will show you the Cows and Bulls you got.\n----Remember----\n1 Cow = 1 CORRECT number in the WRONG place.\n1 Bull = 1 CORRECT number in the CORRECT place.\nClick 'Check' to check it with the correct value.\nClick 'Your Nos.' to see all the values you have entered.\nClick 'Quit' to quit the game.").pack()
    entr1=Entry(root,textvariable=no,justify='center',font=("arial",20,"normal"),relief='solid',borderwidth=2)
    entr1.place(x=5, y=380, width=400)
    entr1.bind('<Return>',lambda x:btnf(no,entr1,root))
    chkbtn=Button(root,text="Check", command=lambda:btnf(no,entr1,root), relief='flat', borderwidth=1, bg='dark green', fg='white', font=('-weight bold')).place(x=20,y=450,width=100,height=25)
    numbtn=Button(root,text="Your Nos.", command=lambda:typed(), relief='flat', borderwidth=1, bg='dark green', fg='white', font=('-weight bold')).place(x=290,y=450,width=100,height=25)
    quitbtn=Button(root,text="Quit", command=lambda:root_destroy(root), relief='flat', borderwidth=1, bg='red', fg='white', font=('-weight bold')).place(x=155,y=450,width=100,height=25)

    root.mainloop()

def easiness(hrdnss):
    global k
    k=easy()
    hrdnss.destroy()
    maingame()
    
def mediness(hrdnss):
    global k
    k=medium()
    hrdnss.destroy()
    maingame()
    
def hardness(hrdnss):
    global k
    k=hard()
    hrdnss.destroy()
    maingame()
    
def presetss(hrdnss):#for dev.. see later
    global k
    k="1234"
    hrdnss.destroy()
    separ.destroy()
    maingame()

def typed():
    
    if len(l1)==0:
        tkMessageBox.showerror("Empty", "You Have Typed Nothing Till Now!!!")
        
    else:
        types=Toplevel()
        types.wm_attributes("-topmost", 1)
        types.focus_force()
        types.geometry("+600+150")
        types.overrideredirect(1)
        types.tkraise()
        types.bind('<Return>',lambda x:types.destroy())
        Button(types,text="OK", command=lambda:types.destroy(),relief='flat',bg='red',fg='white',borderwidth=1,width=20).pack()
        for i in range(len(l1)):
            Label(types,text=l1[i],font=('courier',13,'normal'),width=20).pack()
            Label(types,text=clist[i],font=('courier',13,'normal'),width=20).pack()
            Label(types,text=blist[i],font=('courier',13,'normal'),width=20).pack()
        
def hrdn():
    global k
    global l1
    global clist
    global blist
    global cheat_use
    global limit
    
    k=0
    limit=lim()
    l1=[]
    clist=[]
    blist=[]
    cheat_use=False
    
    hrdnss=Toplevel()
    hrdnss.geometry("+450+300")
    hrdnss.overrideredirect(1)
    hrdnss.title("Cows and Bulls")
    hrdnss.tkraise()

    Label(hrdnss,text="Select A Hardness Level\nTo Get On With The Game\n----------",font=("Times",25,"bold")).pack()

    easybtn=Button(hrdnss,text="|   Easy   |",font=("courier",20,"bold"),command=lambda:easiness(hrdnss),width=25,relief="flat",borderwidth=1,activebackground='grey').pack()
    medibtn=Button(hrdnss,text="|  Medium  |",font=("courier",20,"bold"),command=lambda:mediness(hrdnss),width=25,relief="flat",borderwidth=1,activebackground='grey').pack()
    hardbtn=Button(hrdnss,text="|   Hard   |",font=("courier",20,"bold"),command=lambda:hardness(hrdnss),width=25,relief="flat",borderwidth=1,activebackground='grey').pack()

    #intended for development
    #separ=Toplevel()
    #presbtn=Button(separ,text="Preset", command=lambda:presetss()).pack()
    
    hrdnss.mainloop()
