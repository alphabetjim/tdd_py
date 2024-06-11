#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 12:56:18 2024

@author: james
"""

def add(num1, num2):
    if type(num1) is not int and type(num1) is not float:
        return "Error: num1 must be a number"
    elif type(num2) is not int and type(num2) is not float:
        return "Error: num2 must be a number"
    else:
        return num1 + num2