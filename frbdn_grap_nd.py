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
from frbdn_mod import *
import tkMessageBox

tried=[]
typelist=[]
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

def uno_check(userno,entr1,root,chosen_letter_1,chosen_letter_2,chosen_letter_3,chosen_letter_4,chosen_letter_5):
    #checks for everything. cheats, wrong inputs and also if forbidden no present. when check button is pressed
    global limit
    user_no=userno.get()
    cheat=False
    chosen_letter1=chosen_letter_1
    chosen_letter2=chosen_letter_2
    chosen_letter3=chosen_letter_3
    chosen_letter4=chosen_letter_4
    chosen_letter5=chosen_letter_5

    if user_no=='%reveal':
        #checks if cheat given. again.. cheats are intended for development purposes.
        cheat=True
        win2=Toplevel()
        win2.geometry("300x200+550+100")
        win2.overrideredirect(1)
        win2.tkraise()
        win2.focus_force()
        win2.bind('<Return>',lambda x:win2.destroy())
        Label(win2,text="CHEAT ACCEPTED\n{}, {}, {}, {}, {}".format(chosen_letter1,chosen_letter2,chosen_letter3,chosen_letter4,chosen_letter5),font=("Agency FB",25,"bold"), pady=20).pack()
        entr1.delete(0, 'end')
        Button(win2,text="Okay",command=lambda:win2.destroy(),relief='flat',bg='red',fg='white').place(y=150,x=100,width=100,height=25)
        
    elif user_check(user_no)==False:
        #checks if the input is correct
        win2=Toplevel()
        win2.tkraise()
        win2.overrideredirect(1)
        win2.focus_force()
        win2.geometry("200x70+605+200")
        win2.bind('<Return>',lambda x:win2.destroy())
        Label(win2,text="Your Word has some Errors!!!",font=(20)).pack()
        entr1.delete(0, 'end')
        Button(win2,text="Okay",command=lambda:win2.destroy(),relief='flat',bg='red',fg='white').place(width=100,x=50,y=40,height=25)

    elif len(user_no)==0:
        #if nothing is entered and user presses check
        tkMessageBox.showerror("Nothing Entered!!","You have entered nothing!!!")

    elif correctword(user_no)==False:
        win2=Toplevel()
        win2.tkraise()
        win2.overrideredirect(1)
        win2.focus_force()
        win2.geometry("200x70+605+200")
        win2.bind('<Return>',lambda x:win2.destroy())
        Label(win2,text="Your entry is not\na valid english word.",font=(20)).pack()
        entr1.delete(0, 'end')
        Button(win2,text="Okay",command=lambda:win2.destroy(),relief='flat',bg='red',fg='white').place(width=100,x=50,y=40,height=25)
        
    else:
        #main check, if forbidden no is present
        if(limit<=6):
            global typelist
            global tried
            typelist.append(user_no)
            win2=Toplevel()
            win2.geometry("300x200+550+100")
            win2.overrideredirect(1)
            win2.tkraise()
            win2.focus_force()
            win2.bind('<Return>',lambda x:win2.destroy())
            if user_forbidden(user_no,chosen_letter1,chosen_letter2,chosen_letter3,chosen_letter4,chosen_letter5)=="5fl":
                Label(win2,text="Your word has all 5 forbidden letters in it.\n{} Turns Left.".format(7-limit)).pack()
                tried.append("5 Forbidden Letters")
                entr1.delete(0, 'end')
                Button(win2,text="Okay",command=lambda:win2.destroy(),relief='flat',bg='red',fg='white').place(y=150,x=100,width=100,height=25)
                
            elif user_forbidden(user_no,chosen_letter1,chosen_letter2,chosen_letter3,chosen_letter4,chosen_letter5)=="4fl":
                Label(win2,text="Your word has 4 forbidden letters in it.\n{} Turns Left.".format(7-limit)).pack()
                tried.append("4 Forbidden Letters")
                entr1.delete(0, 'end')
                Button(win2,text="Okay",command=lambda:win2.destroy(),relief='flat',bg='red',fg='white').place(y=150,x=100,width=100,height=25)
                
            elif user_forbidden(user_no,chosen_letter1,chosen_letter2,chosen_letter3,chosen_letter4,chosen_letter5)=="3fl":
                Label(win2,text="Your word has 3 forbidden letters in it.\n{} Turns Left.".format(7-limit)).pack()
                tried.append("3 Forbidden Letters")
                entr1.delete(0, 'end')
                Button(win2,text="Okay",command=lambda:win2.destroy(),relief='flat',bg='red',fg='white').place(y=150,x=100,width=100,height=25)
                
            elif user_forbidden(user_no,chosen_letter1,chosen_letter2,chosen_letter3,chosen_letter4,chosen_letter5)=="2fl":
                Label(win2,text="Your word has 2 forbidden letters in it.\n{} Turns Left.".format(7-limit)).pack()
                tried.append("2 Forbidden Letters")
                entr1.delete(0, 'end')
                Button(win2,text="Okay",command=lambda:win2.destroy(),relief='flat',bg='red',fg='white').place(y=150,x=100,width=100,height=25)
                
            elif user_forbidden(user_no,chosen_letter1,chosen_letter2,chosen_letter3,chosen_letter4,chosen_letter5)=="1fl":
                Label(win2,text="Your word has 1 forbidden letter in it.\n{} Turns Left.".format(7-limit)).pack()
                tried.append("1 Forbidden Letters")
                entr1.delete(0, 'end')
                Button(win2,text="Okay",command=lambda:win2.destroy(),relief='flat',bg='red',fg='white').place(y=150,x=100,width=100,height=25)
                
            elif user_forbidden(user_no,chosen_letter1,chosen_letter2,chosen_letter3,chosen_letter4,chosen_letter5)=="0fl":
                Label(win2,text="You have your word which contains\nnone of the forbidden letters").pack()
                Label(win2,text="You Win!!",font=('-size 20')).pack()
                Label(win2,text="The forbidden letters were {}, {}, {}, {} and {}".format(chosen_letter1,chosen_letter2,chosen_letter3,chosen_letter4,chosen_letter5)).pack()
                if cheat==True:
                    Label(win2,text="\nWITH CHEAT").pack()
                qbtn=Button(win2,text="Okay",command=lambda:fullquit(win2,root),relief='flat',bg='red',fg='white').place(y=150,x=100,width=100,height=25)
                win2.bind('<Return>',lambda x:fullquit(win2,root))
                
            limit+=1
            
        else:
            #when all turns are gone
            win2=Toplevel()
            win2.tkraise()
            win2.geometry("300x200+550+100")
            win2.overrideredirect(1)
            win2.focus_force()
            root.destroy()
            Label(win2,text="You have lost all 6 turns.\nTime to end the game.\n\nThe Letters Were\n{},{},{},{} and {}".format(chosen_letter1,chosen_letter2,chosen_letter3,chosen_letter4,chosen_letter5),font=('comic sans ms',15,'bold')).pack()
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
            Label(types,text=tried[i],font=('courier',13,'normal'),width=20).pack()
        Button(types,text="OK", command=lambda:types.destroy(),width=20,relief='flat',bg='red',fg='white',borderwidth=1).pack()

