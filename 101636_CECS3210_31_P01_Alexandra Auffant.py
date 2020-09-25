#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Rock, Paper, Scissors Game. You play again the program where the user picks
#which one they want to throw (by choosing number) and then the program throws heir random 
#pick.

#Mi razon por hacer este juego es porque fue el primer juego que vino a mi mente ya que es de los primeros juegos que aprendi
# de peque~a. Tambien, siempre me ha encantado la idea de uno tratar de adivinar lo que su "opponent" vaya a tirar para ganarle.

from graphics import*
import random

def main():
    
    win=GraphWin("Rock, Paper, Scissor Game", 600, 500)
    win.setBackground(color_rgb(224,250,250))
    
    Text(Point(300,20),"Rock= 1, Paper= 2, Scissor= 3").draw(win)
    Text(Point(257,45),"Enter the number of your choice:").draw(win)
    choice=Entry(Point(400,45),5)
    choice.setFill("white")
    choice.draw(win)
    Text(Point(300,70),"(Click anywere when you're done choosing)").draw(win)
    
    win.getMouse()
    
    user=choice.getText()
    pick=int(user)
    
#Out of User's Choice
    if pick==1:
        pick1=Text(Point(150,150),'You: Rock')
        shape1=Circle(Point(150, 250), 75)
        shape1.setFill(color_rgb(79,77,79))
        pick1.draw(win)
        shape1.draw(win)
            
    elif pick==2:
        pick2=Text(Point(150,150),'You: Paper')
        shape2=Rectangle(Point(75, 190), Point(225,330))
        shape2.setFill("white")
        pick2.draw(win)
        shape2.draw(win)
            
    elif pick==3:
        pick3=Text(Point(150,100),'You: Scissor')
        shape3=Polygon(Point(75, 190), Point (225, 330), Point(75, 330), Point(225, 190))
        shape3.setFill("yellow")
        pick3.draw(win)
        shape3.draw(win)
            
    else:
        pick0=Text(Point(300,300),'Your pick is not valid, goodbye.')
        pick0.draw(win)
            
#Output of Computer's Choice
    computer=random.randint(1, 3)
        
    if computer==1:
        comp1=Text(Point(450,150),'Opponent: Rock')
        form1=Circle(Point(450, 250), 75)
        form1.setFill(color_rgb(79,77,79))
        comp1.draw(win)
        form1.draw(win)
        
    elif computer==2:
        comp2=Text(Point(450,150),'Opponent: Paper')
        form2=Rectangle(Point(375, 190), Point(525,330))
        form2.setFill("white")
        comp2.draw(win)
        form2.draw(win)
        
    else:
        comp3=Text(Point(450,150),'Opponent: Scissor')
        form3=Polygon(Point(375, 190), Point (525, 330), Point(375, 330), Point(525, 190))
        form3.setFill("yellow")
        comp3.draw(win)
        form3.draw(win)

#Output of who wins, looses or if it's a tie

    if (pick==1 and computer==2 or pick==2 and computer==3 or pick==3 and computer==1):
        Text(Point(300,350),"You lose :(").draw(win)
    elif (pick==2 and computer==1 or pick==3 and computer==2 or pick==1 and computer==3):
        Text(Point(300,350),"You win! :)").draw(win)
    else: #this is when the user and computer have the same choice
        Text(Point(300,350),"Its a tie!").draw(win)
    
#Explanation of why the user won or lost
    
    if (pick==1 and computer==2 or pick==2 and computer==1):
        Text(Point(300,400),"Paper beats Rock since Paper covers Rock.").draw(win)
    elif (pick==2 and computer==3 or pick==3 and computer==2):
        Text(Point(300,400),"Scissor beats Paper since Scissor cuts Paper.").draw(win)
    elif (pick==1 and computer==3 or pick==3 and computer==1):
        Text(Point(300,400),"Rock beats Scissor since Rock breaks Scissor.").draw(win)
    else: #when the user and opponent choose the same item
        Text(Point(300,400), "The opponent and you chose the same item.").draw(win)
    
    win.getMouse()
    win.close()
    
main()
                
   




