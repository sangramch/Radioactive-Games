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


from highlow_mod import *
playing=True
k=secret_select()
alpha=str()
number=()
while playing==True:
    no=raw_input("Enter your guess:  ")
    if no=='%reveal':
        print'CHEAT ACCEPTED\n{}'.format(k)
    elif num_check(no,k)==False:
        print"Try Again!!! You have made a mistake in entering the number."
    else:
        status=luck_check(no,k)
        if status=='win':
            print "YOU WIN!!!"
            playing=False
        elif status=='high':
            print "Sorry, the no you have entered is higher than the selected one."
        elif status=='low':
            print "Sorry, the no you have entered is lower than the selected one."
