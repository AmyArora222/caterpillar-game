import turtle as t
import random as rd

t.bgcolor('yellow')

caterpillar = t.Turtle()      #1
caterpillar.shape('square')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()

leaf = t.Turtle()            #2
leaf_shape = ((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed()

game_started = False      #to keep trache whether the game has started
text_turtle = False       #3
text_turtle = t.Turtle()
text_turtle.write('Press SPACE to start', align='center', font=('Arial', 18, 'bold'))
text_turtle.hideturtle()

score_turtle = t.Turtle()  #4
score_turtle.hideturtle()
score_turtle.speed(0)

#checks for the conditions for game over
def outside_window():
    left_wall = -t.window_width()/2
    right_Wall = t.window_width()/2
    top_wall = t.window_height()/2
    bottom_wall = -t.window_height()/2
    (x,y) = caterpillar.pos()   #retrieves the current pos of the caterpillar(returns a tuple)
    outside = x < left_wall or x > right_Wall or y > top_wall or y < bottom_wall  #checks if the x & y coordinates are outside the boundaries(if any true then outside is set to true:game over)
    return outside


#indicates end of game,displays "game over" & restart by pressing space key after seeing game over msg
def game_over():
    caterpillar.color('yellow')   #to mix up with the bg(game over)
    leaf.color('yellow')          #to mix up with the bg(game over)
    t.penup()           #no more drawing
    t.hideturtle()
    t.write('GAME OVER !', align='center', font=('Arial', 30, 'normal') )
    t.onkey(start_game,'space')   #specifies that when the 'space' key is pressed, the start_game function should be called


#clears the previous score, calculates the new position for displaying the score, moves the turtle to that position, and writes the current score at that location
def display_score(current_score):
    score_turtle.clear()  #common practice before updating the display with new content
    score_turtle.penup()
    x = (t.window_width()/2) - 70   #calculates the x-coordinate for the position where the score will be displayed
    y = (t.window_height()/2) - 70
    score_turtle.setpos(x,y)  #sets the position of score_turtle to the coordinates x & y
    score_turtle.write(str(current_score), align='right', font=('Arial', 40, 'bold'))

#places the leaf at random position & shows it
def place_leaf():
    leaf.hideturtle()
    leaf.setx(rd.randint(-200,200))#rd.randint generates a random integer within the specified range.setx sets the  x-coordinate 
    leaf.sety(rd.randint(-200,200))
    leaf.showturtle()  #After setting the new random position, the turtle cursor becomes visible again on the screen


#start_game function initializes or resets various game-related variables, displays the initial score
# shows the caterpillar on the screen, and places the first leaf for the caterpillar to eat. 
#It also includes logic to prevent the game from restarting if it is already in progress
def start_game():
    global game_started   #declared above(made global to modify it)
    if game_started:      #checks if the game_started variable is already True. If it is, the function returns without doing anything, preventing the game from restarting while it's already in progress
        return
    game_started = True   #If the game has not already started (game_started is False), this line sets game_started to True, indicating that the game has started
    
    score = 0
    text_turtle.clear()   #used to remove the msg("press space to start")

    caterpillar_speed = 2  #2 units per step
    caterpillar_length = 3
    caterpillar.shapesize(1,caterpillar_length,1)  #control the scaling in the x, y, and z directions
    caterpillar.showturtle()  #Makes the turtle cursor for the caterpillar visible on the screen
    display_score(score)      #displays initial score=0
    place_leaf()              #initial(first) placement of the leaf

    while True:
        caterpillar.forward(caterpillar_speed)  #caterpillar is moving
        if caterpillar.distance(leaf) < 20:     #if dist b/w caterpillar & leaf <20 units(means caterpillar has reached leaf & needs to perform the below steps now)
            place_leaf()                        #calls the func to place a new leaf on the screen
            caterpillar_length = caterpillar_length + 1  #inc the length by 1 when it eats a leaf
            caterpillar.shapesize(1,caterpillar_length,1) #Adjusts the size of the caterpillar's segments to reflect the updated length
            caterpillar_speed = caterpillar_speed + 1  #Increases the speed of the caterpillar by 1 when it eats a leaf.
            score = score + 10
            display_score(score)
        if outside_window():   #checks the conditions in the func & if returns true
            game_over()        #calls game over function 
            break

def move_up():
        caterpillar.setheading(90)

def move_down():
        caterpillar.setheading(270)

def move_left():
        caterpillar.setheading(180)

def move_right():
        caterpillar.setheading(0)
        
def restart_game():
 start_game()

t.onkey(start_game,'space')
t.onkey(restart_game,'Up')
t.onkey(move_up,'Up')
t.onkey(move_right,'Right')
t.onkey(move_down,'Down')
t.onkey(move_left,'Left')
t.listen()        #makes the turtle graphics window listen for key events
t.mainloop()      #starts the main event loop for the turtle graphics window, keeping it open and responsive to events such as key presses

#The onkey method is used to associate these functions with specific keys
#and listen and mainloop keep the window responsive to key events.