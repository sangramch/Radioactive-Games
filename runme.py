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
import tkMessageBox
import ScrolledText
import cb_grap_nd
import frbdn_grap_nd
import highlow_grap_nd
import hangman_grap_nd
import os.path
import helpscr
import credit

reference=0
wordtot=""
ltr=['R','a','d','i','o','A','c','t','i','v','e',' ','G','a','m','e','s',' ','I','n','c','.',' ','P','r','e','s','e','n','t','s']

def wtf(lbl1,vroot):
    global reference
    global wordtot
    if reference<len(ltr):
        wordtot+=ltr[reference]
        lbl1.config(text=wordtot)
        if ltr[reference]==" ":
            vroot.after(500, lambda:wtf(lbl1,vroot))
        elif (ltr[reference]=="A" or ltr[reference]=="a"):
            vroot.after(500, lambda:wtf(lbl1,vroot))
        else:
            vroot.after(100, lambda:wtf(lbl1,vroot))
        reference+=1

def destruction(vroot):
    destrm=tkMessageBox.askyesno("Quit?","Are You Sure You Want To Quit?")
    if destrm==1:
        vroot.destroy()

def cb_graphic():
    cb_grap_nd.hrdn()

def frbdn_graphic():
    frbdn_grap_nd.numsel()

def highlow_graphic():
    highlow_grap_nd.select_num()

def hangman_graphic():
    hangman_grap_nd.secret_sel()

def main_vroot():
    vroot=Tk()
    vroot.overrideredirect(1)
    vroot.geometry("520x550+400+100")
    vroot.config(bg='#FEFFA4')
    pic=PhotoImage(file="radioactive.gif")
    logo=Label(vroot,image=pic,height=200,bg='#FEFFA4')
    logo.pack()
    logo.image=pic
    gamename=Label(text="",font=('castellar',18,'normal'),bg='#FEFFA4')
    gamename.pack()
    wtf(gamename,vroot)
    Label(text='\n',font=('castellar',18,'normal'),bg='#FEFFA4').pack()
    cb_btn=Button(vroot,text="Bulls and Cows",command=lambda:cb_graphic(), width=25,relief='flat',font=('britannic bold',18,'normal'),borderwidth=0,bg='#FEFFA4',fg='#2E0000').pack()
    frbdn_btn=Button(vroot,text="Does It Contain Forbidden Letters",command=lambda:frbdn_graphic(), width=35,relief='flat',font=('britannic bold',18,'normal'),borderwidth=0,bg='#FEFFA4',fg='#2E0000').pack()
    highlow_btn=Button(vroot,text="the High Low project",command=lambda:highlow_graphic(), width=25,relief='flat',font=('britannic bold',18,'normal'),borderwidth=0,bg='#FEFFA4',fg='#2E0000').pack()
    hangman_btn=Button(vroot,text="Hangman",command=lambda:hangman_graphic(), width=25,relief='flat',font=('britannic bold',18,'normal'),borderwidth=0,bg='#FEFFA4',fg='#2E0000').pack()
    help_btn=Button(vroot,text="Help",command=lambda:helpscr.help_ask(),relief='flat',bg='black',fg='white',font=('cooper black',15,'bold')).place(x=10,y=500,width=150)
    quit_btn=Button(vroot,text="Quit",command=lambda:destruction(vroot),relief='flat',bg='dark red',fg='white',font=('cooper black',15,'bold')).place(x=185,y=500,width=150)
    credit_btn=Button(vroot,text="Credits",command=lambda:credit.cred(),relief='flat',bg='black',fg='white',font=('cooper black',15,'bold')).place(x=360,y=500,width=150)
    vroot.mainloop()

def accept(tcwin):
    open('tnc_acpt','w')
    tcwin.destroy()
    main_vroot()
def reject(tcwin):
    tcwin.destroy()

def chkbtnclk(var,acceptBtn):
    var1=var.get()
    if var1==1:
        acceptBtn.config(state='normal',bg='dark green',fg='white')
    else:
        acceptBtn.config(state='disabled',bg='grey',fg='black')

def tc_chk():
    if os.path.exists('tnc_acpt')==True:
        main_vroot()
    else:
        tcfile=open('Terms and Conditions.txt','r')
        tcwin=Tk()
        tcwin.geometry("720x600+250+100")
        tcwin.config(bg='#d9d9d9')
        tcwin.overrideredirect(1)
        defaultbg=tcwin.cget('bg')
        Label(tcwin,text="Terms and Conditions",font=('courier',20,'bold'),justify='left',bg='#d9d9d9').place(x=10,y=5)
        tnc=ScrolledText.ScrolledText(tcwin,relief='solid')
        tnc.insert(INSERT,tcfile.read())
        tnc.config(state='disabled')
        tnc.place(x=10,y=50,width=700,height=500)
        var=IntVar()
        acceptBtn=Button(tcwin,text="Accept",command=lambda:accept(tcwin),relief='solid',borderwidth=1,bg='grey',state='disabled')
        acceptBtn.place(x=450,y=560,width=100,height=25)
        rejectBtn=Button(tcwin,text="Reject",command=lambda:reject(tcwin),relief='solid',borderwidth=1,bg='dark red',fg='white').place(x=570,y=560,width=100,height=25)
        agree=Checkbutton(tcwin,text="I agree to the Terms and Conditions",variable=var,command=lambda:chkbtnclk(var,acceptBtn),bg=defaultbg,font='-weight bold')
        agree.place(x=10,y=560)
        agree.var=var
        tcfile.close()
        tcwin.mainloop()

tc_chk()
