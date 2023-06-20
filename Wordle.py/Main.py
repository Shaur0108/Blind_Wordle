import pygame
import sys
import random
import time
from words import *


pygame.init()
pygame.display.set_caption("Blind Wordle")

Width = 650
Height = 900
Green = "#6aaa64"
Yellow = "#c9b458"
Grey = "#787c7e"
outline = "#d3d63a"
filled_outline = "#878a8c"
Guessed_letter_font = pygame.font.Font("Assets/FreeSansBold.otf", 50)
X_Spacing = 85
Y_Spacing = 12
Letter_size = 75
Guesses_count = 0
Guesses = [[]]*6
current_guess = []
current_guess_string = ""
current_letter_bg = 110
game_result = ""


Correct_word = random.choice(WORDS)

Screen = pygame.display.set_mode((Width, Height))
Background = pygame.image.load("Assets/start.jpeg")
Background_rect = Background.get_rect(center=(317,300))

Screen.fill("white")
Screen.blit(Background, Background_rect)
pygame.display.update()

class Letter:
    def __init__(self, text, bg_position):
        self.bg_color = "white"
        self.text_color = "black"
        self.bg_position = bg_position
        self.bg_x = bg_position[0]
        self.bg_y = bg_position[1]
        self.bg_rect = (bg_position[0], self.bg_y, Letter_size, Letter_size)
        self.text = text
        self.text_position = (self.bg_x+36, self.bg_position[1] + 34)
        self.text_surface = Guessed_letter_font.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center= self.text_position)
    
    def draw(self):
        pygame.draw.rect(Screen, self.bg_color,self.bg_rect) 
        if self.bg_color == "white":
            pygame.draw.rect(Screen, filled_outline,self.bg_rect, 3) 
            self.text_surface = Guessed_letter_font.render(self.text, True, self.text_color)
            Screen.blit(self.text_surface,self.text_rect)
            pygame.display.update()
            

    def delete(self):
        pygame.draw.rect(Screen, "white", self.bg_rect)
        pygame.draw.rect(Screen, filled_outline, self.bg_rect)
        pygame.display.update()
    
        

    
def check_guess(guess_to_check):
        global current_letter_bg, game_result, current_guess, current_guess_string, Guesses_count
        game_decided = False
        for i in range(5):
            lower_letter = guess_to_check[i].text.lower()
            if lower_letter in Correct_word:
                 if lower_letter == Correct_word[i]:
                    guess_to_check[i].bg_color = Green 
                    guess_to_check[i].text_color = "white"
                    if not game_decided:
                        game_result = "W"
                 else:
                        guess_to_check[i].bg_color = Yellow
                        guess_to_check[i].text_color = "white"
                        game_result = ""
                        game_decided = True
            else:
                guess_to_check[i].bg_color = Grey 
                guess_to_check[i].text_color = "white"
                game_result = ""
                game_decided = True
                guess_to_check[i].draw()
                pygame.display.update()
        Guesses_count += 1
        current_guess = []
        current_guess_string = ""  
        current_letter_bg = 110
        
        if Guesses_count == 6 and game_result == "":
            game_result = "L"
            
                   
        
        

def play_again():
    pygame.draw.rect(Screen, "white", (10, 600, 1000, 600))
    play_again_font = pygame.font.Font("assets/FreeSansBold.otf", 40)
    play_again_text = play_again_font.render("PLAY AGAIN!", True, "black")     
    play_again_rect = play_again_text.get_rect(center=(Width/2, 700))
    word_was_text = play_again_font.render(f"The word was {Correct_word}!", True, "black")
    word_was_rect = word_was_text.get_rect(center=(Width/2, 650))
    Screen.blit(word_was_text, word_was_rect)
    Screen.blit(play_again_text, play_again_rect)
    pygame.display.update()
    time.sleep(5)
    pygame.quit()
    
def reset():
   

    Screen.fill("white")
    Screen.blit(Background, Background_rect)
    guesses_count = 0
    #CORRECT_WORD = 
    guesses = [[]] * 6
    current_guess = []
    current_guess_string = ""
    game_result = ""
    pygame.display.update()
    
def create_letter():
    global current_guess_string, current_letter_bg
    current_guess_string += Key_pressed
    new_letter = Letter(Key_pressed, (current_letter_bg, Guesses_count*100+Y_Spacing))
    current_letter_bg += X_Spacing
    Guesses[Guesses_count].append(new_letter)
    current_guess.append(new_letter)
    for Guess in Guesses:
        for letters in Guess:
            letters.draw()
    
def delete_letter():
    global current_guess_string, current_letter_bg
    Guesses[Guesses_count][-1].delete()
    Guesses[Guesses_count].pop()
    current_guess_string = current_guess_string[0:-1] 
    current_guess.pop()
    current_letter_bg -= X_Spacing
    
    
        
    

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_RETURN:
                if game_result != "":
                    play_again()
                else:
                    if len(current_guess_string)==5 and current_guess_string.lower() in WORDS:
                        check_guess(current_guess)
            elif events.key == pygame.K_BACKSPACE: 
                if len(current_guess_string) > 0:
                    delete_letter()
            else:
                Key_pressed = events.unicode.upper()
                if Key_pressed in "QWERTYUIOPASDFGHJKLZXCVBNM" and Key_pressed != "":
                    if len(current_guess_string) < 5:
                     create_letter()
                  
                        
                          
            
            