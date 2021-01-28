#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 12:24:34 2021

@author: fritz
"""
from PIL import Image
import numpy as np
import sys, os, shutil

img = Image.open("line.png")
thresh = 200
fn = lambda x : 255 if x > thresh else 0
img = img.convert('L').point(fn, mode='1')
np_img = np.asarray(img)


len_width = np_img.shape[1]
len_height = np_img.shape[0]

tresh_pixel_to_separate = 9
dir_to_save = "separated notes"

def main():
    if os.path.isdir(dir_to_save):
        shutil.rmtree(dir_to_save)    
    os.mkdir(dir_to_save)
    
    space_between_lines, amount_black_pixel = calc_space_between_lines(0)
    marked_cols = mark_col_true_if_is_on_a_note(amount_black_pixel, 0)

    notes = create_list_of_notes(marked_cols)

    convert_notes_to_images(notes)


def calc_space_between_lines(col):
    is_between_to_lines = False
    is_prev_black = False
    
    spaces_between_lines = []
    
    pixel_between_lines = 0
    amout_black_pixel = 0
    
    for pixel in np_img[:, col]:
        if is_between_to_lines and isWhite(pixel):
            pixel_between_lines += 1
            
        elif is_between_to_lines and isBlack(pixel) and not is_prev_black:
            amout_black_pixel += 1
            spaces_between_lines.append(pixel_between_lines)
            is_prev_black = True
            is_between_to_lines = False
            pixel_between_lines = 0
            
        elif is_prev_black and isWhite(pixel):
            is_prev_black = False
            is_between_to_lines = True          
            
            pixel_between_lines += 1
            
        elif isBlack(pixel):
            is_prev_black = True
            amout_black_pixel += 1
            
            
    if len(spaces_between_lines) == 4:
        return np.asarray(spaces_between_lines).mean(), amout_black_pixel
    
    raise Exception()
    
def isBlack(pixel):
    if pixel == True:
        return False 
    else:
        return True
    
    
def isWhite(pixel):
    return not isBlack(pixel)

def calc_amount_black_pixel_in_col(col):
    amount_black_pixel = 0
    
    for pixel in col:
        if isBlack(pixel):
            amount_black_pixel += 1
            
    return amount_black_pixel
        

def mark_col_true_if_is_on_a_note(amount_black_pixel, epsilon):
    marked_cols = np.empty(len_width,dtype=bool)
    
    for i in range(0, len_width):
        col = np_img[:,i]
        amount_black_pixel_in_col = calc_amount_black_pixel_in_col(col)
        
        if amount_black_pixel_in_col > amount_black_pixel + epsilon :
            marked_cols[i] = True
        else:
            marked_cols[i] = False
            
    return marked_cols

def create_list_of_notes(marked_cols):
    is_on_a_note = False
    dist_to_prev_note = sys.maxsize
    
    notes = []
    index = 0;
    for col in marked_cols:
        if is_note_col(col) and dist_to_prev_note > tresh_pixel_to_separate and not is_on_a_note:
            note = [index - tresh_pixel_to_separate]
            
            dist_to_prev_note = 1
            is_on_a_note = True 
            
        elif not is_note_col(col) and dist_to_prev_note > tresh_pixel_to_separate and is_on_a_note:
            note.append(index)
            notes.append(note)
            
            is_on_a_note = False
            dist_to_prev_note += 1
        
        elif not is_note_col(col) and dist_to_prev_note <= tresh_pixel_to_separate and is_on_a_note:
            dist_to_prev_note += 1
            
        elif is_note_col(col):
            dist_to_prev_note = 1 
            
        else:
            dist_to_prev_note += 1
            
            
        index += 1
   
    return notes

def is_note_col(col):
    if col == True:
        return True
    else:
        return False
    
def convert_notes_to_images(notes):
    index = 0
    for note in notes:
        note_matrix = np_img[:, note[0]:note[1]]
        note_img = Image.fromarray(note_matrix)
        note_img.save("{}/note_{}.png".format(dir_to_save, index))
        index += 1
    

if __name__=="__main__": 
    main() 

