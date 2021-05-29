# -*- coding: utf-8 -*-
"""
Created on Fri May 28 07:42:22 2021

@author: joseph Mooney
"""
flines = open('my_file.txt')
all_lines = flines.readlines()
flines.close()
count = 0
for line in all_lines:
    count = count + 1
fwords = open('my_file.txt')
read_lines = fwords.read()
words = read_lines.split()
fwords.close()
print('There are %i lines and'% (count), len(words), 'words in my_file.txt')
    
