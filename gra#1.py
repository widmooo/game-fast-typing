import time
import threading
import random

str_inp = input("Type 'start' to start the game:   ")

# start
while str_inp != "start":
    str_inp = input(
        "Don't worry! It won't hurt to try ;) Type 'start' and check your speed:   ")
if str_inp == "start":
    t = 5  # countdown time
    print('PREPARE! Your game will start in 5 sec...')
    while t > 0:
        print(t, end='...')
        time.sleep(1)
        t -= 1
    print('Go!')
# start

# print random words
base = ("General The software including Boot code and other embedded software documentation interfaces content fonts and any data that came with your Device Original iOS Software as may be updated replaced by feature enhancements software updates system restore software provided by Apple Software Updates whether in read only memory on any other media or in any other form the Original iOS Software and Software Updates are collectively referred to as are licensed not sold to by Apple for use only under the terms of this and its licensors retain ownership of the itself and reserve all rights not expressly granted to you at its discretion may make available future for your if any may not necessarily include all existing software features new features that releases for newer other models of terms of this will govern any Updates provided by that replace supplement product unless such Software is accompanied by a separate in which case terms of that will govern Permitted Uses and Restrictions Subject the terms and conditions of this you are granted a limited non exclusive use the a single except as permitted in Section below and unless as provided in a separate agreement between and this does allow exist on more than one at a time and you may not distribute or make the available over a network where it could be used by multiple devices at the same time This License does grant you any rights to use Apple proprietary interfaces and other intellectual property in the design development manufacture licensing distribution of third party devices and accessories or third party software applications for use with Some of those rights are available under separate licenses from more information on developing third party and accessories for please more information on developing software applications to the terms and conditions of this you are granted a limited license download that may be made available by for your model of to update or restore the on any such Device that own or control does not allow you to update or restore any that do not control or own and may not distribute make available over a network where they could be home used by multiple devices or multiple computers at the same time If you download an to your computer you may make one copy of the Updates stored on your computer in machinereadable form for backup purposes only provided that the backup copy must include all copyright other proprietary notices contained on the originalYou may and agree not to or enable others copy except as expressly permitted by this License decompile reverse engineer disassemble attempt to derive the source code of decrypt modify o create derivative works of or any services provided by any part except as and only extent any foregoing restriction is prohibited by applicable law by licensing terms governing use of components that may be included with storing content you are making a digital copy some jurisdictions it is unlawful to make digital copies without prior permission from rights holder The Software may be used to reproduce materials so long as such use is limited reproduction of materials materials in which you own materials you are authorized legally permitted to reproduce agree to use and Services as defined in Section in compliance with all applicable laws including local laws of the country or region in which you reside or in which you download or use and Services Use of and access to certain features of the and certain Services as defined in Section may require you to apply for a unique user name and password combination known as an In addition back knowledge that many features and Services of the transmit data and could impact charges your data plan and that are responsible for any such charges can control which applications are permitted to use cellular data and view an estimate of how much data such applications have consumed under Cellular Data Settings For more information please consult User Guide for your Transfer You may rent lease lend sell redistribute sublicense You may however make apermanent transfer of all of your rights to It feels like a very different team from a performance perspective and a operations perspective but we still have our work to do to find where we are in comparison to everyone else and until I get the data through from our strategist I do know We have had a good winter test he said It is not been perfect We found that we have plenty of problems that we are trying to iron out And I know how long it will take to iron them out but that is never a bad thing necessarily to discover through testing")
t = base.split(" ")
task = random.sample(t, 50)
print(' '.join(task))
# print random words

########## countdown and type
# ???????????????


def trigger():
    time.sleep(5400)
    gamer = input()


thread = threading.Thread(target=trigger)
thread.daemon = True
thread.start()
# ???????????????
########## countdown and type
