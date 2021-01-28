#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 18:50:05 2021

@author: fritz
"""
from PIL import Image
import shutil
import os
import numpy as np

tresh_for_seperate_black_white = 90
width_out = 40 
height_out = 100

vanilla_path = 'separated_notes'
pre_processed_path = 'pre_processed'
    
def main():

    
    if os.path.isdir(pre_processed_path):
        shutil.rmtree(pre_processed_path)
        
    shutil.copytree(vanilla_path, pre_processed_path)  
    
    for dir_name, subdir_list, file_list in os.walk(pre_processed_path):
        for f_name in file_list:
            f_name_new = "{}_{}".format(f_name[:-4], "pre_processed.png")
            new_location = "{}/{}".format(pre_processed_path, f_name_new)
            
            note_img = load_note_black_white(f_name)
            width, height = note_img.size
            
            np_img = np.asarray(note_img)
            space_between_two_lines, line_width = calc_space_between_lines(np_img, 0)
            
            index_first_line = get_index_first_line(np_img, 0)
            index_last_line = get_index_last_line(np_img, 0)
            
            upper = index_first_line - 2*space_between_two_lines - line_width

            lower = index_last_line + 2*space_between_two_lines + line_width

            white = Image.new('1', (width,lower-upper ), color='white')
            
            if upper < 0:
                upper_crop = 0 
                upper_merge = -upper
            else:
                upper_crop = upper
                upper_merge = 0
                
            if lower > height:
                lower_crop = height
            else:
                lower_crop = lower
                        
            
            cropped_img = note_img.crop((0, upper_crop, width, lower_crop))
            
            white.paste(cropped_img,(0, upper_merge))
            
            resized_img = white.resize((width_out, height_out))
            
            resized_img.save(new_location)
            
      
def load_note_black_white(f_name):
    img_location = "{}/{}".format(pre_processed_path, f_name)
    img = Image.open(img_location)
    fn = lambda x : 255 if x > tresh_for_seperate_black_white else 0
    img = img.convert('L').point(fn, mode ='1')
    os.remove(img_location)
    return img
    
""" calc on the column specified by col"""
# TODO: take different columns because the first column might not be apropriated (in case it contains a note)
def calc_space_between_lines(np_img, col):
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
        return round(np.asarray(spaces_between_lines).mean()), round(amout_black_pixel/5)
    
    raise Exception()
    
def isBlack(pixel):
    if pixel == True:
        return False 
    else:
        return True
    
def isWhite(pixel):
    return not isBlack(pixel)

def get_index_first_line(np_img, col):
    nr_of_rows = np_img[:,col].size
    for i in range(0,nr_of_rows):
        if isBlack(np_img[i, col]):
            return i
    
def get_index_last_line(np_img, col):
    nr_of_rows = np_img[:,col].size
    for i in range(nr_of_rows, 1, -1):
        if isBlack(np_img[i-1, col]):
            return i
        
        
if __name__=="__main__": 
    main() 