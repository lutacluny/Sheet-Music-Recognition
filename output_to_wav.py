#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 12:03:04 2021

@author: fritz
"""
import tomita.legacy.pysynth as ps
from playsound import playsound
from note_dicts import output_note_to_value, output_kind_to_value

f_name = 'prediction'
            
def main():
    note_list = parse_list(f_name)
    ps.make_wav(note_list, fn = "prediction.wav") 
   
    playsound("prediction.wav")
    
def parse_list(f_name):
    note_prediction = []
    lines = open(f_name).read().splitlines()
    for item in lines:
        splitted = item.split('_')
        output_note = splitted.pop(0)
        output_kind = splitted.pop(0) 
        
        note = (output_note_to_value[output_note], output_kind_to_value[output_kind])
        note_prediction.append(note)
    
    return note_prediction

if __name__=="__main__":
    main()
