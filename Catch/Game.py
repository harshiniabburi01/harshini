from tkinter import *
import random
import time
def move_tom(direction):
    """
    This function is used for moving Tom around the screen
    :param direction: moving direction 1: up, 2: down, 3: left, 4: right
    """
    pass
def move_jerry():
    """
    This function is for moving Jerry automatically
    """
    pass
def move_puppies():
    """
    This function is for moving puppies around
    """
    pass
def check_win():
    """
    Check if Tom win
    """
    pass
def check_loose():
    """
    Check if Tom loose
    """
    pass
def key_action(event):
    """
    Processing keyboard activities
    :param event: the pressed keys
    """
    if event.keysym == "Up":
        move_tom(1)
    elif event.keysym == "Down":
        move_tom(2)
    elif event.keysym == "Left":
        move_tom(3)
    else:
        move_tom(4)
def start_game():
    """
    Initialize games
    """
    global tom, tom_x, tom_y, jerry, jerry_x, jerry_y, lst, cond_loose, cond_win
    print("The game start....")
    tom_x = random.randint(5, 595)
    tom_y = random.randint(5, 395)
    jerry_x = random.randint(5, 595)
    jerry_y = random.randint(5, 395)
    jerry_d = random.randint(1, 5)
    world.coords(jerry, jerry_x - 20, jerry_y - 20)
    world.coords(tom, tom_x - 20, tom_y - 20)
    for i in range(len(lst)):
        item = lst[i]
        p, x, y, d = item
        x = random.randint(5, 595)
        y = random.randint(5, 395)
        d = random.randint(1, 5)
        world.coords(p, x - 20, y - 20)
        lst[i] = [p, x, y, d]
        print("create = ", item)
    print("lst = ", lst)
    cond_win = False
    cond_loose = False
def end_game():
    """
    End the game
    """
    global end
    end = True
#####################################################################
# create a tkinter window
root = Tk()
root.bind('<Key>', key_action)
cond_win = False
cond_loose = False
end = False
tom_x = 0
tom_y = 0
jerry_x = 500
jerry_y = 300
jerry_d = 1
# create a drawing canvas
world = Canvas(width = 600, height = 400, bg = "white")
world.grid(row = 0, column = 0)
border = world.create_rectangle(2, 2, 600, 400, width = 3)
imgmap = PhotoImage(file = 'map.png')
world.create_image(0, 0, image = imgmap)
imgtom = PhotoImage(file = 'tom_40.png')
imgjerry = PhotoImage(file = 'jerry_40.png')
imgtyke = PhotoImage(file = 'tyke_40.png')
tom = world.create_image(tom_x - 20, tom_x - 20, image = imgtom)
jerry = world.create_image(jerry_x - 20, jerry_y - 20, image = imgjerry)
lst = []
for i in range(5):
    p = world.create_image(20, 20, image = imgtyke)
    lst.append([p, 0, 0, 1])
# create a button
l1 = Label(text = "Tom is chasing Jerry...")
l1.grid(row = 1, column = 0)
b1 = Button(text = "New Game", command = start_game)
b1.grid(row = 2, column = 0)
b2 = Button(text = "End Game", command = end_game)
b2.grid(row = 3, column = 0)
start_game()
# Animation loop
while end == False:
    if cond_win == False and cond_loose == False:
        move_jerry()
        move_puppies()
        check_win()
        check_loose()
        if cond_win:
            l1.configure(text = "Tom won...")
        if cond_loose:
            l1.configure(text = "Tom loose...")
    root.update_idletasks()
    root.update()
    time.sleep(0.1) 