#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 20:40:33 2021

@author: fritz
"""

'''IMPORTANT files beginning with '_' are not gonna be processed '''

from PIL import Image
import numpy as np
import os
import shutil
import Union_and_Find


thresh = 100
fn = lambda x : 255 if x > thresh else 0


tresh_equiv_class_test = 2

dir_to_open = "png_tests"
dir_to_save = "separated_lines"

def main():
    for dirName, subdirList, fileList in os.walk(dir_to_open):
        for fName in fileList:
            fName.strip()
            if fName[0] == '_':
                continue
            f_name_without_png = fName[:-4]
        
            out_dir = "{}/{}".format(dir_to_save, f_name_without_png)
            if os.path.isdir(out_dir):
                shutil.rmtree(out_dir)    
            os.makedirs(out_dir)
        
            img_name = "{}/{}".format(dirName, fName)
            separate_lines(img_name, out_dir)
    
def separate_lines(img_name, out_dir):
    img = Image.open(img_name)
    img = img.convert('L').point(fn, mode='1')
    np_img = np.asarray(img)
    
    #angle, (x,y) = calc_rotation_angle(np_img)
    #img.rotate(angle, center=(x,y))    
    #img.show()     
    np_img = np.asarray(img)
    
    matching_col_found = False
    col_index = int(np_img.shape[1] / 2)
    
    while matching_col_found == False:
        col_index += 1
        spaces_between_lines = calc_spaces_between_lines(np_img[:,col_index])
        matching_col_found = is_matching_pattern(spaces_between_lines)
        space_between_lines = matching_col_found
        
        
    col = np_img[:, col_index]
    space_indices_above_upper_line = calc_space_indices_above_upper_line(space_between_lines, spaces_between_lines)
    upper_left_y_of_lines = calc_upper_left_y_of_lines(col, space_indices_above_upper_line)
    nr_of_lines = len(upper_left_y_of_lines)
    
    amount_black_pixel_in_col = calc_amount_black_pixel_in_col(col)
    line_width = amount_black_pixel_in_col / (nr_of_lines * 5)
    
    bounding_boxes = calc_bounding_boxes(space_between_lines, line_width, upper_left_y_of_lines, col)
    
    cut_image_on_bounding_boxes(bounding_boxes, np_img, out_dir)
 
       
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
                    
    return spaces_between_lines

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
        global epsilon_space_between_lines  
        epsilon_space_between_lines = calc_max_diff_members(biggest)
        return biggest.repr
        
    else:   
        return False

def calc_max_diff_members(biggest_eq_class):
    members_sorted = sorted(biggest_eq_class.members)
    lowest = members_sorted [0]
    highest = members_sorted[biggest_eq_class.amount_of_members - 1]
    return  highest - lowest
    

def calc_space_indices_above_upper_line(space_between_lines, spaces_between_lines):
    counter = 0
    space_indices_above_upper_line = []
    
    is_space_between_lines = False
    for space in spaces_between_lines:
        
        if abs(space - space_between_lines) <= epsilon_space_between_lines:
            if not is_space_between_lines:   
                space_indices_above_upper_line.append(counter)
                is_space_between_lines = True
        else:         
            is_space_between_lines = False
            
        counter += 1
        
    return space_indices_above_upper_line


def calc_upper_left_y_of_lines(col, space_indices_above_upper_line):
    is_on_blacks = False
       
    index_black_area = 0
    row_index = 0
    next_black_is_upper_line = False
    
    upper_left_y_of_lines = []
    
    for pixel in col:
        
        if len(space_indices_above_upper_line) != 0:
            if index_black_area == space_indices_above_upper_line[0]:
                next_black_is_upper_line = True 
                space_indices_above_upper_line.pop(0)
            
        elif next_black_is_upper_line == False:
            return upper_left_y_of_lines
        
        if isBlack(pixel) and not is_on_blacks:
            
            if next_black_is_upper_line == True:
                upper_left_y_of_lines.append(row_index)
                next_black_is_upper_line = False
                
            is_on_blacks = True
            
        elif isWhite(pixel) and is_on_blacks:
            is_on_blacks = False
            index_black_area += 1
            
        row_index += 1
   
    return upper_left_y_of_lines
    
def calc_amount_black_pixel_in_col(col):
    amount_black_pixel = 0
    
    for pixel in col:
        if isBlack(pixel):
            amount_black_pixel += 1
            
    return amount_black_pixel


def calc_bounding_boxes(space_between_lines, line_width, upper_left_y_of_lines, col_index):
    bounding_boxes = []
    
    for upper_left_y in upper_left_y_of_lines:
        upper_left_y_adjusted = int(upper_left_y - 2*space_between_lines - line_width)
        lower_left_y = int(upper_left_y + 6*space_between_lines + 6*line_width)
        
        bounding_boxes.append((upper_left_y_adjusted, lower_left_y))
        
    return bounding_boxes
        
def cut_image_on_bounding_boxes(bounding_boxes, np_img, out_dir):
    index = 0
    for bounding_box in bounding_boxes:
        upper_left = bounding_box[0]
        lower_left = bounding_box[1]
        
        len_width = np_img.shape[1]
        
        col_index = - 1
        matching_col_found = False
        while matching_col_found == False:
            col_index += 1
            spaces_between_lines = calc_spaces_between_lines(np_img[:,col_index])
            matching_col_found = is_matching_pattern(spaces_between_lines)  
        
        line_matrix = np_img[upper_left:lower_left,col_index:len_width]
        line_img = Image.fromarray(line_matrix)
        line_img.save("{}/line_{}.png".format(out_dir, index))
        index += 1        
        
def isBlack(pixel):
    if pixel == True:
        return False 
    else:
        return True
    
    
def isWhite(pixel):
    return not isBlack(pixel)

def calc_rotation_angle(np_img):
    x_left, y_left = first_black_left(np_img)
    x_right, y_right = first_black_right(np_img)
    
    if y_left >= y_right:
        rotate_clockwise = True
    else:
        rotate_clockwise = False
        
    angle = np.arctan(abs(y_left - y_right) / abs(x_left - x_right))
    
    if rotate_clockwise == True:
        angle = - angle
        
    return angle, (x_left, y_left)

def first_black_left(np_img):
    len_width = np_img.shape[1]
    for x in range(0, len_width):
        col = np_img[:,x]
        y = find_first_black_pixel_in_col(col)
        if y > 0:
            return x, y
        
def first_black_right(np_img):
    len_width = np_img.shape[1]
    for x in range(len_width - 1, -1 , -1):
        col = np_img[:,x]
        y = find_first_black_pixel_in_col(col)
        if y > 0:
            return x, y
        
def find_first_black_pixel_in_col(col):
    index = 0 
    for pixel in col:
        if isBlack(pixel):
            return index 
        index += 1 
        
    return -1
    
if __name__=="__main__": 
    main() 

