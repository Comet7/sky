# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 01:06:35 2022
Define wolf variables of coordinates and behaviors
Functions contain designed algorithms for moving
@author: Yanfeng Li
"""
import random

class wolf:
    def __init__(self, ia,wolf,y,x,color):
        '''
        Code for initialise variables

        Parameters
        ----------
        ia : wolf id
            DESCRIPTION.
        wolf : wolf numbers
            DESCRIPTION.
        y : y coordinates got in data.html
            DESCRIPTION.
        x : x coordinates got in data.html
            DESCRIPTION.
        color : color for wolves
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
        #self.environment = environment
        self.wolf =wolf
        #self.store = 0 # We'll come to this in a second.
        self.color=color
        
            
    def __str__(self):
        '''
        print id and coordinates of wolves

        Returns
        -------
        TYPE
            DESCRIPTION.

        '''
        return "id="+ str(self.id)+",x="+str(self.x)+",y="+str(self.y)
    
    def move(self,dis):
        '''
        Code for wolf movement

        Parameters
        ----------
        dis : distance
            DESCRIPTION.

        Returns
        -------
        None.

        '''
        self.x=self.move_coordinate(self.x,dis)
        self.y=self.move_coordinate(self.y,dis)
    
    def move_coordinate(self,a,dis):
        '''
        Code for allowing agents leaving the top of an area to come in at the bottom,
        and leaving left, coming in on the right.

        Parameters
        ----------
        a : agents of wolf
            DESCRIPTION.
        dis : distance
            DESCRIPTION.

        Returns
        -------
        a : TYPE
            DESCRIPTION.

        '''
        if random.random()<0.2:
            return a
        if random.random()<0.5:
            a=(a+random.randint(1,dis))%100
        else:
            a=(a-random.randint(1,dis))%100
        return a
         
    