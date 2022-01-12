from tkinter import *
import math

FONT_NAME = "Montserrat"
PARAGRAPH = "Studying is the main source of knowledge. Books are indeed never failing friends of man. For a mature " \
            "mind, reading is the greatest source of pleasure and solace to distressed minds. The study of good books "\
            "ennobles us and broadens our outlook. Therefore, the habit of reading should be cultivated. A student " \
            "should never confine himself to his schoolbooks only. He should not miss the pleasure locked in the " \
            "classics, poetry, drama, history, philosophy etc. We can derive benefit from other’s experiences with " \
            "the help of books. The various sufferings, endurance and joy described in books enable us to have a " \
            "closer look at human life. They also inspire us to face the hardships of life courageously. Nowadays " \
            "there are innumerable books and time is scarce. So we should read only the best and the greatest among " \
            "them. With the help of books we shall be able to make our thinking mature and our life more meaningful " \
            "and worthwhile. "


# ---------------------------- INITIATE TIMER ------------------------------- #

def start_timer():
    user_input.grid(column=2, row=0, rowspan=2)
    canvas.grid(column=0, row=0)
    test_label.grid_forget()
    paragraph.grid(column=0, row=1, columnspan=2)
    count_down(60)
    reset_button.grid(column=1, row=0)
    start_button.grid_forget()


# ---------------------------- COUNTING WORDS ------------------------------- #

def count_words():
    # calculate words per minute
    words = user_input.get("1.0", "end-1c")
    words_per_minute = len(words) // 5
    test_label.config(text=f"Congratulations! Your Typing Speed is:\n"
                           f"{words_per_minute} Words per Minute")
    # update display
    test_label.grid(column=0, row=0, columnspan=3)
    reset_button.grid(column=1, row=1)
    canvas.grid_forget()
    paragraph.grid_forget()
    user_input.grid_forget()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    if count == 0:
        count_words()


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    test_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    user_input.grid_forget()
    paragraph.grid_forget()
    canvas.grid_forget()
    test_label.config(text="Welcome to the Typing Test! "
                           "\n\n You will have 60 seconds to type as much of the paragraph as possible."
                           "\n\n Press Start to Begin.",
                      font=(FONT_NAME, 20))
    test_label.grid(column=0, row=0, columnspan=3, padx=50, pady=10)
    start_button.grid(column=1, row=1)
    reset_button.grid_forget()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Welcome to the Typing Test")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

user_input = Text(wrap="word", height=25, highlightbackground="#3a3838", highlightcolor="white",
                  font=(FONT_NAME, 12, "normal"))

canvas = Canvas(width=100, height=100, highlightthickness=0)
timer_text = canvas.create_text(50, 50, text="00:00", font=(FONT_NAME, 35, "bold"))

test_label = Label(
    text="Welcome to the Typing Test!\n\n You will have 60 seconds to type as much of the paragraph as possible.\n "
         "\nPress Start to Begin.",
    font=(FONT_NAME, 20),
    wraplength=400)
test_label.grid(column=0, row=0, columnspan=3, padx=50, pady=10)

start_button = Button(text="Start", font=(FONT_NAME, 15), padx=15, pady=15, highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=1)

reset_button = Button(text="Reset", font=(FONT_NAME, 15), padx=15, pady=15, highlightthickness=0, command=reset_timer)

paragraph = Label(text=PARAGRAPH, wraplength=450, justify="left", font=(FONT_NAME, 15, "normal"))

window.mainloop()
