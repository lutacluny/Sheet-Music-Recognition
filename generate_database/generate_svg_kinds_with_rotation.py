#!/usr/bin/env pxthon3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 17:23:30 2021

@author: fritz
"""

import os 
import shutil
from svgutils.compose import Figure, SVG
from note_dicts import kind_dict, help_line_dict, lines, note_to_index 

kinds_bottom = ["half_bottom", "quarter_bottom", ]
kinds_top = ["half_top", "quarter_top"]

scaling_lines = 2
note_height_in_relation_to_line_gap = 0.9

tol_x = 0.2
amount_of_notes_in_x_range = 5

tol_y = 0.25
amount_of_notes_in_y_range = 5

angle_bounds = (-2,4) # (min_angle, max_angle)
number_of_notes_in_angle_range = 3

scaling_note_deviation = 0.4
number_of_notes_different_sizes = 5

line_gap = (lines["height"] * scaling_lines) / 4.0
svg_out_width = lines["width"] * scaling_lines
svg_out_height = lines["height"] * scaling_lines + 4 * line_gap
is_below_b = False

def main():
    if os.path.isdir("svg_kinds"):
        shutil.rmtree("svg_kinds")

    for note, index in note_to_index.items():
        draw_notes(note, "full", index)      
        
    for note, index in note_to_index.items():
        if index < 8:
            for kind in kinds_bottom:
                draw_notes(note, kind, index)
        else:
            global is_below_b 
            is_below_b = True
            for kind in kinds_top:
                draw_notes(note, kind, index)

def draw_notes(note, kind, index):
    scaling_note, scaled_width_note, scaled_height_note = scale_note(kind)

    x_note, y_note = calc_pos_of_note(index, scaled_width_note, scaled_height_note)
                                                            
    lower_bound_x, lower_bound_y, upper_bound_x, upper_bound_y, step_size_x, step_size_y = calc_bounds_and_step_size(x_note, y_note, scaled_width_note, scaled_height_note)
    
    x = lower_bound_x
    y = lower_bound_y
        
    for i in range(0, amount_of_notes_in_x_range):
        for j in range(0, amount_of_notes_in_y_range):
            scaling_range = calc_scale_range(scaling_note)
            for scaling in scaling_range:    
                generate_svg(note, kind, x, y, scaling, 
                         scaled_width_note, scaled_height_note)
                
            y += step_size_y
            
        y = lower_bound_y
        x += step_size_x
    
def scale_note(kind):
    desired_height = note_height_in_relation_to_line_gap * line_gap
    current_kind = kind_dict[kind]
    scaling_note = desired_height / current_kind["height"]
    scaled_width_note = current_kind["width"] * scaling_note
    scaled_height_note = current_kind["height"] * scaling_note

    return scaling_note, scaled_width_note, scaled_height_note


def calc_pos_of_note(index, scaled_width_note, scaled_height_note):
    global x_centered
    x_centered = svg_out_width / 2.0 
    
    x_note = x_centered - scaled_width_note / 2.0 
    
    global y_centered
    y_centered = (line_gap + index * line_gap) / 2.0
    
    y_note = y_centered - scaled_height_note / 2.0   

    return x_note, y_note
    

def calc_bounds_and_step_size(x_note, y_note, scaled_width_note, scaled_height_note):
    lower_bound_x = x_note - tol_x * scaled_width_note
    lower_bound_y = y_note - tol_y * scaled_height_note

    upper_bound_x = x_note + tol_x * scaled_width_note  
    upper_bound_y = y_note + tol_y * scaled_height_note

    step_size_x = (upper_bound_x - lower_bound_x) / (amount_of_notes_in_x_range-1)      
    step_size_y = (upper_bound_y - lower_bound_y) / (amount_of_notes_in_y_range-1)
    
    return lower_bound_x, lower_bound_y, upper_bound_x, upper_bound_y, step_size_x, step_size_y


def generate_svg(note, kind, x_note, y_note, scaling_note, scaled_width_note, scaled_height_note):
    dir_name = supply_dir(note, kind)
    fname_part_1 = "{}/{}_{}_{}".format(dir_name, note, x_note, y_note)         
            
    angle_range, angle_step = calc_angle_range()
    
    lines_svg = SVG("SVGs/lines.svg")
    lines_svg.scale(scaling_lines).move(0,2*line_gap)   
        
    if is_below_b:
        y_note = adjust_y_note(kind, y_note, scaling_note)
        
    note_svg = SVG("SVGs/{}.svg".format(kind))
    note_svg.scale(scaling_note).move(x_note,y_note)
    
    x_pivot, y_pivot = calc_rotate_pivot(kind, scaling_note)
    
    
    if note == "a" or note == "c,":
        current_help_line = help_line_dict[kind]
        
        scaled_width_help_line = current_help_line["width"] * scaling_note
        scaled_height_help_line = current_help_line["height"] * scaling_note    
        
        x_help_line, y_help_line = calc_pos_of_help_line(scaled_width_help_line,
                                                         scaled_height_help_line)
        
        help_line_svg = SVG("SVGs/{}.svg".format(current_help_line["name"]))
        help_line_svg.scale(scaling_note).move(x_help_line,y_help_line)    
            
        rotate_by = angle_bounds[0]
        for angle in angle_range:
            fname_out = "{}_{}_{}.svg".format(fname_part_1, angle, scaling_note)
            note_svg.rotate(rotate_by, x_pivot, y_pivot)      

            Figure("{}px".format(svg_out_width), "{}px".format(svg_out_height),
                   lines_svg,note_svg, help_line_svg).save(fname_out) 
            
            rotate_by += angle_step
            
    else:
  
        rotate_by = angle_bounds[0]
        for angle in angle_range:
            fname_out = "{}_{}_{}.svg".format(fname_part_1, angle, scaling_note)
            note_svg.rotate(rotate_by, x_pivot, y_pivot)
 
            Figure("{}px".format(svg_out_width), "{}px".format(svg_out_height),
                   lines_svg,note_svg).save(fname_out)   
            
            rotate_by += angle_step
            
 
def supply_dir(note, kind):
    dir_name = "{}/{}".format("svg_kinds", kind)
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)      
        
    return dir_name

def adjust_y_note(kind, y_note, scaling_note):
    current_kind = kind_dict[kind]
    scaled_total_height = (current_kind["total_height"] - current_kind["height"]) * scaling_note
    y_note -= scaled_total_height    
    
    return y_note
    
def calc_pos_of_help_line(scaled_width_help_line, scaled_height_help_line):
    
    x_help_line = x_centered - scaled_width_help_line/2.0
    y_help_line = y_centered - scaled_height_help_line/2.0
    
    return x_help_line, y_help_line
            
def calc_rotate_pivot(kind, scaling_note):
    current_kind = kind_dict[kind]
    
    x_pivot = current_kind["width"] / 2.0 * scaling_note
    
    if is_below_b:
        y_pivot = (current_kind["total_height"] - current_kind["height"] / 2.0) * scaling_note
    else:
        y_pivot = current_kind["height"] / 2.0 * scaling_note
        
    return x_pivot, y_pivot

def calc_angle_range():
    step_size = (angle_bounds[1] - angle_bounds[0]) / (number_of_notes_in_angle_range-1)
    angle_range = []
    
    angle = angle_bounds[0]
    
    for i in range(0, number_of_notes_in_angle_range):
        angle_range.append(angle)
        angle += step_size
        
    return angle_range, step_size
        
        
def calc_scale_range(scaling_note):
    lower = scaling_note - scaling_note_deviation * scaling_note
    upper = scaling_note + scaling_note_deviation * scaling_note
    
    step_size = (upper - lower) / (number_of_notes_different_sizes-1)
    scaling_range = []
    
    scale = lower
    for i in range(0, number_of_notes_different_sizes):
        scaling_range.append(scale)
        scale += step_size
    
    return scaling_range

if __name__=="__main__": 
    main() 
 