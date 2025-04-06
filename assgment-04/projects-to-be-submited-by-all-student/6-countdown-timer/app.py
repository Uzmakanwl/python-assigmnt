import time

def countdown(t):
    while t > 0:
        minutes = t // 60
        seconds = t % 60
        display_time = f"{minutes:02d}:{seconds:02d}"
        print(display_time, end='\r')
        time.sleep(1)
        t = t - 1
    print('Timer completed!')
t = input("Enter the time in seconds: ")
countdown(int(t))