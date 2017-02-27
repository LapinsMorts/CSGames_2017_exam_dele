#!/usr/bin/python
# -*- coding: utf-8 -*-

""" Makes many tournaments happen in a row"""

import subprocess


def main():
    """ Launches many tournaments"""
    for _ in range(20):
        tournament_result = subprocess.check_output("python AutoCorrect.py",
                                                    shell=True)
        print tournament_result

if __name__ == '__main__':
    main()
