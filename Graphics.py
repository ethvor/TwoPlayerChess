import customtkinter as ctk
import numpy as np
from PIL import Image, ImageTk


def center_window(width, height, window):
    # get screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))


def initialGui():
    def nextPage():
        p1name = player1name.get()
        p2name = player2name.get()
        frame.destroy()
        pageTwoGui(p1name, p2name, window)

    window = ctk.CTk()

    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")

    frame = ctk.CTkFrame(master=window)
    frame.pack(pady=50, padx=20, fill="both", expand=True)
    title = ctk.CTkLabel(master=frame, text="Two Player Chess", font=("Roboto", 26), text_color="lightblue")
    title.pack(pady=15, padx=10)

    subtitle = ctk.CTkLabel(master=frame, text="by Ethan Voraritskul", font=("Roboto", 14), text_color="white")
    subtitle.pack(pady=10, padx=10)

    player1name = ctk.CTkEntry(master=frame, placeholder_text="Player 1 Name")
    player1name.pack(pady=20, padx=10)

    player2name = ctk.CTkEntry(master=frame, placeholder_text="Player 2 Name")
    player2name.pack(pady=15, padx=10)

    continueButton = ctk.CTkButton(master=frame, text="Continue", command=nextPage)
    continueButton.pack(pady=15, padx=10)

    center_window(400, 600, window)
    window.mainloop()


def pageTwoGui(p1name, p2name, window):
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("green")

    frame = ctk.CTkFrame(master=window)
    if p1name == "" and p2name == "":
        startGame("", "", window, frame)
        return

    frame.pack(pady=50, padx=20, fill="both", expand=True)

    label = ctk.CTkLabel(master=frame, text="Who will go first?", font=("Roboto", 24))
    label.pack(pady=15, padx=10)

    player1button = ctk.CTkButton(master=frame, text=str(p1name), command=lambda: startGame(p1name, p2name, window, frame))
    player1button.pack(pady=15, padx=10)

    player2button = ctk.CTkButton(master=frame, text=str(p2name), command=lambda: startGame(p2name, p1name, window, frame))
    player2button.pack(pady=15, padx=10)

    randomButton = ctk.CTkButton(master=frame, text="Random", command=lambda: coinflip(p1name, p2name, window, frame),
                                 fg_color="darkgray", hover_color="lightgray", text_color="black")
    randomButton.pack(pady=15, padx=10)


def coinflip(player1_name, player2_name, window, frame):
    winner = np.random.randint(low=1, high=3)
    if winner == 1:
        startGame(player1_name, player2_name, window, frame)
    if winner == 2:
        startGame(player2_name, player1_name, window, frame)


def startGame(whitePlayerName, blackPlayerName, window, frame):
    frame.destroy()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    center_window(screen_width - (screen_width / 6), screen_height - (screen_height / 6), window)
    gameGui(whitePlayerName, blackPlayerName, window)


def gameGui(window, whitePlayerName="Player 1", blackPlayerName="Player 2"):
    frame = ctk.CTkFrame(master=window)
    frame.pack(pady=50, padx=20, fill="both", expand=True)

initialGui()

