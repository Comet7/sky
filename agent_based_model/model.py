# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 00:06:02 2022

@author: lenovo
"""
import random
import operator
import csv
import matplotlib
matplotlib.use('TkAgg')
import tkinter 
import matplotlib.pyplot
import matplotlib.animation 
import sheep_agentframework
import wolf_agentframework
import requests
import bs4

#agents need to know who is near them so they can decide whether or not to interact with other agents
'''def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
    ((agents_row_a.y - agents_row_b.y)**2))**0.5'''

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
#print(td_ys)
#print(td_xs)



#Create a window and a model button which is used to run the model
fig = matplotlib.pyplot.figure(figsize=(7, 7))
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.grid(row=0,rowspan=15, column=1)
tkinter.Label(root, text="Number of sheep (1-96)", font=('Calibri 10')).grid(row=0,column=0)
number= tkinter.Entry(root, width=15)
number.grid(row=1, column=0)

# Just showing menu elements
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)

def set_parameter():
    '''
    Code for set the 'confirm' button
    number.get() get the input number of sheep
    the initial value of sheep number is 96, 
    which means the range of sheep number is between 1-97.
    (Controlled by a conditional statement)
    Returns
    -------
    None.

    '''
    global num_of_agents
    if int(number.get()) > num_of_agents or int(number.get()) <1:
        tkinter.messagebox.showinfo("Error",  "The number of sheep is out of range")
        num_of_agents = 96
    else:
        num_of_agents = int (number.get())
   
#Define a function to clear the Entry Widget Content
def clear_text():
    '''
    a function to clear the value in entry box of sheep number

    Returns
    -------
    None.

    '''
    number.delete('0', tkinter.END)




carry_on=True

def catch(a,b):
    """
    Code for killing sheep
    The function will be excuted when their distance within a certain range

    Parameters
    ----------
    a : Sheep
        DESCRIPTION.
    b : Wolf
        DESCRIPTION.

    Returns
    -------
    None.

    """
    if ((((a.x - b.x)**2) +(((a.y - b.y)**2)))**0.5) <10:
        a.alive= False
        a.color= 'Red'
        print(b, "kill", a)
            

def update(frame_number):
    '''
    Makes an animation by repeatedly calling the function,
    including movement of agents and display on a GUI window.
    The function to call at each frame. 
    The argument will be the next value in frames.

    Parameters
    ----------
    frame_number : integer
        The number of frames in animation motion

    Returns
    -------
    None.

    '''
    global carry_on
    fig.clear()   
    print(frame_number)
    d=2
    dis=4
    
    # Move the agents. 
    '''two dimensional dataset, the purpose of the first dimension is to create agents
    the second dimension is established to create y and x coordinates of agents'''
    #for j in range(num_of_iterations): 
        #print(agents[0])
    for i in range(num_of_agents):
        agents[i].move(d)
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        for j in range(num_of_wolf):
            wolf[j].move(dis)
            catch(agents[i], wolf[j])
        #print(wolf[j])
        #print(agents[i])           
        
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition",frame_number) #print out the frame_number
        
    
    '''for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i][0],agents[i][1])
        #print(agents[i][0],agents[i][1])'''
    matplotlib.pyplot.xlim(0, 99) #	Get or set the x limits of the current axes.
    matplotlib.pyplot.ylim(0, 99) # Get or set the y-limits of the current axes.
    matplotlib.pyplot.imshow(environment) #	Display data as an image, i.e., on a 2D regular raster.
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color=agents[i].color) #A scatter plot of y vs
    matplotlib.pyplot.show() #display all open figures
    for j in range(num_of_wolf):
        matplotlib.pyplot.scatter(wolf[j].x,wolf[j].y, color=wolf[j].color)
    matplotlib.pyplot.show()
def gen_function(b = [0]):
    '''
    Code for set times to update the animation

    Parameters
    ----------
    b : TYPE, optional
        DESCRIPTION. The default is [0].

    Yields
    ------
    TYPE
        DESCRIPTION.

    '''
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < num_of_iterations) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
def run():
    '''
    a funtion to run the model.
    it will be connected to menu and 'run' button

    Returns
    -------
    None.

    '''
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()
    
random.seed(1)
#some initial variables
num_of_wolf = 3
#num_of_agents = 10 
num_of_agents = 96
num_of_iterations = 100
neighbourhood = 90

environment = [] #Create an environment list
agents = [] #use containers to better store our agent coordinates;add several sets of coordinates to this one list
wolf = []
color = []
color_wolf =[]
color.append('Blue')
color.append('White')
color_wolf.append('Black')

#read the csv file
f = open('in.csv', newline='')
dataset = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
for row in dataset: # A list of rows
    rowlist = []
    for value in row: # A list of value
        rowlist.append(value)
    environment.append(rowlist) #save envrionement data into the list
#        print(value) # Floats
f.close() # Don't close until you are done with the reader;
        # the data is read on request.
matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show()       


# Make sheep.
for i in range(num_of_agents): # Create a new set of coordinates, put into for-loop
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    z = i%len(color)
    #add agents, environment, y and x of html files into the agents container.
    agents.append(sheep_agentframework.Agent(i,agents,environment,y,x,color[z]))    
for i in range(num_of_agents): 
    print(agents[i])
    
print("i", i)

# Make wolves
for j in range(num_of_wolf): # Create a new set of coordinates, put into for-loop
    #y_wolf = int(td_ys[j].text)
    y = int(td_ys[j+i].text)
    x = int(td_xs[j+i].text)
    #z_wolf = j%len(color_wolf)
    #add agents, environment, y and x of html files into the agents container.
    #wolf.append(wolf_framework.wolf(j,wolf,y,x,color[z_wolf]))
    wolf.append(wolf_agentframework.wolf(j,wolf,y,x,'Black'))


#for j in range(wolf): 
#   print(agents[j])        

'''for agents_row_b in agents:
    for agents_row_a in agents:
       distance = distance_between(agents_row_a, agents_row_b)'''
#Create a button to confirm the input value of sheep numbers
tkinter.Button(root, text="Confirm", width=15, command=set_parameter).grid(row=2, column=0)
#Create a button to clear the Entry Widget
tkinter.Button(root,text="Clear", width=15, command=clear_text).grid(row=3,column=0)
#Create a button to run the model
tkinter.Button(root, text="Run", width=15, command=run).grid(row=4,column=0)
#text= tkinter.Text(root,width=15, height=8).grid(row=2, column=2)
#text= text.insert(0,agentframework.share_with_neighbours(neighbourhood))
model_menu.add_command(label="Run model", command=run)
tkinter.mainloop()