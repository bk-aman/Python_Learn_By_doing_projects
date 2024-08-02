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
BUTTON_COLOR = (0,0,128)          # green color for button
BUTTON_HOVER_COLOR = (128,128,0)    # Red color when button is hovered 

#Path for sound file
FILE_PATH = "G:\code\\tim_tuts\Beginner_Projects\\alarm_clock\\alarm.mp3"
# FILE_PATH = os.path.join('G:\\', 'code', 'py_tuts', 'Beginner_Projects', 'alarm_clock', 'alarm.mp3')

#Set up display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Alarm Clock with Stop button')

#Set up font
font = pygame.font.SysFont(None, FONT_SIZE)
sound = pygame.mixer.Sound(FILE_PATH)

#Set up button properties
button_rect = pygame.Rect(160, 250, 100, 30)   #Position and size of button
clock = pygame.time.Clock()

def play_sound(loop = -1):
    try:
        sound.play(loop)
        # pygame.time.wait(int(sound.get_length() * 1000))
        return sound

    except pygame.error as e:
        print(f"Error playing sound: {e}")

def draw_input_box(text_input,  message):
    input_box = pygame.Rect(50, 150, 300, 50)  # Position and size of input box
    pygame.draw.rect(screen, TEXT_COLOR, input_box, 2)  # Draw border

    # Render input text
    text = font.render(text_input, True, TEXT_COLOR)
    screen.blit(text, (input_box.x + 5, input_box.y + 10))

    # Display message on screen
    message_text = font.render(message, True, TEXT_COLOR)
    screen.blit(message_text, (WINDOW_WIDTH // 2 - message_text.get_width() // 2, 100))

def get_input_time():
    input_active = True
    text_input = ""
    
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Enter key to submit input
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:  # Backspace to delete last character
                    text_input = text_input[:-1]
                else:
                    text_input += event.unicode  # Add typed character to input

        try:
            float(text_input)
            message = 'Alarm will sound in mins :'
        
        except ValueError:
            message = 'Please, enter a valid number:'

        
        screen.fill(BACKGROUND_COLOR)
        draw_input_box(text_input, message)
        pygame.display.flip()
        clock.tick(30)

    try:
        total_seconds = float(text_input) * 60  # Assume input is in minutes
        return total_seconds
    except ValueError:
        return 0


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


def draw_button():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if button_rect.collidepoint(mouse_x, mouse_y):
        pygame.draw.rect(screen, BUTTON_HOVER_COLOR, button_rect)
    else:
        pygame.draw.rect(screen, BUTTON_COLOR, button_rect)

    text = font.render('Stop!', True, TEXT_COLOR)
    screen.blit(text, (button_rect.x + (button_rect.width - text.get_width()) // 2, button_rect.y + (button_rect.height - text.get_height()) // 2))


def alarm(total_seconds):
    start_time = time.time()
    elapsed_time = 0
    running = True
    sound_playing = False
    
    
    while running : #and elapsed_time < total_seconds:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos): # and sound_playing:
                    if sound_playing:
                        sound.stop()
                        sound_playing = False
                    running = False

        elapsed_time = time.time() - start_time
        seconds_left = max(total_seconds - int(elapsed_time),0)

        screen.fill(BACKGROUND_COLOR)
        draw_timer(seconds_left)
        draw_progress_bar(total_seconds, min(elapsed_time, total_seconds))
        draw_button()
        
        pygame.display.flip()
        
    
        if seconds_left == 0 and not sound_playing:
            play_sound()
            sound_playing = True
            print("Time's up!")
        
        clock.tick(30)

    return sound_playing

# def get_input_time(prompt):
#     while True:
#         try:
#             value = int(input(prompt))
#             if value < 0:
#                 raise ValueError('Please enter a non-negative number')
#             return value
#         except ValueError as e:
#             print(e)



def main():
    # minute = get_input_time('How many minutes to wait: ')
    # second = get_input_time('How many seconds to wait: ')
    # total_seconds = minute * 60 + second

    total_seconds = int(get_input_time())
    user_check = alarm(total_seconds)

    if user_check:
        print('Alarm was completed sucessfully...♥')
    else:
        print('Alarm was stoped by user☺')

if __name__ == "__main__":
    main()
    pygame.quit()

