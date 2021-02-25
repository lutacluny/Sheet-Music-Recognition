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

z_full = {
    "width":7.0 ,
    "height":3.0 ,
    "name":"z_full"}
 
z_half = {
    "width":7.0 ,
    "height":3.0 ,
    "name":"z_half"}
 
z_quarter = {
    "width": 4.832,
    "height": 17.2,
    "name":"z_quarter"}
 
z_eigth = {
    "width": 6.771,
    "height": 10.561,
    "name":"z_eigth"}
 
M_C = {
    "width": 9.156,
    "height": 12.102,
    "name":"M_C"}
 
M_4_4 = {
    "width": 11.784,
    "height": 23.875,
    "name":"M_4_4"}

M_3_4 = {
    "width": 11.784,
    "height": 23.875,
    "name":"M_3_4"}
 
M_2_4 = {
    "width": 11.784,
    "height": 23.875,
    "name":"M_2_4"}
 
M_6_8 = {
    "width": 11.334,
    "height": 24.102,
    "name":"M_6_8"}
 
K_Bb = {
    "width": 11.584,
    "height": 25.884,
    "name":"K_Bb"}
 
K_F = {
    "width": 6.084,
    "height": 16.884,
    "name":"K_F"}
 
K_D = {
    "width": 10.28,
    "height": 22.284,
    "name":"K_D"}
 
K_G = {
    "width": 4.78,
    "height": 13.284,
    "name":"K_G"}
 
repeat_start = {
    "width": 11.2,
    "height": 24.0,
    "name":"repeat_start"}
 
repeat_end = {
    "width": 11.2,
    "height": 24.0,
    "name":"repeat_end"}
 
K_C = {
    "width": 16.319,
    "height": 43.605,
    "name":"K_C"}
 
K_C_cleff_bass = {
    "width": 18.360,
    "height": 20.129,
    "name":"K_C_cleff_bass"}
 
symbol_dict = {
    "z_full":z_full ,
    "z_half":z_half ,
    "z_quarter":z_quarter ,
    "z_eigth":z_eigth ,
    "M_2_4": M_2_4 ,
    "M_3_4": M_3_4 ,
    "M_4_4": M_4_4 ,
    "M_6_8":M_6_8 ,
    "M_C":M_C ,
    "K_D":K_D ,
    "K_G":K_G ,
    "K_Bb":K_Bb, 
    "K_F":K_F ,
    "K_C_cleff_bass":K_C_cleff_bass ,
    "K_C":K_C,
    "repeat_start":repeat_start,
    "repeat_end":repeat_end
    }

symbol_pos_centered = [M_2_4, M_3_4, M_4_4, M_6_8, M_C, 
                       repeat_start, repeat_end, 
                       z_half, z_quarter, z_eigth, 
                       K_D, K_G, K_Bb, K_F]



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


symbol_to_value = {
    "z":"r",
    "M":"M",
    "G":"G",
    "D":"D",
    "F":"F",
    "Bb":"Bb",
    "K":"K" ,
    "repeat":"repeat"
}
