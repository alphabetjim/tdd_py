#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 12:54:26 2024

@author: James Bridgwater Court

File implementing tests as initial step into TDD
Beginning by writing using basic Python syntax instead of frameworks
"""

from code_to_test import add

#assert add(1, 1) == 2

test_cases = [
    {"num1": 1, "num2": 3, "expected": 4},
    {"num1": 1, "num2": "invalid", "expected": "Error: num2 must be a number"}, 
    {"num1": [1,2,3], "num2": 2, "expected": "Error: num1 must be a number"},
    {"num1": -1, "num2": 1, "expected": 0},
    {"num1": 3.5, "num2": 2.5, "expected": 6.0}, 
    {"num1": 100, "num2": 200, "expected": 300}
]

for test in test_cases:
    assert add(test["num1"], test["num2"]) == test["expected"]

print("All tests passed!")