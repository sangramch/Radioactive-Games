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

def secret_select():
     import random
     k=str(random.randint(1,99))
     return k

def num_check(no,k):
     errorlist=0
     for100=False
     numlist=['1','2','3','4','5','6','7','8','9','0']
     for i in range(len(no)):
          if (no[i] not in numlist):
               errorlist+=1
               for100=True
     if for100==False:
          if(int(no)>99) or (int(no)<1):
               errorlist+=1
     if (errorlist>0):
          return False
     else:
          return True
     

def luck_check(no,k):
     if no==k:
          return 'win'
     elif no>k:
          return 'high'
     elif no<k:
          return 'low'
