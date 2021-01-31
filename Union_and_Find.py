#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 22:09:39 2021

@author: fritz
"""

import Equiv_Class

class Union_and_Find():
    def __init__(self, collection, epsilon):
        self.collection = collection
        self.eq_classes = []
        self.epsilon = epsilon
        
    def calc_eq_classes(self):
        for elem in self.collection:
            class_of_e = self.find(elem)
            
            if class_of_e == False:
                new_class = Equiv_Class.Equiv_Class(elem)
                self.eq_classes.append(new_class)
                
            else: 
                self.assign_class(elem, class_of_e)
                   
        return self.eq_classes
    
    def find(self, elem):
        for eq_class in self.eq_classes:
            if abs(elem - eq_class.repr) <= self.epsilon:
                return eq_class
            
        return False
        
    def assign_class(self, e, eq_class):
        eq_class.members.append(e)
        eq_class.members = sorted(eq_class.members)
        median = int((len(eq_class.members)) / 2 - 1)
        eq_class.repr = eq_class.members[median]
        eq_class.amount_of_members += 1 
        
    def sort_eq_classes_by_members_descending(self):
        self.eq_classes = sorted(self.eq_classes, key=lambda x: x.amount_of_members, reverse=True)
        