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

def cb_help():
    helpscr=Toplevel()
    helpscr.overrideredirect(1)
    helpscr.geometry("+300+50")
    Label(helpscr,text="Help for",font='-size 20').pack()
    Label(helpscr,text="Bulls and Cows",font='-size 30').pack()
    Label(helpscr,text="----- Description -----",font='-size 15').pack()
    Label(helpscr,text="You were a ranch owner and you knew everything about cattle.\nBut what you did not know was that the cattle are intelligent.\nAnd they were planning on a seige on your ranch.\nThe night they attacked, you were making a game involving cows and bulls.\nThe cattle found the notes you made\nAnd now they have turned the tables on you.").pack()
    Label(helpscr,text="----- Basic Rules -----",font='-size 15').pack()
    Label(helpscr,text="The cattle king Lord Moo has decided to play your game with you.\nHe will select a random four digit no.\nYou have to guess another four digit no and he will show you cattle.\nThe digits in your number which are correct but in the wrong place will be the no. of Cows.\nAnd the no of digits which are correct and in the correct place will be the no. of Bulls.\nYou must guess the correct number before 25 turns, or he will have you plough lands.").pack()
    Label(helpscr,text="----- Hardness Levels -----",font='-size 15').pack()
    Label(helpscr,text="-- Easy --",font='-weight bold').pack()
    Label(helpscr,text="You have flattered the king with your honeyed words.\nSo, he will select the no. from a prebuilt list of 20 numbers").pack()
    Label(helpscr,text="-- Medium --",font='-weight bold').pack()
    Label(helpscr,text="The king is in a good mood, so he will excuse your manners.\nHe will select any four digit number, but it will have no zeroes.").pack()
    Label(helpscr,text="-- Hard --",font='-weight bold').pack()
    Label(helpscr,text="You have defied the king directly, and he is very angry.\nSo, in the number he selects, anything can be present\n\n").pack()
    helpscr.bind('<Return>',lambda x:helpscr.destroy())
    Button(helpscr,text='Okay',command=lambda:helpscr.destroy(),relief='flat',bg='red',fg='white',font='-weight bold',width=9).pack()

def frbdn_help():
    helpscr=Toplevel()
    helpscr.overrideredirect(1)
    helpscr.geometry("+300+50")
    Label(helpscr,text="Help for",font='-size 20').pack()
    Label(helpscr,text="Does It Contain Forbidden Letters",font='-size 30').pack()
    Label(helpscr,text="----- Description -----",font='-size 15').pack()
    Label(helpscr,text="After your village was plagued by a deadly disease, you set out to find a cure.\nAfter a long search elsewhere, you entered the Forbidden Forest, a dark and deadly place.\nBut you still did not find the cure.\nWhen you were starting to think of returning, you met with an ancient witch.\nShe told you she has the cure, but nothing in the world is free.\nSo, you have to play a game.").pack()
    Label(helpscr,text="----- Basic Rules -----",font='-size 15').pack()
    Label(helpscr,text="The witch will have selected 5 random secret letters from the english scripts.\nYou will have to find the word which contains none of the letters.\nBut the witch is impatient, and after 6 tries, she will leave.\nYou must win the game to save your village\n\n").pack()
    helpscr.bind('<Return>',lambda x:helpscr.destroy())
    Button(helpscr,text='Okay',command=lambda:helpscr.destroy(),relief='flat',bg='red',fg='white',font='-weight bold',width=9).pack()

def highlow_help():
    helpscr=Toplevel()
    helpscr.overrideredirect(1)
    helpscr.geometry("+300+50")
    Label(helpscr,text="Help for",font='-size 20').pack()
    Label(helpscr,text="the High Low project",font='-size 30').pack()
    Label(helpscr,text="----- Description -----",font='-size 15').pack()
    Label(helpscr,text="You are the Count of MaximBurd.\nYou have been invited to a duel of wits.\nBy the cunning Duke of Relamont as a reprieve to an ancient wrong.\nBut you know he seeks to take your estates and land once you die.\nAnd he has deviced a devious game for this duel.").pack()
    Label(helpscr,text="----- Basic Rules -----",font='-size 15').pack()
    Label(helpscr,text="The Duke will select a number between 1 and 99.\nYou will tell a number and the Duke will tell you if your number is Higher or Lower than his.\nIf within 10 guesses you can guess his number, You Win.\nOr, your life is forfeit.\n\n").pack()
    helpscr.bind('<Return>',lambda x:helpscr.destroy())
    Button(helpscr,text='Okay',command=lambda:helpscr.destroy(),relief='flat',bg='red',fg='white',font='-weight bold',width=9).pack()

def hangman_help():
    helpscr=Toplevel()
    helpscr.overrideredirect(1)
    helpscr.geometry("+300+50")
    Label(helpscr,text="Help for",font='-size 20').pack()
    Label(helpscr,text="Hangman",font='-size 30').pack()
    Label(helpscr,text="----- Description -----",font='-size 15').pack()
    Label(helpscr,text="The king's brother has been murdered, and you are the suspect.\nYou have been taken to the royal jails and you have been sentenced to be hanged publicly\nBut, you are innocent, and you have one chance to prove it.\nThe Three Seers have deemed you worthy of their attention.\nIf you play a game with them and win, they will know who the real murderer is.").pack()
    Label(helpscr,text="----- Basic Rules -----",font='-size 15').pack()
    Label(helpscr,text="The Seers will select a random word.\n You will be telling them a letter and if it is present in the word, you will be told the position.\nIf not, you will be taken another steps closer to the noose.\nAfter six steps, you will be hanged.\nTo save your honor and your life, you must win.\n\n").pack()
    helpscr.bind('<Return>',lambda x:helpscr.destroy())
    Button(helpscr,text='Okay',command=lambda:helpscr.destroy(),relief='flat',bg='red',fg='white',font='-weight bold',width=9).pack()

def help_ask():
    root=Toplevel()
    root.overrideredirect(1)
    root.geometry("400x320+300+100")
    Label(root,text="Game Help",font=('rockwell',30,'bold')).pack()
    Button(root,text="Bulls and Cows",command=lambda:cb_help(),relief='flat',font='-size 15',borderwidth=0).place(x=0,y=70,width=400,height=30)
    Button(root,text="Does it contain Forbidden Letters",command=lambda:frbdn_help(),relief='flat',font='-size 15',borderwidth=0).place(x=0,y=120,width=400,height=30)
    Button(root,text="the High Low project",command=lambda:highlow_help(),relief='flat',font='-size 15',borderwidth=0).place(x=0,y=170,width=400,height=30)
    Button(root,text="Hangman",command=lambda:hangman_help(),relief='flat',font='-size 15',borderwidth=0).place(x=0,y=220,width=400,height=30)
    root.bind('<Return>',lambda x:root.destroy())
    Button(root,text='Okay',command=lambda:root.destroy(),relief='flat',bg='red',fg='white',font='-weight bold').place(x=150,y=270,width=100,height=30)
    root.mainloop()
