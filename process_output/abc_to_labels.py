#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 13:41:52 2021

@author: fritz
"""
import os, shutil

abc_dir = "abc_files"
label_dir = "label_files"

def main():
    if os.path.isdir(label_dir):
        shutil.rmtree(label_dir)
    os.mkdir(label_dir) 
    
    for dirName, subdirList, fileList in os.walk("abc_files"):
        for f_name in fileList:
            process_file(f_name)
            
            
def process_file(f_name):
    header = [] 
    body = []
    f_name_in = "{}/{}".format(abc_dir, f_name) 
    lines = open(f_name_in).readlines()
    
    header, index_body = parse_header(lines) 
    
    body = parse_body(lines, index_body)
    
    f_name_out = "{}/{}".format(label_dir,f_name)
    f_out = open(f_name_out, "w")
    f_out.writelines(header+body)
    
def parse_header(lines):
    header = [] 
    index = 0
    
    for item in lines:
        item = item.strip()
        if item[0] == 'X':
            index += 1
            continue
            
        elif item[0] == 'M':
            new_item = item.replace(":","_")
            new_item = new_item.replace("/","_")
            header.append(new_item + " ")
                
        elif item[0] == 'K':
            new_item = item.replace(":","_")
            new_item = new_item.replace("/","_")
            new_item = new_item.replace(" ","_")
            header.append(new_item+ " ")

        elif item[0] == 'L':
            index += 1
            continue
            
        else:
            return header, index
        
        index += 1
    
def parse_body(lines, index_body ):
    body = [] 
    index = 0 
    
    for line in lines:
        if index < index_body:
            index += 1 
            continue
        
        for item in line.split(" "):
            if len(item) == 0:
                continue
            item = item.strip()
            
            if item == "|":
                continue
     
            elif item == "|:":
                new_item = "repeat_start"
                
            elif item == ":|":
                new_item = "repeat_end"         

            else: 
                
                new_item = item.replace("/","_")
                splitted = new_item.split("_")
                
                if len(splitted) == 1:
                    new_item = item + "_full"
                    
                else:
                    kind = splitted[1]
                
                    if kind == "2":
                        new_item = new_item.replace("2","half")
    
                    if kind == "4":
                        new_item = new_item.replace("4","quarter")
                    
                    if kind == "8":
                        new_item = new_item.replace("8","eigth")   
                
            body.append(new_item + " ")
            
        body.append("\n")
        
    return body



    
if __name__ =='__main__':
    main()