# Wizard-cardgame-helper
A short python code, which calulates the number of tricks you are going to make using statistics. 
Note: The current version does not remark the previous cards.

The class 'cards' contains the calculations of the statistic. The explanation for the statistics can be found bellow.
The class 'Mainwindow' contains the Userinterface (using PyQt5).

How the probability is calculated:
- If the Trump color is none the probability for one card is:

    <img src="https://render.githubusercontent.com/render/math?math=P=\biggl(\product_{i=0}^{17-card}\frac{42-i-card}{59-i}\biggr)">
  
  Where card is the number on the individual card.
  
- If the Trump color is not none the probability is:
  
    <img src="https://render.githubusercontent.com/render/math?math=P=\biggl(\product_{i=0}^{17-card}\frac{42-i-card}{59-i} %2B 0.3 \biggr)">   If the card has the trump color
    <img src="https://render.githubusercontent.com/render/math?math=P=\biggl(\product_{i=0}^{17-card}\frac{29-i-card}{59-i} \biggr)">   If the card has not the trump color

  The 0.3 is added, because in rounds, where the number of total dealt card is high, it is likely to get a trick with a trump card even if the number is low.
  
 Finaly we have to add a with, n is the number of cards and x the number of players, linear increasing likelyhood to get a trick with a card, even if a bettercard is in the game.
 
   <img src="https://render.githubusercontent.com/render/math?math=P_{new}=P_{old} %2B m(n\cdot x) %2B b"> 
   
The parameters are currently set to a=0.023 and b=-0.2. These parameters can be adjusted individualy by the player, to costumize the probability to their playstyle.
   
  
