#Lucia Johnson
#Final Project

#import graphics
from graphics import *

#Creates first GUI
def screen1():
    win1=GraphWin("Movie Input", 700, 300)
    win1.setCoords(-10, -10, 10, 10)
    win1.setBackground('light grey')

    #Creates Text explaining the program
    expl1 = Text(Point(0, 9), "This program gives you a description for the movie you enter below.")
    expl2 = Text(Point(0, 7), "Please enter the exact name of the movie you are looking for. Then press the ENTER button.")
    expl1.setTextColor('purple')
    expl2.setTextColor('purple')
    expl1.draw(win1)
    expl2.draw(win1)

    #Creates Entry Field
    name_input = Entry(Point(0, 5), 25)
    name_input.draw(win1)

    #Creates Enter button
    button = Rectangle(Point(-2, -1), Point(2, -3))
    button.setFill("blue")
    button.draw(win1)
    enter = Text(Point(0, -2),"ENTER")
    enter.setStyle("bold")
    enter.draw(win1)

    #Checks if Enter button was clicked
    while True:
        click = win1.getMouse()
        clickX = click.getX()
        clickY = click.getY()
        if 3 > clickX> -3 and -1 > clickY > -3:
            break
        else:
            continue
    
    #Tries to open the imdb file
    try:
        imdb = open('imdb.txt', 'r')
    except:
        print('Error. Couldn\'t open file')
        quit()

    #Gets Text from Entry Field and checks if the movie is on the list
    movie_name=name_input.getText()
    movie_description= 'Your movie wasn\'t found. Please try again and make sure the spelling is correct.'
    #starts a loop to go over each line
    for line in imdb:
        #Splits each line into fileds
        fields = line.split(',*,')
        #Checks each line if it starts with the movie name
        if fields[0]==movie_name:
            #Defines and prints out the movie description and sets the availability to true
            movie_description= fields[1]
        #Moves on to the next line if the line doesn't contain the desired movie
        else:
            continue
#I was able to find every movie I tried except for the first one Guardians of the Galaxy.
#I looked at the example file for WA11 for help but that also couldn't find it
#I think the for loop skips over the first line when it is reading the file, but I can't figure out how to make it read the line.
    win1.close()
    screen2(movie_name, movie_description)

#Creates the second GUI
def screen2(name, desc):
    win2=GraphWin('Movie Output', 1300, 600)
    win2.setCoords(-10, -10, 10, 10)
    win2.setBackground('light grey')

    #Creates a Textfield with the movie name and a blank one for the description
    ntext='Your selected movie was '+ name
    n=Text(Point(0, 9), ntext)
    n.setTextColor('purple')
    n.draw(win2)
    d=Text(Point(0, 7), '')
    d.setText(desc)
    d.setSize(9)
    d.setTextColor('purple')
    d.draw(win2)
    a=Text(Point(0, -3),'Do you want to enter another movie?')
    a.setTextColor('purple')
    a.draw(win2)


    #Creates a yes and a no button
    ybutton = Rectangle(Point(-6, -6), Point(-4, -4))
    ybutton.setFill("green")
    ybutton.draw(win2)
    yes = Text(Point(-5, -5),"YES")
    yes.setStyle("bold")
    yes.draw(win2)

    nbutton = Rectangle(Point(6, -6), Point(4, -4))
    nbutton.setFill("orange")
    nbutton.draw(win2)
    no = Text(Point(5, -5),"NO")
    no.setStyle("bold")
    no.draw(win2)

    #Creates an image of a DVD for decoration
    dvdouter=Circle(Point(5, 3), 1.5)
    dvdouter.setFill('PowderBlue')
    dvdouter.draw(win2)
    dvdinner=Circle(Point(5, 3), 0.15)
    dvdinner.setFill('light grey')
    dvdinner.draw(win2)

    #Checks if the user clicked the yes or the no button. If yes then screen 1 is started over again
    while True:
        click = win2.getMouse()
        clickX = click.getX()
        clickY = click.getY()
        if -4 > clickX> -6 and -4 > clickY > -6:
            win2.close()
            screen1()
        elif 6 > clickX > 4 and -4 > clickY > -6:
            win2.close()
            break
        else:
            continue
        break
#Runs the program          
screen1()
