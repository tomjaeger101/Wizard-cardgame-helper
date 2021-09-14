# Wizard-cardgame-helper
A short python code, which calulates the number of tricks you are going to make using statistics. 
Note: The current version does not remark the previous cards.

The class 'cards' contains the calculations of the statistic. The explanation for the statistics can be found bellow.
The class 'Mainwindow' contains the Userinterface (using PyQt5).

How the probability is calculated:
- If the Trump color is none

  <img src="https://render.githubusercontent.com/render/math?math=P=\biggl(\product_{i=0}^{17-n}\frac{42-i-n}{59-i}\biggr) %2B m(n\cdot x) %2B b">
  Where n is the number of cards and x is the number of players. m and b are two parameters to compensate the the increasing probability to get a trick with a 'lower' card, 
  if the of overall dealt cards is increasing.

