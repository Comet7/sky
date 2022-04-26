NAME : A simple agent-based model-simulate the relationship between wolf and sheep, namely predator and prey

Content List:

model.py- used to build the model, including making agents and behavior of agents,
have the function of interecting with user

sheep_agentframework.py- define sheep variables of coordinates and behaviors

wolf_agentframewok.py- define wolf variables of coordinates and behaviors

in.csv- raster environment data (grass), each value is deemed as a pixel.

Outline of the model:
1. The purpose of the model
With the development of high-performance, people are able to build some independent model which called '' individual level models''
rather than aggregation models. The main advantages that can be used are to investigate characteristics 
of independent entities and study the behavior patterns. Therefore, an agent-based model had been emerged, in which
individual objects have the ''agency''. Agent-based model (ABM) can be used in many fields. Besides, The stability of predator-prey ecosystems 
is a matter of concern. It is interesting to simulate a simple food-chain relationship between sheep and wolf based on agent-based model.

2. how it can be run
Sheep and wolves are restricted to a 100×100 environment (grassland). The behavior of agents (sheep and wolf) will be given into a Graphical User Interface
(GUI) through pressing the ''run model'' botton under the ''model'' button, but this method only implements the default parameter Settings in the code.
If user wish to change the number of sheep, you can enter any number from 1 to 96, because the total number of agents is defined within 100 and the number 
of wolf is 3 (fixed parameter).  When your set number out of the range, it will pop up a alert box which tell you ''the number of sheep is out of range''. After setting 
the sheep number, just click the ''confirm'' button and ''run'' button the model will run automatically.

3. The process of the model (what will happen after running)
Sheep and wolves wander randomly on the grass( the envrionment), wolves will chase and eat sheep to replenish energy, whilst sheep try to escape
being hunted by moving away wolves. In this model, only assuming the sheep have enough grass to eat, wolves chase the sheep and eat them  
Once the model has been run,  the sheep, namley blue and white dots, will move randomly, the behave of wolves (black dots) is the same. 
If sheep are within a certain distance from wolves during the movement, the wolves will kill the sheep. What will happpen in the model is that a sheep eaten by a wolf 
stop moving and its color turn red (the colors of dots transforming from blue or white to red ).

Known issues:
1.  I try to realise a function that is able to delete the previous input parameter and run the model again through pressing the ''confirm''  and ''run'' button. Although click the 
''clear'' button the numer in the enry box can be removed, it report errors after rerunning the model. It seems the model can only run a time. If users want to run the model again, 
they must close and restart it.
2.  I try to add a text widget in Tkinter which is used to show total store between sheep, but I failed. When I run the model , there is no stores in the text widget.

testing:
1. I try to print the coordinates of wolf and sheep, recording sheep were killed by wolves.
2. I try to print the store between sheep in each frame and total records.
3. I try to print the frame number, to see how many frames when the model stops running.
4. I try to print the restricted 100 coordinates, scraping on the web (data.html).

Some ideas for further development:
1. Show the total store in the GUI correctly.
2. In the GUI, the model can modify parameters repeatedly and run multiple times, without closing and re-running.
3. Try to add a function to provide different speed of movement for wolves and sheep, restoring the real chasing scene.