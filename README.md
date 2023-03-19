<h1>Pong!</h1>

<h2>Description</h2>
This project is a Python implementation of the classic arcade game Pong, created using the Turtle library. The main objective of this project was to develop my skills in class methods and objects in Python, create a Graphical User Interface (GUI), and implement sound effects.

In this project, the turtle module is used for building the game. The window size is set to 800x600 pixels using the setup function of the Turtle screen. The game window is updated using the tracer function, which stops the window from updating and hence speeds up the game.

There are three Turtle objects created in the game, two for the paddles and one for the ball. The paddles' attributes, such as speed, shape, color, and size, are set using the Turtle object's methods. The ball's attributes, such as speed, shape, color, and initial position, are set using the Turtle object's attributes. The dx and dy attributes are used to set the direction of the ball's movement.

A pen object is also created using Turtle to display the scores of both players. The scores are updated after each point is scored by either player.

The game's controls are bound using the listen function of the Turtle screen, and the arrow keys and w and s keys are used to move the paddles. The movement of the paddles is implemented using the Turtle sety function.

The main game loop runs continuously until the game is exited. The game is updated using the update function of the Turtle screen. The ball's movement is implemented using the setx and sety functions of the Turtle ball object. The game has border checking to ensure that the ball does not move out of the game screen. Collision detection is implemented using if statements to determine if the ball has collided with the paddles or the walls of the game screen.

Finally, the game features sound effects, which are implemented using the winsound module. Different sound effects are played when the ball collides with the walls or the paddles.

In summary, this project showcases my skills in Python's class methods and objects, as well as my ability to create a GUI, implement sound effects, and bind keys to control objects' movement.
<br />
