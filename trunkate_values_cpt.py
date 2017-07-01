# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 10:46:31 2017

@author: Katie Bug
"""

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

f3 = open('C:/Users/Katie Bug/Desktop/ProHealth/cpt_bde_year20.txt', 'r') 
w3 = open('C:/Users/Katie Bug/Desktop/ProHealth/cpt_bde_year20_new.txt', 'w') 
for line in f3:
    new_line = ""
    sp = line.split()
    for s in sp:
        print(s)
        if is_number(s):
            trunk = '%.3f'%float(s)
            print(trunk)
            new_line += "\t" + trunk
        else:
            new_line += "\t" + s
    new_line += "\n"
    w3.write(new_line)