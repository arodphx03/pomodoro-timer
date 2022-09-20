import time

def timercount(t):
    while (t >= 0):
        minutes, seconds = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(minutes, seconds)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1
    print("Focus time is over!\n")

def breakcount(t):
    while (t >= 0):
        minutes, seconds = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(minutes, seconds)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1
    print("Break time is over!\n")

m = int(input("Enter desired focus minutes: "))
mins = m * 60
s = int(input("Enter desired focus seconds: "))
secs = s 
t = mins + secs

print("\n--- Focus time ---")
timercount(t)

m = int(input("Enter desired break minutes: "))
mins = m * 60
s = int(input("Enter desired break seconds: "))
secs = s 
t = mins + secs

print("\n--- Break Time ---")
breakcount(t)