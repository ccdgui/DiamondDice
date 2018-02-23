# DiamondDice
## Django web development learning project. 

#### Overview 
This is a learning project to get familiar with the building blocks of a web application in Django. 
DiamondDice is a personal twist on  a game called 'Dice 10,000' (also known as 'Ten Grand' or  'Dix-Mille'), a popular dice games in some countries. The project is to build a solo player web version.
This game is played with 5 dice: Dice can be rolled until one player reaches the score 10,000, hence the original name. The part about the Diamonds is not in the original rules. The player can roll the dice and accumulate points so long as there are coins remaining. Once the player has reached 10,000 points she gets one Gemstone. The game is played until the player has enough points to get a Diamond.  

#### Output 

View of the player interface: 

![diamonddice](https://user-images.githubusercontent.com/25650135/36594941-937b3adc-18a0-11e8-8160-bb25084a380e.PNG)


#### Technical Outline  
The Dice are model objects that can take the value 'unlocked', 'locked' and 'scored'. Dice that haven't been rolled yet are 'unlocked', dice that have been played in a previous round are 'locked' and dice that have scored in the current round are 'scored'. 

When the player clicks the 'save' and 'roll' buttons a GET request fetches new values from the game_action.py script. This script has multiple functions corresponding to the basic actions of the game which are:  
  * roll_dice(): called when 'roll' is clicked. A random value is generated for all Dice that are 'unlocked'. 
  * save_dice(): called when 'save' is clicked. Current Dice value is saved if sum of Dice value is more than 0. 
  * reset_dice(): all Dice status is set to 'unlock' and the Dice value is set to 0.
