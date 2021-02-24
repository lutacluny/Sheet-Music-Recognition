#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 12:24:34 2021

@author: fritz
"""

'''IMPORTANT directories beginning with '_' are not gonna be processed '''

from PIL import Image
import numpy as np
import sys, os, shutil
import Union_and_Find

thresh = 140
fn = lambda x : 255 if x > thresh else 0

amount_black_pixel_deviation = 1
tresh_delete_noise_of_marked_cols = 0.05
seperate_width = 1/15 #per cent of the line width

dir_to_save = "separated_notes"
dir_to_open = "groups_to_separate"

def main():    
    for dirName, subdirList, fileList in os.walk(dir_to_open):
        split = dirName.split('/')
        
        if len(split) > 2:
            
            test_name = split[1]
            line_name = split[2]     
            out_dir = "{}/{}/{}".format(dir_to_save, test_name, line_name)
        
        for fName in fileList:
            fName.strip()

            if test_name[0] == '_':
                continue
        

            img = Image.open("{}/{}".format(dirName,fName))
            np_img = np.asarray(img)
            img = img.convert('L').point(fn, mode='1')

            len_width = np_img.shape[1]
            len_height = np_img.shape[0]
            
            global tresh_pixel_to_separate
            tresh_pixel_to_separate = int (len_width * seperate_width)
            
            col_index = 0
            counter = 0 
            number_of_cols = 10
            
            amount_black_pixel_array = np.zeros(number_of_cols, dtype=int)
            
            while amount_black_pixel_array[number_of_cols-1] == 0:
                col = np_img[:, col_index].tolist()
                spaces_between_lines, amount_black_pixel = calc_spaces_between_lines(col)
                
                if is_matching_pattern(spaces_between_lines):
                    amount_black_pixel_array[counter] = amount_black_pixel
                    counter += 1                
                    
                col_index += 1
                

            amount_black_pixel = int(amount_black_pixel_array.mean())
            
            marked_cols = mark_col_true_if_is_on_a_note(amount_black_pixel, np_img, len_width, len_height)

            #distribution = calc_distribution_of_amount_of_related_black_pixel(marked_cols)
            #marked_cols = delete_noise_of_marked_cols(marked_cols, distribution)
            
            notes = create_list_of_notes(marked_cols)

            convert_notes_to_images(notes, out_dir, fName, np_img)


def calc_spaces_between_lines(col):
    is_between_to_lines = False
    is_prev_black = False
    
    spaces_between_lines = []
    
    pixel_between_lines = 0
    amout_black_pixel = 0
    
    for pixel in col:
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
                    
    return spaces_between_lines, amout_black_pixel


def is_matching_pattern(spaces_between_lines):
    spaces_between_lines = np.asarray(spaces_between_lines)
    
    len_spaces_between_lines = len(spaces_between_lines) 
    
    if len_spaces_between_lines == 0:
        return False 
    
    union_and_find = Union_and_Find.Union_and_Find(spaces_between_lines, 3)
    union_and_find.calc_eq_classes()
    union_and_find.sort_eq_classes_by_members_descending()
    
    biggest = union_and_find.eq_classes.pop(0)
        
    nr_of_lines = (len_spaces_between_lines + 1) / 5
    
    len_matches = nr_of_lines == int(nr_of_lines)
    
    if biggest.amount_of_members % 4 == 0 and len_matches:
        return True
    else:   
        return False

    
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
        

def mark_col_true_if_is_on_a_note(amount_black_pixel, np_img, len_width, len_height):
    #marked_cols = np.empty(len_width,dtype=bool)
    marked_cols = []
    
    for i in range(0, len_width):
        col = np_img[:,i].tolist()
        amount_black_pixel_in_col = calc_amount_black_pixel_in_col(col)
        
        upper_bound = amount_black_pixel + amount_black_pixel * amount_black_pixel_deviation
    
        if amount_black_pixel_in_col > upper_bound:
            marked_cols.append(True)
        else:
            marked_cols.append(False)

            

    return marked_cols

def create_list_of_notes(marked_cols):
    is_on_a_note = False
    dist_to_prev_note = sys.maxsize
    
    notes = []
    index = 0;
    for col in marked_cols:
        if is_note_col(col) and dist_to_prev_note > tresh_pixel_to_separate and not is_on_a_note:
            #TODO : setting index to 0 if index - tresh_pixel_to_separate < 0 might cause problems
            index_lower = max(0, index - tresh_pixel_to_separate)
            note = [index_lower]
            
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
    
def convert_notes_to_images(notes, out_dir, fName, np_img):
    index = 0
    fName = fName[:-4]
    for note in notes:
        note_matrix = np_img[:, note[0]:note[1]]
        note_img = Image.fromarray(note_matrix)
        note_img.save("{}/{}_{}.png".format(out_dir, fName, index))
        index += 1
    

def calc_distribution_of_amount_of_related_black_pixel(marked_cols):
    is_prev_note_col = False
    actual_amount = 0
    
    distribution = []
    
    index_start = 0
    
    index = 0
    for col in marked_cols:
        
        if is_note_col(col) and is_prev_note_col == False:
            index_start = index
            is_prev_note_col = True
            actual_amount += 1
    
        if not is_note_col(col) and is_prev_note_col == True:
            distribution.append((actual_amount, index_start))
            actual_amount = 0 
            is_prev_note_col = False
            
        if is_note_col(col) and is_prev_note_col == True:
            actual_amount += 1
            
        index += 1
        
    return distribution

def delete_noise_of_marked_cols(marked_cols, distribution):
    np_marked_cols = np.array(marked_cols)
    sorted_distribution = sorted(distribution, key=lambda x: x[0])
    max_pixel = sorted_distribution.pop()[0]
    
    tresh = int(tresh_delete_noise_of_marked_cols * max_pixel) + 1
    
    to_delete = [] 
    
    for actual in sorted_distribution:
        if actual[0] < tresh:
            to_delete.append(actual)   
        else: 
            break

       
    for actual in to_delete:
        index_start = actual[1]
        index_stop = actual[1] + actual[0]
        for i in range(index_start, index_stop):
            np_marked_cols[i] = False 
            
        
    return np_marked_cols.tolist()
    
if __name__=="__main__": 
    main() 

