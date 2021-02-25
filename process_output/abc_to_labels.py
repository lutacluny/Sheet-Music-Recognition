#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 13:41:52 2021

@author: fritz
"""

f_name = "test_abc_files/Der Mond ist aufgegangen"
def main():
    header = [] 
    body = []
    
    lines = open(f_name).readlines()
    
    header, index_body = parse_header(lines) 
    
    body = parse_body(lines, index_body)
    
    f_output = open("Der Mond ist aufgegangen_labeled", "w")
    f_output.writelines(header+body)
    
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
            
            if len(item) > 1:
                if item[0:1] == "|:":
                    new_item = "repeat_start"
                
                if item[0:1] == ":|":
                    new_item = "repeat_end"

            new_item = item.replace("/","_")
                
            if len(new_item) <= 1:
                new_item = item + "_full"
                    
            else:
                kind = new_item.split("_")[1]
                
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