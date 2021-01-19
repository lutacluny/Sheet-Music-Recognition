#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 10:59:53 2021

@author: fritz
"""

lines = {
        "width":20.0,
        "height":25.0,
        "name":"lines"
        }

help_line = {
        "width":12.0,
        "height":0.7,
        "name":"help_line"
        }
    
help_line_full = {
        "width":14.0,
        "height":0.7,
        "name":"help_line_full"
        }
    
full = {
        "width":11.2,
        "height":6.0,
        "name":"full"
        }
    
half_bottom = {
        "width":7.711,
        "height":6.948,
        "name":"half_bottom"
        }

half_top = {
        "width":7.771,
        "height":6.948,
        "total_height":24.474,
        "name":"half_top"
        }
    

quarter_bottom = {
        "width":7.957,
        "height":6.129,
        "name":"quarter_bottom"
        }

quarter_top = {
        "width":7.957,
        "height":6.129,
        "total_height":24.064,
        "name":"quarter_top"
        }  

kind_dict = {
    "full":full,
    "half_bottom":half_bottom,
    "half_top":half_top,
    "quarter_bottom":quarter_bottom,
    "quarter_top":quarter_top
    }

help_line_dict = {
    "full":help_line_full,
    "half_bottom":help_line,
    "half_top":help_line,
    "quarter_bottom":help_line,
    "quarter_top":help_line
    }

note_to_index = {
        "a":1,
        "g":2,
        "f":3,
        "e":4,
        "d":5,
        "c":6,
        "b,":7,
        "a,":8,
        "g,":9,
        "f,":10,
        "e,":11,
        "d,":12,
        "c,":13
        }