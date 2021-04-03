Hi there, what a fun project to work on! 
I wanted to make some clarifications for a few parts of my code. 

Firstly, I recognize that both the begin_turn and computer_turn methods are long, and are pulling a lot of weight. For the game to work, the turns have to alternate, which, in the first draft of the program with separate methods that all checked inputs individually, was a spaghetti-code mess. It was a lot cleaner to use begin_turn as more of a main method. 

Secondly, the player turn and computer turn were really fun to code! Since the computer could only do hard-coded actions, and the player had more freedom, the way their play was coded had to be very different. 

Third, I tested the difficulty of the game, and found that the player won around half the time, which I think is ideal!
