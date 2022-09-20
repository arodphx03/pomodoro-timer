import time, sys

pomodoroCount = 0

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

while True:
    while True:
        userInput = input("Enter 's' to start timer or 'q' to quit: ").lower()
        if userInput == 'q':
            print("You have exited the program.")
            sys.exit()
        if userInput == 's':
            break

    if userInput == 's':
        mins = int(input("Enter desired focus minutes: "))
        mins = mins * 60
        secs = int(input("Enter desired focus seconds: "))
        t = mins + secs

        print("\n--- Focus time ---")
        timercount(t)

        mins = int(input("Enter desired break minutes: "))
        mins = mins * 60
        secs = int(input("Enter desired break seconds: "))
        t = mins + secs

        print("\n--- Break Time ---")
        breakcount(t)
        pomodoroCount = pomodoroCount + 1

        print(f"Congratulations! You earned {pomodoroCount} pomodoro(s)!\n")