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


kinds_bottom = ["half_bottom", "quarter_bottom", "eigth_bottom"]
kinds_top = ["half_top", "quarter_top", "eigth_top"]

  
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

eigth_bottom = {
        "width":7.978,
        "height":6.129,
        "name":"quarter_bottom"
        }

eigth_top = {
        "width":7.957,
        "height":6.129,
        "total_height":24.065,
        "name":"quarter_top"
        }  


kind_dict = {
    "full":full,
    "half_bottom":half_bottom,
    "half_top":half_top,
    "quarter_bottom":quarter_bottom,
    "quarter_top":quarter_top,
    "eigth_bottom":eigth_bottom,
    "eigth_top":eigth_top
    }

help_line_dict = {
    "full":help_line_full,
    "half_bottom":help_line,
    "half_top":help_line,
    "quarter_bottom":help_line,
    "quarter_top":help_line,
    "eigth_bottom":help_line,
    "eigth_top":help_line
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
