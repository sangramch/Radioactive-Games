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
from highlow_mod import *
import tkMessageBox

typelist=[]
trial=[]
cheat_use=False
limit=lim()

def fullquit(win2,root):
    #when won
    win2.destroy()
    root.destroy()

def quitting(root):
    #when pressed quit in main window
    quitvar=tkMessageBox.askyesno("Are You Sure?","Are you sure you want to Quit?")
    if quitvar==1:
        root.destroy()
        
def uno_check(no1,k,root,entr1):
    no=no1.get()
    if no=='%reveal':
        global cheat_use
        cheat_use=True
        win2=Toplevel()
        win2.geometry("300x200+550+100")
        win2.overrideredirect(1)
        win2.tkraise()
        win2.focus_force()
        win2.bind('<Return>',lambda x:win2.destroy())
        Label(win2,text="CHEAT ACCEPTED\n{}".format(k),font=("Agency FB",25,"bold"), pady=20).pack()
        entr1.delete(0, 'end')
        Button(win2,text="Okay",command=lambda:win2.destroy(),relief='flat',bg='red',fg='white').place(y=150,x=100,width=100,height=25)
        
    elif len(no)==0:
        #if nothing is entered and user presses check
        tkMessageBox.showerror("Nothing Entered!!","You have entered nothing!!!")
        
    elif num_check(no,k)==False:
        #if the number entered wrong in any way
        win2=Toplevel()
        win2.tkraise()
        win2.overrideredirect(1)
        win2.focus_force()
        win2.geometry("200x70+605+200")
        win2.bind('<Return>',lambda x:win2.destroy())
        Label(win2,text="You have entered something wrong.",font=(20)).pack()
        entr1.delete(0, 'end')
        Button(win2,text="Okay",command=lambda:win2.destroy(),relief='flat',bg='red',fg='white').place(width=100,x=50,y=40,height=25)
        
    else:
        #main check, if no is high or low
        global limit
        if limit<=10:
            global typelist
            global trial
            typelist.append(no)
            limit+=1
            win2=Toplevel(bg='white')
            win2.geometry("300x220+550+100")
            win2.overrideredirect(1)
            win2.tkraise()
            win2.focus_force()
            win2.bind('<Return>',lambda x:win2.destroy())
            if luck_check(no,k)=='win':
                win2.bind('<Return>',lambda x:fullquit(win2,root))
                if cheat_use==True:
                    Label(win2,text="You Win!!",font=('-family broadway -size 40'),bg='white').pack()
                    Label(win2,text='\n\nWITH CHEAT',bg='white').pack()
                else:
                    Label(win2,text="You Win!!",font=('-family broadway -size 40'),pady=40,bg='white').pack()
                entr1.delete(0, 'end')
                Button(win2,text="Okay",command=lambda:fullquit(win2,root),relief='flat',bg='red',fg='white').place(y=190,x=100,width=100,height=25)
            elif luck_check(no,k)=='high':
                Label(win2,text="Your number is",font=('-size 13'),bg='white').pack()
                Label(win2,text="Higher",font=('-size 20'),bg='white').pack()
                Label(win2,text="Chances Left:  {}".format(12-limit),justify='center').pack()
                highimg=PhotoImage(file='high.gif')
                highlbl=Label(win2,image=highimg,bg='white')
                highlbl.pack()
                highlbl.image=highimg
                Button(win2,text="Okay",command=lambda:win2.destroy(),relief='flat',bg='red',fg='white').place(y=190,x=100,width=100,height=25)
                trial.append('Higher')
                entr1.delete(0, 'end')
            elif luck_check(no,k)=='low':
                Label(win2,text="Your number is",font=('-size 13'),bg='white').pack()
                Label(win2,text="Lower",font=('-size 20'),bg='white').pack()
                Label(win2,text="Chances Left:  {}".format(12-limit),justify='center').pack()
                lowimg=PhotoImage(file='low.gif')
                lowlbl=Label(win2,image=lowimg)
                lowlbl.pack()
                lowlbl.image=lowimg
                Button(win2,text="Okay",command=lambda:win2.destroy(),relief='flat',bg='red',fg='white').place(y=190,x=100,width=100,height=25)
                trial.append('Lower')
                entr1.delete(0, 'end')
        else:
            #when all turns are gone
            win2=Toplevel()
            win2.tkraise()
            win2.geometry("300x200+550+100")
            win2.overrideredirect(1)
            win2.focus_force()
            root.destroy()
            Label(win2,text="You have lost all 6 turns.\nTime to end the game.\n\nYour Number Was {}".format(k),font=('comic sans ms',15,'bold')).pack()
            win2.bind('<Return>',lambda x:win2.destroy())
            Button(win2,text="Okay",command=lambda:win2.destroy(),relief='flat',bg='red',fg='white').place(y=150,x=100,width=100,height=25)

def typed():
    #the no which have already been typed
    if len(typelist)==0:
        tkMessageBox.showerror("Empty", "You Have Typed Nothing Till Now!!!")
        
    else:
        types=Toplevel()
        types.wm_attributes("-topmost", 1)
        types.focus_force()
        types.geometry("+600+100")
        types.overrideredirect(1)
        types.tkraise()
        types.bind('<Return>',lambda x:types.destroy())
        for i in range(len(typelist)):
            Label(types,text=typelist[i],font=('courier',13,'normal'),width=20).pack()
            Label(types,text=trial[i],font=('courier',13,'normal'),width=20).pack()
        Button(types,text="OK", command=lambda:types.destroy(),width=20,relief='flat',bg='red',fg='white',borderwidth=1).pack()

def mainwin(k):
    root=Toplevel()
    root.title("The High Low Project")
    root.geometry("410x500+500+80")
    root.overrideredirect(1)
    root.tkraise()
    root.focus_force()

    cover =PhotoImage(file='highlowcover.gif')
    cvr_lbl = Label(root,image=cover)
    cvr_lbl.pack()
    cvr_lbl.image=cover

    no1=StringVar()

    Label(root,text="We have selected a random number for you.\nType in a number and we will show you if it is higher or lower.\n----Remember----\nThe number must be between 1 and 99.\nThe number must not have letters.\nClick 'Your Nos.' to see all the values you have entered.\nClick 'Quit' to quit the game.").pack()
    entr1=Entry(root,textvariable=no1,justify='center',relief='solid',borderwidth=2,font=("arial",20,"normal"))
    entr1.place(x=5, y=380, width=400)
    entr1.bind('<Return>',lambda x:uno_check(no1,k,root,entr1))
    chkbtn=Button(root,text="Check",command=lambda:uno_check(no1,k,root,entr1), relief='flat', borderwidth=1, bg='dark green', fg='white', font=('-weight bold')).place(x=20,y=450,width=100,height=25)
    quitbtn=Button(root,text="Exit",command=lambda:quitting(root), relief='flat', borderwidth=1, bg='red', fg='white', font=('-weight bold')).place(x=155,y=450,width=100,height=25)
    numbtn=Button(root,text="Your Nos.", command=lambda:typed(), relief='flat', borderwidth=1, bg='dark green', fg='white', font=('-weight bold')).place(x=290,y=450,width=100,height=25)

    root.mainloop()
    
def select_num():
    global typelist
    global trial
    global cheat_use
    global limit
    
    typelist=[]
    trial=[]
    limit=lim()
    cheat_use=False
    
    k=secret_select()
    mainwin(k)
