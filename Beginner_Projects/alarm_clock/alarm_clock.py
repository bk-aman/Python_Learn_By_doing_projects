import time
import pygame

pygame.init()

# Costants for pygame
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
BACKGROUND_COLOR = (30,30,30)     # dark grey     
TEXT_COLOR = (255,255,255)        # White color text
BAR_COLOR = (0,255,0)             # red
BAR_BG_COLOR = (255,0,0)          # green
FONT_SIZE = 32                    # size of font on screen


#Path for sound file
FILE_PATH = "G:\code\Tim_tuts\Beginner_Projects\\alarm_clock\\alarm.mp3"
# FILE_PATH = os.path.join('G:\\', 'code', 'Tims_tuts', 'Beginner_Projects', 'alarm_clock', 'alarm.mp3')

#Set up display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Alarm Clock with stop button')

#Set up font
font = pygame.font.SysFont(None, FONT_SIZE)
pygame.mixer.init()

#Set up button properties
button_react = pygame.Rect(150, 200, 100, 50)   #Position and size of button



def play_sound(file_path):
    try:
        sound = pygame.mixer.Sound(file_path)
        sound.play()
        pygame.time.wait(int(sound.get_length() * 1000))

    except pygame.error as e:
        print(f"Error playing sound: {e}")


def draw_timer(seconds_left):
    minutes = seconds_left // 60
    second = seconds_left % 60
    timer_text = f"{minutes:02d}:{second:02d}"
    text = font.render(timer_text, True, TEXT_COLOR)
    screen.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, WINDOW_HEIGHT // 2 - text.get_height() // 2))


def draw_progress_bar(total_seconds, elapsed_seconds):
    bar_length = 300
    bar_height = 30
    filled_length = int(bar_length * elapsed_seconds // total_seconds)
    
    pygame.draw.rect(screen, BAR_BG_COLOR, ((WINDOW_WIDTH - bar_length) // 2, (WINDOW_HEIGHT // 2) + 50, bar_length, bar_height))
    pygame.draw.rect(screen, BAR_COLOR, ((WINDOW_WIDTH - bar_length) // 2, (WINDOW_HEIGHT // 2) + 50, filled_length, bar_height))

def alarm(total_seconds):
    start_time = time.time()
    elapsed_time = 0
    running = True

    while running and elapsed_time < total_seconds:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        elapsed_time = time.time() - start_time
        seconds_left = total_seconds - int(elapsed_time)

        screen.fill(BACKGROUND_COLOR)
        draw_timer(seconds_left)
        draw_progress_bar(total_seconds, elapsed_time)
        pygame.display.flip()

        time.sleep(1)
    
    if elapsed_time >= total_seconds:
        play_sound(FILE_PATH)
        print("Time's up!")

def get_input_time(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError('Please enter a non-negative number')
            return value
        except ValueError as e:
            print(e)

def main():
    """
    Main function to run the alarm clock program.
    """
    minute = get_input_time('How many minutes to wait: ')
    second = get_input_time('How many seconds to wait: ')

    total_seconds = minute * 60 + second
    alarm(total_seconds)

if __name__ == "__main__":
    main()
    pygame.quit()

