import time
import threading
import random
import sys

# Start

print("Hi, in this game You can check Your typing speed!.")
time.sleep(0.3)
print("1. Easy")
time.sleep(0.2)
print("2. Normal")
time.sleep(0.1)
print("3. Hard")
time.sleep(0.1)
print("4. Impossible!")
time.sleep(0.3)
lvl = input("Choose lvl: ")
print("Ok! Loading level " + str(lvl))
print("Type 'start' to start the game NOW!")
str_inp = input()
while str_inp != "start":
    str_inp = input(
        "Don't worry! It won't hurt to try ;) Type 'start' and check your speed:")
if str_inp == "start":
    t = 3  # countdown time
    print('PREPARE! Your game will start in 5 sec...')
    while t > 0:
        print(t, end='...')
        time.sleep(1)
        t -= 1
    print('Go!')


# Print random words
f = open("base.txt")
base = f.read()
t = base.split(" ")
if lvl == "1":
    task = random.sample(t, 5)
elif lvl == "2":
    task = random.sample(t, 15)
elif lvl == "3":
    task = random.sample(t, 30)
elif lvl == "4":
    task = random.sample(t, 55)
task_to_compare = ' '.join(task).lower()
print(task_to_compare)


# Compare result to task + time counting
start = time.time()
result = str(input())
stop = time.time()
timeSpent = round(stop - start, 2)

if result == task_to_compare:
    print("Congrats! Your time is: " + str(timeSpent) + " sec !")
else:
    print("Ups... Something is messed up... Practice and come back")
