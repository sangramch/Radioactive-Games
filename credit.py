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
import webbrowser

def contact_us():
    cntc=Toplevel()
    cntc.overrideredirect(1)
    cntc.geometry("410x500+500+80")
    GameLogo=PhotoImage(file="radioactive.gif")
    bg=Label(cntc,image=GameLogo,height=180)
    bg.pack()
    bg.image=GameLogo
    Label(cntc,text="RadioActive Games Inc.",font="-size 28").pack()
    Label(cntc,text="For game related queries e-mail at: radioactive.classics@gmail.com").pack()
    Label(cntc,text="For reporting bugs or complaints e-mail at: radioactive.bugs@gmail.com").pack()
    Label(cntc,text="\n",font="-size 5").pack()
    Label(cntc,text="Or Contact Us Individually:",font="-size 20").pack()
    Label(cntc,text="Sangramjit Chakraborty: sangramjich@gmail.com").pack()
    Label(cntc,text="Rahul Pramanik: jiorahul@hotmail.com").pack()
    Label(cntc,text="Jyotirmay Sikdar: jyotirmaysikdar0@gmail.com").pack()
    Label(cntc,text="Sayantan Parua: p.sayontan951@gmail.com").pack()
    Label(cntc,text="Saunak Banik: saunakbanik123@gmail.com").pack()
    quitbtn=Button(cntc,text="Okay",command=lambda:cntc.destroy(), relief='flat', borderwidth=1, bg='red', fg='white', font=('-weight bold')).place(x=155,y=450,width=100,height=25)
    cntc.mainloop()

def cred():
    root=Toplevel()
    root.title("The High Low Project")
    root.geometry("410x600+500+80")
    root.overrideredirect(1)
    root.tkraise()
    root.focus_force()

    cover =PhotoImage(file='grp_membrs.gif')
    cvr_lbl = Label(root,image=cover)
    cvr_lbl.pack()
    cvr_lbl.image=cover

    bama_img=PhotoImage(file="bama.gif")
    para_img=PhotoImage(file="para.gif")
    joga_img=PhotoImage(file="joga.gif")
    prua_img=PhotoImage(file="prua.gif")
    bnka_img=PhotoImage(file="bnka.gif")

    bama_lbl=Label(root,image=bama_img)
    bama_lbl.place(x=5,y=160,width=80,height=80)
    bama_lbl.image=bama_img
    Label(root,text=('{}'.format('Sangramjit Chakraborty')),font="-weight bold").place(x=90,y=160)
    Label(root,text='Cows and Bulls Game Development, Building Base Platform, \nGame Debugging, Tkinter Integration and Documentation').place(x=90,y=185)
    
    para_lbl=Label(root,image=para_img)
    para_lbl.place(x=5,y=230,width=80,height=80)
    para_lbl.image=para_img
    Label(root,text=('{}'.format('Rahul Pramanik')),font=("-weight bold")).place(x=90,y=230)
    Label(root,text='Hangman Game Development, Tkinter Integration Help').place(x=90,y=255)

    joga_lbl=Label(root,image=joga_img)
    joga_lbl.place(x=5,y=310,width=80,height=80)
    joga_lbl.image=joga_img
    Label(root,text=('{}'.format('Jyotirmay Sikdar')),font=("-weight bold")).place(x=90,y=310)
    Label(root,text='High or Low Game Development').place(x=90,y=335)

    prua_lbl=Label(root,image=prua_img)
    prua_lbl.place(x=5,y=390,width=80,height=80)
    prua_lbl.image=prua_img
    Label(root,text=('{}'.format('Sayantan Parua')),font=("-weight bold")).place(x=90,y=390)
    Label(root,text='Does It Contain Forbidden Letters Game Development').place(x=90,y=415)

    joga_lbl=Label(root,image=bnka_img)
    joga_lbl.place(x=5,y=470,width=80,height=80)
    joga_lbl.image=bnka_img
    Label(root,text=('{}'.format('Saunak Banik')),font=("-weight bold")).place(x=90,y=470)
    Label(root,text='None').place(x=90,y=495)
    
    chkbtn=Button(root,text="Licence",command=lambda:webbrowser.open('http://www.apache.org/licenses/LICENSE-2.0', new=2, autoraise=True), relief='flat', borderwidth=1, bg='dark green', fg='white', font=('-weight bold')).place(x=20,y=550,width=100,height=25)
    quitbtn=Button(root,text="Exit",command=lambda:root.destroy(), relief='flat', borderwidth=1, bg='red', fg='white', font=('-weight bold')).place(x=155,y=550,width=100,height=25)
    numbtn=Button(root,text="Contact Us", command=lambda:contact_us(), relief='flat', borderwidth=1, bg='dark green', fg='white', font=('-weight bold')).place(x=290,y=550,width=100,height=25)

    root.mainloop()
