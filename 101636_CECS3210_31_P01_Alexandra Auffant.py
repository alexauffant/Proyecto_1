#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Rock, Paper, Scissors Game. You play again the program where the user picks
#which one they want to throw (by choosing number) and then the program throws heir random 
#pick.
from graphics import*
import random

def main():
    print("Rock: 1")
    print("Paper: 2")
    print("Scissor: 3")
    
    pick=int(input("Enter the number of your choice:"))
    
    print("Rock, Paper, Scissors, GO!")
    
    win=GraphWin("Rock, Paper, Scissor Game", 600, 500)
    win.setBackground(color_rgb(224,250,250))

#Out of User's Choice
    if pick==1:
        pick1=Text(Point(150,100),'User: Rock')
        shape1=Circle(Point(150, 200), 75)
        shape1.setFill(color_rgb(79,77,79))
        pick1.draw(win)
        shape1.draw(win)
            
    elif pick==2:
        pick2=Text(Point(150,100),'User: Paper')
        shape2=Rectangle(Point(75, 140), Point(225,280))
        shape2.setFill("white")
        pick2.draw(win)
        shape2.draw(win)
            
    elif pick==3:
        pick3=Text(Point(150,100),'User: Scissor')
        shape3=Polygon(Point(75, 140), Point (225, 280), Point(75, 280), Point(225, 140))
        shape3.setFill("yellow")
        pick3.draw(win)
        shape3.draw(win)
            
    else:
        pick0=Text(Point(300,300),'Your pick is not valid, goodbye.')
        pick0.draw(win)
            
#Output of Computer's Choice
    computer=random.randint(1, 3)
        
    if computer==1:
        comp1=Text(Point(450,100),'Opponent: Rock')
        form1=Circle(Point(450, 200), 75)
        form1.setFill(color_rgb(79,77,79))
        comp1.draw(win)
        form1.draw(win)
        
    elif computer==2:
        comp2=Text(Point(450,100),'Opponent: Paper')
        form2=Rectangle(Point(375, 140), Point(525,280))
        form2.setFill("white")
        comp2.draw(win)
        form2.draw(win)
        
    else:
        comp3=Text(Point(450,100),'Opponent: Scissor')
        form3=Polygon(Point(375, 140), Point (525, 280), Point(375, 280), Point(525, 140))
        form3.setFill("yellow")
        comp3.draw(win)
        form3.draw(win)

#Output of who wins, looses or if it's a tie

    if (pick==1 and computer==2):
        txt1=Text(Point(300,400),"You lose :(")
        txt1.draw(win)
    elif (pick==2 and computer==1):
        txt2=Text(Point(300,400),"You win! :)")
        txt2.draw(win)
    elif (pick==2 and computer==3):
        txt3=Text(Point(300,400),"You lose :(")
        txt3.draw(win)
    elif (pick==3 and computer==2):
        txt4=Text(Point(300,400),"You win! :)")
        txt4.draw(win)
    elif (pick==3 and computer==1):
        txt5=Text(Point(300,400),"You lose :(")
        txt5.draw(win)
    elif (pick==1 and computer==3):
        txt6=Text(Point(300,400),"You win! :)")
        txt6.draw(win)
    else: #this is when the user and computer have the same choice
        txt7=Text(Point(300,400),'Its a tie!')
        txt7.draw(win)
    
    
    win.getMouse()
    win.close()
main()
                
    


# In[ ]:





# In[ ]:




