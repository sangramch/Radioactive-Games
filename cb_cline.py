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

from cb_mod import *


playing=True
seloop=True
trial=0
nolist=[]

print "Enter the number beside the hardness level:\n\n1 -- Easy\n\n2 -- Medium\n\n3 -- Hard\n"
while seloop==True:
    sel=raw_input("What's your choice:  ")
    if sel=='1':
        k=easy()
        seloop=False
    elif sel=='2':
        k=medium()
        seloop=False
    elif sel=='3':
        k=hard()
        seloop=False
    elif sel=="":
        print "\n\nEnter Something...\n\n"
        seloop=True        
    else:
        print"\n\nWrong Choice..\n\n"
        seloop=True

while playing==True:
    chk=True
    
    while chk==True:
        no=raw_input("Enter the no:  ")
        if no=="reveal":#Cheatcode.. intended for debugging
            print "Cheat Accepted..."
            print k
            chk=True
        elif no=="":
            print "Input Something..."
            chk=True
        elif num_check(no,k)==False:
            print "Input is Unacceptable."
            chk=True
        else:
            trial+=1
            nolist.append(no)
            chk=False

    if bull(no,k)==4:
        print "You win..."
        print "You tried {} times...".format(trial)
        print "The nos you tried are:"
        for i in range(len(nolist)):
            if i==len(nolist)-1:
                print nolist[i],
            else:
                print nolist[i],",",
        playing=False
    else:
        print "You got {} Cows and {} Bulls...".format(cow(no,k),bull(no,k))
