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

pause_full = {
    "width":7.0 ,
    "heigth":3.0 ,
    "name":"pause_full"}
 
pause_half = {
    "width":7.0 ,
    "heigth":3.0 ,
    "name":"pause_half"}
 
pause_quarter = {
    "width": 4.832,
    "heigth": 17.2,
    "name":"pause_quarter"}
 
pause_eigth = {
    "width": 6.771,
    "heigth": 10.561,
    "name":"pause_eigth"}
 
beat_C = {
    "width": 9.156,
    "heigth": 12.102,
    "name":"beat_C"}
 
beat_4_4 = {
    "width": 11.784,
    "heigth": 23.875,
    "name":"beat_4_4"}

beat_3_4 = {
    "width": 11.784,
    "heigth": 23.875,
    "name":"beat_3_4"}
 
beat_2_4 = {
    "width": 11.784,
    "heigth": 23.875,
    "name":"beat_2_4"}
 
beat_6_8 = {
    "width": 11.334,
    "heigth": 24.102,
    "name":"beat_6_8"}
 
double_sharp = {
    "width": 11.584,
    "heigth": 25.884,
    "name":"double_sharp"}
 
single_sharp = {
    "width": 6.084,
    "heigth": 16.884,
    "name":"single_sharp"}
 
double_flat = {
    "width": 10.28,
    "heigth": 22.284,
    "name":"double_flat"}
 
single_flat = {
    "width": 4.78,
    "heigth": 13.284,
    "name":"single_flat"}
 
repeat_start = {
    "width": 11.2,
    "heigth": 24.0,
    "name":"repeat_start"}
 
repeat_end = {
    "width": 11.2,
    "heigth": 24.0,
    "name":"repeat_end"}
 
g_key = {
    "width": 16.319,
    "heigth": 43.605,
    "name":"g_key"}
 
f_key = {
    "width": 18.360,
    "heigth": 20.129,
    "name":"f_key"}
 
symbol_dict = {
    "pause_full":pause_full ,
    "pause_half":pause_half ,
    "pause_quarter":pause_quarter ,
    "pause_eigth":pause_eigth ,
    "beat_2_4": beat_2_4 ,
    "beat_3_4": beat_3_4 ,
    "beat_4_4": beat_4_4 ,
    "beat_6_8":beat_6_8 ,
    "beat_C":beat_C ,
    "double_flat":double_flat ,
    "single_flat":single_flat ,
    "double_sharp":double_sharp, 
    "single_sharp":single_sharp ,
    "f_key":f_key ,
    "g_key":g_key,
    "repeat_start":repeat_start,
    "repeat_end":repeat_end
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


output_symbol_to_abc = {
    "pause_full":"z" ,
    "pause_half":"z/2" ,
    "pause_quarter":"z/4" ,
    "pause_eigth":"z/8" ,
    "beat_2_4": "M:2/4" ,
    "beat_3_4": "M:3/4" ,
    "beat_4_4": "M:4/4" ,
    "beat_6_8":"M:6/8" ,
    "beat_C":"M:C" ,
    "double_flat":"K:F" ,
    "single_flat":"K:Bb" ,
    "double_sharp":"K:D", 
    "single_sharp":"K:F" ,
    "f_key":", clef=bass" ,
    "g_key":"",
    "repeat_start":"|:",
    "repeat_end":":|"
}
