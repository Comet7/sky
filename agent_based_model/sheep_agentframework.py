# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 00:04:41 2022
Define sheep variables of coordinates and behaviors.
Functions contain designed algorithms for moving agents, eating grass, 
judging the distance to other agents, and sharing food with peers.  
@author: Yanfeng Li
"""
import random
#make a agent class
class Agent:
    
    def __init__(self, ia,a, environment,y,x,color):
        '''
        Code for define variables

        Parameters
        ----------
        ia : sheep id
            DESCRIPTION.
        a : sheep numbers
            DESCRIPTION.
        environment : TYPE
            DESCRIPTION.
        y : y coordinates got in data.html
            DESCRIPTION.
        x : x coordinates got in data.html
            DESCRIPTION.
        color : color for sheep
            DESCRIPTION.

        Returns
        -------
        None.

        '''
        self.id=ia
        #self.x=random.randint(0,99) #generate int values between start and end;locate to a random location
        #self.y=random.randint(0,99) #randomise their starting points within a 100x100 grid
        self.x=x 
        self.y=y
        self.environment = environment
        self.agents =a
        self.alive = True
        self.store = 0 # We'll come to this in a second.
        self.color=color
        if (x == None):
            self._x = random.randint(0,99)
        else:
            self._x = x
        if (y == None):
            self._y = random.randint(0,99)
        else:
            self._y = y
    
    def __str__(self):
        '''
        print id, coordinates and stores of sheep

        Returns
        -------
        TYPE
            DESCRIPTION.

        '''
        return "id="+ str(self.id)+",x="+str(self.x)+",y="+str(self.y)+",sharing="+str(self.store)
    
    def move(self,d):
        '''
        Code for agents movement

        Parameters
        ----------
        d : distance
            DESCRIPTION.

        Returns
        -------
        None.

        '''
        if (self.alive):
         self.x=self.move_coordinate(self.x,d)
         self.y=self.move_coordinate(self.y,d)
         '''why self.x rather than agents[i][1]? 
         as we're now inside the class/agent objects, 
         not outside them looking at them in a container '''
         #allow agents leaving the top of an area to come in at the bottom, and leaving left, come in on the right
         #if random.random() < 0.5:#It generates a random floating point number within the range zero to just less than one
         #   self.x = (self.x + 1) % 100
         #else:
         #   self.x = (self.x - 1) % 100

         #if random.random() < 0.5:
         #  self.y = (self.y + 1) % 100
         #else:
         #   self.y = (self.y - 1) % 100 
    
   
    def move_coordinate(self,a,d):
        '''
        Code for allowing agents leaving the top of an area to come in at the bottom,
        and leaving left, coming in on the right.

        Parameters
        ----------
        a : agents of sheep
            DESCRIPTION.
        d : distance
            DESCRIPTION.

        Returns
        -------

        '''
        if random.random()<0.2:
            return a
        if random.random()<0.5:
            a=(a+random.randint(1,d))%100
        else:
            a=(a-random.randint(1,d))%100
        return a
   
    def eat(self): 
        '''
        sheep eat grass(environemt) to gain store.

        Returns
        -------
        None.

        '''
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
    def share_with_neighbours(self,neighbourhood):
        '''
        

        Parameters
        ----------
        neighbourhood : integer data
            define a distance, if distance between two agents less than 
            neighbourhood, they share the store.

        Returns
        -------
        None.

        '''
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                #print("sharing " + str(dist) + " " + str(ave))
    def distance_between(self, agent):
        '''
        calculate distance between agents

        Parameters
        ----------
        agent : sheep or wolves (dots)
            DESCRIPTION.

        Returns
        -------
        TYPE
            DESCRIPTION.

        '''
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
   

        