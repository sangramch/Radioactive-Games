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
from hangman_mod import *
import tkMessageBox

entered_list=[]
typelist=[]
trial=[]
star_list=['*','*','*','*']
hang=0
cheat_use=False

def fullquit(win2,root):
    #when won
    win2.destroy()
    root.destroy()

def quitting(root):
    #when pressed quit in main window
    quitvar=tkMessageBox.askyesno("Are You Sure?","Are you sure you want to Quit?")
    if quitvar==1:
        root.destroy()

def uno_check(user_char1,secret_word,root,entr1,wordlbl):
    global star_list
    global hang
    global entered_list
    global cheat_use
    user_char=user_char1.get()
    
    if len(user_char)==0:
        tkMessageBox.showerror("Nothing Entered!!","You have entered nothing!!!")
    else:
        win2=Toplevel()
        win2.geometry("300x200+550+100")
        win2.overrideredirect(1)
        win2.tkraise()
        win2.focus_force()
        win2.bind('<Return>',lambda x:win2.destroy())
        
        if '*' in star_list:
            if user_char=='%reveal':
                cheat_use=True
                Label(win2,text='CHEAT ACCEPTED!!\n{}'.format(secret_word),font=("Agency FB",25,"bold"), pady=20).pack()
                Button(win2,text="Okay",command=lambda:win2.destroy(),relief='flat',bg='red',fg='white').place(y=150,x=100,width=100,height=25)
                entr1.delete(0, 'end')
                
            elif already(user_char,entered_list)==False:
                entered_list.append(user_char)
                if check(user_char)== True:
                    starword=""
                    typelist.append(user_char)
                    
                    if user_char in secret_word and len(user_char)==1:
                        for i in range(len(secret_word)):
                            if user_char==secret_word[i]:
                                star_list[i]=user_char
                                
                        for j in range(len(star_list)):
                            starword+=star_list[j]

                        if '*' in star_list:                            
                            Label(win2,text='Congrats!! Your Entry is present!!\n The revealed letters are',pady=20,font=(20)).pack()
                            Label(win2,text='{}'.format(starword),font='-size 25').pack()
                            trial.append(starword)
                            Button(win2,text="Okay",command=lambda:win2.destroy(),relief='flat',bg='red',fg='white').place(y=150,x=100,width=100,height=25)
                            wordlbl.config(text=starword)
                            entr1.delete(0, 'end')
                        else:
                            wordlbl.config(text=starword)
                            Label(win2,text='You Won!!!',font=('-family broadway -size 35')).pack()
                            if cheat_use==True:
                                Label(win2,text='USED CHEAT').pack()
                            win2.bind('<Return>',lambda x:fullquit(win2,root))
                            Button(win2,text="Okay",command=lambda:fullquit(win2,root),relief='flat',bg='red',fg='white').place(y=150,x=100,width=100,height=25)
                            
                    elif user_char==secret_word:
                        wordlbl.config(text=starword)
                        Label(win2,text='You Won!!!',font=('-family broadway -size 35')).pack()
                        if cheat_use==True:
                            Label(win2,text='USED CHEAT').pack()
                        win2.bind('<Return>',lambda x:fullquit(win2,root))
                        Button(win2,text="Okay",command=lambda:fullquit(win2,root),relief='flat',bg='red',fg='white').place(y=150,x=100,width=100,height=25)

                    else:
                        if hang<6:
                            starword=""
                            hangpic=PhotoImage(file='hang{}.gif'.format(hang))
                            Label(win2,text="\nDamn!! You are part hanged!!",font=(20)).pack()
                            picturehang=Label(win2,image=hangpic)
                            picturehang.pack()
                            picturehang.image=hangpic
                            trial.append('Hanged')
                            Button(win2,text="Okay",command=lambda:win2.destroy(),relief='flat',bg='red',fg='white').place(y=150,x=100,width=100,height=25)
                            entr1.delete(0, 'end')
                            
                            for j in range(len(star_list)):
                                starword+=star_list[j]
                                
                            Label(win2,text=starword,font=(20)).place(y=180,width=300)
                            hang+=1
                            
                        elif hang>=6:
                            Label (win2,text="Shit!! You are fully hanged!!",font=(20)).pack()
                            Label (win2,text="Your Word Was '{}'".format(secret_word)).pack()
                            hangpic=PhotoImage(file='hang6.gif')
                            picturehang=Label(win2,image=hangpic)
                            picturehang.pack()
                            picturehang.image=hangpic
                            root.destroy()
                            Button(win2,text="Okay",command=lambda:win2.destroy(),relief='flat',bg='red',fg='white').place(y=150,x=100,width=100,height=25)
                            
                elif check(user_char)== False:
                    Label(win2,text='Your letter is faulty!!\nTry Again!!',font=(20)).pack()
                    entr1.delete(0, 'end')
                    Button(win2,text="Okay",command=lambda:win2.destroy(),relief='flat',bg='red',fg='white').place(y=150,x=100,width=100,height=25)
                    
            elif already(user_char,entered_list)==True:
                Label(win2,text='This Letter has\nalready been entered').pack()
                Button(win2,text="Okay",command=lambda:win2.destroy(),relief='flat',bg='red',fg='white').place(y=150,x=100,width=100,height=25)
                entr1.delete(0, 'end')
                
        else:
            Label(win2,text='\nYou Won!!!',font=('-family broadway -size 35')).pack()
            if cheat_use==True:
                Label(win2,text='\n\nWITH CHEAT').pack()
            win2.bind('<Return>',lambda x:fullquit(win2,root))
            Button(win2,text="Okay",command=lambda:fullquit(win2,root),relief='flat',bg='red',fg='white').place(y=150,x=100,width=100,height=25)

