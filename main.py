from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
choice = {}

try:
    # If a CSV file is available, load the words from it.
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    # Load the original data if the file isn't there.
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient = "records")
else:
    to_learn = data.to_dict(orient="records")

# Displays the following flashcard in the list.
def next_card():
    global choice, flip_timer
    window.after_cancel(flip_timer)
    # Pick a word at random from the list of vocabulary terms.
    choice = random.choice(to_learn)

    # Set the canvas to show the selected word in French.
    canvas.itemconfig(language, text="French", fill = "black")
    canvas.itemconfig(french, text=choice["French"], fill = "black")
    canvas.itemconfig(front_canvas, image=logo_ing)

    # Programme a timer to flip the card for you after three seconds.
    flip_timer = window.after(3000, func=flip_card)

# Flip the flashcard to reveal its English translation with this function.
def flip_card():
    # Set up the canvas to show the word's English translation.
    canvas.itemconfig(language, text="English", fill = "white")
    canvas.itemconfig(french, text=choice["English"], fill = "white")
    canvas.itemconfig(front_canvas, image = back_card)

# The ability to designate a term as known and take it from the list.
def is_known():
    # Cross off the word you're reading from your list of words to learn.
    to_learn.remove(choice)

    # Add the amended list to the CSV file.
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    # Show the following flashcard.
    next_card()


# Construct the primary application window.
window = Tk()
window.minsize(width= 500, height= 300)
window.title("Flashy")
window.config(padx= 50 ,pady = 50, bg = BACKGROUND_COLOR, highlightthickness=0)

# Set a timer for three seconds, then flip the card.
flip_timer = window.after(3000, func=flip_card)

# Make the canvas for the flashcard presentation.
canvas = Canvas(width = 800, height = 526, bg = BACKGROUND_COLOR, highlightthickness=0)
logo_ing = PhotoImage(file = "images/card_front.png")
back_card = PhotoImage(file= "images/card_back.png")
front_canvas = canvas.create_image(400,263, image = logo_ing)
language = canvas.create_text(400, 150, text="word", fill ="Black", font=("Ariel", 40, "italic"))
french = canvas.create_text(400, 263, text="text", fill ="Black", font=("Ariel", 40, "bold"))
canvas.grid(column= 0, row= 0, columnspan= 2)

# Make "wrong" and "right" answer buttons
my_image = PhotoImage(file = "images/wrong.png")
wrong_button = Button(image= my_image, highlightthickness= 0, command= next_card)
wrong_button.grid(column= 0 ,row = 1)


right_image = PhotoImage(file = "images/right.png")
right_button = Button(image= right_image, highlightthickness=0, command=is_known)
right_button.grid(column= 1,row = 1)

# Display the first flashcard to launch the app.

next_card()



# Start the primary event loop.
window.mainloop()
