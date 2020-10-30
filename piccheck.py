from tkinter import *  # Importing Tkinter library for GUI.
import random  # Importing Random library to generate Random Values.
from PIL import Image, ImageTk  # Importing PILLOW.
from boott import *  # Importing Bot.
import winsound  # Importing WinSound to use music files.
import pyttsx3 as pp  # Importing Audio library.

# Initialising Speak library.
voic = pp.init()

voices = voic.getProperty('voices')
voic.setProperty('voice', voices[1].id)


# Bot's response in Voice.
def bol(word):
    voic.say(word)
    voic.runAndWait()


rand_indexes = []

index = 0  # variable to keep track of the index of rand_indexes list.

x1 = 0     # variable to get value placed in rand_indexes list.

score = 0

# Questions as per Given Images.
questions = [

        '1.png',
        '2.png',
        '3.png',
        '4.png',
        '5.png',
        '6.png',
        '7.png',
        '8.png',
        '9.png',
        '10.png',
        '11.png',
        '12.png',
        '13.png',
        '14.png',
        '15.png',
        '16.png',
        '17.png',
        '18.png',
        '19.png',
        '20.png',
        '21.png',
        '22.png',
        '23.png',
        '24.png',
        '25.png',
        '26.png',
        '27.png',
        '28.png',
        '29.png',
        '30.png',
        '31.png',
        '32.png',
        '33.png',
        '34.png',
        '35.png',
        '36.png',
        '37.png',
        '38.png',
        '39.png',
        '40.png',
        '41.png',
        '42.png',
        '43.png',
        '44.png',
        '45.png',
        '46.png',
        '47.png',
        '48.png',
        '49.png',
        '50.png',

 ]

# Answer List as per Given Questions.
answer_list = [

        'jin',
        'light yagami',
        'hinata',
        'zoro',
        'eren',
        'mikasa',
        'luffy',
        'levi',
        'kirito',
        'gon',
        'hisoka',
        'tanziro',
        'killua',
        'inosuke',
        'yuno gasai',
        'bam',
        'erza scarlet',
        'natsu dragneel',
        'mob',
        'deku',
        'bakugo',
        'saitama',
        'all might',
        'ichigo kurosaki',
        'ban',
        'genos',
        'meliodas',
        'kise',
        'kuroko',
        'soma yukihira',
        'zero',
        'ken kaneki',
        'shoto todoroki',
        'blank',
        'yahiko',
        'madara uchiha',
        'frieza',
        'l',
        'aizen',
        'kid buu',
        'cell',
        'obito',
        'itachi',
        'naruto',
        'goku',
        'vegeta',
        'gohan',
        'sasuke',
        'kageyama',
        'kakashi',

               ]


# ---------------------------------------------------------------------------------------
# INITIAL WINDOW..


root = Tk()
root.title("Anime Quiz")
root.geometry("1200x600")
root.resizable(0, 0)
winsound.PlaySound('Fairy_Tail', winsound.SND_ASYNC)  # To start Music on start of the game.
startmusic = PhotoImage(file='start_music.png')
stopmusic = PhotoImage(file='stop_music.png')
counter = 0


# Function to Start the Music.
def start_music():
    global counter
    if (counter % 2) == 1:

        start_music.config(image=stopmusic,
                           border=0,
                           bg="black",
                           relief=FLAT,
                           activebackground="black",)
        winsound.PlaySound('Fairy_Tail', winsound.SND_ASYNC)
    elif (counter % 2) == 0:

        start_music.config(image=startmusic,
                           border=0,
                           bg="black",
                           relief=FLAT,
                           activebackground="black",)
        winsound.PlaySound(None, winsound.SND_ASYNC)
    else:

        print("Error")
    counter = counter + 1


# generates the random sequence of numbers.
def gen():
    global rand_indexes
    while True:
        x = random.randint(0, 49)

        if len(rand_indexes) == 10:
            break
        elif x not in rand_indexes:
            rand_indexes.append(x)
        else:
            continue


# Checking answers and updating score.
def evaluation():

    global score, answer_list, x1

    a = str(e1.get())
    if answer_list[x1] == a.lower():
        score += 2
    elif answer_list[x1] != a.lower():
        score -= 1


# To show the final result.
def show_result():
    global score

    # cleaning the window to show result.
    remove_game_window()

    # placing the result on window.
    score_label.config(text='You Scored: ' + str(score) + ' of 20')
    score_label.place(y=260, x=380, height=70, width=500)
    restart_button.place(y=420, x=670, height=40, width=100)
    exit_button.place(y=420, x=500, height=40, width=100)


