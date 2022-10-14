from tkinter import *
import random
import time

# ---
#       You are starting at Step 5: Creating Bouncing Ball Movement.
# ---

# --- BALL CLASS ---
class BALL:
    def __init__(self, canvas, bat, color): # Init with the variables self, canvas, and color.
        self.canvas = canvas # Set the initial starting values.
        self.bat = bat # We assign the bat parameter to the object varibale bat.
        self.id=canvas.create_oval(30, 30, 50, 50, fill=color) # The starting default values for the ball.
        # Note: x and y coordinates for top left corner and x and y coordinates for the bottom right corner, and finally the fill color for the oval.
        # 0 = Don't move horizontally (a + no. would indicate movement along the horizontal axis)
        # -1 = move 1 pixel up the screen (-y) - remember the computer coordinate system.
        self.canvas.move(self.id, 100, 200) # This moves the oval to the specified location.

        starting_position = [-3, -2, -1, 1, 2, 3] # Creates a list with various starting positions.
        random.shuffle(starting_position) # Mixes up with a random shuffle function.
        self.x = starting_position[0] # Set's the x value to the first number in starting_position
        self.y = -3 # Increases the rate at which it moves along the y axis.
        self.canvas_height = self.canvas.winfo_height() # Set's the canvas height by calling the canvas function.
        self.canvas_width = self.canvas.winfo_width() # Determines the width of the canvas the l/r movement.
        self.hit_bottom = False

    def hit_bat(self, pos):
        bat_pos = self.canvas.coords(self.bat.id) # Retrieves the coordinates of the bat position.
        if pos[2] >= bat_pos[0] and pos[0] <= bat_pos[2]: # If the right side of the ball (that is the x right hand coordinate) is greater than the left side of the bat, and the left side of the ball is less that the right side of the bat ... move etc...
            if pos[3] >= bat_pos[1] and pos[3] <= bat_pos[3]: # If the bottom of the ball (pos[3]) is between the paddle's top (bat pos[1]) and bottom (pos[3])
                return True
        return False

    def draw(self): # A draw method.
        self.canvas.move(self.id, self.x, self.y) # Pass it 3 parameters, the id of the oval, and 0 and -1
        # 0 = Don't move horizontally (a + no. would indicate movement along the horizontal axis)
        # -1 = move 1 pixel up the screen (-y) - remember the computer coordinate system.

        pos = self.canvas.coords(self.id) # Creates a variable for position.
        # The above would return the x and y position of anything drawing on the canvas so long as you know the id.
        # In this case the oval's identifier (self.id) that gives us the coordinates.

        # --- DETECTS VERTICAL COLLISIONS ---
        if pos[1] <= 0: # If you hit the top of the screen, stop subtracting one and therefore stop moving up.
            self.y = 1
        if pos[3] >= self.canvas_height:
            self.y = -1 # Subtracts so makes the object move upwards again.

        # --- COLLISIONS WITH THE BAT ---
        if self.hit_bat(pos) >= self.canvas_height: # Checks to see if the ball has hit the bottom of the screen.
            self.hit_bottom = True

        # --- DETECTS HORIZONTAL COLLISIONS ---
        if pos[0] <= 0:
            self.x = 6
        if pos[2] >= self.canvas_width:
            self.x = -6

# --- PONGBAT CLASS ---
class PONGBAT():
    def __init__(self, canvas, color): # Initializes with the parameters self, canvas, color.
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color) # This creates the rectangle which will be the bat.
        self.canvas.move(self.id, 200, 300) # Initial 'movement' of the bat is declared here.

        self.x = 0 # Add's an x variable to the pong bat object.
        self.canvas_width = self.canvas.winfo_width() # Creates a varibale for the canvas width
        self.canvas.bind_all('K_a',self.left_turn) # Binds the pong bats movement to the left movement key.
        self.canvas.bind_all('K_d',self.right_turn) # Binds the pong bats movement to the right movement key.

    # --- PONG BAT's DRAW CLASS
    def draw(self): # The paddle's draw function
        self.canvas.move(self.id, self.x, 0) # Moves the bat in the direction of the x variable
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0: # If the left x coordinate ia less than or equal to 0, then we want it to stop.
            self.x = 0
        if pos[2] > self.canvas_width:
            self.x = 0

    def left_turn(self,evt):
        self.x = -10 # Change this variable to change the speed of the bat.
    def right_turn(self,evt):
        self.x = 10

# --- MAIN GAME LOOP ---
def main():
    tk = Tk() # Creates a tkinter object.
    tk.title("My 21st Century Pong Game") # Gives the tkinter window a title.
    tk.resizable(0, 0) # Makes the window resizable.
    tk.wm_attributes("-topmost", 1) # The wm_attributes tells tkinter to place *this* window infront of all the other windows on the screen.
    canvas=Canvas(tk, bg = 'black', width = '500', height = '400', bd = 0, highlightthickness = 0) # Creates a canvas and creates a few additional features, passing in the parameters for border and thickness.
    canvas.pack() # Tells the canvas to size itself according to the width and height parameters just given.
    tk.update() # Update tells tkinter to init itself for the animation in the game to come.

    bat1 = PONGBAT(canvas, 'red')  # Creates an instance of the pong bat.
    ball1 = BALL(canvas, bat1,'white') # I am creating a green ball object.

    while 1:
        if ball1.hit_bottom == False: # This creates the condition that the ball can't hit the bottom of the screen.
            tk.update()
            ball1.draw() # Calls the balls draw method.
            bat1.draw() # Calls the pong bats draw method.
        time.sleep(0.02)

main()