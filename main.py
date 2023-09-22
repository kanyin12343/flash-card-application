from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
choice = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient = "records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global choice, flip_timer
    window.after_cancel(flip_timer)
    choice = random.choice(to_learn)
    canvas.itemconfig(language, text="French", fill = "black")
    canvas.itemconfig(french, text=choice["French"], fill = "black")
    canvas.itemconfig(front_canvas, image=logo_ing)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(language, text="English", fill = "white")
    canvas.itemconfig(french, text=choice["English"], fill = "white")
    canvas.itemconfig(front_canvas, image = back_card)


def is_known():
    to_learn.remove(choice)

    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()





window = Tk()
window.minsize(width= 500, height= 300)
window.title("Flashy")
window.config(padx= 50 ,pady = 50, bg = BACKGROUND_COLOR, highlightthickness=0)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width = 800, height = 526, bg = BACKGROUND_COLOR, highlightthickness=0)
logo_ing = PhotoImage(file = "images/card_front.png")
back_card = PhotoImage(file= "images/card_back.png")
front_canvas = canvas.create_image(400,263, image = logo_ing)
language = canvas.create_text(400, 150, text="word", fill ="Black", font=("Ariel", 40, "italic"))
french = canvas.create_text(400, 263, text="text", fill ="Black", font=("Ariel", 40, "bold"))
canvas.grid(column= 0, row= 0, columnspan= 2)

my_image = PhotoImage(file = "images/wrong.png")
wrong_button = Button(image= my_image, highlightthickness= 0, command= next_card)
wrong_button.grid(column= 0 ,row = 1)


right_image = PhotoImage(file = "images/right.png")
right_button = Button(image= right_image, highlightthickness=0, command=is_known)
right_button.grid(column= 1,row = 1)

next_card()




window.mainloop()
