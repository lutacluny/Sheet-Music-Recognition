#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 12:24:34 2021

@author: fritz
"""

'''IMPORTANT directories beginning with '_' are not gonna be processed '''

from PIL import Image
import numpy as np
import os, shutil
import Union_and_Find

thresh = 140
fn = lambda x : 255 if x > thresh else 0

epsilon_equiv_classes = 1.2 # of smallest width

dir_to_save = "groups_to_separate"
dir_to_open = "separated_notes"

def main():    
    for dirName, subdirList, fileList in os.walk(dir_to_open):
        isLineDir = False
        split = dirName.split('/')
        
        if len(split) > 2:
            isLineDir = True
            test_name = split[1]
            line_name = split[2]     
            out_dir = "{}/{}/{}".format(dir_to_save, test_name, line_name)
            
            if os.path.isdir(out_dir):
                shutil.rmtree(out_dir)    
            os.makedirs(out_dir)
        
        
        width_list_mapping = []
        width_list = []
        for fName in fileList:
            fName.strip()

            if test_name[0] == '_':
                continue
    
            img = Image.open("{}/{}".format(dirName,fName))
            np_img = np.asarray(img)
            img = img.convert('L').point(fn, mode='1')

            width = np_img.shape[1]
            
            width_list_mapping.append((width, fName))
            width_list.append(width)
            
        if isLineDir:
            width_list_mapping_sorted = sorted(width_list_mapping, key=lambda x: x[0], reverse=True)

            epsilon = epsilon_equiv_classes * width_list_mapping_sorted[-1][0]
            
            union_and_find = Union_and_Find.Union_and_Find(width_list, epsilon)
            union_and_find.calc_eq_classes()
            
            while len(union_and_find.eq_classes) > 1: 
                union_and_find.sort_eq_classes_by_repr_descending()
                
                biggest_class = union_and_find.eq_classes.pop(0)
                
                for member in biggest_class.members:
                    
                    copy_to_outdir(dirName, out_dir, width_list_mapping_sorted.pop(0)[1])

                        
                
def copy_to_outdir(dirName, outdir, fName):
    src = "{}/{}".format(dirName,fName)
    dst = "{}/{}".format(outdir,fName)
    shutil.move(src,dst)
    
if __name__=="__main__": 
    main() 

