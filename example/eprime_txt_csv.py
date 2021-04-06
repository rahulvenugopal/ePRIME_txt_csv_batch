#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 23:18:10 2021
@author: Rahul Venugopal
Just a wrapper to automate bulk converting .txt files to .csv files
"""
# Loading library
from convert_eprime.convert import text_to_csv
from tkinter.filedialog import askopenfilenames
from tkinter import Tk
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing

# Selecting multiple text files using GUI
filelist = askopenfilenames(initialdir = "cwd",title = "Select file",
                              filetypes = (("Text file","*.txt"),
                                           ("All files","*.*")))

for file in filelist:
    in_file = file
    out_file = in_file[0:-3]+str('csv')
    text_to_csv(in_file, out_file)
