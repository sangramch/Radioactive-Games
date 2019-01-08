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

import random
from Tkinter import *
import tkMessageBox
import time
import os

usedic=True
try:
     import enchant
     usedic=True
except ImportError:
     tkMessageBox.showerror("Error!","You do not have a dictionary module installed.")
     usedic=False

stock_forbidden_letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def correctword(user_val):
     if usedic==True:
          dictionary=enchant.Dict("en_US")
          return dictionary.check(user_val)
     else:
          return True

def lim():
     return 1

def selnum1():
     return (random.choice(stock_forbidden_letters))

def selnum2():
     return (random.choice(stock_forbidden_letters))

def selnum3():
     return (random.choice(stock_forbidden_letters))

def selnum4():
     return (random.choice(stock_forbidden_letters))

def selnum5():
     return (random.choice(stock_forbidden_letters))
     
def user_check(user_val):
     numlist=['1','2','3','4','5','6','7','8','9','0']
     alphalist=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
     alphalist2=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
     for i in range (len(user_val)):
          if (user_val[i] not in alphalist2) or (user_val[i] in alphalist) or (user_val[i] in numlist):
               return False
          
     else:
          return True
def user_forbidden(user_val,chosen_letter1,chosen_letter2,chosen_letter3,chosen_letter4,chosen_letter5):
     lno=0
     for i in range(6):
          if i==1:
               if chosen_letter1 in user_val:
                    lno+=1
          elif i==2:
               if chosen_letter2 in user_val:
                    lno+=1
          elif i==3:
               if chosen_letter3 in user_val:
                    lno+=1
          elif i==4:
               if chosen_letter4 in user_val:
                    lno+=1
          elif i==5:
               if chosen_letter5 in user_val:
                    lno+=1
     return"{}fl".format(lno)