# Evaluation as per hint used
def hint_used():
    global score
    var = str(e.get())
    var = var.lower()
    if var.strip() == "hint":
        score -= 0.5
    return score


# Removing extras from window.
def remove_main_menu():
    btnStart.place(y=1200)
    label_text.place(y=1230)


# Undoing the remove_main_menu for restarting the game.
def place_main_menu():
    label_text.place(x=400, y=20)
    btnStart.place(x=430, y=450, height=60, width=400)


# Removing extras from window.
def remove_game_window():

    q_label.place(y=1300)
    q_tag.place(y=1320)
    e1.place(y=1340)
    next1.place(y=1360)
    f1.place(y=1380)
    f_bot.place(y=1400)


# placing the bot.
def place_game_window():

    q_label.place(x=0, y=0, height=450, width=740)
    q_tag.place(x=250, y=0)
    q_num.place(x=0, y=0)
    e1.place(x=50, y=500, width=550, height=40)
    next1.place(x=660, y=500, height=40, width=100)
    f_bot.place(x=775, y=10, height=530, width=410)


# Initializing the global data for use.
def nullifying():
    global rand_indexes, index, x1, score
    rand_indexes.clear()
    index, x1, score = 0, 0, 0
    e1.delete(0, END)
    m.config(state='normal')
    m.delete(1.0, END)
    m.config(state="disable")


# Function to Restart the Game.
def restart():

    global rand_indexes, index, x1, score
    nullifying()

    # Removing the items from the result window.
    score_label.place(y=1300, x=430, height=70, width=500)
    restart_button.place(y=1420, x=690, height=40, width=100)
    exit_button.place(y=1420, x=560, height=40, width=100)

    # Placing the main menu.
    place_main_menu()


# Move to next question and calling necessary functions.
def move_next():

    global rand_indexes, index, x1, score

    a = str(e1.get())

    if a.strip() != "" and index < 9:
        evaluation()
    elif a.strip() != "" and index == 9:
        evaluation()
        show_result()
        return 0
    elif a.strip() == "" and index == 9:
        show_result()
        return 0

    if index < 9:
        index += 1

    e1.delete(0, END)  # clearing the entry box

    if index < 10:
        x1 = rand_indexes[index]
    else:
        exit(102)

    if x1 < 50:
        img3_1 = ImageTk.PhotoImage(Image.open(questions[x1]))
        q_label.config(image=img3_1)
        q_num.config(text="Q.no: " + str(index + 1))
    else:
        exit(101)  # just for checking the index out of scope error.

    f1.mainloop()


# starting the game.
def start():
    global questions, x1, rand_indexes, index

    remove_main_menu()

    # -----------------------------------------------------------------
    gen()  # called to generate random sequence of questions

    # frame for question images.
    f1.place(x=20, y=10, height=450, width=740)

    if index == 0:          # for correct evaluation of first question.
        x1 = rand_indexes[0]
        q_num.config(text="Q.no: " + str(index + 1))

    img3 = ImageTk.PhotoImage(Image.open(questions[rand_indexes[0]]))

    q_label.config(image=img3)

    place_game_window()

    f1.mainloop()

# ----------------------------------------------------------------------------------
# Main menu Window defining.


# Opening an image for background.
img = Image.open('bg1.jpg')
img = ImageTk.PhotoImage(img)

f_ini = Frame(root)
f_ini.place(height="600", width="1200")

label_image = Label(f_ini, image=img)
label_image.place(x=0, y=0)

# Label containing the game title.
label_text = Label(
    f_ini,
    text="ANIME CHARACTER QUIZ",
    font=("Comic sans MS", 24, "bold"),
    bg="grey10", fg="white"
)
label_text.place(x=400, y=20)

# Button to start the Game.
btnStart = Button(
    f_ini,
    text="START",
    font="ariel 20",
    fg="white",
    bg="grey10",
    activeforeground="black",
    activebackground="white",
    command=start,
)
btnStart.place(x=430, y=450, height=60, width=400)
# ---------------------------------------------------------------------------------------------------------------
# _____________________________________
#                                                ---- HINT BOT code ----

# Frame to contain the Chat Bot.
f_bot = Frame(f_ini)


# Taking the bot's response and inserting in textbox.
def bot_respond():
    global x1
    var = str(e.get())
    var = var.lower()
    if var.strip() == "hint" or var.strip() == "hint please" or var.strip() == "give hint" or var.strip() == "hint me":
        response = bot.get_response("QCODE" + str(1 + x1))
        m.insert(INSERT, "BOT : " + str(response) + "\n")
        bol(response)
    else:
        response = bot.get_response(var)
        m.insert(INSERT, "BOT : " + str(response) + "\n")
        bol(response)