def typed():
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
    
def mainwin(secret_word,hint):
    root=Toplevel()
    root.title("Hangman")
    root.geometry("410x500+500+80")
    root.overrideredirect(1)
    root.tkraise()
    root.focus_force()

    cover =PhotoImage(file='hangmancover.gif')
    cvr_lbl = Label(root,image=cover)
    cvr_lbl.pack()
    cvr_lbl.image=cover

    user_char1=StringVar()

    Label(root,text="We have selected a random word for you.\nType in a letter and we will show you if it is present.\n----Remember----\nIf you enter wrong letter, you are hanged partly.\nThere must only be one letter or the full word.\nClick 'Your Letters' to see all the letters you have entered.").pack()
    Label(root,text="Hint:  {}".format(hint), font=("bold")).pack()
    wordlbl=Label(root,text='****',font='-size 20',relief='solid')
    wordlbl.place(x=205, y=380, width=190)
    entr1=Entry(root,textvariable=user_char1,justify='center',relief='solid',borderwidth=2,font=("arial",20,"normal"))
    entr1.place(x=5, y=380, width=190)
    entr1.bind('<Return>',lambda x:uno_check(user_char1,secret_word,root,entr1,wordlbl))
    chkbtn=Button(root,text="Check",command=lambda:uno_check(user_char1,secret_word,root,entr1,wordlbl), relief='flat', borderwidth=1, bg='dark green', fg='white', font=('-weight bold')).place(x=20,y=450,width=100,height=25)
    quitbtn=Button(root,text="Exit",command=lambda:quitting(root), relief='flat', borderwidth=1, bg='red', fg='white', font=('-weight bold')).place(x=155,y=450,width=100,height=25)
    numbtn=Button(root,text="Your Letters", command=lambda:typed(), relief='flat', borderwidth=1, bg='dark green', fg='white', font=('-weight bold')).place(x=290,y=450,width=100,height=25)

    root.mainloop()

def secret_sel():
    global entered_list
    global typelist
    global trial
    global hang
    global cheat_use
    global star_list

    entered_list=[]
    typelist=[]
    trial=[]
    hang=1
    cheat_use=False
    star_list=['*','*','*','*']
    
    secret=select_word()
    secret_word=secret[0]
    hint=secret[1]
    mainwin(secret_word,hint)
