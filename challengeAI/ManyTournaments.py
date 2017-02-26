#!/usr/bin/python3]
# -*- coding: utf-8 -*-

import subprocess


for i in range(0, 20):
    tournament_result = subprocess.check_output("python AutoCorrect.py",
                                                shell=True)
    print(tournament_result)
