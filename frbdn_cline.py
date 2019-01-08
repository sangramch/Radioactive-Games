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

import time
from frbdn_mod import *
print"Let me tell you a little something about Does It Contain Forbidden Letters."
time.sleep(1)
print"I will select five random letters as the forbidden letters."
time.sleep(1)
print"When you enter a word, the forbidden letters must not be present in your word"
time.sleep(1)
print"Thats it!!! Enjoy!!!"
time.sleep(1)

playing=True
unolist=[]
stock_forbidden_letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
chosen_letter1=(random.choice(stock_forbidden_letters))
chosen_letter2=(random.choice(stock_forbidden_letters))
chosen_letter3=(random.choice(stock_forbidden_letters))
chosen_letter4=(random.choice(stock_forbidden_letters))
chosen_letter5=(random.choice(stock_forbidden_letters))

while playing==True:
    user_no=raw_input("Enter the word you want to try:  ")
    unolist.append(user_no)

    if user_no=='reveal':
        print "CHEAT ACCEPTED"
        print chosen_letter1
        print chosen_letter2
        print chosen_letter3
        print chosen_letter4
        print chosen_letter5
        
    elif user_check(user_no)==False:
        print "Your Word has some Errors. The rules are,\n1 --- There must be no numbers in the word.\n2 --- There must be no UPPER CASE in the word."

    else:
        if user_forbidden(user_no,chosen_letter1,chosen_letter2,chosen_letter3,chosen_letter4,chosen_letter5)=="1fl":
            print "Your word has 1 forbidden letter in it."
        elif user_forbidden(user_no,chosen_letter1,chosen_letter2,chosen_letter3,chosen_letter4,chosen_letter5)=="2fl":
            print "Your word has 2 forbidden letters in it."
        elif user_forbidden(user_no,chosen_letter1,chosen_letter2,chosen_letter3,chosen_letter4,chosen_letter5)=="3fl":
            print "Your word has 3 forbidden letters in it."
        elif user_forbidden(user_no,chosen_letter1,chosen_letter2,chosen_letter3,chosen_letter4,chosen_letter5)=="4fl":
            print "Your word has 4 forbidden letters in it."
        elif user_forbidden(user_no,chosen_letter1,chosen_letter2,chosen_letter3,chosen_letter4,chosen_letter5)=="5fl":
            print "Your word has all 5 forbidden letters in it."
        elif user_forbidden(user_no,chosen_letter1,chosen_letter2,chosen_letter3,chosen_letter4,chosen_letter5)=="0fl":
            print "You have your word which contains none of the forbidden letters"
            print "The forbidden letters were {} and {}".format(chosen_letter1,chosen_letter2)
            print "The words you tried are:",
            for i in range(len(unolist)):
                print unolist[i],"  ",
            playing=False
