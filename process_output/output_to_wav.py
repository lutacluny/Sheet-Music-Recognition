#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 12:03:04 2021

@author: fritz
"""

import tomita.legacy.pysynth as ps
from note_dicts import index_to_note_key_f, index_to_note_key_g, note_to_index, kind_to_value
from symbol_dicts import symbol_to_value 

f_name = 'label_files/Fuchs du hast die Gans gestohlen'
            

    
def main():    
    musical_object_list = parse_list(f_name)
    ps.make_wav(musical_object_list, fn = "prediction.wav") 
   
    
def parse_list(f_name):
    musical_object_prediction = []
    global is_g_key 
    is_g_key = True 

    global is_double_flat
    is_double_flat = False 
    
    global is_single_flat
    is_single_flat = False
    
    global is_double_sharp
    is_double_sharp = False
    
    global is_single_sharp
    is_single_sharp = False
    lines = open(f_name).read().splitlines()
    
    for line in lines:
        for item in line.split(' '):
            if len(item) == 0:
                continue
            splitted = item.split('_')
            
            musical_object = splitted[0]
            kind = splitted[1] 
            
            if musical_object == "K":
                if kind == "G":
                    is_single_sharp = True 
                    
                elif kind == "D":
                    is_double_sharp = True
                    
                elif kind == "F":
                    is_single_flat = True 
                    
                elif kind == "Bb":
                    is_double_flat = True 
                    
                elif len(splitted) > 2:
                    is_g_key = False 
                    
                continue
        
            
            elif musical_object == "M":
                continue
                    
            elif musical_object == "repeat":
                continue 
                    
            elif musical_object == "z":
                output_object = symbol_to_value[musical_object]
                output_kind = kind_to_value[kind]

                    
            else:
                index = note_to_index[musical_object] - 1
                output_kind = kind_to_value[kind]
                
                if is_g_key:
                    output_object = process_note_g_key(index)
                    
                else:
                    output_object = process_note_f_key(index)
                    
            musical_object_out = (output_object, output_kind)
            musical_object_prediction.append(musical_object_out)
        
    return musical_object_prediction

def process_note_g_key(index):
    if is_single_flat:
        output_object = index_to_note_key_g[index] + "b"
                    
    elif is_double_flat:
        if index - 1 < 0:
            output_object = 'b3'
        else:
            output_object = index_to_note_key_g[index-1]
                            
    elif is_single_sharp: 
        output_object = index_to_note_key_g[index] + "#" 
                    
    elif is_double_sharp:
        if index + 1 > 12:
            output_object = 'b5'
        else:
            output_object = index_to_note_key_g[index+1]
              
    else:
        output_object = index_to_note_key_g[index]    
        
    return output_object
        

def process_note_f_key(index):
    if is_single_flat:
        output_object = index_to_note_key_g[index] + "b"
                    
    elif is_double_flat:
        if index - 1 < 0:
            output_object = 'd2'
        else:
            output_object = index_to_note_key_g[index-1]
                            
    elif is_single_sharp: 
        output_object = index_to_note_key_f[index] + "#" 
                    
    elif is_double_sharp:
        if index + 1 > 12:
            output_object = 'd'
        else:
            output_object = index_to_note_key_f[index+1]
              
    else:
        output_object = index_to_note_key_g[index]      
        
    return output_object
            
            
if __name__=="__main__":
    main()