def mainwin(chosen_letter_1,chosen_letter_2,chosen_letter_3,chosen_letter_4,chosen_letter_5):
    #main window. every operation takes place from here
    root=Toplevel()
    root.title("Does It Contain Forbidden Letters")
    root.geometry("410x500+500+80")
    root.overrideredirect(1)
    root.tkraise()
    root.focus_force()

    cover =PhotoImage(file='frbdncover.gif')
    cvr_lbl = Label(root,image=cover)
    cvr_lbl.pack()
    cvr_lbl.image=cover

    userno=StringVar()

    Label(root,text="We have selected 5 random letters for you.\nType in a word and we will show you if it got a forbidden letter.\n----Remember----\nThere must be no numbers or symbols in the word.\nThere must be no UPPER CASE in the word.\nClick 'Your Words' to see all the values you have entered.\nClick 'Quit' to quit the game.").pack()
    entr1=Entry(root,textvariable=userno,justify='center',relief='solid',borderwidth=2,font=("arial",20,"normal"))
    entr1.place(x=5, y=380, width=400)
    entr1.bind('<Return>',lambda x:uno_check(userno,entr1,root,chosen_letter_1,chosen_letter_2,chosen_letter_3,chosen_letter_4,chosen_letter_5))
    chkbtn=Button(root,text="Check",command=lambda:uno_check(userno,entr1,root,chosen_letter_1,chosen_letter_2,chosen_letter_3,chosen_letter_4,chosen_letter_5), relief='flat', borderwidth=1, bg='dark green', fg='white', font=('-weight bold')).place(x=20,y=450,width=100,height=25)
    quitbtn=Button(root,text="Exit",command=lambda:quitting(root), relief='flat', borderwidth=1, bg='red', fg='white', font=('-weight bold')).place(x=155,y=450,width=100,height=25)
    numbtn=Button(root,text="Your Words", command=lambda:typed(), relief='flat', borderwidth=1, bg='dark green', fg='white', font=('-weight bold')).place(x=290,y=450,width=100,height=25)

    root.mainloop()

def numsel():
    global tried
    global typelist
    global limit
    
    tried=[]
    typelist=[]
    limit=lim()
    
    #for selection of numbers from another module
    stock_forbidden_letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    chosen_letter_1=selnum1()
    chosen_letter_2=selnum2()
    chosen_letter_3=selnum3()
    chosen_letter_4=selnum4()
    chosen_letter_5=selnum5()
    mainwin(chosen_letter_1,chosen_letter_2,chosen_letter_3,chosen_letter_4,chosen_letter_5)
