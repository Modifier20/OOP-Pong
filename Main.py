from tkinter import *
import random
import time

# --- BALL CLASS ---
class BALL:
    def __init__(self, canvas, color): # Init with the variables self, canvas, and color.
        self.canvas = canvas # Set the initial starting values.
        self.id=canvas.create_oval(30, 30, 50, 50, fill=color) # The starting default values for the ball.
        self.canvas.move(self.id, 0, 0) # This moves the oval to the specified location.

    def draw(self): # A draw method
        pass

tk = Tk() # Creates a tkinter object.
tk.title("My 21st Century Pong Game") # Gives the tkinter window a title.
tk.resizable(0, 0) # Makes the window resizable.
tk.wm_attributes("-topmost", 1) # The wm_attributes tells tkinter to place *this* window infront of all the other windows on the screen.
canvas=Canvas(tk, bg = 'black', width = '500', height = '400', bd = 0, highlightthickness = 0) # Creates a canvas and creates a few additional features, passing in the parameters for border and thickness.
canvas.pack() # Tells the canvas to size itself according to the width and height parameters just given.
tk.update() # Update tells tkinter to init itself for the animation in the game to come.

ball1 = BALL(canvas, 'green') # Creates a green ball object on the screen.

input('Press <Enter> to end the program')