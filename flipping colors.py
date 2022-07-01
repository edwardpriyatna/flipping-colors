import turtle
import random

screen = turtle.Screen()
screen.setup(width = 500, height = 500)
wn = turtle.Screen()
wn.tracer(0)

picked = None

def create_board(): #function to create baord
    ori_square = turtle.Turtle()  # creating original square
    ori_square.penup()
    ori_square.color("white", "white")
    ori_square.shape("square")
    ori_square.shapesize(3, outline=3)
    ori_square.pendown()

    global board
    board = []
    global color
    color = ["red", "green", "blue", "orange", "purple"]
    x = 125
    y = 225

    for col in range(5):  # adding numbers to board list the numbers determine the color of the square
        for row in range(5):
            board.append(random.randint(0, 4))
    global tiles
    tiles = [] #a list containing square objects
    for a in range(5):  # creating 5 by 5 board
        y = y - 65
        for b in range(5):
            square = turtle.Turtle()
            square.hideturtle()
            square = ori_square.clone()  # cloning original square
            square.penup()
            square.goto((-1 * x) + b * 65, y)
            square.pendown()
            square.fillcolor(color[board[a * 5 + b]])
            tiles.append(square) #appending square object
    return board

def flipRecursive(row, col, to, flipped): #function to flip the list board
    global board
    if to == flipped:
        return
    if row < 0  or row >= 5:
        return 
    if col < 0 or col >= 5:
        return
    if board[row * 5 + col] != flipped:
        return 
    
    board[row * 5 + col] = to
    
    flipRecursive(row - 1, col, to, flipped)
    flipRecursive(row + 1, col, to, flipped)
    flipRecursive(row, col - 1, to, flipped)
    flipRecursive(row, col + 1, to, flipped)
    
def flip(clr): #function to flip color of turtle screen
    global picked
    if picked == None:
        return 
    row, col = divmod(picked, 5) #return a tuple containing row index and collumn index
    flipRecursive(row, col, clr, board[picked])
    
    for i in range(len(tiles)):
        tiles[i].color("white", color[board[i]]) #to replace tile with new color
    picked = None
    wn.update()

def select_tile(idx): #make chosen tile in board black
    global tiles
    global picked
    tiles[idx].color("black", tiles[idx].color()[1])#change color of that tile to black border but with the same color
    if picked != None and picked != idx:
        tiles[picked].color("white", tiles[picked].color()[1])#change border to white if you switch picked tiles
    picked = idx
    wn.update()

def screenClick_board(x, y):
    #to determine what square is clicked, and what is the index of the square in board list
    y_square=225 
    for j in range (5):
        y_square = y_square - 65
        x_square= -190
        for i in range (5):
            x_square = x_square + 65
            if -28.5 < x_square - x < 28.5 and -28.5 < y_square - y < 28.5:
                square_index = j * 5 + i
                return select_tile(square_index)
    #to determine what color button is clicked
    x_button=-125 + 30
    y_button=-150 - 30
    for k in range(5):
        if -30 < x_button - x < 30 and -30 < y_button - y < 30:
            flip(k)
        x_button = x_button + 60

def create_button(): #function to create the color button
    button = [0, 1, 2, 3, 4]
    button_square = turtle.Turtle()
    button_square.penup()
    button_square.goto(-125, -150)
    button_square.pendown()
    button_square.hideturtle()
    for b in range(5):
        button_square.fillcolor(color[b])
        button_square.begin_fill()
        for n in range(5):
            button_square.forward(60)
            if n != 4:
                button_square.right(90)
        button_square.end_fill()
    wn.update()
    return button

if __name__ == "__main__":
    create_board()
    create_button()
    wn.listen()
    wn.onclick(screenClick_board)
    wn.mainloop()

