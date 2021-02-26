#!/usr/bin/env pxthon3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 17:23:30 2021

@author: fritz
"""

import os 
import shutil
from svgutils.compose import Figure, SVG
from symbol_dicts import symbol_dict, symbol_pos_centered, lines


''' Define the output resolution as follows: 
    width/heigth = 50 * scaling_lines '''

    
scaling_lines = 2
symbol_height_in_relation_to_line_gap = 1.0

tol_x = 0.20
amount_of_symbols_in_x_range = 3

tol_y = 0.05
amount_of_symbols_in_y_range = 3

angle_bounds = (-2,4) # (min_angle, max_angle)
number_of_symbols_in_angle_range = 3

scaling_lines_deviation = 0.1
number_of_symbols_different_sizes = 3

line_gap = (lines["height"] * scaling_lines) / 4.0
svg_out_width = lines["width"] * scaling_lines
svg_out_height = lines["height"] * scaling_lines + 4 * line_gap
is_below_b = False

def main():
    if os.path.isdir("svg_symbols"):
        shutil.rmtree("svg_symbols")
     
    for symbol in symbol_pos_centered:
        scaled_width_symbol, scaled_height_symbol = scale_symbol(symbol)
        x_symbol, y_symbol = calc_pos_of_symbol(scaled_width_symbol, scaled_height_symbol)
        draw_symbols(scaled_width_symbol,scaled_height_symbol,x_symbol, y_symbol, symbol)
        

    draw_g_key()
    draw_f_key() 
    
def draw_g_key():
    symbol = symbol_dict["K_C"]
    scaled_width_symbol, scaled_height_symbol = scale_symbol(symbol)
    
    global x_centered
    x_centered = svg_out_width / 2.0 
    x_symbol = x_centered - scaled_width_symbol / 2.0 
    
    global y_centered
    y_centered = svg_out_width / 2.0
    y_symbol = scaling_lines
    
    draw_symbols(scaled_width_symbol,scaled_height_symbol,x_symbol, y_symbol, symbol)

def draw_f_key():
    symbol = symbol_dict["K_C_cleff_bass"]
    scaled_width_symbol, scaled_height_symbol = scale_symbol(symbol)
    
    global x_centered
    x_centered = svg_out_width / 2.0 
    x_symbol = x_centered - scaled_width_symbol / 2.0 
    
    global y_centered
    y_centered = svg_out_width / 2.0
    y_symbol = line_gap * 2
    
    draw_symbols(scaled_width_symbol,scaled_height_symbol,x_symbol, y_symbol, symbol)
    
    
def draw_symbols(scaled_width_symbol, scaled_height_symbol, x_symbol, y_symbol, symbol):
    lower_bound_x, lower_bound_y, upper_bound_x, upper_bound_y, step_size_x, step_size_y = calc_bounds_and_step_size(x_symbol, y_symbol, scaled_width_symbol, scaled_height_symbol)
    
    x = lower_bound_x
    y = lower_bound_y
        
    for i in range(0, amount_of_symbols_in_x_range):
        for j in range(0, amount_of_symbols_in_y_range):
            scaling_range = calc_scale_range(scaling_lines)
            for scaling in scaling_range:    
                generate_svg(symbol, x, y, scaling, 
                    scaled_width_symbol, scaled_height_symbol)
                
            y += step_size_y
            
        y = lower_bound_y
        x += step_size_x
    
def scale_symbol(symbol):
    scaled_width_symbol = symbol["width"] * scaling_lines
    scaled_height_symbol = symbol["height"] * scaling_lines

    return scaled_width_symbol, scaled_height_symbol


def calc_pos_of_symbol(scaled_width_symbol, scaled_height_symbol):
    global x_centered
    x_centered = svg_out_width / 2.0 
    
    x_symbol = x_centered - scaled_width_symbol / 2.0 
    
    global y_centered
    y_centered = svg_out_width / 2.0
    
    y_symbol = y_centered - scaled_height_symbol / 2.0   

    return x_symbol, y_symbol
    

def calc_bounds_and_step_size(x_symbol, y_symbol, scaled_width_symbol, scaled_height_symbol):
    lower_bound_x = x_symbol - tol_x * scaled_width_symbol
    lower_bound_y = y_symbol - tol_y * scaled_height_symbol

    upper_bound_x = x_symbol + tol_x * scaled_width_symbol  
    upper_bound_y = y_symbol + tol_y * scaled_height_symbol

    step_size_x = (upper_bound_x - lower_bound_x) / (amount_of_symbols_in_x_range-1)      
    step_size_y = (upper_bound_y - lower_bound_y) / (amount_of_symbols_in_y_range-1)
    
    return lower_bound_x, lower_bound_y, upper_bound_x, upper_bound_y, step_size_x, step_size_y


def generate_svg(symbol, x_symbol, y_symbol, scaling_lines, scaled_width_symbol, scaled_height_symbol):
    dir_name = supply_dir(symbol)
    fname_part_1 = "{}/{}_{}_{}".format(dir_name, symbol["name"], x_symbol, y_symbol)         
            
    angle_range, angle_step = calc_angle_range()
    
    lines_svg = SVG("SVGs/lines.svg")
    lines_svg.scale(scaling_lines).move(0,2*line_gap)   
        
    symbol_svg = SVG("SVGs/{}.svg".format(symbol["name"]))
    symbol_svg.scale(scaling_lines).move(x_symbol,y_symbol)
    
    
    rotate_by = angle_bounds[0]
    for angle in angle_range:
        fname_out = "{}_{}_{}.svg".format(fname_part_1, angle, scaling_lines)
        symbol_svg.rotate(rotate_by, x_centered, y_centered)      

        Figure("{}px".format(svg_out_width), "{}px".format(svg_out_height),
               lines_svg,symbol_svg).save(fname_out) 
            
        rotate_by += angle_step

            
 
def supply_dir(symbol):
    dir_name = "{}/{}".format("svg_symbols", symbol["name"])
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)      
        
    return dir_name


def calc_angle_range():
    step_size = (angle_bounds[1] - angle_bounds[0]) / (number_of_symbols_in_angle_range-1)
    angle_range = []
    
    angle = angle_bounds[0]
    
    for i in range(0, number_of_symbols_in_angle_range):
        angle_range.append(angle)
        angle += step_size
        
    return angle_range, step_size
        
        
def calc_scale_range(scaling_lines):
    lower = scaling_lines - scaling_lines_deviation * scaling_lines
    upper = scaling_lines + scaling_lines_deviation * scaling_lines
    
    step_size = (upper - lower) / (number_of_symbols_different_sizes-1)
    scaling_range = []
    
    scale = lower
    for i in range(0, number_of_symbols_different_sizes):
        scaling_range.append(scale)
        scale += step_size
    
    return scaling_range

if __name__=="__main__": 
    main() 
 