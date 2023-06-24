import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pandas.read_csv(R"D:\100 days of python\CAPSTONE PROJECTS\flash-card-project-start\data\words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv(R"D:\100 days of python\CAPSTONE PROJECTS\flash-card-project-start\data\French to English - Sheet1.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
current_card = {}

def nextcard():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French',fill = "black")
    canvas.itemconfig(card_word, text=current_card["French"],fill = "black")
    canvas.itemconfig(canvas_image,image = card_front)
    flip_timer = window.after(3000, func=flip_card)



def flip_card():
    canvas.itemconfig(card_title, text='English',fill = "white")
    canvas.itemconfig(card_word,text =current_card["English"],fill = "white" )
    canvas.itemconfig(canvas_image, image=back_image)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv(R"D:\100 days of python\CAPSTONE PROJECTS\flash-card-project-start\data\words_to_learn.csv",index=False)
    nextcard()



window = Tk()
window.title("French Quiz App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file=R"D:\100 days of python\CAPSTONE PROJECTS\flash-card-project-start\images\card_front.png")
back_image = PhotoImage(file=R"D:\100 days of python\CAPSTONE PROJECTS\flash-card-project-start\images\card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file=R"D:\100 days of python\CAPSTONE PROJECTS\flash-card-project-start\images\wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=nextcard)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file=R"D:\100 days of python\CAPSTONE PROJECTS\flash-card-project-start\images\right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

nextcard()


window.mainloop()
