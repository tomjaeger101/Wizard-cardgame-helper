from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QFrame
from PyQt5.QtGui import QIntValidator
import sys
from numpy import round
import os




class card:
    color = 'none'
    number = 0
    trump = 'none'

    def __init__(self, color, number, trump):

        if color == 'b':
            self.color = 'blue'
        elif color == 'g':
            self.color = 'green'
        elif color == 'r':
            self.color = 'red'
        elif color == 'y':
            self.color = 'yellow'
        else:
            self.color = 'none'

        if trump == 'b':
            self.trump = 'blue'
        elif trump == 'g':
            self.trump = 'green'
        elif trump == 'r':
            self.trump = 'red'
        elif trump == 'y':
            self.trump = 'yellow'
        else:
            self.trump = 'none'

        self.number = number
        self.m = 0.023
        self.b = -0.2

    def printcard(self):
        if self.color + ' ' + str(self.number) == 'none 0':
            self.cardinfo = 'Noob'
        elif self.color + ' ' + str(self.number) == 'none 14':
            self.cardinfo = 'Wizard'
        else:
            self.cardinfo = self.color + ' ' + str(self.number)

        return self.cardinfo

    def probability(self, Numberofcards, Numberofplayers):

        if self.trump == 'none':
            if self.number == 0:
                prob = 0
            elif self.number == 14:
                prob = 1
            else:
                prob = 1
                bettercards = 13 - self.number + 4
                for i in range(Numberofcards * Numberofplayers):
                    if i <= bettercards:
                        denominator = 59 - i
                        counter = denominator - bettercards
                        prob = prob * (counter / denominator)
                    else:
                        prob = prob
        elif self.trump == self.color:
            if self.number == 0:
                prob = 0
            elif self.number == 14:
                prob = 1
            else:
                prob = 1
                bettercards = 13 - self.number + 4
                for i in range(Numberofcards * Numberofplayers):
                    if i <= bettercards:
                        denominator = 59 - i
                        counter = denominator - bettercards
                        prob = prob * (counter / denominator)
                    else:
                        prob = prob
                prob = prob + 0.3
        else:
            if self.number == 0:
                prob = 0
            elif self.number == 14:
                prob = 1
            else:
                prob = 1
                bettercards = 26 - self.number + 4
                for i in range(Numberofcards * Numberofplayers):
                    if i <= bettercards:
                        denominator = 59 - i
                        counter = denominator - bettercards
                        prob = prob * (counter / denominator)
                    else:
                        prob = prob

        return prob

    def probabilityappend(self, Numberofcards, Numberofplayers):
        totalnumberofcards = Numberofcards * Numberofplayers
        ap = self.m * totalnumberofcards + self.b
        return ap