# Inserting the user's input and bot response in text box (m).
def ins():

    var = e.get()
    if var.strip() == "":
        return
    m.config(state="normal")
    m.insert(INSERT, "You : " + var + "\n")
    bot_respond()
    m.config(state="disable")
    hint_used()
    e.delete(0, len(var))


# To clear the Text box(m).
def clr():

    m.config(state="normal")
    m.delete(1.0, END)
    m.config(state="disable")


# Frame to contain textbox(m).
top_frame = Frame(f_bot, bg='black')
top_frame.place(height=350, width=410, x=0, y=0)

# Frame to contain entry box(e) and send button(b).
bot_frame = Frame(f_bot, bg='black')
bot_frame.place(height=185, width=410, x=0, y=350)

# Text box to show the chat.
m = Text(top_frame,
         fg="white",
         bg="grey10",
         bd=3)
m.place(height=340, width=392, x=3, y=3)

# scrollbar for top frame containing textbox(m).
scroll = Scrollbar(top_frame)
scroll.place(x=392, y=4, height=340)
m['yscrollcommand'] = scroll.set
scroll.config(command=m.yview)

# Credits
crb1 = Label(bot_frame, text="MADE BY : AKSHAT ", font=8, bg='black', fg='white',)
crb2 = Label(bot_frame, text="                     VIBHAV SINGH ", font=8, bg='black', fg='white',)
crb3 = Label(bot_frame, text="                     SIDDHANT SHARMA ", font=8, bg='black', fg='white',)
crb1.place(y=95, x=80)
crb2.place(y=120, x=80)
crb3.place(y=145, x=80)


# Entry box for user's input for Chat bot.
e = Entry(bot_frame,
          fg="white",
          bg="grey10",
          insertbackground="white",
          font="Ariel",
          bd=3)
e.place(height=70, width=274, x=5, y=10)


def aut(eve):  # Button to capture Event invoked by "Enter Key"
    b.invoke()


root.bind('<Return>', aut)  # Binding with "Enter Key" on Keyboard to Button "b"

# Button to send message to Bot
b = Button(bot_frame,
           text="SEND",
           font=20,
           bg="red2",
           activebackground="VioletRed1",
           fg="black",
           activeforeground="red",
           bd=5,
           command=ins)
b.place(height=80, width=128, x=279, y=5)


#                                        ----- HINT BOT Code END ----
# -----------------------------------------------------------------------------------------------------------------
# Contents to be placed in show_result window.
# --------------------------------------------------------------------------


# Label to show the Score
score_label = Label(f_ini,
                    text='You Scored: ' + str(score) + ' of 20',
                    font="Ariel 30",
                    fg="white",
                    bg='grey10')

# To Restart the Game
restart_button = Button(f_ini,
                        text="Play Again",
                        font="16",
                        fg="white",
                        bg="grey10",
                        activeforeground="black",
                        activebackground="white",
                        command=restart)

# To exit the Game
exit_button = Button(f_ini,
                     text="Quit",
                     font="16",
                     fg="white",
                     bg="grey10",
                     activeforeground="black",
                     activebackground="white",
                     command=quit)

# --------------------------------------------------------------------------
# Contents to be placed in start()
# --------------------------------------------------------------------------

# Frame to contain pictures
f1 = Frame(f_ini)

# Label to contain Images
q_label = Label(f1)

# Label for Questions
q_tag = Label(f1,
              text="-:: Identify  The  Character ::-",
              font='Ariel 12',
              bg='grey10',
              fg='white')

# To show the Question Numbers
q_num = Label(f1,
              text="Q.no: " + str(index + 1),
              font='Ariel 12',
              bg='grey10',
              fg='white')

# Entry Box for Answers to Questions
e1 = Entry(f_ini,
           font="Ariel 14",
           fg="white",
           bg="grey10",
           insertbackground="white")

# Button to move the Next Image
next1 = Button(f_ini,
               text="NEXT",
               font="Ariel 20",
               fg="white",
               bg="grey10",
               activeforeground="black",
               activebackground="white",
               command=move_next)

# Button to start the Music
start_music = Button(bot_frame,
                     image=stopmusic,
                     border=0,
                     bg='black',
                     command=start_music,
                     activebackground="black")
start_music.place(x=10, y=105)


root.mainloop()
