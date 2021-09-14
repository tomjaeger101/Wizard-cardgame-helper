# Wizard-cardgame-helper
A short python code, which calulates the number of tricks you are going to make using statistics. 
Note: The current version does not remark the previous cards.

The class 'cards' contains the calculations of the statistic. The explanation for the statistics can be found bellow.
The class 'Mainwindow' contains the Userinterface (using PyQt5).

How the probability is calculated:
- If the Trump color is none
  ```math
P = \frac{\sigma}{\sqrt{n}}
```

