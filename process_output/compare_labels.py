#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 10:18:38 2021

@author: fritz
"""

import os 


dir_ground_truth = "label_files"
dir_prediction = "output_label_files"

def main():
    ground_truth_files = os.listdir(dir_ground_truth)
    
    for dirName, subdirList, fileList in os.walk(dir_prediction):
        for f_prediction in fileList:
            for f_ground_truth in ground_truth_files:
                
                if f_prediction == f_ground_truth:
                    print(f_prediction)
                    f1 = "{}/{}".format(dir_ground_truth, f_ground_truth)
                    f2 = "{}/{}".format(dir_prediction, f_prediction)
                    compare_files(f1, f2)
                    print("\n")
    
def compare_files(f1_name, f2_name):
    f1 = open(f1_name).readlines() 
    f2 = open(f1_name).readlines()
    
    f_len = len(f1) 
    
    for i in range(0,f_len):
        f1_line = f1[i].split()
        f2_line = f2[i].split()
        
        line_len = len(f1_line) 
        
        number_of_matches = 0
        
        for j in range(0,line_len):
            if f1_line[j] == f2_line[j]:
                number_of_matches += 1
                
        print("line_{}: {}/{}".format(i, number_of_matches, line_len))
    
if __name__ == '__main__':
    main()