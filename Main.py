from tkinter import *
import random
import time

# ---
#       You are starting at Step 5: Creating Bouncing Ball Movement.
# ---

# --- BALL CLASS ---
class BALL:
    def __init__(self, canvas, color): # Init with the variables self, canvas, and color.
        self.canvas = canvas # Set the initial starting values.
        self.id=canvas.create_oval(30, 30, 50, 50, fill=color) # The starting default values for the ball.
        # Note: x and y coordinates for top left corner and x and y coordinates for the bottom right corner, and finally the fill color for the oval.
        # 0 = Don't move horizontally (a + no. would indicate movement along the horizontal axis)
        # -1 = move 1 pixel up the screen (-y) - remeber the computer coordinate system.
        self.canvas.move(self.id, 100, 200) # This moves the oval to the specified location.

    def draw(self): # A draw method.
        self.canvas.move(self.id, 0, -1) # Pass it 3 parameters, the id of the oval, and 0 and -1
        # 0 = Don't move horizontally (a + no. would indicate movement along the horizontal axis)
        # -1 = move 1 pixel up the screen (-y) - remeber the computer coordinate system.

# --- MAIN GAME LOOP ---
def main():
    tk = Tk() # Creates a tkinter object.
    tk.title("My 21st Century Pong Game") # Gives the tkinter window a title.
    tk.resizable(0, 0) # Makes the window resizable.
    tk.wm_attributes("-topmost", 1) # The wm_attributes tells tkinter to place *this* window infront of all the other windows on the screen.
    canvas=Canvas(tk, bg = 'black', width = '500', height = '400', bd = 0, highlightthickness = 0) # Creates a canvas and creates a few additional features, passing in the parameters for border and thickness.
    canvas.pack() # Tells the canvas to size itself according to the width and height parameters just given.
    tk.update() # Update tells tkinter to init itself for the animation in the game to come.

    ball1 = BALL(canvas, 'green') # I am creating a green ball object.
    while 1:
        tk.update()
        ball1.draw() # Calls the balls draw method.
        time.sleep(0.01)

main()