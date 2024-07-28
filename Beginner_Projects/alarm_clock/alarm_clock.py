import time
from playsound import playsound

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"
RESET = "\033[0m"


def alarm(seconds):
    try:
        print(CLEAR)
        time_left = seconds

        while time_left >= 0:
            min_left = time_left // 60
            sec_left = time_left % 60

            if sec_left < 10:
                color_code = '\033[31m' # Red
            else:
                color_code = '\033[92m' # Green
            print(f'{CLEAR_AND_RETURN} {color_code}{min_left:02d} : {sec_left:02d} {RESET}')
            time.sleep(1)
            time_left -= 1

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