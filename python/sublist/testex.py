#!/usr/bin/env python3

"""Runs Exercism exercise tests.
"""

import os, subprocess

def main():

    exercise = os.getcwd().split('/')[-1]

    if '-' in exercise:
        exercise.replace('-','_')
    
    test = f'python3 -m pytest -o marker=task -v {exercise}_test.py'.split()
    
    subprocess.call(test)

if __name__ == "__main__":
    main()