import customtkinter as ctk
import numpy as np
from PIL import Image, ImageTk
import os
import Game

ROOT_DIR_BACKSLASH = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = ROOT_DIR_BACKSLASH.replace("\\", "/")
board = Game.Board()
posDict = board.posDict
square_centers = []


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
    renderBoard(window, frame, gameWindowWidth, gameWindowHeight)
    renderLabels(window, frame, whitePlayerName, blackPlayerName)


def renderBoard(window, frame, gameWindowWidth, gameWindowHeight):
    global square_centers
    canvas_height = gameWindowHeight * 0.85
    canvas_width = canvas_height
    canvas = ctk.CTkCanvas(master=frame, width=canvas_width, height=canvas_height)

    color = 'gray'

    squaresize = int(canvas_height / 8)

    # got inspiration for this loop below to render a checkerboard from stackoverflow
    # https://stackoverflow.com/questions/59356899/create-checkerboard-pattern-with-python-canvas
    # modified it, but its close enough to credit the author, "furas" (Dec 16, 2019 at 13:08)

    for y in range(8):
        for x in range(8):

            y1 = canvas_height - (y * squaresize)
            y2 = canvas_height - ((y + 1) * squaresize)
            x1 = x * squaresize + (squaresize / 32)
            x2 = x1 + squaresize

            centery = (y1 + y2) / 2
            centerx = (x1 + x2) / 2

            column = ["a", "b", "c", "d", "e", "f", "g", "h"]
            rows = ["1", "2", "3", "4", "5", "6", "7", "8"]

            squareName = column[x] + rows[y]

            doRender = True
            pieceToRender = posDict.get(squareName)
            if pieceToRender == "None":
                doRender = False

            print(squareName, ":", pieceToRender, doRender)

            canvas.create_rectangle((x1, y1, x2, y2), fill=color)

            if color == 'lightgray':
                color = 'gray'
            else:
                color = 'lightgray'

            if doRender:
                renderPiece(squareName, canvas, window, squaresize, color)

            # add center coordinates to the square_centers dictionary
            square_centers.append((squareName, (centerx, centery)))

        if color == 'lightgray':
            color = 'gray'
        else:
            color = 'lightgray'

    canvas.pack(expand=True)
    frame.pack(pady=50, padx=50, fill="both", expand=True)




def renderLabels(window, frame, whitePlayerName, blackPlayerName):
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    frame2 = ctk.CTkFrame(master=frame, width=window_width * (7 / 8), height=window_height * (7 / 8))
    turnlabeltext = whitePlayerName + " goes first"
    turnlabel = ctk.CTkLabel(master=frame2, text=turnlabeltext, font=('Roboto', 26), text_color='black')

    turnlabel.pack()
    frame2.pack(padx=200, pady=0, expand=True)


def imageRender(x, y, canvas, window, filename, squaresize): #This function got to an almost working state by me, and then was perfected by GPT-4
    path = ROOT_DIR + "/" + filename
    rawImage = Image.open(path)
    unconvertedImage = rawImage.resize((squaresize, squaresize))

    # Store the PhotoImage object as a canvas attribute
    canvas.image = ImageTk.PhotoImage(unconvertedImage)

    piece_id = canvas.create_image(x, y, image=canvas.image, anchor='nw')
    canvas.tag_bind(piece_id, "<Button-1>", lambda event: canvas.tag_raise(piece_id))
    canvas.tag_bind(piece_id, "<B1-Motion>", lambda event: canvas.moveto(piece_id, event.x, event.y))





def renderPiece(squareName, canvas, window, squaresize, color):
    piecename = posDict.get(squareName)
    filename = piecename + ".png"

    # Calculate the center of the square
    column = ["a", "b", "c", "d", "e", "f", "g", "h"]
    x = (column.index(squareName[0]) + 0.5) * squaresize
    y = (8 - int(squareName[1]) + 0.5) * squaresize

    # Check if the canvas already has a PhotoImage for the given filename
    if hasattr(canvas, filename):
        image = getattr(canvas, filename)
    else:
        # Otherwise, create a new PhotoImage and store it as an attribute of the canvas
        path = ROOT_DIR + "/" + filename
        rawImage = Image.open(path)
        unconvertedImage = rawImage.resize((squaresize, squaresize))
        image = ImageTk.PhotoImage(unconvertedImage)
        setattr(canvas, filename, image)

    # Create the image on the canvas using the existing or new PhotoImage object
    piece_id = canvas.create_image(x, y, image=image, anchor='center')
    canvas.tag_bind(piece_id, "<Button-1>", lambda event: on_piece_click(canvas, piece_id, event.x, event.y))
    canvas.tag_bind(piece_id, "<B1-Motion>", lambda event, p=piece_id: (on_piece_drag(canvas, p, event.x, event.y, squaresize), canvas.tag_raise(piece_id)))
    canvas.tag_bind(piece_id, "<ButtonRelease-1>",
                    lambda event, p=piece_id, x=x, y=y: on_piece_drop(event, squareName,canvas, p, x, y, squaresize))

def on_piece_click(canvas, piece_id, x, y):
    canvas.piece_x = x
    canvas.piece_y = y

def on_piece_drag(canvas, piece_id, x, y, squaresize):
    dx = x - canvas.piece_x
    dy = y - canvas.piece_y
    canvas.move(piece_id, dx, dy)
    canvas.piece_x = x
    canvas.piece_y = y







def on_piece_drop(event, squareName, canvas, piece_id, old_x, old_y, squaresize):
    # Check if the piece is over a square


    new_x = event.x
    new_y = event.y


    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()

    if new_x > 0 and new_x <= canvas_width and new_y > 0 and new_y <= canvas_height: #check to see if coords are within bounds of canvas (needs modifying)
        #Move to new location
        print("MOVE TO NEW LOC")

        closestSquareTouple = closestSquareToCoords(new_x,new_y)
        closestSquareName = closestSquareTouple[0]
        closestSquareCoords = closestSquareTouple[1]

        closest_square_x,closest_square_y = closestSquareCoords

        #move to new loc
        canvas.coords(piece_id,closest_square_x,closest_square_y)





    # If the piece is not over a square, move it back to its original square
    else:
        print("NOT OVER SQUARE")
        closestSquareName = squareName
        canvas.coords(piece_id, old_x,old_y)


    # If the piece is dropped onto a new square, print the move
    if closestSquareName is not None:
        print("DROPPED ONTO NEW SQUARE")
        old_square = squareName
        print(f"Moved from {old_square} to {closestSquareName}")




def closestSquareToCoords(x, y):
    centertouples = [item[1] for item in square_centers]
    print(centertouples)

    dist = []
    for touple in centertouples:
        cx,cy = touple
        dist.append(np.sqrt((x-cx)**2+(y-cy)**2))

    min_dist = min(dist)

    index = dist.index(min_dist)

    touple = square_centers[index]

    return touple

def moveToNewSquare(squareName,piece_id,canvas,closest_square):
    print("DROPPED ONTO NEW SQUARE")
    old_square = squareName

    print(f"Moved from {old_square} to {closest_square}")

def returnToOldSquare():
    print("old square")


initialGui()
print(square_centers)
closestSquareToCoords(321,950)