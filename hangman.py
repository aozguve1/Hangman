import tkinter as tk
from tkinter import messagebox
import random

guessed_letters = []
attempts = 6

window = tk.Tk()
window.title("Hangman Game")
window.geometry("600x800")



def get_a_word(file):
    with open(file_path, "r") as file:
        lines = file.readlines()
    index=random.randint(0,len(lines))
    return lines[index].strip()


file_path = "words.txt"
word_to_guess = get_a_word(file_path)

def start_game():
    play_button.pack_forget()
    reset_game()
    word_label.pack()
    score_label.pack()
    attempts_label.pack()
    guessed_letter_label.pack()
    letter_entry.pack()
    guess_button.pack()
    reset_button.pack(side=tk.BOTTOM)
    exit_button.pack(side=tk.BOTTOM) 
    canvas.pack()

def exit_game():
    window.destroy()

def check_win():
    for letter in word_to_guess:
        if letter not in guessed_letters:
            return False  
    return True  
    
def check_loss():
    return attempts == 0

def guess_letter():
    global attempts, score
    letter = letter_entry.get().lower()
    
    if letter.isalpha() and len(letter) == 1:
        if letter in guessed_letters:
            messagebox.showinfo("Hangman", f"You have already guessed '{letter}'")
            
        elif letter in word_to_guess:
            guessed_letters.append(letter)
            update_guessed_letters_display()
            update_word_display()
            if check_win():
                score+=1
                score_label.config(text=f"Score: {score}")
                messagebox.showinfo("Hangman", "Congratulations! You Win!")
                reset_game()
        else:
            guessed_letters.append(letter)
            attempts -= 1
            update_guessed_letters_display()
            update_attempts_display()
            draw_hangman()
            if check_loss():
                messagebox.showinfo("Hangman", "You lose! The word was: " + word_to_guess)
                reset_game()
        letter_entry.delete(0, tk.END)
    else:
        messagebox.showinfo("Hangman", "Please enter a single letter.")

def reset_game():
    global word_to_guess, guessed_letters, attempts
    word_to_guess = get_a_word(file_path)
    guessed_letters = [] 
    attempts = 6
    update_word_display()
    update_attempts_display()
    update_guessed_letters_display()
    draw_hangman()

def update_word_display():
    display_word = " ".join(letter if letter in guessed_letters else "_" for letter in word_to_guess)
    word_label.config(text=display_word)

def update_attempts_display():
    attempts_label.config(text=f"Attempts left: {attempts}")

def update_guessed_letters_display():
    guessed_letters_string = ' '.join(guessed_letters)
    guessed_letter_label.config(text=f"Guessed Letters: {guessed_letters_string}")


def draw_hangman():
    canvas.delete("hangman")
    if attempts < 6:
        canvas.create_oval(125, 75, 175, 125, width=2, tags="hangman")  
    if attempts < 5:
        canvas.create_line(150, 125, 150, 175, width=2, tags="hangman") 
    if attempts < 4:
        canvas.create_line(150, 150, 125, 125,width=2, tags="hangman")  
    if attempts < 3:
        canvas.create_line(150, 150, 175, 120, width=2, tags="hangman")  
    if attempts < 2:
        canvas.create_line(150, 175, 125, 200, width=2, tags="hangman") 
    if attempts < 1:
        canvas.create_line(150, 175, 175, 200, width=2, tags="hangman") 

score = 0
play_button = tk.Button(window, text="Play", command=start_game)
exit_button = tk.Button(window, text="Exit", command=exit_game)
word_label = tk.Label(window, text="", font=("Arial", 24))
attempts_label = tk.Label(window, text ="", font={"Arial",16})
score_label = tk.Label(window, text =f"Score: {score}", font=("Arial", 16))
guessed_letter_label = tk.Label(window, text =f"Guessed Letters: {guessed_letters}", font=("Arial", 16))
letter_entry = tk.Entry(window, text ="", font ={"Arial",16})
guess_button = tk.Button(window, text ="Guess", command =guess_letter)
reset_button = tk.Button(window, text ="Reset", command = reset_game)
canvas = tk.Canvas(window, width =300, height =300)
canvas.create_line(50,200,250,200,width = 5 )
canvas.create_line(200,200,200,50, width = 5 )
canvas.create_line(100,50,200,50, width = 5 )
canvas.create_line(150,50,150,70,width = 5 )
play_button.pack()
exit_button.pack()
update_word_display()
update_attempts_display()
draw_hangman()
window.mainloop()
