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


def lim():
    return 1

def easy():#List made for selection of random nos. But, personally, I like random nos.
    import random
    nolist=['1234','2345','3456','4567','5678','6789','7890','8901','9012','0123','1357','2468','3579','4680','5791','6802','7913','8024','9135','0246']
    k=random.choice(nolist)
    '''print "\n\nEASY\nI see you are an amateur.. Or just a noob..\n"'''
    return k

def medium():#Or if you like medium hardness
    import random
    nolist1=[]
    for l in range(1111,10000):
        if '0' not in str(l):
            nolist1.append(l)

    k=random.choice(nolist1)
    k=str(k)
    '''print "\n\nMEDIUM\nAh, you like to play on the safe side.. or it is just that you are afraid to play the hardy style..\n"'''
    return k

def hard():#Hardest one.. be aware
    import random
    k=random.randint(1000,9999)#So, here it is... Random nos.
    k=str(k)
    '''print "\n\nHARD\nSo, you are a pro.. or just plain oversmart.. We will see..\n"'''
    return k

def num_check(no,k):
    errorlist=0
    numlist=['1','2','3','4','5','6','7','8','9','0']
    for i in range(len(no)):
        if ((no[i] not in numlist) or (len(no)!=4)):
            errorlist+=1
    if (errorlist>0):
        return False
    else:
        return True
def cow(no,k):
    cow=0
    for i in range(4):
        if no[i] in k and no[i]!=k[i]:
            cow+=1
    return str(cow)

def bull(no,k):
    bull=0
    for i in range(4):
        if no[i]==k[i]:
            bull+=1
    return str(bull)

def win(no,k):
    if no==k:
        return True
    else:
        return False
