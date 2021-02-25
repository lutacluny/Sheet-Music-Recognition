#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 10:59:53 2021

@author: fritz
"""

lines = {
        "width":49.4,
        "height":24.7,
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


kinds_bottom = ["eigth_bottom_group_left", "eigth_bottom_group_middle", "eigth_bottom_group_right"]
kinds_top = ["eigth_top_group_left", "eigth_top_group_middle", "eigth_top_group_right"]



eigth_bottom_group_left = {
        "width":7.957,
        "height":6.129,
        "name":"eigth_bottom_group_left"
        }

eigth_bottom_group_middle = {
        "width":7.957,
        "height":6.129,
        "name":"eigth_bottom_group_middle"
        }  

eigth_bottom_group_right = {
        "width":7.957,
        "height":6.129,
        "name":"eigth_bottom_group_right"
        }

eigth_top_group_left = {
        "width":7.978,
        "height":6.129,
        "total_height":26.11,
        "name":"eigth_top_group_left"
        }  

eigth_top_group_middle = {
        "width":7.978,
        "height":6.129,
        "total_height":25.407,
        "name":"eigth_top_group_middle"
        }

eigth_top_group_right = {
        "width":7.978,
        "height":6.129,
        "total_height":23.266,
        "name":"eigth_top_group_right"
        }  

kind_dict = {
    "eigth_bottom_group_left":eigth_bottom_group_left,
    "eigth_bottom_group_middle":eigth_bottom_group_middle,
    "eigth_bottom_group_right":eigth_bottom_group_right,
    "eigth_top_group_left":eigth_top_group_left,
    "eigth_top_group_middle":eigth_top_group_middle,
    "eigth_top_group_right":eigth_top_group_right
    }

help_line_dict = {
    "eigth_bottom_group_left":help_line,
    "eigth_bottom_group_middle":help_line,
    "eigth_bottom_group_right":help_line,
    "eigth_top_group_left":help_line,
    "eigth_top_group_middle":help_line,
    "eigth_top_group_right":help_line
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

output_kind_to_value = {
    "full":1,
    "half":2,
    "quarter":4,
    "eigth":8,
    }

output_note_to_value_key_g = {
        "a":'a5',
        "g":'g5',
        "f":'f5',
        "e":'e5',
        "d":'d5',
        "c":'c5',
        "b,":'b',
        "a,":'a',
        "g,":'g',
        "f,":'f',
        "e,":'d',
        "d,":'d',
        "c,":'c'
    }

output_note_to_value_key_f = {
        "a":'c',
        "g":'b4',
        "f":'a4',
        "e":'g4',
        "d":'f4',
        "c":'e4',
        "b,":'d3',
        "a,":'c3',
        "g,":'b3',
        "f,":'a3',
        "e,":'g3',
        "d,":'f3',
        "c,":'e3'
    }
