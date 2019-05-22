#! /usr/bin/env python

''' 

'''
from .. item_base import Item_Base

class Controller_Base(Item_Base):

    def __init__(self, container, id):
        Item_Base.__init__(self,container)

        self.id = id
        self.name = id

        self.add_property('state', 'idle') 
        self.add_property('heatbeat','none')


    def __str__(self):
        return ("Controller: {}; state {}; status {}".format(self.id, self.properties['state'], self.properties['status']))

 