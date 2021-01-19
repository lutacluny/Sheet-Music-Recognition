#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 12:35:28 2021

@author: fritz
"""
from cairosvg import svg2png
from PIL import  Image
import shutil
import os



def main():
    if os.path.isdir('jpg_notes'):
        shutil.rmtree('jpg_notes')
       
    shutil.copytree('svg_notes', 'jpg_notes')   
    
    
    for dirName, subdirList, fileList in os.walk('jpg_notes'):
        for fName in fileList:
            svgLocation = "{}/{}".format(dirName, fName)
        
            fNameNew = fName[:-4] + ".png"
            imgLocation = "{}/{}".format(dirName, fNameNew)      
        
            svg2png(url=svgLocation, write_to=imgLocation)

            note = Image.open(imgLocation)
            make_background_white(note)
            converted = note.convert('L')      
            converted.save(imgLocation)
            
            os.remove(svgLocation)

def make_background_white(note):
    note_with_white_background = []
    
    for data in note.getdata():
        if data == (0,0,0,0):
            note_with_white_background.append((255,255,255,255))
        else:
            note_with_white_background.append((0,0,0,255))

    note.putdata(note_with_white_background)    

if __name__=="__main__": 
    main() 

