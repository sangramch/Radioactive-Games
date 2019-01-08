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
from hangman_mod import *

selected=select_word()
star_list=[]
entered_list=[]
playing=True
hang=0
hangimg=[
    '''
 +---+
 |   |
     |
     |
     |
     |
 =========
''',
    '''
 +---+
 |   |
 O   |
     |
     |
     |
 =========
''',
    '''
 +---+
 |   |
 O   |
 |   |
     |
     |
 =========
''',
    '''
 +---+
 |   |
 O   |
/|   |
     |
     |
 =========
''',
    '''
 +---+
 |   |
 O   |
/|\  |
     |
     |
 =========
''',
    '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
 =========
''',
    '''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
 =========
''',
    '''
 +---+
 |   |
 |   |
 O   |
/|\  |
/ \  |
     |
 =========
'''
    ]

for i in range(len(selected)):
    star_list.append('*')
while playing==True:
    if '*' in star_list:
        user_enter=raw_input("\nPlease Enter a Single Character:  ")
        if user_enter=='%reveal':
            print 'CHEAT ACCEPTED'
            print selected
        elif already(user_enter,entered_list)==False:
            entered_list.append(user_enter)
            if check(user_enter)==True:
                if user_enter in selected:
                    for i in range(len(selected)):
                        if user_enter == selected[i]:
                            star_list[i]=user_enter
                    print"Congrats!!! Your character is present.."
                    for j in range(len(star_list)):
                        print star_list[j],
                else:
                    if hang<=6:
                        hang+=1
                        print "\nDamn!!! You are part hanged!!"
                        print "Chances Remaining: {}".format(6-hang)
                        print hangimg[hang-1]
                        for j in range(len(star_list)):
                            print star_list[j],
                    else:
                        print "\nShit!!! You are fully hanged!!"
                        print hangimg[7]
                        playing=False
            else:
                print"\nTry Again"
        else:
            print "\nYou have already entered the letter. Try Again:"

    else:
        print "\nYou Win!!!"
        playing=False
