import customtkinter as ctk
import tkinter as tk
import numpy as np
from PIL import Image, ImageTk
import os

ROOT_DIR_BACKSLASH = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = ROOT_DIR_BACKSLASH.replace("\\", "/")


# taken from https://stackoverflow.com/questions/14910858/how-to-specify-where-a-tkinter-window-opens
# author: xxmbabanexx (Feb 16, 2013 at 16:47)
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

    player1button = ctk.CTkButton(master=frame, text=str(p1name),
                                  command=lambda: startGame(p1name, p2name, window, frame))
    player1button.pack(pady=15, padx=10)

    player2button = ctk.CTkButton(master=frame, text=str(p2name),
                                  command=lambda: startGame(p2name, p1name, window, frame))
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
    gameWindowWidth = screen_width - (screen_width / 6)
    gameWindowHeight = screen_height - (screen_height / 6)
    center_window(gameWindowWidth, gameWindowHeight, window)
    gameGui(window, whitePlayerName, blackPlayerName, gameWindowWidth, gameWindowHeight)


def gameGui(window, whitePlayerName, blackPlayerName, gameWindowWidth, gameWindowHeight):
    frame = ctk.CTkFrame(master=window, bg_color="darkgray", fg_color="darkgray")
    renderSquares(window, frame, gameWindowWidth, gameWindowHeight)


def renderSquares(window, frame, gameWindowWidth, gameWindowHeight):
    canvas_height = gameWindowHeight * 0.85
    canvas_width = canvas_height
    canvas = ctk.CTkCanvas(master=frame, width=canvas_width, height=canvas_height)

    color = 'gray'

    squaresize = canvas_height / 8

    # got inspiration for this loop below to render a checkerboard from stackoverflow
    # https://stackoverflow.com/questions/59356899/create-checkerboard-pattern-with-python-canvas
    # modified it slightly, but its close enough to credit the author, "furas" (Dec 16, 2019 at 13:08)

    for i in range(8):
        for j in range(8):
            corner1 = j * squaresize
            corner2 = i * squaresize
            corner3 = corner1 + squaresize
            corner4 = corner2 + squaresize
            canvas.create_rectangle((corner1, corner2, corner3, corner4), fill=color)
            if color == 'gray':
                color = 'lightgray'
            else:
                color = 'gray'

        if color == 'gray':
            color = 'lightgray'
        else:
            color = 'gray'

    canvas.pack(expand=True)
    frame.pack(pady=50, padx=50, fill="both", expand=True)
    renderPieces(canvas, window)


def imageRender(x, y, canvas, window, filename):
    path = "/Users\ofzel/PycharmProjects/Chess/" + filename
    print(path)
    unconvertedImage = Image.open(path)
    convertedImage = ImageTk.PhotoImage(unconvertedImage)
    ctkImage = ctk.CTkImage(unconvertedImage)
    canvas.create_image(x, y, image=convertedImage)
    label = ctk.CTkLabel(window, image=ctkImage)
    label.image = convertedImage


def renderPieces(canvas, window):
    renderPieceList = ["whiteBishop", "blackBishop", "whiteKing", "blackKing", "whiteKnight", "blackKnight",
                       "whiteQueen",
                       "blackQueen", "whiteRook", "blackRook", "whitePawn", "blackPawn"]

    for piece in renderPieceList:
        filename = piece + ".png"
        coordx = renderPieceList.index(piece) * 50 + 10
        # this just splays them out so i can see that they're all there YAY
        coordy = coordx
        imageRender(coordx, coordy, canvas, window, filename)


initialGui()