class mainwindow(QMainWindow):
    def __init__(self):
        super(mainwindow, self).__init__()
        self.setGeometry(700, 550, 850, 360)
        self.setWindowTitle('Wizard helper')
        self.cardslist = []
        self.colorlist = []
        self.numberofcards = 0
        self.numberofplayer = 0
        self.cards = []
        self.trump = 'n'
        self.count = 0
        self.setui()
    def setui(self):

        self.frame1 = QFrame(self)
        self.frame1.move(3, 3)
        self.frame1.setFrameShape(QFrame.StyledPanel)
        self.frame1.setLineWidth(1)
        self.frame1.resize(430, 70)

        self.numofply = QtWidgets.QLabel(self)
        self.numofply.setText('Number of players:')
        self.numofply.move(10, 10)

        self.numofcrd = QtWidgets.QLabel(self)
        self.numofcrd.setText('Number of cards:')
        self.numofcrd.move(150, 10)

        self.check1 = QtWidgets.QPushButton(self)
        self.check1.setText('Okay')
        self.check1.move(300, 10)
        self.check1.clicked.connect(self.check1clicked)

        self.innumply = QLineEdit(self)
        self.innumply.setValidator(QIntValidator())
        self.innumply.setMaxLength(2)
        self.innumply.move(110, 16)
        self.innumply.resize(30, 20)

        self.innumcrd = QLineEdit(self)
        self.innumcrd.setValidator(QIntValidator())
        self.innumcrd.setMaxLength(2)
        self.innumcrd.move(245, 16)
        self.innumcrd.resize(30, 20)

        self.trumplabel = QtWidgets.QLabel(self)
        self.trumplabel.setText('Trump:')
        self.trumplabel.move(10, 40)

        self.trumpblue = QtWidgets.QCheckBox(self)
        self.trumpblue.setText('Blue')
        self.trumpblue.move(50, 41)

        self.trumpyellow = QtWidgets.QCheckBox(self)
        self.trumpyellow.setText('Yellow')
        self.trumpyellow.move(120, 41)

        self.trumpred = QtWidgets.QCheckBox(self)
        self.trumpred.setText('Red')
        self.trumpred.move(190, 41)

        self.trumpgreen = QtWidgets.QCheckBox(self)
        self.trumpgreen.setText('Green')
        self.trumpgreen.move(260, 41)

        self.trumpnone = QtWidgets.QCheckBox(self)
        self.trumpnone.setText('None')
        self.trumpnone.move(330, 41)

        #####################################################################

        self.frame2 = QFrame(self)
        self.frame2.move(3, 78)
        self.frame2.setFrameShape(QFrame.StyledPanel)
        self.frame2.setLineWidth(0.9)
        self.frame2.resize(430, 270)


        self.insertcard = QtWidgets.QLabel(self)
        self.insertcard.setText('Insert cards')
        self.insertcard.move(10, 80)

        self.colorlabel = QtWidgets.QLabel(self)
        self.colorlabel.setText('Color:')
        self.colorlabel.move(10, 110)

        self.colorblue = QtWidgets.QCheckBox(self)
        self.colorblue.setText('Blue')
        self.colorblue.move(90, 111)

        self.coloryellow = QtWidgets.QCheckBox(self)
        self.coloryellow.setText('Yellow')
        self.coloryellow.move(160, 111)

        self.colorred = QtWidgets.QCheckBox(self)
        self.colorred.setText('Red')
        self.colorred.move(230, 111)

        self.colorgreen = QtWidgets.QCheckBox(self)
        self.colorgreen.setText('Green')
        self.colorgreen.move(300, 111)

        self.number = QtWidgets.QLabel(self)
        self.number.setText('Number:')
        self.number.move(10, 140)

        self.num1 = QtWidgets.QCheckBox(self)
        self.num1.setText('1')
        self.num1.move(90, 141)

        self.num2 = QtWidgets.QCheckBox(self)
        self.num2.setText('2')
        self.num2.move(160, 141)

        self.num3 = QtWidgets.QCheckBox(self)
        self.num3.setText('3')
        self.num3.move(230, 141)

        self.num4 = QtWidgets.QCheckBox(self)
        self.num4.setText('4')
        self.num4.move(300, 141)

        self.num5 = QtWidgets.QCheckBox(self)
        self.num5.setText('5')
        self.num5.move(90, 171)

        self.num6 = QtWidgets.QCheckBox(self)
        self.num6.setText('6')
        self.num6.move(160, 171)

        self.num7 = QtWidgets.QCheckBox(self)
        self.num7.setText('7')
        self.num7.move(230, 171)

        self.num8 = QtWidgets.QCheckBox(self)
        self.num8.setText('8')
        self.num8.move(300, 171)

        self.num9 = QtWidgets.QCheckBox(self)
        self.num9.setText('9')
        self.num9.move(90, 201)

        self.num10 = QtWidgets.QCheckBox(self)
        self.num10.setText('10')
        self.num10.move(160, 201)

        self.num11 = QtWidgets.QCheckBox(self)
        self.num11.setText('11')
        self.num11.move(230, 201)

        self.num12 = QtWidgets.QCheckBox(self)
        self.num12.setText('12')
        self.num12.move(300, 201)

        self.num13 = QtWidgets.QCheckBox(self)
        self.num13.setText('13')
        self.num13.move(90, 231)

        self.wizzard = QtWidgets.QCheckBox(self)
        self.wizzard.setText('Wizard')
        self.wizzard.move(160, 261)

        self.noob = QtWidgets.QCheckBox(self)
        self.noob.setText('Noob')
        self.noob.move(300, 261)

        self.confirmcard = QtWidgets.QPushButton(self)
        self.confirmcard.setText('Confirm card')
        self.confirmcard.move(160, 311)
        self.confirmcard.clicked.connect(self.check2clicked)


        self.specialcard = QtWidgets.QLabel(self)
        self.specialcard.setText('Special cards:')
        self.specialcard.move(10, 260)

        ##################################################################

        self.frame3 = QFrame(self)
        self.frame3.move(440, 50)
        self.frame3.setFrameShape(QFrame.StyledPanel)
        self.frame3.setLineWidth(1)
        self.frame3.resize(405, 230)

        self.exit = QtWidgets.QPushButton(self)
        self.exit.setText('Exit')
        self.exit.move(460, 300)
        self.exit.clicked.connect(self.close)

        self.nextround = QtWidgets.QPushButton(self)
        self.nextround.setText('Next round')
        self.nextround.move(580, 300)
        self.nextround.clicked.connect(self.next_round_click)

        self.reset = QtWidgets.QPushButton(self)
        self.reset.setText('Reset')
        self.reset.move(700, 300)
        self.reset.clicked.connect(self.restart_program)

        self.numbofcall = QtWidgets.QLabel(self)
        self.numbofcall.setText('Number of tricks:')
        self.numbofcall.move(460, 10)

        self.numbofticks = QtWidgets.QLabel(self)
        self.numbofticks.setText('0')
        self.numbofticks.move(550, 10)

        self.infolabel = QtWidgets.QLabel(self)
        self.infolabel.setText('Set the parameters on left side.')
        self.infolabel.resize(180, 30)
        self.infolabel.move(660, 10)

        self.cardlabel = QtWidgets.QLabel(self)
        self.cardlabel.setText('Card: 0/0')
        self.cardlabel.resize(100, 15)
        self.cardlabel.move(700, 60)

        self.card1 = QtWidgets.QLabel(self)
        self.card1.setText('')
        self.card1.resize(150, 25)
        self.card1.move(450, 60)

        self.card2 = QtWidgets.QLabel(self)
        self.card2.setText('')
        self.card2.resize(150, 25)
        self.card2.move(450, 80)

        self.card3 = QtWidgets.QLabel(self)
        self.card3.setText('')
        self.card3.resize(150, 25)
        self.card3.move(450, 100)

        self.card4 = QtWidgets.QLabel(self)
        self.card4.setText('')
        self.card4.resize(150, 25)
        self.card4.move(450, 120)

        self.card5 = QtWidgets.QLabel(self)
        self.card5.setText('')
        self.card5.resize(150, 25)
        self.card5.move(450, 140)

        self.card6 = QtWidgets.QLabel(self)
        self.card6.setText('')
        self.card6.resize(150, 25)
        self.card6.move(450, 160)

        self.card7 = QtWidgets.QLabel(self)
        self.card7.setText('')
        self.card7.resize(150, 25)
        self.card7.move(450, 180)

        self.card8 = QtWidgets.QLabel(self)
        self.card8.setText('')
        self.card8.resize(150, 25)
        self.card8.move(450, 200)

        self.card9 = QtWidgets.QLabel(self)
        self.card9.setText('')
        self.card9.resize(150, 25)
        self.card9.move(450, 220)

        self.card10 = QtWidgets.QLabel(self)
        self.card10.setText('')
        self.card10.resize(150, 25)
        self.card10.move(450, 240)

        self.card11 = QtWidgets.QLabel(self)
        self.card11.setText('')
        self.card11.resize(150, 25)
        self.card11.move(550, 60)

        self.card12 = QtWidgets.QLabel(self)
        self.card12.setText('')
        self.card12.resize(150, 25)
        self.card12.move(550, 80)

        self.card13 = QtWidgets.QLabel(self)
        self.card13.setText('')
        self.card13.resize(150, 25)
        self.card13.move(550, 100)

        self.card14 = QtWidgets.QLabel(self)
        self.card14.setText('')
        self.card14.resize(150, 25)
        self.card14.move(550, 120)

        self.card15 = QtWidgets.QLabel(self)
        self.card15.setText('')
        self.card15.resize(150, 25)
        self.card15.move(550, 140)

        self.card16 = QtWidgets.QLabel(self)
        self.card16.setText('')
        self.card16.resize(150, 25)
        self.card16.move(550, 160)

        self.card17 = QtWidgets.QLabel(self)
        self.card17.setText('')
        self.card17.resize(150, 25)
        self.card17.move(550, 180)

        self.card18 = QtWidgets.QLabel(self)
        self.card18.setText('')
        self.card18.resize(150, 25)
        self.card18.move(550, 200)

        self.card19 = QtWidgets.QLabel(self)
        self.card19.setText('')
        self.card19.resize(150, 25)
        self.card19.move(550, 220)

        self.card20 = QtWidgets.QLabel(self)
        self.card20.setText('')
        self.card20.resize(150, 25)
        self.card20.move(550, 240)


    def check1clicked(self):
        if (self.trumpblue.isChecked() == True and self.trumpred.isChecked() == True) or \
            (self.trumpblue.isChecked() == True and self.trumpyellow.isChecked() == True) or \
            (self.trumpblue.isChecked() == True and self.trumpgreen.isChecked() == True) or \
            (self.trumpblue.isChecked() == True and self.trumpnone.isChecked() == True) or \
            (self.trumpred.isChecked() == True and self.trumpyellow.isChecked() == True) or \
            (self.trumpred.isChecked() == True and self.trumpgreen.isChecked() == True) or \
            (self.trumpred.isChecked() == True and self.trumpnone.isChecked() == True) or \
            (self.trumpyellow.isChecked() == True and self.trumpgreen.isChecked() == True) or \
            (self.trumpyellow.isChecked() == True and self.trumpnone.isChecked() == True) or \
            (self.trumpgreen.isChecked() == True and self.trumpnone.isChecked() == True):

            self.infolabel.setText('Only set one trump color.')
            self.infolabel.update()
        elif self.trumpblue.isChecked() == False and self.trumpred.isChecked() == False and\
            self.trumpyellow.isChecked() == False and self.trumpgreen.isChecked() == False and \
            self.trumpnone.isChecked() == False:

            self.infolabel.setText('Please set a trump color.')
            self.infolabel.update()
        else:
            self.infolabel.setText('Parameters have been saved.  Insert card information.')
            self.infolabel.setWordWrap(True)
            self.infolabel.update()

        if self.trumpblue.isChecked() == True:
            self.trump = 'b'
        elif self.trumpred.isChecked() == True:
            self.trump = 'r'
        elif self.trumpyellow.isChecked() == True:
            self.trump = 'y'
        elif self.trumpgreen.isChecked() == True:
            self.trump = 'g'
        elif self.trumpnone.isChecked() == True:
            self.trump = 'n'

        self.numberofcards = int(self.innumcrd.text())
        self.numberofplayer = int(self.innumply.text())

        self.cardlabel.setText('Card: 0/' + str(self.numberofcards))
        self.cardlabel.update()

    def check2clicked(self):
        self.count = self.count + 1
        if self.num1.isChecked() == True:
            self.cardslist.append(1)
        elif self.num2.isChecked() == True:
            self.cardslist.append(2)
        elif self.num3.isChecked() == True:
            self.cardslist.append(3)
        elif self.num4.isChecked() == True:
            self.cardslist.append(4)
        elif self.num5.isChecked() == True:
            self.cardslist.append(5)
        elif self.num6.isChecked() == True:
            self.cardslist.append(6)
        elif self.num7.isChecked() == True:
            self.cardslist.append(7)
        elif self.num8.isChecked() == True:
            self.cardslist.append(8)
        elif self.num9.isChecked() == True:
            self.cardslist.append(9)
        elif self.num10.isChecked() == True:
            self.cardslist.append(10)
        elif self.num11.isChecked() == True:
            self.cardslist.append(11)
        elif self.num12.isChecked() == True:
            self.cardslist.append(12)
        elif self.num13.isChecked() == True:
            self.cardslist.append(13)
        elif self.wizzard.isChecked() == True:
            self.cardslist.append(14)
        elif self.noob.isChecked() == True:
            self.cardslist.append(0)

        if self.colorred.isChecked() == True:
            self.colorlist.append('r')
        elif self.colorblue.isChecked() == True:
            self.colorlist.append('b')
        elif self.coloryellow.isChecked() == True:
            self.colorlist.append('y')
        elif self.colorgreen.isChecked() == True:
            self.colorlist.append('g')
        elif self.wizzard.isChecked() == True or self.noob.isChecked() == True:
            self.colorlist.append('n')

        self.color = self.colorlist[-1]
        self.number = self.cardslist[-1]
        self.summ = 0
        self.cards.append(card(self.color, self.number, self.trump))
        for i in range(len(self.cardslist)):
            self.summ = self.summ + float(self.cards[i].probability(int(self.numberofcards), int(self.numberofplayer)))
        self.summ = self.summ + self.cards[0].probabilityappend(int(self.numberofcards), int(self.numberofplayer))

        self.numbofticks.setText(str(round(self.summ)) + ' (' + str(round(self.summ, decimals=5)) + ')')
        self.numbofticks.update()

        self.cardlabel.setText('Card: ' + str(self.count) + '/' + str(self.numberofcards))
        self.cardlabel.update()

        self.num1.setChecked(False)
        self.num2.setChecked(False)
        self.num3.setChecked(False)
        self.num4.setChecked(False)
        self.num5.setChecked(False)
        self.num6.setChecked(False)
        self.num7.setChecked(False)
        self.num8.setChecked(False)
        self.num9.setChecked(False)
        self.num10.setChecked(False)
        self.num11.setChecked(False)
        self.num12.setChecked(False)
        self.num13.setChecked(False)
        self.colorred.setChecked(False)
        self.colorblue.setChecked(False)
        self.colorgreen.setChecked(False)
        self.coloryellow.setChecked(False)
        self.wizzard.setChecked(False)
        self.noob.setChecked(False)

        if self.count == self.numberofcards:
            self.infolabel.setText('All cards have been inserted.')
            self.infolabel.update()

        for i in range(len(self.cardslist)):
            self.cardinfo = self.cards[i].printcard()
            if i == 0:
                self.card1.setText(self.cardinfo)
            elif i == 1:
                self.card2.setText(self.cardinfo)
            elif i == 2:
                self.card3.setText(self.cardinfo)
            elif i == 3:
                self.card4.setText(self.cardinfo)
            elif i == 4:
                self.card5.setText(self.cardinfo)
            elif i == 5:
                self.card6.setText(self.cardinfo)
            elif i == 6:
                self.card7.setText(self.cardinfo)
            elif i == 7:
                self.card8.setText(self.cardinfo)
            elif i == 8:
                self.card9.setText(self.cardinfo)
            elif i == 9:
                self.card10.setText(self.cardinfo)
            elif i == 10:
                self.card11.setText(self.cardinfo)
            elif i == 11:
                self.card12.setText(self.cardinfo)
            elif i == 12:
                self.card13.setText(self.cardinfo)
            elif i == 13:
                self.card14.setText(self.cardinfo)
            elif i == 14:
                self.card15.setText(self.cardinfo)
            elif i == 15:
                self.card16.setText(self.cardinfo)
            elif i == 16:
                self.card17.setText(self.cardinfo)
            elif i == 17:
                self.card18.setText(self.cardinfo)
            elif i == 18:
                self.card19.setText(self.cardinfo)
            elif i == 19:
                self.card20.setText(self.cardinfo)


    def restart_program(self):
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def next_round_click(self):

        self.numberofcards = int(self.innumcrd.text())
        self.numnew = self.numberofcards + 1
        self.innumcrd.setText(str(self.numnew))

        self.num1.setChecked(False)
        self.num2.setChecked(False)
        self.num3.setChecked(False)
        self.num4.setChecked(False)
        self.num5.setChecked(False)
        self.num6.setChecked(False)
        self.num7.setChecked(False)
        self.num8.setChecked(False)
        self.num9.setChecked(False)
        self.num10.setChecked(False)
        self.num11.setChecked(False)
        self.num12.setChecked(False)
        self.num13.setChecked(False)
        self.colorred.setChecked(False)
        self.colorblue.setChecked(False)
        self.colorgreen.setChecked(False)
        self.coloryellow.setChecked(False)
        self.wizzard.setChecked(False)
        self.noob.setChecked(False)
        self.trumpnone.setChecked(False)
        self.trumpred.setChecked(False)
        self.trumpblue.setChecked(False)
        self.trumpgreen.setChecked(False)
        self.trumpyellow.setChecked(False)

        self.count = 0
        self.colorlist = []
        self.cardslist = []
        self.cards = []

        self.card1.setText('')
        self.card2.setText('')
        self.card3.setText('')
        self.card4.setText('')
        self.card5.setText('')
        self.card6.setText('')
        self.card7.setText('')
        self.card8.setText('')
        self.card9.setText('')
        self.card10.setText('')
        self.card11.setText('')
        self.card12.setText('')
        self.card13.setText('')
        self.card14.setText('')
        self.card15.setText('')
        self.card16.setText('')
        self.card17.setText('')
        self.card18.setText('')
        self.card19.setText('')
        self.card20.setText('')

        self.cardlabel.setText('Card: ' + str(self.count) + '/' + str(self.numnew))
        self.infolabel.setText('Set the parameters on left side.')
        self.numbofticks.setText('0')


def win():
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    win = mainwindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    import qdarkstyle
    win()



'''
time wasted:
    25.6 3,5h
    26.6 3h
    28.6 1h
    20.8 4h
    22.8 3h
    5.9 3h
'''