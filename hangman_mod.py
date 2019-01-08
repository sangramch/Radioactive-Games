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
def select_word():
    wfile=open("words.dat","r")
    rawwords=wfile.readlines()
    wfile.close()
    forword=[]
    for i in rawwords:
        forword.append(i[:-1])
    hfile=open("hints.dat","r")
    rawhints=hfile.readlines()
    hfile.close()
    hint=[]
    for i in rawhints:
        hint.append(i[:-1])
    rand=random.randint(0,len(forword))
    returner=(forword[rand],hint[rand])
    return returner

def check(word):
    alphalist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    if len(word)!=1 or word not in alphalist:
        if len(word)==4:
            return True
        else:
            return False
    else:
        return True
    
def already(word,entered_list):
    if word in entered_list:
        return True
    
    else:
        return False
