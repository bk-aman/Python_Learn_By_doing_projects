import time
from playsound import playsound

#ANSI escape character to control cursor and color
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"
MOVE_TO_SECOND_LINE = "\033[2;0H"
COLOR_BAR_PLACE = "\033[2;10H"
MOVE_TO_THIRD_LINE = "\033[3;0H"
RESET = "\033[0m"
GREEN = "\033[92m"
RED = "\033[31m"

def print_progress_bar(total_seconds, elapsed_seconds):
    bar_length = 30  
    filled_length = int(bar_length * elapsed_seconds // total_seconds)  
    bar = '█' * filled_length + '-' * (bar_length - filled_length)  
    percent = (elapsed_seconds / total_seconds) * 100  
    print(f"[{COLOR_BAR_PLACE}{bar}] {percent:.2f}%")  
    
def alarm(seconds):
    time_elapsed = 0
    try:
        print(CLEAR)
        print(f'{CLEAR_AND_RETURN}Starting the Countdown.....')

        while time_elapsed < seconds:
            time.sleep(1)
            time_elapsed += 1

            time_left = seconds - time_elapsed
            min_left = time_left // 60
            sec_left = time_left % 60

            color_code = GREEN if sec_left > 10 else RED

            print(f'{MOVE_TO_SECOND_LINE}{color_code}{min_left:02d} : {sec_left:02d} {RESET}')
            print_progress_bar(seconds, time_elapsed)
            
        print(f'{MOVE_TO_THIRD_LINE} Times up....')
        playsound('alarm.mp3')
       

    except KeyboardInterrupt:
        print('\n Alarm cancelled')

    finally:
        print(CLEAR_AND_RETURN)

def get_input_time(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError('Please enter a non-negetive number')
            return value
        
        except ValueError as e:
            print(e)

minute = get_input_time('How many minutes to wait: ')
second = get_input_time('How many seconds to wait: ')

tot_sec = minute*60 + second

alarm(tot_sec)